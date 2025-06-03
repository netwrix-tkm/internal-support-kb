#!/usr/bin/env python
"""
Knowledge Base Utilities

Helper functions for the KB tool.
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Optional

def list_available_products(base_dir: str, data_type: str = "data") -> List[Dict[str, str]]:
    """
    List all available products, components, and features in the KB.
    
    Args:
        base_dir: Base directory path
        data_type: Type of data to list ("data" for ticket data, "summaries" for summaries)
        
    Returns:
        List of dictionaries with platform, component, and feature information
    """
    if data_type == "data":
        directory = Path(base_dir) / "internal_kb_tools" / "ticket_processing" / "collated_ticket_data"
    elif data_type == "summaries":
        directory = Path(base_dir) / "internal_kb_tools" / "ticket_processing" / "ticket_summaries"
    else:
        directory = Path(base_dir) / data_type
    
    results = []
    
    if not directory.exists():
        return results
        
    for platform in os.listdir(directory):
        platform_path = directory / platform
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
                    
                # Count files in the directory
                file_count = len([f for f in os.listdir(feature_path) 
                                 if os.path.isfile(feature_path / f)])
                    
                results.append({
                    "platform": platform,
                    "component": component,
                    "feature": feature,
                    "path": f"{platform}/{component}/{feature}",
                    "file_count": file_count
                })
    
    return results

def print_available_products(base_dir: str, data_type: str = "data"):
    """
    Print all available products, components, and features in the KB.
    
    Args:
        base_dir: Base directory path
        data_type: Type of data to list ("data" for ticket data, "summaries" for summaries)
    """
    products = list_available_products(base_dir, data_type)
    
    if not products:
        print(f"No {data_type} found.")
        return
        
    print(f"\nAvailable products in {data_type}:")
    print("-" * 80)
    print(f"{'Platform':<25} {'Component':<25} {'Feature':<25} {'Files':<5}")
    print("-" * 80)
    
    for product in products:
        print(f"{product['platform']:<25} {product['component']:<25} {product['feature']:<25} {product['file_count']:<5}")
    
    print("-" * 80)
    print(f"Total: {len(products)} feature paths found\n")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        data_type = sys.argv[1]
    else:
        data_type = "data"
        
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print_available_products(base_dir, data_type) 