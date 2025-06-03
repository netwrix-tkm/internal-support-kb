# Internal Support Knowledge Base

An intelligent system for capturing, organizing, and publishing troubleshooting knowledge from resolved support tickets. This tool converts raw support data into structured, searchable knowledge base articles that support teams can reference, update, and use for training new hires.

## Overview and Vision

The Internal Support Knowledge Base is designed to capture critical troubleshooting information from resolved support tickets and transform it into a valuable knowledge repository. Key aspects:

- **Real-time Knowledge Capture**: Eventually will process tickets within 3 minutes of closure to ensure knowledge is immediately preserved
- **Comprehensive Coverage**: Documents solutions for every product, component, and feature
- **AI-Powered Processing**: Uses advanced language models to analyze ticket content and generate structured documentation
- **Self-Improving System**: Knowledge base continuously grows and improves with each resolved ticket
- **Training Resource**: Serves as a comprehensive training resource for new support team members

By July 2024, the knowledge base will be published on Docusaurus, restricted to Netwrix employees only, with full search and editing capabilities.

## Future Enhancements

- **AI Support Agent**: Knowledge will be vectorized to create a support onboarding AI assistant that helps new team members learn everything needed for success
- **Full Automation**: The final system will automatically evaluate every ticket solution and add appropriate content to the KB

## AI-Powered Knowledge Extraction

This system uses artificial intelligence to transform raw support data into structured knowledge:

1. **Data Collection**: Processes multiple data sources:
   - Ticket data with details and solutions
   - Email communications between support and customers
   - Internal text posts in the ticket feed
   - Comments from R&D

2. **AI Processing Pipeline**:
   - **Stage 1 - Organization and Analysis**: 
     - Raw CSV data is parsed and organized by product/component/feature
     - GPT-4o-mini analyzes each case to identify key information, challenges, and solutions
     - Cases are summarized with technical details preserved
   
   - **Stage 2 - Knowledge Synthesis**:
     - GPT-4o processes all related case summaries for a feature
     - Creates comprehensive markdown articles that synthesize solutions, troubleshooting approaches, and best practices
     - Automatically structures content with headings, code blocks, and procedural steps
     - Preserves technical accuracy while improving readability

3. **Knowledge Organization**:
   - Articles are organized in a hierarchical structure (Product → Component → Feature)
   - Cross-linking between related topics
   - Technical details are preserved but presented in a consistent, readable format

## Directory Structure

- `internal_kb_tools/`: Core processing scripts
  - `ticket_data/`: Raw CSV exports from Salesforce (excluded from GitHub due to file size)
  - `ticket_processing/`: Processed ticket data
    - `collated_ticket_data/`: Organized CSV files
    - `ticket_summaries/`: Generated case summaries
  - `templates/`: Prompt templates for LLM processing
- `internal_kb_articles/`: Generated knowledge base articles

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

### Parameters

- `--stage`: Processing stage
  - `1`: Organize data and generate summaries
  - `2`: Generate knowledge base articles
- `--path`: Path filter (Platform, Platform/Component, or Platform/Component/Feature)
- `--config`: Path to configuration file (default: internal_kb_tools/config.yaml)

## Requirements

- Python 3.8+
- Packages listed in requirements.txt
- Azure OpenAI API access (set AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, and AZURE_OPENAI_VERSION environment variables)

## Technical Workflow

1. **Data Ingestion**: Parses multiple CSV files (tickets, emails, posts, comments) with special handling for multiline content
2. **Data Organization**: Classifies and organizes information by product hierarchy
3. **Stage 1 - Case Analysis**: Processes each case to extract key troubleshooting knowledge
4. **Stage 2 - Knowledge Synthesis**: Combines insights from multiple cases into comprehensive articles
5. **Output**: Generates markdown files ready for publishing to the knowledge base

## Benefits

- **Knowledge Preservation**: Captures critical troubleshooting expertise that would otherwise be lost
- **Consistency**: Ensures consistent documentation across all products
- **Efficiency**: Reduces the time to onboard new support team members
- **Continuous Improvement**: Knowledge base grows and improves with each resolved ticket

## License

This project is proprietary and for internal Netwrix use only. 