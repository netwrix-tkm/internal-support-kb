# Knowledge Base Reference Guide: Troubleshooting File System Issues in the Action Module

## Overview
This guide focuses on troubleshooting issues related to the File System feature within the Action Module of Netwrix Enterprise Auditor. The File System feature is critical for monitoring and auditing file system activities, ensuring compliance, and maintaining security. Understanding and resolving issues in this category is essential to ensure uninterrupted functionality and accurate reporting.

## Technical Background
The File System feature in the Action Module is designed to collect and analyze data from file systems, providing insights into access patterns, permissions, and changes. Key components include:
- **Action Module**: Executes specific tasks, such as data collection and reporting.
- **SATagParser**: A utility for tagging and parsing data.
- **Results Tables**: Database tables where action results are stored.
- **COM Objects**: Used for integration with external applications like Microsoft Excel.

### Key Terminology
- **SATagParser.CLI.EXE**: Command-line interface for the SATagParser utility.
- **Results_actions Table**: Database table storing action results.
- **COM Class Factory**: A Windows component responsible for creating instances of COM objects.
- **.NET Core and ASP.NET**: Frameworks used by Netwrix Enterprise Auditor for web-based functionalities.

## Issue Recognition & Triage
### Symptoms
- Unexpected log file creation in executable directories.
- Incorrect file permissions on executables.
- Results tables not updating despite successful action completion.
- Errors related to COM object instantiation (e.g., "Server execution failed").

### Priority Assessment
- **High Priority**: Issues causing data loss, security vulnerabilities, or complete feature inoperability.
- **Medium Priority**: Issues causing partial functionality loss or performance degradation.
- **Low Priority**: Cosmetic issues or minor inconveniences.

## Diagnostic Methodology
1. **Reproduce the Issue**: Attempt to replicate the problem in a controlled environment.
2. **Verify Environment Details**: Confirm software versions, configurations, and dependencies.
3. **Analyze Logs**: Review application and system logs for error messages or anomalies.
4. **Engage R&D**: If the issue involves a potential defect, escalate to the R&D team for further investigation.
5. **Test Fixes**: Apply potential solutions in a lab environment before deploying to production.

## Information Collection
### Questions to Ask Customers
- What specific error messages or symptoms are observed?
- When did the issue first occur, and were there any recent changes (e.g., upgrades)?
- What is the current version of the product and its components?
- Are there any custom configurations or scripts in use?

### Logs and Data to Collect
- Application logs from the Action Module.
- System event logs for related errors.
- Screenshots or detailed descriptions of error messages.
- Database logs for issues involving results tables.

## Common Scenarios & Solutions
### Scenario 1: Log Files Created in Executable Directory
- **Symptoms**: SATagParser.CLI.EXE generates log files in its executable folder.
- **Root Cause**: Product defect causing incorrect log file output configuration.
- **Solution**: Apply hotfix (e.g., SA_11.5_098) to redirect log output to the bin folder.

### Scenario 2: Incorrect Permissions on Executable Files
- **Symptoms**: "Users" group has modify permissions on sensitive executable files.
- **Root Cause**: Permissions incorrectly set during installation or troubleshooting.
- **Solution**: Remove "Users" group from modify permissions and restrict access to administrators.

### Scenario 3: Results Table Not Updating
- **Symptoms**: Results table remains unchanged despite successful action completion.
- **Root Cause**: Software bug in the current version.
- **Solution**: Upgrade to the latest version with a hotfix addressing the issue.

### Scenario 4: COM Object Instantiation Failure
- **Symptoms**: PowerShell commands fail with "Server execution failed" error.
- **Root Cause**: Corrupted Microsoft Excel installation or improper COM object permissions.
- **Solution**: Reinstall Microsoft Excel and verify COM object permissions.

## Detailed Case Studies
### Case 1: Log File Creation Issue
- **Ticket ID**: [500Qk00000BppDRIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BppDRIAZ/view)
- **Symptoms**: Log files generated in the executable folder after upgrading SATagParser.
- **Diagnostic Steps**: Verified issue, engaged R&D, tested hotfix.
- **Resolution**: Applied hotfix to redirect log output.
- **Key Takeaways**: Always test upgrades in a lab environment to identify potential defects.

### Case 2: File Permissions Vulnerability
- **Ticket ID**: [500Qk00000Ex0ggIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ex0ggIAB/view)
- **Symptoms**: "Users" group had modify permissions on an executable file.
- **Diagnostic Steps**: Reviewed permissions, discussed implications, removed modify permissions.
- **Resolution**: Secured file by restricting permissions.
- **Key Takeaways**: Regularly audit file permissions to prevent vulnerabilities.

### Case 3: Results Table Not Updating
- **Ticket ID**: [500Qk00000Gk3pkIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Gk3pkIAB/view)
- **Symptoms**: Results table not updating despite successful action completion.
- **Diagnostic Steps**: Verified action completion, checked database tables, escalated to R&D.
- **Resolution**: Upgraded to the latest version with a hotfix.
- **Key Takeaways**: Ensure customers are on the latest version to avoid known bugs.

### Case 4: COM Object Instantiation Failure
- **Ticket ID**: [500Qk00000HOfbKIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HOfbKIAT/view)
- **Symptoms**: PowerShell command failed with "Server execution failed" error.
- **Diagnostic Steps**: Verified Excel installation, reinstalled Excel, tested PowerShell command.
- **Resolution**: Reinstalled Excel to restore COM components.
- **Key Takeaways**: Verify dependencies like Excel are properly installed and configured.

## Best Practices & Tips
- **Test Upgrades**: Always test new versions and hotfixes in a lab environment before deployment.
- **Audit Permissions**: Regularly review and secure permissions on sensitive files and directories.
- **Monitor Logs**: Continuously monitor application and system logs for early detection of issues.
- **Document Changes**: Maintain detailed records of configuration changes and troubleshooting steps.
- **Communicate Clearly**: Provide customers with clear instructions and set expectations for resolution timelines.

## Escalation Guidelines
- **When to Escalate**:
  - Issues involving potential product defects.
  - Problems requiring changes to core components or architecture.
  - Cases where standard troubleshooting steps fail to resolve the issue.
- **How to Escalate**:
  - Provide a detailed summary of the issue, including logs, screenshots, and steps taken.
  - Clearly state the impact on the customer and urgency of the resolution.
  - Engage the R&D team or escalate to higher-tier support as necessary.