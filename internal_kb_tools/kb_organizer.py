#!/usr/bin/env python
"""
Knowledge Base Organizer

Main script for organizing and processing support tickets into a structured knowledge base.
"""

import argparse
import logging
import os
import sys
from pathlib import Path
from typing import Dict
import os.path

# Adjust path to include the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Import local modules
from config import load_config
from data_processor import DataProcessor
from llm_pipeline import LLMPipeline
from kb_generator import KBGenerator

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(os.path.join(current_dir, 'kb_organizer.log'))
    ]
)
logger = logging.getLogger(__name__)

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Organize and process support tickets into a structured knowledge base"
    )
    
    parser.add_argument(
        "--stage", 
        type=int,
        choices=[1, 2], 
        required=True,
        help="Processing stage: 1=organize and summarize, 2=generate KB articles"
    )
    
    parser.add_argument(
        "--path",
        type=str,
        help="Optional path filter (e.g., 'Platform/Component/Feature')"
    )
    
    parser.add_argument(
        "--config",
        type=str,
        default=os.path.join(current_dir, "config.yaml"),
        help="Path to configuration file"
    )
    
    return parser.parse_args()

def main():
    """Main entry point."""
    args = parse_args()
    
    logger.info(f"Starting knowledge base organizer (stage {args.stage})")
    
    # Load configuration
    config = load_config(args.config)
    logger.info(f"Loaded configuration from {args.config}")
    
    # Update logging level if specified in config
    if 'logging_level' in config:
        logging_level = getattr(logging, config['logging_level'])
        logging.getLogger().setLevel(logging_level)
    
    if args.stage == 1:
        # Stage 1: Organize data and generate summaries
        logger.info("Running Stage 1: Organizing data and generating summaries")
        
        # Initialize DataProcessor
        data_processor = DataProcessor(config)
        # Process tickets and related data
        data_processor.process_data(args.path)
        
        # Initialize LLM pipeline for stage 1
        llm_pipeline = LLMPipeline(config)
        # Generate summaries
        llm_pipeline.run_stage1(args.path)
        
    elif args.stage == 2:
        # Stage 2: Generate knowledge base articles
        logger.info("Running Stage 2: Generating knowledge base articles")
        
        # Initialize KB generator
        kb_generator = KBGenerator(config)
        # Generate KB articles
        kb_generator.generate_kb(args.path)

if __name__ == "__main__":
    main() 