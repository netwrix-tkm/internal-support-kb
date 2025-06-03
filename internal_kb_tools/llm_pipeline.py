"""
LLM Pipeline Module

Handles the two-stage LLM processing pipeline:
1. Stage 1: Summarizing individual cases with a lighter model
2. Stage 2: Generating knowledge base content with a more powerful model
"""

import csv
import json
import logging
import os
import time
from pathlib import Path
import requests
from typing import Dict, List, Optional, Any
import pandas as pd
from datetime import datetime
import tqdm

# Add dotenv import
try:
    from dotenv import load_dotenv
    # Load environment variables from .env file
    load_dotenv()
except ImportError:
    logging.warning("python-dotenv not installed. Environment variables must be set manually.")

logger = logging.getLogger(__name__)

class LLMPipeline:
    """Implements a two-stage LLM pipeline for processing support cases."""
    
    def __init__(self, config: Dict):
        """
        Initialize the LLM pipeline.
        
        Args:
            config: Configuration dictionary
        """
        self.config = config
        self.output_dir = Path(config['output_dir'])
        self.summaries_dir = Path(config['summaries_dir'])
        self.kb_articles_dir = Path(config.get('kb_articles_dir', 'kb_output/kb_articles'))
        
        # Ensure the directories exist
        self.summaries_dir.mkdir(parents=True, exist_ok=True)
        self.kb_articles_dir.mkdir(parents=True, exist_ok=True)
        
        # Load prompt templates
        self.stage1_prompt_template = self._load_prompt_template(config['stage1_prompt_template'])
        self.stage2_prompt_template = self._load_prompt_template(config['stage2_prompt_template'])
        
        # Update model names to the correct ones
        if self.config['stage1_model'] == '4o-mini':
            self.config['stage1_model'] = 'gpt-4o-mini-support'
            
        if self.config['stage2_model'] == 'gpt-4':
            self.config['stage2_model'] = 'gpt-4o-support'
        
        # Check for environment variable overrides
        if os.environ.get('STAGE1_MODEL'):
            self.config['stage1_model'] = os.environ.get('STAGE1_MODEL')
            
        if os.environ.get('STAGE2_MODEL'):
            self.config['stage2_model'] = os.environ.get('STAGE2_MODEL')
            
        # API settings
        self.api_key = os.environ.get('AZURE_OPENAI_API_KEY')
        if not self.api_key:
            logger.warning("AZURE_OPENAI_API_KEY not found in environment variables")
            
        logger.info(f"Using Stage 1 model: {self.config['stage1_model']}")
        logger.info(f"Using Stage 2 model: {self.config['stage2_model']}")
        
    def _load_prompt_template(self, template_path: str) -> str:
        """Load prompt template from file."""
        try:
            template_file = Path(template_path)
            if template_file.exists():
                with open(template_file, 'r', encoding='utf-8') as f:
                    return f.read()
            else:
                # Create default templates directory
                template_file.parent.mkdir(parents=True, exist_ok=True)
                
                # Create default stage1 prompt
                if template_path.endswith('stage1_prompt.txt'):
                    default_prompt = """
You are a technical support onboarding and enablement specialist. Your task is to create a comprehensive
summary of this support case that contains all the relevant information about the problem
and its resolution.

Please include:
1. The problem description
2. Key technical details and symptoms
3. Troubleshooting steps that were attempted
4. The root cause
5. The solution that resolved the issue
6. Any important notes or warnings for future reference

Case Information:
[CASE_DETAILS]

Email Communications:
[EMAIL_DETAILS]

Posts:
[POST_DETAILS]

Comments:
[COMMENT_DETAILS]

Create a clear, concise summary that would help another support technician understand and
resolve a similar issue in the future. Format your summary in Markdown.
"""
                # Create default stage2 prompt
                elif template_path.endswith('stage2_prompt.txt'):
                    default_prompt = """
You are a technical documentation specialist for Netwrix. Your task is to create comprehensive
technical support training materials based on the provided case summaries.

Case Summaries:
[CASE_SUMMARIES]

Please organize this information into a well-structured technical knowledge base article that:
1. Clearly defines the common issues in this category
2. Provides step-by-step troubleshooting procedures
3. Explains root causes of typical problems
4. Outlines tested solutions with specific commands or configuration changes
5. Includes any important warnings or best practices

The document should be formatted in Markdown and organized with clear headings, lists, and
code blocks where appropriate. This will be used to train new support staff.
"""
                
                # Write the default template
                with open(template_file, 'w', encoding='utf-8') as f:
                    f.write(default_prompt)
                logger.info(f"Created default prompt template at {template_path}")
                return default_prompt
                
        except Exception as e:
            logger.error(f"Error loading prompt template: {e}")
            return "Error: Could not load prompt template"
            
    def run_stage1(self, path_filter: Optional[str] = None):
        """
        Run Stage 1 of the LLM pipeline to generate case summaries.
        
        Args:
            path_filter: Optional path filter
        """
        start_time = datetime.now()
        logger.info(f"Starting Stage 1: Case Summarization at {start_time}")
        
        # Get all case files matching the filter
        case_files = self._get_case_files(path_filter)
        total_cases = len(case_files)
        logger.info(f"Found {total_cases} cases to summarize")
        
        # Process in batches
        batch_size = self.config.get('stage1_batch_size', 10)
        
        # Initialize progress bar
        progress_bar = tqdm.tqdm(total=total_cases, desc="Generating Summaries", unit="case")
        
        processed = 0
        for i in range(0, total_cases, batch_size):
            batch = case_files[i:i+batch_size]
            logger.info(f"Processing batch {i//batch_size + 1} ({len(batch)} cases)")
            
            for case_file in batch:
                try:
                    self._process_case(case_file)
                    processed += 1
                    progress_bar.update(1)
                    
                    # Calculate and display progress information
                    current_time = datetime.now()
                    elapsed_time = current_time - start_time
                    percent_done = (processed / total_cases) * 100
                    
                    logger.debug(f"Progress: {processed}/{total_cases} ({percent_done:.1f}%) - {elapsed_time}")
                    
                except Exception as e:
                    logger.error(f"Error processing case {case_file}: {e}")
        
        # Close progress bar
        progress_bar.close()
        
        # Log completion
        end_time = datetime.now()
        total_time = end_time - start_time
        logger.info(f"Completed Stage 1 in {total_time}. Generated {processed} summaries.")
        
    def _get_case_files(self, path_filter: Optional[str] = None) -> List[Path]:
        """
        Get all case files matching the filter.
        
        Args:
            path_filter: Optional path filter
            
        Returns:
            List of case file paths
        """
        case_files = []
        filter_parts = path_filter.split('/') if path_filter else None
        
        for platform in os.listdir(self.output_dir):
            platform_path = self.output_dir / platform
            if not platform_path.is_dir():
                continue
                
            # Skip if platform doesn't match filter
            if filter_parts and platform != filter_parts[0]:
                continue
                
            for component in os.listdir(platform_path):
                component_path = platform_path / component
                if not component_path.is_dir():
                    continue
                    
                # Skip if component doesn't match filter (only check if we have more than 1 filter part)  
                if filter_parts and len(filter_parts) >= 2 and component != filter_parts[1]:
                    continue
                    
                for feature in os.listdir(component_path):
                    feature_path = component_path / feature
                    if not feature_path.is_dir():
                        continue
                        
                    # Skip if feature doesn't match filter (only check if we have more than 2 filter parts)
                    if filter_parts and len(filter_parts) >= 3 and feature != filter_parts[2]:
                        continue
                    
                    # Get only the main case files (not the related files)
                    for file in feature_path.glob("*.csv"):
                        # Skip files that have _emails, _posts, or _comments in the name
                        if "_emails" not in file.name and "_posts" not in file.name and "_comments" not in file.name:
                            case_files.append(file)
        
        return case_files

    def run_stage2(self, path_filter: Optional[str] = None):
        """
        Run Stage 2 of the pipeline: Process summaries to generate knowledge base articles.
        
        Args:
            path_filter: Optional path filter to process specific sections
        """
        logger.info("Starting Stage 2: Processing summaries to generate knowledge base articles")
        
        # Create dictionary to track directories to process
        directories_to_process = []
        filter_parts = path_filter.split('/') if path_filter else None
        
        # Find all directories that need to be processed
        for platform in os.listdir(self.summaries_dir):
            platform_path = self.summaries_dir / platform
            if not platform_path.is_dir():
                continue
                
            # Skip if platform doesn't match filter
            if filter_parts and platform != filter_parts[0]:
                continue
                
            for component in os.listdir(platform_path):
                component_path = platform_path / component
                if not component_path.is_dir():
                    continue
                    
                # Skip if component doesn't match filter (only check if we have more than 1 filter part)  
                if filter_parts and len(filter_parts) >= 2 and component != filter_parts[1]:
                    continue
                    
                for feature in os.listdir(component_path):
                    feature_path = component_path / feature
                    if not feature_path.is_dir():
                        continue
                        
                    # Skip if feature doesn't match filter (only check if we have more than 2 filter parts)
                    if filter_parts and len(filter_parts) >= 3 and feature != filter_parts[2]:
                        continue
                        
                    # Add to list of directories to process
                    directories_to_process.append({
                        'platform': platform,
                        'component': component,
                        'feature': feature,
                        'path': feature_path
                    })
        
        # Process each directory
        for directory in directories_to_process:
            platform = directory['platform']
            component = directory['component']
            feature = directory['feature']
            path = directory['path']
            
            try:
                # Only proceed if there are summary files
                summary_files = list(path.glob("*.md"))
                if not summary_files:
                    logger.info(f"No summary files found in {path}, skipping")
                    continue
                    
                # Read all summary files
                summaries = []
                for summary_file in summary_files:
                    with open(summary_file, 'r', encoding='utf-8') as f:
                        summaries.append(f.read())
                
                # Process summaries in batches if needed
                batch_size = self.config['stage2_batch_size']
                kb_content = ""
                
                if len(summaries) <= batch_size:
                    # Process all summaries in a single batch
                    kb_content = self._process_summaries(summaries, platform, component, feature)
                else:
                    # Process summaries in multiple batches and combine results
                    batch_contents = []
                    for i in range(0, len(summaries), batch_size):
                        batch_summaries = summaries[i:i + batch_size]
                        batch_content = self._process_summaries(
                            batch_summaries, 
                            platform, 
                            component, 
                            feature,
                            batch=f"Batch {i//batch_size + 1}/{(len(summaries) + batch_size - 1)//batch_size}"
                        )
                        batch_contents.append(batch_content)
                    
                    # Process all batch contents together to create final KB article
                    kb_content = self._process_batch_contents(
                        batch_contents,
                        platform,
                        component,
                        feature
                    )
                
                # Create output directory
                kb_output_dir = self.kb_articles_dir / platform / component
                kb_output_dir.mkdir(parents=True, exist_ok=True)
                
                # Write KB article
                kb_file = kb_output_dir / f"{feature}.md"
                with open(kb_file, 'w', encoding='utf-8') as f:
                    f.write(kb_content)
                    
                logger.info(f"Generated KB article for {platform}/{component}/{feature}")
                
            except Exception as e:
                logger.error(f"Error processing {platform}/{component}/{feature}: {e}")
                
            # Introduce delay to respect API rate limits
            time.sleep(2)
            
        logger.info(f"Stage 2 complete: Generated KB articles for {len(directories_to_process)} features") 

    def _process_case(self, case_file: Path) -> str:
        """
        Process a single case to generate a summary.
        
        Args:
            case_file: Path to case CSV file
            
        Returns:
            str: Generated summary
        """
        logger.info(f"Processing case {case_file.name}")
        
        # Extract case ID, platform, component, feature from the path
        case_id = case_file.stem
        feature = case_file.parent.name
        component = case_file.parent.parent.name
        platform = case_file.parent.parent.parent.name
        
        # Create summary directory
        summary_dir = self.summaries_dir / platform / component / feature
        summary_dir.mkdir(parents=True, exist_ok=True)
        
        # Check if summary already exists
        summary_file = summary_dir / f"{case_id}.md"
        if summary_file.exists():
            logger.info(f"Summary already exists for case {case_id}, skipping")
            return "Summary already exists"
        
        # Find related files
        emails_file = case_file.parent / f"{case_id}_emails.csv"
        posts_file = case_file.parent / f"{case_id}_posts.csv"
        comments_file = case_file.parent / f"{case_id}_comments.csv"
        
        # Read case details
        case_details = self._read_csv_to_text(case_file)
        email_details = self._read_csv_to_text(emails_file) if emails_file.exists() else "No email communications."
        post_details = self._read_csv_to_text(posts_file) if posts_file.exists() else "No posts."
        comment_details = self._read_csv_to_text(comments_file) if comments_file.exists() else "No comments."
        
        # Create prompt
        prompt = self.stage1_prompt_template
        prompt = prompt.replace("[CASE_DETAILS]", case_details)
        prompt = prompt.replace("[EMAIL_DETAILS]", email_details)
        prompt = prompt.replace("[POST_DETAILS]", post_details)
        prompt = prompt.replace("[COMMENT_DETAILS]", comment_details)
        
        # Call LLM API
        try:
            case_summary = self._call_llm_api(
                prompt,
                model=self.config['stage1_model'],
                max_retries=self.config.get('stage1_max_retries', 3),
                retry_delay=self.config.get('stage1_retry_delay', 5)
            )
            
            # Write summary to file
            with open(summary_file, 'w', encoding='utf-8') as f:
                f.write(case_summary)
            
            logger.info(f"Generated summary for {case_id}")
            return case_summary
            
        except Exception as e:
            logger.error(f"Error generating summary for {case_id}: {e}")
            raise
    
    def _process_summaries(self, summaries: List[str], platform: str, component: str, feature: str, batch: str = "") -> str:
        """
        Process a batch of summaries to generate knowledge base content.
        
        Args:
            summaries: List of case summaries
            platform: Platform name
            component: Component name
            feature: Feature name
            batch: Optional batch identifier
            
        Returns:
            str: Generated knowledge base content
        """
        batch_info = f" ({batch})" if batch else ""
        logger.info(f"Processing {len(summaries)} summaries for {platform}/{component}/{feature}{batch_info}")
        
        # Create prompt
        prompt = self.stage2_prompt_template
        prompt = prompt.replace("[CASE_SUMMARIES]", "\n\n===== NEXT CASE =====\n\n".join(summaries))
        
        # Add context information
        context = f"""
Platform: {platform}
Component: {component}
Feature: {feature}
Number of Cases: {len(summaries)}
{batch_info}

Generate a comprehensive knowledge base article for the above feature based on the case summaries provided.
"""
        prompt = prompt + "\n\n" + context
        
        # Call LLM API
        try:
            kb_content = self._call_llm_api(
                prompt,
                model=self.config['stage2_model'],
                max_retries=self.config.get('stage2_max_retries', 3),
                retry_delay=self.config.get('stage2_retry_delay', 10)
            )
            return kb_content
            
        except Exception as e:
            logger.error(f"Error generating KB article for {platform}/{component}/{feature}: {e}")
            raise

    def _process_batch_contents(self, batch_contents: List[str], platform: str, component: str, feature: str) -> str:
        """
        Process multiple batch contents to create a unified knowledge base article.
        
        Args:
            batch_contents: List of knowledge base contents from different batches
            platform: Platform name
            component: Component name
            feature: Feature name
            
        Returns:
            str: Unified knowledge base content
        """
        logger.info(f"Consolidating {len(batch_contents)} batches for {platform}/{component}/{feature}")
        
        # Create prompt for consolidation
        sections = ""
        for i, content in enumerate(batch_contents):
            sections += f"\n\n----- SECTION {i+1} -----\n\n{content}"
        
        prompt = f"""
You are a technical documentation specialist for Netwrix. Your task is to create a unified, 
comprehensive knowledge base article by consolidating multiple sections of content.

Each section below represents knowledge derived from different batches of support cases related 
to the same feature. Analyze all sections and create a single, coherent knowledge base article
that combines all the information without redundancy.

Platform: {platform}
Component: {component}
Feature: {feature}

CONTENT SECTIONS TO CONSOLIDATE:
----- SECTION 1 -----{sections}

Please create a single, well-organized knowledge base article that combines all the information
from these sections. Remove any redundancy while ensuring all unique information is preserved.
Format the article in Markdown with clear headings, lists, and code blocks as appropriate.
"""
        
        # Call LLM API
        try:
            kb_content = self._call_llm_api(
                prompt,
                model=self.config['stage2_model'],
                max_retries=self.config.get('stage2_max_retries', 3),
                retry_delay=self.config.get('stage2_retry_delay', 10)
            )
            return kb_content
            
        except Exception as e:
            logger.error(f"Error consolidating KB article for {platform}/{component}/{feature}: {e}")
            raise

    def _read_csv_to_text(self, file_path: Path) -> str:
        """
        Read a CSV file and convert it to a readable text format.
        
        Args:
            file_path: Path to CSV file
            
        Returns:
            str: Text representation of CSV data
        """
        if not file_path.exists():
            return "File not found."
        
        try:
            # Read with pandas using proper quoting settings
            try:
                df = pd.read_csv(
                    file_path, 
                    encoding='utf-8', 
                    quoting=csv.QUOTE_ALL, 
                    quotechar='"', 
                    escapechar='\\',
                    engine='python'  # Python engine is more tolerant of malformed CSV
                )
                
                # Format as readable text
                rows_text = []
                for _, row in df.iterrows():
                    row_data = []
                    for col, value in row.items():
                        if pd.notna(value):  # Only include non-null values
                            # Clean up the value if it's a string
                            if isinstance(value, str):
                                cleaned_value = value.strip()
                                if cleaned_value:  # Only include non-empty values
                                    row_data.append(f"{col}: {cleaned_value}")
                            else:
                                row_data.append(f"{col}: {value}")
                    rows_text.append("\n".join(row_data))
                
                return "\n\n---\n\n".join(rows_text)
                
            except Exception as e:
                logger.warning(f"Could not read {file_path} with pandas: {e}, falling back to manual CSV parsing")
                
                # Fallback to manual CSV parsing
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    csv_reader = csv.reader(f, quoting=csv.QUOTE_ALL, quotechar='"', escapechar='\\')
                    headers = next(csv_reader, [])
                    
                    rows_text = []
                    for row in csv_reader:
                        row_data = []
                        for i, value in enumerate(row):
                            if i < len(headers) and value.strip():  # Only include non-empty values
                                header = headers[i]
                                row_data.append(f"{header}: {value.strip()}")
                        rows_text.append("\n".join(row_data))
                    
                    return "\n\n---\n\n".join(rows_text)
                
        except Exception as e:
            logger.error(f"Error reading CSV file {file_path}: {e}")
            return f"Error reading file: {e}"

    def _call_llm_api(self, prompt: str, model: str, max_retries: int = 3, retry_delay: int = 5) -> str:
        """
        Call the LLM API with retries.
        
        Args:
            prompt: Prompt to send to the LLM
            model: Model ID to use
            max_retries: Maximum number of retries
            retry_delay: Delay between retries in seconds
            
        Returns:
            str: LLM response
        """
        # Check for API key
        if not self.api_key:
            error_msg = "Azure OpenAI API key not found. Please set AZURE_OPENAI_API_KEY environment variable."
            logger.error(error_msg)
            raise ValueError(error_msg)
        
        # Get Azure OpenAI endpoint
        endpoint = os.environ.get('AZURE_OPENAI_ENDPOINT')
        if not endpoint:
            error_msg = "Azure OpenAI endpoint not found. Please set AZURE_OPENAI_ENDPOINT environment variable."
            logger.error(error_msg)
            raise ValueError(error_msg)
        
        # Get Azure OpenAI API version
        api_version = os.environ.get('AZURE_OPENAI_VERSION', '2024-02-15-preview')
        
        # Build request URL
        url = f"{endpoint}/openai/deployments/{model}/chat/completions?api-version={api_version}"
        
        # Build request headers
        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key
        }
        
        # Build request payload
        payload = {
            "messages": [
                {
                    "role": "system",
                    "content": "You are a technical support knowledge base assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.1,
            "max_tokens": 4096
        }
        
        # Try the API call with retries
        for attempt in range(max_retries):
            try:
                logger.debug(f"Calling LLM API (attempt {attempt + 1}/{max_retries})")
                response = requests.post(url, headers=headers, json=payload)
                response.raise_for_status()  # Raise exception for HTTP errors
                
                response_data = response.json()
                result = response_data["choices"][0]["message"]["content"]
                return result
                
            except requests.RequestException as e:
                logger.error(f"API error (attempt {attempt + 1}/{max_retries}): {e}")
                
                if attempt < max_retries - 1:
                    logger.info(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                else:
                    logger.error(f"Failed after {max_retries} attempts")
                    raise ValueError(f"API request failed: {e}")
            
            except (KeyError, IndexError) as e:
                logger.error(f"Malformed API response (attempt {attempt + 1}/{max_retries}): {e}")
                
                if attempt < max_retries - 1:
                    logger.info(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                else:
                    logger.error(f"Failed after {max_retries} attempts")
                    raise ValueError(f"Malformed API response: {e}") 