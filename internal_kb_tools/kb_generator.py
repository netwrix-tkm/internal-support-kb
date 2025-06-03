"""
Knowledge Base Generator Module

Handles the generation of knowledge base articles using the LLM pipeline.
"""

import logging
import os
from pathlib import Path
from typing import Dict, Optional
import time
from datetime import datetime
import tqdm

from llm_pipeline import LLMPipeline

logger = logging.getLogger(__name__)

class KBGenerator:
    """Generates knowledge base articles using the LLM pipeline."""
    
    def __init__(self, config: Dict):
        """
        Initialize the knowledge base generator.
        
        Args:
            config: Configuration dictionary
        """
        self.config = config
        self.llm_pipeline = LLMPipeline(config)
        self.kb_articles_dir = Path(config.get('kb_articles_dir', 'kb_output/kb_articles'))
        
        # Ensure the output directory exists
        self.kb_articles_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_kb(self, path_filter: Optional[str] = None):
        """
        Generate knowledge base articles based on summaries.
        
        Args:
            path_filter: Optional path filter to process specific sections
        """
        logger.info("Starting knowledge base generation")
        
        # Count total number of feature paths to process
        total_paths = self._count_feature_paths(path_filter)
        logger.info(f"Found {total_paths} feature paths to process")
        
        # Run Stage 2 of the LLM pipeline with progress tracking
        start_time = datetime.now()
        self._run_stage2_with_progress(path_filter, total_paths, start_time)
        
        # Create index files for easy navigation
        self._create_index_files()
    
    def _count_feature_paths(self, path_filter: Optional[str] = None) -> int:
        """
        Count the total number of feature paths to process.
        
        Args:
            path_filter: Optional path filter
            
        Returns:
            int: Total number of feature paths
        """
        count = 0
        filter_parts = path_filter.split('/') if path_filter else None
        
        for platform in os.listdir(self.llm_pipeline.summaries_dir):
            platform_path = self.llm_pipeline.summaries_dir / platform
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
                    
                    # Only count if there are summary files
                    summary_files = list(feature_path.glob("*.md"))
                    if summary_files:
                        count += 1
        
        return count
    
    def _run_stage2_with_progress(self, path_filter: Optional[str], total_paths: int, start_time: datetime):
        """
        Run Stage 2 of the LLM pipeline with progress tracking.
        
        Args:
            path_filter: Optional path filter
            total_paths: Total number of paths to process
            start_time: Start time of the process
        """
        processed_paths = 0
        
        # Get all feature paths to process
        feature_paths = self._get_feature_paths(path_filter)
        
        # Initialize progress bar
        progress_bar = tqdm.tqdm(total=total_paths, desc="Generating KB Articles", unit="feature")
        
        # Process each feature path
        for platform, component, feature in feature_paths:
            # Process summaries and generate KB article
            self.llm_pipeline.run_stage2(f"{platform}/{component}/{feature}")
            
            # Update progress
            processed_paths += 1
            progress_bar.update(1)
            
            # Calculate and display progress information
            current_time = datetime.now()
            elapsed_time = current_time - start_time
            percent_done = (processed_paths / total_paths) * 100 if total_paths > 0 else 0
            
            # Display progress information
            logger.info(f"Progress: {processed_paths}/{total_paths} ({percent_done:.1f}%) - {elapsed_time}")
        
        # Close progress bar
        progress_bar.close()
        
        # Log completion information
        end_time = datetime.now()
        total_time = end_time - start_time
        logger.info(f"Completed knowledge base generation in {total_time}")
    
    def _get_feature_paths(self, path_filter: Optional[str]) -> list:
        """
        Get all feature paths to process.
        
        Args:
            path_filter: Optional path filter
            
        Returns:
            list: List of (platform, component, feature) tuples
        """
        feature_paths = []
        filter_parts = path_filter.split('/') if path_filter else None
        
        for platform in os.listdir(self.llm_pipeline.summaries_dir):
            platform_path = self.llm_pipeline.summaries_dir / platform
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
                    
                    # Only include if there are summary files
                    summary_files = list(feature_path.glob("*.md"))
                    if summary_files:
                        feature_paths.append((platform, component, feature))
        
        return feature_paths
    
    def _create_index_files(self):
        """Create index files for easy navigation of the knowledge base."""
        logger.info("Creating knowledge base index files")
        
        # Create main index
        main_index_path = self.kb_articles_dir / "index.md"
        platforms = [d for d in os.listdir(self.kb_articles_dir) if (self.kb_articles_dir / d).is_dir()]
        
        with open(main_index_path, 'w', encoding='utf-8') as f:
            f.write("# Netwrix Technical Support Knowledge Base\n\n")
            f.write("This knowledge base contains technical support training materials generated from support cases.\n\n")
            f.write("## Platforms\n\n")
            
            for platform in platforms:
                f.write(f"- [{platform}](./{platform}/index.md)\n")
        
        logger.info(f"Created main index at {main_index_path}\n")
        
        # Create platform indexes
        for platform in platforms:
            platform_path = self.kb_articles_dir / platform
            components = [d for d in os.listdir(platform_path) if (platform_path / d).is_dir()]
            
            platform_index_path = platform_path / "index.md"
            with open(platform_index_path, 'w', encoding='utf-8') as f:
                f.write(f"# {platform} Knowledge Base\n\n")
                f.write(f"Technical support training materials for {platform}.\n\n")
                f.write("## Components\n\n")
                
                for component in components:
                    f.write(f"- [{component}](./{component}/index.md)\n")
                
                f.write("\n\n[Back to main index](../index.md)\n")
            
            logger.info(f"Created platform index for {platform}\n")
            
            # Create component indexes
            for component in components:
                component_path = platform_path / component
                features = []
                
                # Collect all feature files (md files) in this component
                for file in os.listdir(component_path):
                    if file.endswith('.md') and file != 'index.md':
                        features.append(file[:-3])  # Remove .md extension
                
                # Also check subdirectories
                for dir_name in os.listdir(component_path):
                    dir_path = component_path / dir_name
                    if dir_path.is_dir():
                        features.append(dir_name)
                
                component_index_path = component_path / "index.md"
                with open(component_index_path, 'w', encoding='utf-8') as f:
                    f.write(f"# {component} ({platform}) Knowledge Base\n\n")
                    f.write(f"Technical support training materials for {component} in {platform}.\n\n")
                    f.write("## Features\n\n")
                    
                    for feature in features:
                        f.write(f"- [{feature}](./{feature}.md)\n")
                    
                    f.write("\n\n[Back to platform index](../index.md) | [Back to main index](../../index.md)\n")
                
                logger.info(f"Created component index for {platform}/{component}")

    def _generate_kb_from_summaries(self, path_filter: Optional[str] = None):
        """
        Generate KB articles from case summaries using GPT.
        
        Args:
            path_filter: Optional path filter
        """
        # Find all summary directories
        directories_to_process = []
        filter_parts = path_filter.split('/') if path_filter else None
        
        # Find all directories to process
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

    def _create_kb_index(self, path_filter: Optional[str] = None):
        """
        Create KB index files.
        
        Args:
            path_filter: Optional path filter
        """
        # Collect all KB articles
        kb_structure = {}
        filter_parts = path_filter.split('/') if path_filter else None
        
        # Scan KB directory
        for platform in os.listdir(self.kb_articles_dir):
            platform_path = self.kb_articles_dir / platform
            if not platform_path.is_dir():
                continue
                
            # Skip if platform doesn't match filter
            if filter_parts and platform != filter_parts[0]:
                continue
                
            kb_structure[platform] = {}
            
            for component in os.listdir(platform_path):
                component_path = platform_path / component
                if not component_path.is_dir():
                    continue
                    
                # Skip if component doesn't match filter (only check if we have more than 1 filter part)  
                if filter_parts and len(filter_parts) >= 2 and component != filter_parts[1]:
                    continue
                    
                kb_structure[platform][component] = []
                
                for feature_file in component_path.glob("*.md"):
                    feature = feature_file.stem
                    
                    # Skip if feature doesn't match filter (only check if we have more than 2 filter parts)
                    if filter_parts and len(filter_parts) >= 3 and feature != filter_parts[2]:
                        continue
                        
                    kb_structure[platform][component].append(feature) 