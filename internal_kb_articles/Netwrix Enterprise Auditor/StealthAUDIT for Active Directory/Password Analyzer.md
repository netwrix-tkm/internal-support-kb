# Knowledge Base Reference Guide: Troubleshooting Password Analyzer Issues in StealthAUDIT for Active Directory

## Overview
This guide focuses on troubleshooting issues related to the Password Analyzer feature in StealthAUDIT for Active Directory, a component of Netwrix Enterprise Auditor. The Password Analyzer is a critical tool for identifying weak passwords in Active Directory environments, ensuring compliance with security policies, and mitigating risks associated with password vulnerabilities. Understanding and resolving issues in this category is essential for maintaining the integrity and functionality of the Password Analyzer.

## Technical Background
The Password Analyzer feature in StealthAUDIT for Active Directory evaluates Active Directory accounts for weak passwords based on predefined criteria, such as dictionary-based checks and password complexity rules. Key components include:
- **AD_WeakPasswords Job**: The primary job responsible for analyzing weak passwords.
- **Offline Dictionary File**: A file containing weak password patterns used for comparison.
- **Connection Profiles**: User-defined profiles that enable jobs to connect to Active Directory and other resources.
- **Historical Password Analysis**: An optional feature that includes historical password data in the analysis.

Common dependencies include:
- Proper configuration of connection profiles.
- Accessibility of dictionary files.
- Compatibility with security tools and antivirus software.
- Correct job scheduling and execution settings.

## Issue Recognition & Triage
### Symptoms
- Job fails to execute or terminates abruptly.
- Errors related to connection profiles or missing components.
- Inaccurate or unclear weak password reports.
- Job runs interactively but fails when scheduled.
- Logs indicate missing libraries, invalid database objects, or security tool interference.

### Priority Assessment
- **High Priority**: Job failures impacting compliance or security reporting.
- **Medium Priority**: Issues with report accuracy or clarity.
- **Low Priority**: Configuration questions or minor discrepancies.

## Diagnostic Methodology
1. **Verify Environment**: Confirm the Netwrix Enterprise Auditor version, Active Directory configuration, and system dependencies.
2. **Reproduce the Issue**: Attempt to replicate the problem in the customer's environment.
3. **Analyze Logs**: Review debug logs, event logs, and job-specific logs for errors or warnings.
4. **Check Configuration**: Validate connection profiles, dictionary file paths, and job settings.
5. **Test Execution**: Run the job interactively and via scheduled tasks to identify discrepancies.
6. **Isolate External Factors**: Investigate potential interference from antivirus or security tools.

## Information Collection
When troubleshooting, request the following from the customer:
- Job export files and relevant logs.
- Screenshots of job settings and error messages.
- Details about the environment, including installed components and security tools.
- Output from diagnostic PowerShell scripts (if applicable).

## Common Scenarios & Solutions
### Scenario 1: Job Fails Due to Incorrect Dictionary File Configuration
- **Symptoms**: Job fails to run; logs indicate missing libraries or invalid object names.
- **Root Cause**: Incorrect password input or misconfigured dictionary file.
- **Resolution**: Ensure the dictionary file is in the correct format and accessible. Provide documentation for proper setup. Example: [Case 500Qk00000CGihKIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CGihKIAT/view).

### Scenario 2: Connection Profile Not Assigned
- **Symptoms**: Error message: `'Job connection profile is not available'`.
- **Root Cause**: Missing or unassigned connection profile.
- **Resolution**: Assign the appropriate connection profile in the job properties. Example: [Case 500Qk00000KGe1CIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KGe1CIAT/view).

### Scenario 3: Scheduled Task Fails to Execute
- **Symptoms**: Job terminates abruptly when run via scheduled tasks; leaves a `running.lck` file.
- **Root Cause**: Security tool interference.
- **Resolution**: Temporarily disable the security tool and implement exclusions for the job. Example: [Case 500Qk00000LdNrtIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LdNrtIAF/view).

### Scenario 4: Report Accuracy and Clarity Issues
- **Symptoms**: Weak password report includes unclear or inaccurate data.
- **Root Cause**: Historical password analysis enabled, causing discrepancies.
- **Resolution**: Disable the "ANALYZE HISTORICAL PASSWORDS" option in job settings. Example: [Case 500Qk00000MkTaHIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MkTaHIAV/view).

## Detailed Case Studies
### Case Study 1: Dictionary File Misconfiguration
- **Ticket ID**: [500Qk00000CGihKIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CGihKIAT/view)
- **Symptoms**: Job failed to run; logs indicated missing libraries and invalid object names.
- **Diagnostic Steps**: Verified dictionary file configuration, analyzed logs, and reviewed job settings.
- **Resolution**: Corrected dictionary file setup and provided documentation.
- **Key Takeaways**: Always validate dictionary file format and accessibility.

### Case Study 2: Missing Connection Profile
- **Ticket ID**: [500Qk00000KGe1CIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KGe1CIAT/view)
- **Symptoms**: Error: `'Job connection profile is not available'`.
- **Diagnostic Steps**: Reviewed job properties and connection settings.
- **Resolution**: Assigned the correct connection profile.
- **Key Takeaways**: Ensure all jobs have valid connection profiles assigned.

### Case Study 3: Scheduled Task Interference
- **Ticket ID**: [500Qk00000LdNrtIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LdNrtIAF/view)
- **Symptoms**: Job terminated abruptly when scheduled; ran successfully interactively.
- **Diagnostic Steps**: Recreated the task, analyzed logs, and tested with security tools disabled.
- **Resolution**: Implemented antivirus exclusions.
- **Key Takeaways**: Investigate security tool interference for scheduled task failures.

### Case Study 4: Report Clarity Issues
- **Ticket ID**: [500Qk00000MkTaHIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MkTaHIAV/view)
- **Symptoms**: Weak password report included unclear data.
- **Diagnostic Steps**: Reviewed job settings and report criteria.
- **Resolution**: Disabled historical password analysis.
- **Key Takeaways**: Align job settings with reporting requirements.

## Best Practices & Tips
- **Validate Configurations**: Regularly review job settings, connection profiles, and dictionary file paths.
- **Document Changes**: Maintain detailed records of configuration changes for future reference.
- **Antivirus Exclusions**: Configure security tools to allow necessary processes to run without interference.
- **Customer Communication**: Provide clear instructions and documentation to customers for resolving common issues.
- **Proactive Monitoring**: Periodically test scheduled tasks and analyze logs to identify potential issues early.

## Escalation Guidelines
- **When to Escalate**:
  - Issues persist after following standard troubleshooting steps.
  - Logs indicate critical errors or missing components that require development team input.
  - Customer environment constraints prevent resolution.
- **How to Escalate**:
  - Collect all relevant logs, screenshots, and configuration details.
  - Document all troubleshooting steps taken.
  - Submit a detailed escalation request to the appropriate internal team.