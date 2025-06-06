# Comprehensive Knowledge Base Guide: Troubleshooting Report Issues in StealthAUDIT for Windows

## Overview
This guide focuses on troubleshooting issues related to report generation in the StealthAUDIT for Windows component of Netwrix Enterprise Auditor. Reports are a critical feature for customers, enabling them to audit and analyze data effectively. Understanding and resolving issues in this category ensures customer satisfaction and system reliability.

## Technical Background
StealthAUDIT for Windows is a powerful auditing tool within Netwrix Enterprise Auditor, designed to collect, analyze, and report on data from Windows environments. Key features include:
- **Job Trees**: Hierarchical workflows that define auditing tasks.
- **Reports**: Outputs generated from collected data, providing actionable insights.
- **Tables**: Data storage structures used during audits, such as `_Details` tables for granular information.

Common challenges include stale data, incomplete scans, and file path limitations. These issues often stem from environmental factors, configuration errors, or system limitations.

## Issue Recognition & Triage
### Symptoms
- Reports fail to generate or contain incomplete data.
- Stale or outdated information persists in audit tables.
- Errors related to file path or name length during report generation.

### Priority Assessment
- **High Priority**: Issues affecting critical business operations, such as identifying privileged accounts or service configurations.
- **Medium Priority**: Errors impacting report generation but not critical workflows.
- **Low Priority**: Minor discrepancies or cosmetic issues in reports.

## Diagnostic Methodology
1. **Understand the Problem**: Review the customer’s description and clarify the issue.
2. **Reproduce the Issue**: Attempt to replicate the problem in a controlled environment.
3. **Analyze Logs**: Examine job logs for errors or anomalies.
4. **Verify Configuration**: Check job settings, permissions, and environmental factors.
5. **Test Solutions Incrementally**: Apply fixes step-by-step and validate results.

## Information Collection
### Questions to Ask Customers
- What specific report or job is failing?
- Are there any error messages or logs available?
- Has the environment or configuration changed recently?
- What is the urgency of resolving this issue?

### Logs and Data to Collect
- Job execution logs.
- Screenshots of error messages.
- Configuration details for the affected job.
- Relevant registry settings (e.g., `LongPathsEnabled`).

## Common Scenarios & Solutions
### Scenario 1: Identifying Services Running with Specific AD Accounts
**Symptoms**: Customer needs to identify servers running services with a specific AD service account.

**Solution**:
1. Navigate to the job tree:  
   ```
   Windows > Privileged Accounts > Service Accounts > SG_ServiceAccounts > Results > ServiceAccounts
   ```
2. Generate a report listing all services, their statuses, and associated accounts.
3. Provide the report to the customer for analysis.

**Reference Case**: [Ticket ID 500Qk00000Gk3XyIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Gk3XyIAJ/view)

---

### Scenario 2: Stale Data in Local Admins Audit Table
**Symptoms**: Deleted or disabled users continue to appear as active in the `_Details` table.

**Solution**:
1. Rename the old `_Details` table to preserve data.
2. Execute the job against a smaller host to rebuild the table.
3. Configure the job to run against all hosts and clear the `_Details` table.
4. Verify permissions and protocols to ensure successful scans.

**Reference Case**: [Ticket ID 500Qk00000NPQN6IAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NPQN6IAP/view)

---

### Scenario 3: File Path Length Limitation
**Symptoms**: Report generation fails due to file path or name exceeding Windows limits.

**Solution**:
1. Verify the path and file name length.
2. Modify the registry key to enable long paths:  
   ```
   Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem\LongPathsEnabled
   ```
3. Move the job to a higher directory in the hierarchy to reduce path length.
4. Re-run the job and confirm successful report generation.

**Reference Case**: [Ticket ID 500Qk00000ORN7aIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ORN7aIAH/view)

---

## Detailed Case Studies
### Case Study 1: Identifying Services Running with Specific AD Accounts
**Initial Symptoms**: Customer required a report to identify servers running services with a specific AD service account.

**Diagnostic Steps**:
- Reviewed the job tree structure.
- Generated a report listing services and associated accounts.

**Key Information**:
- Job tree navigation was critical to locating the relevant data.

**Resolution**:
- Provided the customer with a comprehensive report.

**Takeaways**:
- Familiarity with job tree structures expedites troubleshooting.

---

### Case Study 2: Stale Data in Local Admins Audit Table
**Initial Symptoms**: Deleted or disabled users appeared as active in the `_Details` table.

**Diagnostic Steps**:
- Ran the job and observed stale audit dates.
- Rebuilt the `_Details` table and verified permissions.

**Key Information**:
- Erroring hosts prevented successful scans.

**Resolution**:
- Cleared and rebuilt the `_Details` table.

**Takeaways**:
- Monitor hosts during scans to ensure data integrity.

---

### Case Study 3: File Path Length Limitation
**Initial Symptoms**: Report generation failed due to excessive path length.

**Diagnostic Steps**:
- Verified path length and modified registry settings.
- Relocated the job to reduce path length.

**Key Information**:
- Windows file path limitations were the root cause.

**Resolution**:
- Successfully generated the report after reducing path length.

**Takeaways**:
- Keep job paths and file names within Windows limits.

---

## Best Practices & Tips
- **Job Tree Familiarity**: Understand the structure and navigation of job trees to locate relevant data quickly.
- **Monitor Hosts**: Ensure all hosts are reporting correctly during scans to avoid stale data.
- **Path Length Awareness**: Configure jobs with paths and file names well within Windows limits.
- **Incremental Testing**: Apply fixes step-by-step and validate results to isolate issues effectively.
- **Customer Communication**: Provide clear instructions and updates throughout the troubleshooting process.

## Escalation Guidelines
### Criteria for Escalation
- Issues persist after applying documented solutions.
- Critical business operations are impacted.
- Errors involve unsupported configurations or third-party dependencies.

### Escalation Procedure
1. Document all troubleshooting steps and findings.
2. Collect relevant logs and data.
3. Submit the case to the escalation team with detailed notes and urgency level.
4. Follow up with the customer to ensure timely resolution.

This guide serves as a definitive reference for handling report-related issues in StealthAUDIT for Windows, enabling support engineers to resolve cases efficiently and consistently.