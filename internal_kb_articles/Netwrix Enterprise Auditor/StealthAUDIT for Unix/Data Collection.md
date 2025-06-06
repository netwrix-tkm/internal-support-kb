# Netwrix Enterprise Auditor Knowledge Base Reference Guide  
## Overview  
This guide focuses on troubleshooting issues related to data collection in Netwrix Enterprise Auditor (NEA) when using the StealthAUDIT for Unix component. Specifically, it addresses scenarios where alias information or permissions are not captured correctly, impacting reporting accuracy. Understanding and resolving these issues is critical for ensuring comprehensive audit data collection and maintaining customer trust in the product's capabilities.  

## Technical Background  
Netwrix Enterprise Auditor (NEA) is a platform designed to provide visibility into IT environments by collecting and analyzing audit data. The StealthAUDIT for Unix component is used for data collection from Unix-based systems, including file systems and storage platforms.  

Key concepts:  
- **Aliases**: Alternate names or references for file system objects, often used in storage platforms like Cohesity.  
- **Permissions**: Access control settings that define user and group rights to file system objects.  
- **Data Collection Jobs**: Automated processes configured in NEA to gather audit data from target systems.  
- **Unsupported Platforms**: Systems not officially supported by NEA may exhibit limited functionality or require custom configurations.  

## Issue Recognition & Triage  
### Symptoms  
- Missing alias information in audit reports.  
- Permissions not captured correctly for specific file systems or storage platforms.  
- No errors reported in data collection jobs, but incomplete data is observed.  

### Priority Assessment  
- **High Priority**: If the issue impacts compliance reporting or critical audit functions.  
- **Medium Priority**: If the issue affects non-critical systems or secondary reporting features.  

## Diagnostic Methodology  
### Step-by-Step Approach  
1. **Verify Platform Compatibility**: Check if the target system (e.g., Cohesity) is officially supported by NEA. Unsupported platforms may require custom configurations or manual adjustments.  
2. **Review Data Collection Job Logs**: Examine logs for errors or warnings that could indicate configuration issues.  
3. **Reproduce the Issue**: Run the data collection job and confirm the missing alias or permissions data.  
4. **Analyze Permissions Settings**: Investigate the target system's permissions configuration to ensure compatibility with NEA's data collection mechanisms.  
5. **Engage Customer**: Schedule a web meeting to review the environment and settings with the customer.  

## Information Collection  
### Customer Requests  
- **PowerShell Output**: Request output from diagnostic scripts to gather information about installed Netwrix and Stealth applications.  
- **Job Logs**: Collect logs from the affected data collection jobs for analysis.  
- **Environment Details**: Confirm platform version, build number, and configuration settings.  

### Logs to Examine  
- **Data Collection Job Logs**: Look for errors, warnings, or incomplete data entries.  
- **System Logs**: Review logs from the target system (e.g., Cohesity) for permission-related issues.  

## Common Scenarios & Solutions  
### Scenario 1: Missing Alias Information  
- **Root Cause**: Permissions set incorrectly on the target system, preventing alias data from being captured.  
- **Resolution**: Adjust permissions settings within the target system to ensure compatibility with NEA's data collection mechanisms.  

### Scenario 2: Unsupported Platform  
- **Root Cause**: The target system (e.g., Cohesity) is not officially supported by NEA, leading to limited functionality.  
- **Resolution**: Work with the customer to identify alternative configurations or manual data collection methods.  

## Detailed Case Studies  
### Case Study: Missing Alias Information on Cohesity  
- **Ticket ID**: [500Qk00000CzbYPIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CzbYPIAZ/view)  
- **Initial Symptoms**: Customer reported missing alias information for permissions determination across their filer system. No errors were observed in the data collection job logs.  
- **Diagnostic Steps**:  
  1. Requested PowerShell output to verify installed applications and configurations.  
  2. Scheduled a web meeting to investigate the issue with the customer and their network security admin.  
  3. Confirmed that the Cohesity platform was not officially supported, which contributed to the issue.  
- **Key Information Leading to Solution**: Permissions were set incorrectly within the Cohesity platform, preventing alias data from being captured.  
- **Resolution**: Adjusted permissions settings within Cohesity to ensure alias information was captured correctly.  
- **Key Takeaways**:  
  - Unsupported platforms may require manual adjustments or alternative configurations.  
  - Permissions settings on the target system are critical for accurate data collection.  
- **Efficiency Improvements**: Proactively verify platform compatibility during initial troubleshooting to streamline resolution.  

## Best Practices & Tips  
- **Verify Platform Compatibility**: Always confirm whether the target system is officially supported by NEA before proceeding with troubleshooting.  
- **Engage Customers Early**: Schedule web meetings to review configurations and settings directly with the customer.  
- **Document Resolutions**: Maintain detailed records of resolution steps for future reference and pattern recognition.  
- **Use Diagnostic Scripts**: Leverage PowerShell scripts to quickly gather environment details and identify potential issues.  
- **Educate Customers**: Provide guidance on configuring permissions correctly within their systems to prevent recurring issues.  

## Escalation Guidelines  
### Criteria for Escalation  
- **Unsupported Platforms**: Escalate to product management or development teams if the issue involves unsupported systems and requires custom solutions.  
- **Critical Compliance Impact**: Escalate immediately if the issue affects compliance reporting or critical audit functions.  
- **Unresolved After Initial Troubleshooting**: Escalate if the issue persists despite following standard diagnostic and resolution steps.  

### Escalation Procedure  
1. Document all troubleshooting steps and findings.  
2. Include relevant logs, PowerShell outputs, and customer environment details.  
3. Submit the case to the appropriate escalation team with a detailed summary of the issue and resolution attempts.  