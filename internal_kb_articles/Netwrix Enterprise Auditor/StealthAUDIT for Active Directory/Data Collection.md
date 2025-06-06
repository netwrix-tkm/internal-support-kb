# Comprehensive Knowledge Base Guide: Troubleshooting Data Collection Issues in StealthAUDIT for Active Directory

## Overview
This guide focuses on troubleshooting issues related to the **Data Collection** feature in **StealthAUDIT for Active Directory**, a component of **Netwrix Enterprise Auditor**. Data collection is critical for maintaining accurate and actionable insights into Active Directory environments. Understanding and resolving issues in this category ensures the integrity of audits, compliance reporting, and security monitoring.

## Technical Background
### Key Concepts
- **Active Directory Inventory (ADI):** A scan that collects data from Active Directory objects, including users, groups, computers, and attributes.
- **Jobs:** Specific tasks within StealthAUDIT that perform data collection, such as AD_Scan, AD_ChangeTracking, and AD_ServiceAccounts.
- **Event Logs:** Windows Security Auditing logs (e.g., 4662, 5136) that track access and changes to AD objects.
- **Custom Attributes:** User-defined attributes added to queries for tracking changes or collecting specific data.
- **Host Lists:** Lists of servers or domain controllers targeted by specific jobs.

### Terminology
- **SPN (Service Principal Name):** A unique identifier for service accounts in Active Directory.
- **Differential Scans:** Scans that collect only changes since the last full scan.
- **Connection Profiles:** Credentials and configurations used by jobs to access AD objects.

### System Context
StealthAUDIT interacts with Active Directory through read-only operations, SQL queries, and scheduled jobs. Proper configuration of jobs, permissions, and audit policies is essential for accurate data collection.

## Issue Recognition & Triage
### Symptoms
- Missing or incomplete data in reports.
- Unexpected Windows Security Auditing events (e.g., 4662).
- Failed or hanging scans during specific job steps.
- Empty host lists or missing attributes in reports.
- Errors related to job dependencies or licensing.

### Priority Assessment
- **High Priority:** Issues affecting compliance reporting, security monitoring, or critical business operations.
- **Medium Priority:** Performance issues or incomplete data that do not immediately impact operations.
- **Low Priority:** Configuration clarifications or non-critical warnings.

## Diagnostic Methodology
### Systematic Approach
1. **Identify the affected job:** Determine which job is failing or producing unexpected results.
2. **Review logs:** Examine job logs for errors, warnings, or blocked transactions.
3. **Check configurations:** Verify job schedules, connection profiles, and audit policies.
4. **Test manually:** Run manual queries or scans to isolate the issue.
5. **Analyze dependencies:** Investigate whether other jobs or system processes are causing conflicts.

### Decision Points
- If logs indicate permission issues, verify service account credentials.
- If scans fail during specific steps, check for resource constraints (e.g., disk space, memory).
- If data is missing, confirm that the necessary attributes are being collected.

## Information Collection
### Customer Questions
- What symptoms are you observing (e.g., missing data, failed scans)?
- Have there been any recent changes to the environment (e.g., updates, configuration changes)?
- Are you seeing specific event log entries (e.g., 4662, 5136)?
- What is the schedule and frequency of the affected job?

### Logs and Data to Collect
- Job logs from StealthAUDIT.
- Windows Event Logs from domain controllers.
- SQL database logs for jobs involving queries.
- Configuration details for affected jobs (e.g., connection profiles, host lists).

## Common Scenarios & Solutions
### Scenario 1: Unexpected Event Logs (4662)
- **Root Cause:** A job (e.g., Weak Passwords) triggers read-only access events.
- **Solution:** Disable the problematic job or adjust audit policy settings.
- **Reference Case:** [500Qk00000CF6UPIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CF6UPIA1/view)

### Scenario 2: Empty Host Lists
- **Root Cause:** Scheduling conflicts or improperly configured cleanup jobs.
- **Solution:** Reschedule jobs to avoid conflicts and disable cleanup jobs.
- **Reference Case:** [500Qk00000CG4s2IAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CG4s2IAD/view)

### Scenario 3: Missing Custom Attributes
- **Root Cause:** Change collection not enabled or missing job execution.
- **Solution:** Enable change collection and ensure all required jobs are executed.
- **Reference Case:** [500Qk00000CqPDAIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CqPDAIA3/view)

