# Knowledge Base Reference Guide: Troubleshooting Custom Reports in Netwrix Enterprise Auditor

## Overview

Custom Reports in Netwrix Enterprise Auditor allow users to tailor data presentation to meet specific organizational needs. This category covers issues related to report customization, including data scope limitations, formatting challenges, and automation requirements. Understanding this category is critical for ensuring customers can leverage Netwrix Enterprise Auditor effectively to monitor and audit their environments.

## Technical Background

### Key Concepts
- **Netwrix Enterprise Auditor**: A platform for auditing IT environments, providing visibility into changes, configurations, and access permissions.
- **Custom Reports**: User-defined reports that extract and present data based on specific criteria.
- **StealthAUDIT for NetApp**: A collector module used to gather data from NetApp storage systems, including permission changes and folder activity.
- **Shares vs. Local Folders**: Shares refer to top-level network resources accessible across systems, while local folders are specific to individual systems.

### System Context
Custom Reports rely on data collected by modules like StealthAUDIT for NetApp. The scope of data included in reports is determined by the configuration of the collector and the report query parameters. Misconfigurations or incomplete queries can lead to gaps in the data presented.

## Issue Recognition & Triage

### Symptoms
- Reports fail to include expected data (e.g., permission changes for shares).
- Customers request modifications to expand report scope.
- Duplicate reports or excessive notifications cause confusion.

### Priority Assessment
- **High Priority**: Reports critical for compliance or security monitoring are incomplete.
- **Medium Priority**: Reports require enhancements for operational efficiency.
- **Low Priority**: Cosmetic or formatting adjustments.

## Diagnostic Methodology

### Systematic Approach
1. **Understand the Report Scope**: Review the report configuration and query parameters to identify limitations.
2. **Clarify Customer Requirements**: Engage with the customer to determine the desired data scope and report functionality.
3. **Verify Collector Configuration**: Ensure the relevant collector module (e.g., StealthAUDIT for NetApp) is properly configured to gather the required data.
4. **Test Report Adjustments**: Modify the report query and validate the output against customer expectations.
5. **Automate and Optimize**: Set up scheduled reports and disable duplicates to streamline operations.

## Information Collection

### Customer Questions
- What specific data is missing from the report?
- Are there particular shares or folders that need to be included?
- How frequently should the report be generated and delivered?
- Are there any additional formatting or automation requirements?

### Logs and Data to Collect
- Current report configuration and query parameters.
- Collector module settings (e.g., StealthAUDIT for NetApp).
- Sample output from the existing report.
- Error logs or system messages related to report generation.

## Common Scenarios & Solutions

### Scenario 1: Missing Data from Shares
**Symptoms**: Reports only include local folder data, excluding top-level shares.  
**Resolution**: Modify the report query to include permission changes for shares. Validate the collector configuration to ensure it gathers data from all relevant sources.

### Scenario 2: Duplicate Reports
**Symptoms**: Multiple reports with overlapping data are generated, causing confusion.  
**Resolution**: Identify and disable duplicate reports. Consolidate data into a single, comprehensive report.

### Scenario 3: Automation Requests
**Symptoms**: Customers request scheduled delivery of reports via email.  
**Resolution**: Configure report scheduling and email notifications. Test the automation to ensure reliability.

## Detailed Case Studies

### Case Study: Expanding Report Scope to Include Shares
**Ticket ID**: [500Qk00000GZA4yIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GZA4yIAH/view)  
**Initial Symptoms**: The customer reported that their existing report only displayed permission changes for user directories, excluding top-level shares.  
**Diagnostic Steps**:  
1. Reviewed the report configuration and identified that it was limited to local folders.  
2. Engaged with the customer to clarify the requirement for including all shares.  
3. Investigated the feasibility of modifying the report query without requiring professional services.  
4. Tested adjustments to the report query to include permission changes for shares.  

**Key Information Leading to Solution**: The collector module (StealthAUDIT for NetApp) was configured to gather data from shares, but the report query did not utilize this data. Expanding the query resolved the issue.  

**Resolution**: Developed a new report that included permission changes for the top two levels of shares. Scheduled weekly email delivery of the report to meet customer requirements.  

**Key Takeaways**:  
- Always verify collector configuration when reports exclude expected data.  
- Engage with customers to clarify requirements before making adjustments.  
- Automate report delivery to improve efficiency and customer satisfaction.  

**Efficiency Improvements**: Standardize report templates to include both local folders and shares by default.

## Best Practices & Tips

- **Standardize Report Templates**: Ensure default templates include comprehensive data scopes to minimize customization requests.
- **Engage Early with Customers**: Clarify requirements upfront to avoid unnecessary iterations.
- **Test Before Deployment**: Validate report adjustments in a test environment before delivering to customers.
- **Automate Report Delivery**: Use scheduling features to streamline operations and reduce manual effort.
- **Disable Duplicates**: Consolidate overlapping reports to prevent confusion and reduce system load.

## Escalation Guidelines

### Criteria for Escalation
- Report adjustments require changes to collector module configurations beyond standard support capabilities.
- Customer requests involve complex customizations that may require professional services.
- Issues persist despite following standard troubleshooting steps.

### Escalation Procedure
1. Document all troubleshooting steps and findings.
2. Provide detailed logs and customer requirements.
3. Escalate to the appropriate team (e.g., Professional Services or Development) with a clear summary of the issue and proposed next steps.