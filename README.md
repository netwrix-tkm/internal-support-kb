# Internal Support Knowledge Base Generator

A tool for processing Salesforce support case exports into a structured knowledge base. The system organizes cases by Platform/Component/Feature, processes them with a two-stage LLM pipeline, and creates comprehensive technical documentation.

## Directory Structure

- `internal_kb_tools/`: Core processing scripts
  - `ticket_data/`: Raw CSV exports from Salesforce
  - `ticket_processing/`: Processed ticket data
    - `collated_ticket_data/`: Organized CSV files
    - `ticket_summaries/`: Generated case summaries
  - `internal_kb_articles/`: Generated knowledge base articles
  - `templates/`: Prompt templates for LLM processing

## Usage

Use the launcher script to run the tool:

```bash
# Stage 1: Process and summarize cases
python run_kb_tool.py --stage 1 --path "Platform"

# Stage 2: Generate knowledge base articles
python run_kb_tool.py --stage 2 --path "Platform"
```

You can specify paths at different levels of specificity:
- Just the platform name (e.g., "Netwrix Endpoint Protector") to process all components and features
- Platform/Component (e.g., "Netwrix Endpoint Protector/Device Control") to process all features of a component
- Platform/Component/Feature (e.g., "Netwrix Endpoint Protector/Device Control/Custom Classes") to process a specific feature

### VS Code Tasks

VS Code tasks are configured to streamline the workflow. Access them via the Command Palette (`Ctrl+Shift+P`) and select "Tasks: Run Task", then choose from:

- **Run KB Tool Stage 1**: Run Stage 1 processing with product name input
- **Run KB Tool Stage 2**: Run Stage 2 KB generation with product name input 

When prompted, enter just the product name (e.g., "Netwrix Endpoint Protector") to process all components and features for that product.

### Parameters

- `--stage`: Processing stage
  - `1`: Organize data and generate summaries
  - `2`: Generate knowledge base articles
- `--path`: Path filter (Platform, Platform/Component, or Platform/Component/Feature)
- `--config`: Path to configuration file (default: internal_kb_tools/config.yaml)

## Configuration

The tool is configured with the `internal_kb_tools/config.yaml` file. Key settings include:

- Input/output directories
- Source file names
- LLM model configuration
- Processing batch sizes

## Requirements

- Python 3.8+
- Packages listed in requirements.txt
- Azure OpenAI API access (set AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, and AZURE_OPENAI_VERSION environment variables)

## Data Processing Pipeline

1. **Data Organization**: Parse CSV exports and organize into Platform/Component/Feature structure
2. **Stage 1 - Case Summarization**: Process each case with GPT-4o-mini to generate concise summaries
3. **Stage 2 - KB Generation**: Process all summaries in a category with GPT-4o to generate comprehensive knowledge base articles

## Notes

- Only processes tickets created after June 1, 2024 (configurable in code)
- Handles multiline content in CSV exports properly
- Includes robust error handling and retry mechanisms

## Design Decisions

1. **Chunked Processing**: Large CSV files are processed in chunks to manage memory usage
2. **Rate Limiting**: API calls include delays and retries to handle rate limits
3. **Intermediate Storage**: All intermediate results are stored to enable restarting at any point
4. **Path Filtering**: Processing can be limited to specific paths to support incremental updates
5. **Batch Processing**: Summaries are processed in batches to handle large volumes efficiently

## Error Handling

- All errors are logged to both console and a log file (`kb_organizer.log`)
- The system will attempt to continue processing other cases when one fails
- API calls include retry logic with configurable retry counts and delays

## Log File

The application logs all operations to `kb_organizer.log`. Check this file for error details and processing information.

## License

This project is proprietary and for internal Netwrix use only. 