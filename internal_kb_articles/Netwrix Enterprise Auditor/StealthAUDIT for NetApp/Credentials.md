# Knowledge Base Reference Guide: Troubleshooting Scheduled Task Failures in Netwrix Enterprise Auditor

## Overview
Scheduled tasks are a critical feature in Netwrix Enterprise Auditor, enabling automated data collection, auditing, and reporting. Failures in scheduled tasks can disrupt workflows, delay audits, and compromise operational efficiency. This guide provides a systematic approach to diagnosing and resolving issues related to scheduled task failures, particularly those involving StealthAUDIT for NetApp and credential-related problems.

## Technical Background
### Key Concepts
- **Scheduled Tasks**: Automated jobs configured in the Windows Task Scheduler to execute specific actions at predefined intervals.
- **Service Accounts**: Dedicated accounts used by applications or services to perform tasks with specific permissions.
- **Database Permissions**: Access rights granted to accounts for interacting with databases, including reading, writing, and executing stored procedures.

### System Context
Netwrix Enterprise Auditor relies on Windows Task Scheduler to execute scheduled tasks. These tasks often require:
1. **Local System Permissions**: Access to folders such as `C:\Windows\Tasks` and `C:\Windows\System32\Tasks`.
2. **Database Permissions**: Rights to access and interact with the application's database.

Failures can occur if permissions are misconfigured or if the service account lacks necessary rights.

## Issue Recognition & Triage
### Symptoms
- Scheduled tasks fail to execute.
- Windows Task Scheduler logs errors such as:
  - **Event ID 203**: Task failed to launch.
  - **Event ID 101**: Task failed to start.
- Application logs indicate errors like "Login failed for user."

### Priority Assessment
- **High Priority**: If the failure impacts critical auditing or compliance workflows.
- **Medium Priority**: If the failure affects non-critical tasks or reporting.
- **Low Priority**: If the issue is isolated and does not affect overall functionality.

## Diagnostic Methodology
### Step-by-Step Approach
1. **Verify Permissions**:
   - Confirm that the service account is part of the Administrators group.
   - Check Local Security Policy for "Log On As Batch Job" rights.
2. **Inspect Task Scheduler Folders**:
   - Verify access to `C:\Windows\Tasks` and `C:\Windows\System32\Tasks`.
   - Ensure scheduled jobs are present and correctly configured.
3. **Review Application Logs**:
   - Look for login errors or database-related issues.
4. **Test Database Connectivity**:
   - Use the service account credentials to manually connect to the database.
   - Check for permission errors.

## Information Collection
### Customer Questions
- What is the operating system version?
- Are there any recent changes to the service account or its permissions?
- What is the frequency and purpose of the failing scheduled tasks?

### Logs and Data to Collect
- Windows Task Scheduler logs (Event Viewer > Windows Logs > System).
- Application logs from Netwrix Enterprise Auditor.
- Database error logs.
- Screenshots of task configurations and permissions.

## Common Scenarios & Solutions
### Scenario 1: Missing "Log On As Batch Job" Rights
**Symptoms**: Scheduled tasks fail with Event ID 203.  
**Solution**: Grant "Log On As Batch Job" rights to the service account via Local Security Policy.

### Scenario 2: Folder Permission Issues
**Symptoms**: Tasks fail to execute; folders `C:\Windows\Tasks` or `C:\Windows\System32\Tasks` are inaccessible.  
**Solution**: Ensure the service account has full control over these folders.

### Scenario 3: Database Permission Errors
**Symptoms**: Application logs show "Login failed for user."  
**Solution**: Grant appropriate database permissions (e.g., db_datareader, db_datawriter) to the service account.

## Detailed Case Studies
### Case Study: Ticket ID [500Qk00000FeyJOIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FeyJOIAZ/view)
#### Initial Symptoms
The customer reported that scheduled tasks were failing to execute. Task Scheduler logs showed Event IDs 203 and 101, and application logs indicated "Login failed for user."

#### Diagnostic Steps
1. Verified local permissions for the service account:
   - Confirmed membership in the Administrators group.
   - Checked "Log On As Batch Job" rights.
2. Inspected folder permissions:
   - `C:\Windows\Tasks` was empty.
   - `C:\Windows\System32\Tasks` contained scheduled jobs.
3. Reviewed application logs:
   - Identified database login errors.

#### Key Information Leading to Resolution
The service account lacked necessary database permissions, despite having correct local system permissions.

#### Resolution
Granted database permissions to the service account, including db_datareader and db_datawriter roles. Scheduled tasks executed successfully after this change.

#### Key Takeaways
- Always verify both local and database permissions for service accounts.
- Database login errors are a common root cause for scheduled task failures.

#### Efficiency Improvements
- Create a checklist for verifying permissions during initial setup.
- Automate permission audits for service accounts.

## Best Practices & Tips
- **Permission Audits**: Regularly review and audit permissions for service accounts to ensure compliance and operational integrity.
- **Documentation**: Maintain detailed records of service account configurations and permissions.
- **Proactive Monitoring**: Set up alerts for scheduled task failures to enable rapid response.
- **Customer Communication**: Clearly explain the importance of permissions and provide guidance on maintaining them.

## Escalation Guidelines
### Criteria for Escalation
- The issue persists despite following all troubleshooting steps.
- The root cause involves complex database configurations or third-party integrations.
- The customer reports widespread impact on critical workflows.

### Escalation Procedure
1. Collect all relevant logs and data.
2. Document troubleshooting steps taken and their outcomes.
3. Escalate to the appropriate team with a detailed summary of findings and actions.