### Scenario 4: Job Errors Due to Dependencies
- **Root Cause:** Failed AD_Scan job affecting dependent jobs.
- **Solution:** Rerun the AD_Scan job and verify host accessibility.
- **Reference Case:** [500Qk00000DgYDuIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DgYDuIAN/view)

### Scenario 5: Account Lockout Alerts Not Generated
- **Root Cause:** Incorrect job schedule and Event Log settings.
- **Solution:** Adjust job schedule and ensure Event Logs are properly configured.
- **Reference Case:** [500Qk00000GUwNBIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GUwNBIA1/view)

### Scenario 6: Performance Issues During Scans
- **Root Cause:** Licensing problems disabling job groups.
- **Solution:** Update licenses and re-enable affected job groups.
- **Reference Case:** [500Qk00000IW2kHIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IW2kHIAT/view)

### Scenario 7: Service Accounts Not Identified
- **Root Cause:** Missing SPNs for service accounts.
- **Solution:** Populate SPNs manually or submit a feature request for heuristic detection.
- **Reference Case:** [500Qk00000OZSd7IAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OZSd7IAH/view)

## Detailed Case Studies
### Case Study 1: Unexpected Event Logs (4662)
- **Symptoms:** Customer observed 4662 events during ADI scans.
- **Diagnostic Steps:** Verified audit policy settings and isolated the Weak Passwords job.
- **Resolution:** Disabled the Weak Passwords job and split ADI scans into separate jobs.
- **Key Takeaways:** Monitor job configurations to avoid triggering security events.

### Case Study 2: Empty Host Lists
- **Symptoms:** Host lists showed no data; manual queries failed.
- **Diagnostic Steps:** Investigated cleanup job and SQL database backup conflicts.
- **Resolution:** Disabled cleanup job and rescheduled AD_Scan to avoid conflicts.
- **Key Takeaways:** Avoid scheduling conflicts and review custom job configurations.

### Case Study 3: Missing Custom Attributes
- **Symptoms:** Changes to custom attributes not reflected in reports.
- **Diagnostic Steps:** Enabled change collection and executed 2-AD_Changes job.
- **Resolution:** Data appeared after ensuring proper job execution.
- **Key Takeaways:** Verify settings and job execution after full scans.

### Case Study 4: Job Errors Due to Dependencies
- **Symptoms:** Nine jobs failed due to AD_Scan issues.
- **Diagnostic Steps:** Reran AD_Scan and verified host accessibility.
- **Resolution:** Dependent jobs functioned correctly after AD_Scan completion.
- **Key Takeaways:** Monitor dependencies and host configurations.

### Case Study 5: Account Lockout Alerts Not Generated
- **Symptoms:** Lockout alerts failed intermittently.
- **Diagnostic Steps:** Adjusted job schedule and Event Log settings.
- **Resolution:** Alerts generated successfully after configuration changes.
- **Key Takeaways:** Ensure frequent job schedules and adequate Event Log retention.

### Case Study 6: Performance Issues During Scans
- **Symptoms:** Scans failed during "Group Usage" step.
- **Diagnostic Steps:** Identified licensing issues disabling job groups.
- **Resolution:** Disabled affected job group until license was updated.
- **Key Takeaways:** Maintain valid licenses to avoid functionality disruptions.

### Case Study 7: Service Accounts Not Identified
- **Symptoms:** Service accounts missing from reports.
- **Diagnostic Steps:** Verified SPN collection and SQL query criteria.
- **Resolution:** Recommended manual SPN population or feature request submission.
- **Key Takeaways:** Ensure SPNs are populated for accurate reporting.

## Best Practices & Tips
- **Job Configuration:** Regularly review job schedules, host lists, and connection profiles.
- **Audit Policies:** Enable relevant audit subcategories (e.g., Directory Service Access) for comprehensive logging.
- **Event Log Management:** Monitor log size and retention settings to prevent data loss.
- **License Validation:** Ensure all necessary licenses are valid and up-to-date.
- **Documentation:** Maintain detailed records of configuration changes and troubleshooting steps.
- **Customer Communication:** Provide clear explanations and actionable recommendations during support interactions.

## Escalation Guidelines
### Criteria for Escalation
- Issues persist after following standard troubleshooting steps.
- Critical business operations are impacted.
- Licensing or product functionality requires vendor intervention.

### Escalation Procedure
1. Gather all relevant logs, configurations, and customer details.
2. Document troubleshooting steps and findings.
3. Submit a detailed escalation request to the appropriate team or vendor.
4. Follow up regularly to ensure timely resolution.