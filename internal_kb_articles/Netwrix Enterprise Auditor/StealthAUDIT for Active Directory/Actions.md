# Knowledge Base Reference Guide: Troubleshooting Issues in the "Actions" Feature of StealthAUDIT for Active Directory

## Overview

This guide focuses on troubleshooting issues related to the "Actions" feature within the StealthAUDIT for Active Directory component of Netwrix Enterprise Auditor. The "Actions" feature is critical for automating tasks such as tagging files, collecting activity data, and executing custom scripts. Understanding and resolving issues in this category ensures the reliability of automated workflows and minimizes disruptions to customer operations.

## Technical Background

### Key Concepts
- **StealthAUDIT for Active Directory**: A component of Netwrix Enterprise Auditor designed to audit and manage Active Directory environments.
- **Actions Module**: A feature that allows users to perform automated tasks, such as tagging files or collecting activity data, based on predefined configurations.
- **Service Account**: A dedicated account used by the system to execute jobs and access resources.
- **SQL ScriptEditor**: A tool used to configure and customize SQL scripts for data processing within the Actions module.
- **FSAA Job**: File System Activity Auditing job, responsible for collecting file-level details.

### Terminology
- **RowKey**: A database column used to uniquely identify rows in a table.
- **SAM Log Archive**: A repository for logs generated by the Netwrix Activity Monitor (SAM).
- **AD_ActivityCollection Job**: A job that collects activity data from Active Directory environments.

### System Context
The Actions feature relies on proper configuration of jobs, permissions, and data sources. Misconfigurations or permission issues can lead to errors such as "Invalid column name" or "Access denied."

## Issue Recognition & Triage

### Symptoms
- Errors such as "Invalid column name 'RowKey'" or "Access denied."
- Failure of jobs like FSAA or AD_ActivityCollection.
- Missing or incomplete data in the output (e.g., custom tags not appearing).

### Priority Assessment
- **High Priority**: Errors that prevent critical jobs from running (e.g., AD_ActivityCollection job failure).
- **Medium Priority**: Issues affecting non-critical tasks (e.g., missing custom tags).
- **Low Priority**: Cosmetic or non-blocking issues.

## Diagnostic Methodology

1. **Verify Configuration**: Check the job setup, including SQL scripts and data sources.
2. **Review Logs**: Examine action logs for error messages and stack traces.
3. **Test in Lab**: Replicate the issue in a controlled environment.
4. **Check Permissions**: Ensure the service account has the necessary access rights.
5. **Validate Dependencies**: Confirm that all required components (e.g., SAM API) are functional.

## Information Collection

### Questions to Ask Customers
- What specific error messages are you encountering?
- Have there been any recent changes to the environment (e.g., permissions, configurations)?
- What version of Netwrix Enterprise Auditor are you using?
- Can you provide screenshots or logs of the issue?

### Logs and Data to Collect
- Action logs from the affected job.
- Configuration files for the job (e.g., SQL scripts).
- Permissions details for the service account.
- SAM Log Archive access settings (if applicable).

## Common Scenarios & Solutions

### Scenario 1: "Invalid column name 'RowKey'" Error
- **Root Cause**: Permissions issue and misconfiguration in the SQL ScriptEditor.
- **Solution**:
  1. Grant the service account read and write permissions on the target files.
  2. Update the SQL ScriptEditor configuration to reference the correct file (e.g., `newdata1.csv`).
  3. Verify that the FSAA job is set to collect file-level details.

### Scenario 2: AD_ActivityCollection Job Fails with "Access Denied"
- **Root Cause**: Misconfiguration of the job to import logs from an invalid source.
- **Solution**:
  1. Reconfigure the job to import logs from the correct SAM Log Archive location.
  2. Verify permissions for the SAM Log Archive.
  3. Test the job to confirm successful execution.

## Detailed Case Studies

### Case Study 1: "Invalid column name 'RowKey'" Error
- **Ticket ID**: [500Qk00000FG8VeIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FG8VeIAL/view)
- **Initial Symptoms**: Customer reported missing custom tags and an error message during the tagging process.
- **Diagnostic Steps**:
  1. Verified the tagging job configuration.
  2. Reviewed action logs and identified a permissions issue.
  3. Tested the SQL ScriptEditor configuration and found a discrepancy in the temp table reference.
- **Resolution**:
  - Updated the SQL ScriptEditor to reference the correct file (`newdata1.csv`).
  - Granted the service account appropriate permissions.
  - Confirmed successful tagging after reconfiguration.
- **Key Takeaways**:
  - Always verify service account permissions for file metadata access.
  - Double-check SQL ScriptEditor configurations for accuracy.

### Case Study 2: AD_ActivityCollection Job Fails with "Access Denied"
- **Ticket ID**: [500Qk00000LqT0EIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LqT0EIAV/view)
- **Initial Symptoms**: Job failed with an "access denied" error despite correct setup documentation.
- **Diagnostic Steps**:
  1. Reviewed the job configuration and logs.
  2. Identified that the job was attempting to import logs from itself.
  3. Verified permissions for the SAM Log Archive.
- **Resolution**:
  - Reconfigured the job to use the correct SAM Log Archive as the source.
  - Tested the job, which then executed successfully.
- **Key Takeaways**:
  - Validate log source configurations during setup.
  - Ensure permissions are correctly applied when migrating configurations.

## Best Practices & Tips

- **Permissions**: Always verify that the service account has the necessary read and write permissions for all resources it interacts with.
- **Configuration Validation**: Double-check job configurations, especially when migrating settings between environments.
- **Testing**: Use a lab environment to replicate and troubleshoot issues before applying fixes in production.
- **Documentation**: Maintain detailed records of configurations and changes to facilitate troubleshooting.
- **Proactive Monitoring**: Regularly review logs and job results to identify potential issues early.

## Escalation Guidelines

- **When to Escalate**:
  - If the issue persists after following all diagnostic and resolution steps.
  - If the root cause involves product defects or requires development team intervention.
  - If the customer environment has unique complexities that require specialized expertise.

- **How to Escalate**:
  1. Collect all relevant logs, configurations, and error details.
  2. Document the steps already taken and their outcomes.
  3. Submit a detailed escalation request to the appropriate internal team, including all gathered information.

By following this guide, support engineers can systematically diagnose and resolve issues related to the "Actions" feature in StealthAUDIT for Active Directory, ensuring consistent and effective customer support.