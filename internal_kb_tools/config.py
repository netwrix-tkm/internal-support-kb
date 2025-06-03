"""
Configuration handling for KB Organizer

This module handles loading and validating configuration settings.
"""

import logging
import os
from pathlib import Path
import yaml

logger = logging.getLogger(__name__)

# Get the base directory (internal-support-kb)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Get the tools directory (internal_kb_tools)
TOOLS_DIR = os.path.join(BASE_DIR, 'internal_kb_tools')

DEFAULT_CONFIG = {
    'input_dir': os.path.join(TOOLS_DIR, 'ticket_data'),
    'output_dir': os.path.join(TOOLS_DIR, 'ticket_processing/collated_ticket_data'),
    'summaries_dir': os.path.join(TOOLS_DIR, 'ticket_processing/ticket_summaries'),
    'kb_articles_dir': os.path.join(BASE_DIR, 'internal_kb_articles'),
    'ticket_file': 'sfdc_tickets_export.csv',
    'email_files': [
        'sfdc_email_export_1.csv', 
        'sfdc_email_export_2.csv', 
        'sfdc_email_export_3.csv'
    ],
    'posts_file': 'sfdc_posts_export.csv',
    'comments_file': 'sfdc_comments_export.csv',
    'stage1_model': 'gpt-4o-mini-support',
    'stage1_prompt_template': os.path.join(TOOLS_DIR, 'templates/stage1_prompt.txt'),
    'stage1_batch_size': 10,
    'stage1_max_retries': 3,
    'stage1_retry_delay': 5,
    'stage2_model': 'gpt-4o-support',
    'stage2_prompt_template': os.path.join(TOOLS_DIR, 'templates/stage2_prompt.txt'),
    'stage2_batch_size': 50,
    'stage2_max_retries': 3,
    'stage2_retry_delay': 10,
    'logging_level': 'INFO',
    'target_statuses': ["Closed - Resolved", "Closed - Resolved on first contact"],
    'ticket_record_type': "Support Ticket"
}

def load_config(config_path='config.yaml'):
    """
    Load configuration from a YAML file, falling back to defaults if needed.
    
    Args:
        config_path: Path to the configuration file
        
    Returns:
        dict: Configuration dictionary
    """
    config = DEFAULT_CONFIG.copy()
    
    # Try to load from config file
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                file_config = yaml.safe_load(f)
                if file_config:
                    config.update(file_config)
            logger.info(f"Loaded configuration from {config_path}")
        except Exception as e:
            logger.warning(f"Failed to load config from {config_path}: {e}")
    else:
        logger.info(f"Config file {config_path} not found, using defaults")
        
        # Create default config file if it doesn't exist
        try:
            os.makedirs(os.path.dirname(os.path.abspath(config_path)), exist_ok=True)
            with open(config_path, 'w') as f:
                yaml.dump(DEFAULT_CONFIG, f, default_flow_style=False)
            logger.info(f"Created default config file at {config_path}")
        except Exception as e:
            logger.warning(f"Failed to create default config file: {e}")
    
    return config 