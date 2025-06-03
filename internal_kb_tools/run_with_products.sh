#!/bin/bash
# Script to list available products and then run the KB tool

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

# Ensure we're using the virtual environment if it exists
if [ -d "$PARENT_DIR/.venv" ]; then
  source "$PARENT_DIR/.venv/Scripts/activate" 2>/dev/null || source "$PARENT_DIR/.venv/bin/activate" 
  echo "Activated virtual environment"
fi

# Check arguments
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <stage>"
  echo "  stage: 1 or 2"
  exit 1
fi

STAGE=$1

# List available products
echo "Listing available products for stage $STAGE..."
python "$SCRIPT_DIR/list_products.py" --stage "$STAGE"

if [ $? -ne 0 ]; then
  echo "Failed to list products. Trying alternative approach..."
  cd "$PARENT_DIR"
  python -m internal_kb_tools.list_products --stage "$STAGE"
  
  if [ $? -ne 0 ]; then
    echo "Error listing products. Please check your setup."
    exit 1
  fi
fi

# Ask for product path
echo ""
echo "Enter product path from the list above (e.g. 'Netwrix Endpoint Protector/Device Control/Custom Classes'):"
read -r PRODUCT_PATH

# Run the KB tool
echo "Running KB tool stage $STAGE for path: $PRODUCT_PATH"
python "$PARENT_DIR/run_kb_tool.py" --stage "$STAGE" --path "$PRODUCT_PATH"

if [ $? -ne 0 ]; then
  echo "Failed to run KB tool. Trying alternative approach..."
  cd "$PARENT_DIR"
  python run_kb_tool.py --stage "$STAGE" --path "$PRODUCT_PATH"
fi 