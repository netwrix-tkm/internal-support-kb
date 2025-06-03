"""
Data Processor Module

Handles reading and processing Salesforce CSV export data into a structured format.
"""

import csv
import logging
import os
from pathlib import Path
import pandas as pd
from typing import Dict, List, Optional, Tuple, Set

logger = logging.getLogger(__name__)

class DataProcessor:
    """Processes Salesforce CSV data and organizes it into a structured folder hierarchy."""
    
    def __init__(self, config: Dict):
        """
        Initialize the data processor.
        
        Args:
            config: Configuration dictionary
        """
        self.config = config
        self.input_dir = Path(config['input_dir'])
        self.output_dir = Path(config['output_dir'])
        self.target_statuses = set(config['target_statuses'])
        self.ticket_record_type = config['ticket_record_type']
        
    def process_data(self, path_filter: Optional[str] = None) -> Dict:
        """
        Process data from CSV files and organize it into folders.
        
        Args:
            path_filter: Optional filter for specific platform/component/feature path
            
        Returns:
            Dict: Structure of organized cases
        """
        logger.info("Processing ticket data and organizing into folders")
        
        # Process tickets to get filtered data structure
        case_structure = self._process_tickets(path_filter)
        
        # Process related data (emails, posts, comments)
        self._process_related_data(case_structure)
        
        return case_structure
    
    def _process_tickets(self, path_filter: Optional[str] = None) -> Dict:
        """
        Process ticket data and create folder structure.
        
        Args:
            path_filter: Optional path filter
            
        Returns:
            Dict: Structure of all cases organized by platform/component/feature
        """
        ticket_path = self.input_dir / self.config['ticket_file']
        logger.info(f"Processing tickets from {ticket_path}")
        
        case_structure = {}
        filter_parts = path_filter.split('/') if path_filter else None
        
        # Define date filter (June 1, 2024)
        date_filter = "2024-06-01T00:00:00.000Z"
        logger.info(f"Filtering tickets created on or after {date_filter}")
        
        # Try parsing with pandas first
        try:
            logger.info("Attempting to process tickets with pandas")
            # Use pandas with the python engine which is better at handling problematic files
            df = pd.read_csv(
                ticket_path, 
                encoding='utf-8', 
                quoting=csv.QUOTE_ALL,  # Quote all fields
                quotechar='"',  # Use double quotes for quoting
                escapechar='\\',  # Use backslash as escape character
                on_bad_lines='skip',  # Skip bad lines
                engine='python',  # Use the Python parser
                low_memory=False,  # Don't use low_memory mode
            )
            
            # Filter based on Status, Record Type, and CreatedDate
            filtered_df = df[
                (df['Status'].isin(self.target_statuses)) & 
                (df['Ticket_Record_Type_Name__c'] == self.ticket_record_type) &
                (df['CreatedDate'] >= date_filter)  # Add date filter
            ]
            
            # Process each row
            for _, row in filtered_df.iterrows():
                self._process_ticket_row(row, case_structure, filter_parts)
                
        except Exception as e:
            logger.error(f"Error processing tickets with pandas: {e}")
            logger.info("Falling back to manual CSV processing")
            
            # Fallback to manual CSV parsing, line by line
            with open(ticket_path, 'r', encoding='utf-8', errors='ignore') as f:
                csv_reader = csv.reader(f, quoting=csv.QUOTE_ALL, quotechar='"', escapechar='\\')
                
                # Read header
                headers = next(csv_reader, [])
                if not headers:
                    logger.error("Could not read headers from ticket file")
                    return case_structure
                
                # Find the index of important columns
                id_index = -1
                status_index = -1
                record_type_index = -1
                platform_index = -1
                component_index = -1
                feature_index = -1
                created_date_index = -1  # Add created date index
                
                for i, header in enumerate(headers):
                    if header == 'Id':
                        id_index = i
                    elif header == 'Status':
                        status_index = i
                    elif header == 'Ticket_Record_Type_Name__c':
                        record_type_index = i
                    elif header == 'Platform__c':
                        platform_index = i
                    elif header == 'Collector_Code__c':
                        component_index = i
                    elif header == 'Feature__c':
                        feature_index = i
                    elif header == 'CreatedDate':
                        created_date_index = i  # Store created date index
                
                if id_index == -1 or status_index == -1 or record_type_index == -1 or created_date_index == -1:
                    logger.error("Required columns not found in ticket file")
                    return case_structure
                
                # Process rows
                for row_idx, row in enumerate(csv_reader, 1):
                    try:
                        # Make sure the row has enough elements
                        max_index = max(id_index, status_index, record_type_index, 
                                      platform_index, component_index, feature_index, created_date_index)
                        if len(row) <= max_index:
                            logger.warning(f"Row {row_idx} has insufficient fields, skipping")
                            continue
                        
                        # Check if created date meets filter
                        created_date = row[created_date_index]
                        if created_date < date_filter:
                            continue  # Skip tickets created before June 1, 2024
                        
                        # Check if this ticket matches our criteria
                        status = row[status_index]
                        record_type = row[record_type_index]
                        
                        if status in self.target_statuses and record_type == self.ticket_record_type:
                            # Create a dict representation of the row
                            row_dict = {}
                            for i, value in enumerate(row):
                                if i < len(headers):
                                    row_dict[headers[i]] = value
                            
                            # Process the row
                            self._process_ticket_row(pd.Series(row_dict), case_structure, filter_parts)
                    except Exception as e:
                        logger.error(f"Error processing row {row_idx}: {e}")
        
        # Log summary
        total_cases = sum(
            len(cases) 
            for platform in case_structure.values() 
            for component in platform.values() 
            for cases in component.values()
        )
        logger.info(f"Processed {total_cases} cases matching criteria (created on or after June 1, 2024)")
        return case_structure
        
    def _process_ticket_row(self, row, case_structure: Dict, filter_parts: Optional[List[str]]):
        """
        Process a single ticket row and add it to the case structure.
        
        Args:
            row: Row data (pandas Series or dict-like)
            case_structure: Case structure to update
            filter_parts: Optional path filter parts
        """
        # Extract values safely with defaults
        platform = str(row.get('Platform__c', '')).strip() or 'Unknown_Platform'
        component = str(row.get('Collector_Code__c', '')).strip() or 'Unknown_Component'
        feature = str(row.get('Feature__c', '')).strip() or 'Unknown_Feature'
        
        # Clean up path components to ensure they are valid directory names
        platform = self._clean_path_component(platform)
        component = self._clean_path_component(component)
        feature = self._clean_path_component(feature)
        
        # Skip if doesn't match path filter
        if filter_parts:
            # If only product name is provided, only check platform
            if len(filter_parts) == 1:
                if platform != filter_parts[0]:
                    return
            # Otherwise check all parts of the path
            else:
                parts_to_check = [platform, component, feature][:len(filter_parts)]
                if parts_to_check != filter_parts:
                    return
        
        # Create the structure if it doesn't exist
        if platform not in case_structure:
            case_structure[platform] = {}
        if component not in case_structure[platform]:
            case_structure[platform][component] = {}
        if feature not in case_structure[platform][component]:
            case_structure[platform][component][feature] = []
        
        # Add case to structure
        case_id = row['Id']
        case_structure[platform][component][feature].append(case_id)
        
        # Create folder structure
        folder_path = self.output_dir / platform / component / feature
        folder_path.mkdir(parents=True, exist_ok=True)
        
        # Write case file - using proper quoting to preserve newlines
        case_file = folder_path / f"{case_id}.csv"
        with open(case_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(row.index)
            writer.writerow(row.values)
    
    def _clean_path_component(self, path_component: str) -> str:
        """
        Clean a path component to ensure it's a valid directory name.
        
        Args:
            path_component: Path component string
            
        Returns:
            str: Cleaned path component
        """
        # Replace invalid characters with underscores
        invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
        cleaned = path_component
        
        for char in invalid_chars:
            cleaned = cleaned.replace(char, '_')
            
        # Remove leading/trailing spaces and dots
        cleaned = cleaned.strip('. ')
        
        # Replace multiple spaces with a single space
        cleaned = ' '.join(cleaned.split())
        
        # If empty after cleaning, use a default
        if not cleaned:
            cleaned = "Unknown"
            
        return cleaned
    
    def _process_related_data(self, case_structure: Dict):
        """
        Process related data (emails, posts, comments) for each case.
        
        Args:
            case_structure: Structure of cases organized by platform/component/feature
        """
        # Create a flat set of all case IDs for faster lookup
        all_case_ids = {
            case_id 
            for platform in case_structure.values()
            for component in platform.values()
            for feature in component.values()
            for case_id in feature
        }
        
        # Process emails
        for email_file in self.config['email_files']:
            self._process_relationship_file(
                file_path=self.input_dir / email_file,
                case_ids=all_case_ids,
                id_field='Id',
                parent_id_field='ParentId',
                output_suffix='_emails'
            )
        
        # Process posts
        self._process_relationship_file(
            file_path=self.input_dir / self.config['posts_file'],
            case_ids=all_case_ids,
            id_field='Id',
            parent_id_field='ParentId',
            output_suffix='_posts'
        )
        
        # Process comments
        self._process_relationship_file(
            file_path=self.input_dir / self.config['comments_file'],
            case_ids=all_case_ids,
            id_field='Id',
            parent_id_field='ParentId',
            output_suffix='_comments'
        )
    
    def _process_relationship_file(self, file_path: Path, case_ids: Set[str], 
                                   id_field: str, parent_id_field: str, 
                                   output_suffix: str):
        """
        Process a relationship file (emails, posts, comments) and associate with cases.
        
        Args:
            file_path: Path to the relationship file
            case_ids: Set of case IDs to match against
            id_field: Field name for the record ID
            parent_id_field: Field name for the parent case ID
            output_suffix: Suffix to append to output file names
        """
        logger.info(f"Processing related data from {file_path}")
        
        # Find case locations for faster lookup
        case_locations = {}
        for platform in os.listdir(self.output_dir):
            platform_path = self.output_dir / platform
            if not platform_path.is_dir():
                continue
                
            for component in os.listdir(platform_path):
                component_path = platform_path / component
                if not component_path.is_dir():
                    continue
                    
                for feature in os.listdir(component_path):
                    feature_path = component_path / feature
                    if not feature_path.is_dir():
                        continue
                        
                    for file in os.listdir(feature_path):
                        if file.endswith('.csv') and not file.endswith(output_suffix + '.csv'):
                            case_id = file.split('.')[0]
                            if case_id in case_ids:
                                case_locations[case_id] = feature_path
        
        # Check if case locations were found
        if not case_locations:
            logger.info(f"No matching case locations found for {file_path.name}")
            return
            
        # Track which cases have records to avoid empty files
        cases_with_records = set()
        
        # Use a dictionary to collect records by parent ID
        records_by_parent = {}
        
        try:
            # Try to parse the file using pandas with more robust settings
            try:
                # Read the first few lines to get headers
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    header_line = f.readline().strip()
                    
                # Use pandas with the python engine which is better at handling problematic files
                df = pd.read_csv(
                    file_path, 
                    encoding='utf-8', 
                    quoting=csv.QUOTE_ALL,  # Quote all fields
                    quotechar='"',  # Use double quotes for quoting
                    escapechar='\\',  # Use backslash as escape character
                    on_bad_lines='skip',  # Skip bad lines
                    engine='python',  # Use the Python parser
                    low_memory=False,  # Don't use low_memory mode
                )
                
                # Check if parent ID field exists in the dataframe
                if parent_id_field in df.columns:
                    # Filter to only rows related to our cases
                    filtered_df = df[df[parent_id_field].isin(case_ids)]
                    
                    # Group records by parent ID
                    for _, row in filtered_df.iterrows():
                        parent_id = row[parent_id_field]
                        if parent_id not in records_by_parent:
                            records_by_parent[parent_id] = []
                        records_by_parent[parent_id].append(row)
                        cases_with_records.add(parent_id)
                else:
                    logger.warning(f"Parent ID field '{parent_id_field}' not found in {file_path.name}")
                    
            except Exception as e:
                logger.error(f"Error reading {file_path} with pandas: {e}")
                logger.info(f"Falling back to manual CSV parsing for {file_path.name}")
                
                # Use a more robust CSV parser that preserves all content
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    # Read the header line
                    csv_reader = csv.reader(f, quotechar='"', quoting=csv.QUOTE_ALL, escapechar='\\')
                    headers = next(csv_reader, [])
                    
                    # Find the indices for the important fields
                    id_index = -1
                    parent_id_index = -1
                    
                    for i, header in enumerate(headers):
                        if header == id_field:
                            id_index = i
                        if header == parent_id_field:
                            parent_id_index = i
                    
                    if parent_id_index == -1:
                        logger.error(f"Parent ID field '{parent_id_field}' not found in header")
                        return
                    
                    # Process each row
                    line_count = 0
                    for row in csv_reader:
                        line_count += 1
                        if line_count % 100000 == 0:
                            logger.info(f"Processed {line_count} lines from {file_path.name}")
                        
                        try:
                            # Check if this record is related to one of our cases
                            if parent_id_index < len(row) and row[parent_id_index] in case_ids:
                                parent_id = row[parent_id_index]
                                record = pd.Series(dict(zip(headers, row)))
                                
                                if parent_id not in records_by_parent:
                                    records_by_parent[parent_id] = []
                                records_by_parent[parent_id].append(record)
                                cases_with_records.add(parent_id)
                        except Exception as e:
                            logger.debug(f"Error processing line {line_count}: {e}")
                            continue
                
        except Exception as e:
            logger.error(f"Failed to process {file_path.name}: {e}")
            return
        
        # Write records to files
        for case_id in cases_with_records:
            if case_id in case_locations:
                output_file = case_locations[case_id] / f"{case_id}{output_suffix}.csv"
                records = records_by_parent.get(case_id, [])
                
                if records:  # Only write if there are records
                    try:
                        with open(output_file, 'w', newline='', encoding='utf-8') as f:
                            # Use csv writer with proper quoting to preserve all content
                            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
                            writer.writerow(records[0].index)  # Header
                            for record in records:
                                writer.writerow(record.values)
                    except Exception as e:
                        logger.error(f"Error writing {output_file}: {e}")
        
        logger.info(f"Added {output_suffix} data for {len(cases_with_records)} cases") 

    def _save_case_file(self, case_id: str, content: str, platform: str, component: str, feature: str):
        """
        Save a case file to the appropriate directory structure.
        
        Args:
            case_id: Case ID
            content: Content to save
            platform: Platform name
            component: Component name
            feature: Feature name
        """
        # Create the directory structure
        case_dir = self.output_dir / platform / component / feature
        case_dir.mkdir(parents=True, exist_ok=True)
        
        # Save the case file
        case_file = case_dir / f"{case_id}.csv"
        with open(case_file, 'w', encoding='utf-8', newline='') as f:
            f.write(content)

        logger.debug(f"Saved case file: {case_file}")
        
        return case_file 