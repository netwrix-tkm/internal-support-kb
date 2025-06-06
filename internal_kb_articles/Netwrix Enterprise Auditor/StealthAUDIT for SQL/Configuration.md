# Netwrix Enterprise Auditor: StealthAUDIT for SQL Configuration Troubleshooting Guide

## Overview
This guide provides a comprehensive reference for troubleshooting configuration issues related to StealthAUDIT for SQL within Netwrix Enterprise Auditor. It is designed to help support engineers systematically diagnose and resolve common problems encountered by customers. Understanding this category is critical for ensuring SQL-related jobs execute correctly, minimizing downtime, and maintaining customer satisfaction.

## Technical Background
StealthAUDIT for SQL is a component of Netwrix Enterprise Auditor that enables auditing and monitoring of SQL Server environments. Key features include SQL job scheduling, permissions scans, and activity monitoring. Proper configuration is essential for ensuring accurate data collection and reporting. Common issues often stem from hostlist misconfigurations, SQL server connectivity problems, or incorrect audit settings.

### Key Concepts
- **Hostlist Records**: A list of SQL servers or hosts that jobs reference during execution. Missing or incorrect records can prevent jobs from running.
- **SQL Authentication vs. Windows Authentication**: Two methods for connecting to SQL servers. Connection strings vary based on the authentication type.
- **Job Scheduling Conflicts**: Overlapping or conflicting job schedules can cause delays or failures.
- **Ping Settings**: The "Skip host if cannot Ping" option can mark hosts as offline if they are unreachable via ping, even if they are otherwise accessible.
- **Database Auditing**: Required for certain SQL Server activities to be monitored by Netwrix Access Analyzer.

## Issue Recognition & Triage
### Symptoms
- SQL jobs fail to start or execute.
- Errors such as "Invalid Object Name" appear during job execution.
- Hosts are marked as offline despite being reachable.
- SQL permission scans succeed on some servers but fail on others.
- Customers request visibility into SQL connection strings or inquire about auditing capabilities.

### Priority Assessment
- **High Priority**: Issues affecting production environments or critical SQL jobs (e.g., login activity monitoring).
- **Medium Priority**: Configuration errors causing partial functionality (e.g., permission scans failing on some servers).
- **Low Priority**: Informational requests or non-critical configuration questions.

## Diagnostic Methodology
### Step-by-Step Approach
1. **Verify Hostlist Configuration**: Check for missing or incorrect hostlist records.
2. **Review Job Logs**: Search for relevant error messages or connection string details.
3. **Test Connectivity**: Use UDL tests or SQL query previews to confirm server accessibility.
4. **Check Scheduling Conflicts**: Identify overlapping jobs that may cause delays or failures.
5. **Audit Settings**: Ensure database auditing is enabled if required for the job.
6. **Ping Settings**: Review the "Skip host if cannot Ping" option for hosts marked offline.

### Decision Points
- If hostlist records are missing, recreate or update the hostlist.
- If connectivity tests fail, verify SQL server access settings and authentication methods.
- If job logs indicate configuration errors, review audit settings and job parameters.

## Information Collection
### Customer Questions
- What specific error messages are you encountering?
- Are all SQL servers configured in the hostlist?
- What authentication method is being used (SQL or Windows)?
- Are there any overlapping or conflicting job schedules?
- Is database auditing enabled on the SQL servers?

### Logs and Data to Collect
- SQL job logs (search for "setting connection string to").
- Hostlist configuration details.
- UDL test results for connectivity verification.
- Screenshots or exports of job settings and schedules.

## Common Scenarios & Solutions
### Scenario 1: Missing Hostlist Records
- **Symptoms**: SQL jobs fail to start; hostlist records are missing.
- **Solution**: Recreate the hostlist and ensure all required records are present. Monitor for scheduling conflicts.
- **Reference Case**: [500Qk00000CLEInIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CLEInIAP/view)

### Scenario 2: "Invalid Object Name" Error
- **Symptoms**: SQL jobs fail with "Invalid Object Name" errors.
- **Solution**: Verify audit settings and ensure the SQL server is correctly configured in the hostlist. Install necessary add-ons if required.
- **Reference Case**: [500Qk00000ETqMaIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ETqMaIAL/view)

### Scenario 3: Host Marked Offline
- **Symptoms**: SQL Query job shows host as offline despite successful query validation.
- **Solution**: Disable the "Skip host if cannot Ping" option to prevent hosts from being marked offline due to ping failures.
- **Reference Case**: [500Qk00000Kt3zXIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Kt3zXIAR/view)

### Scenario 4: SQL Permission Scans Failing
- **Symptoms**: Permission scans succeed on one server but fail on others.
- **Solution**: Correct access settings on SQL servers and verify hostlist configurations.
- **Reference Case**: [500Qk00000OfohQIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OfohQIAR/view)

### Scenario 5: SQL Connection String Visibility
- **Symptoms**: Customer requests visibility into SQL connection strings.
- **Solution**: Advise the customer to search job logs for "setting connection string to" and provide examples of connection strings for SQL and Windows Authentication.
- **Reference Case**: [500Qk00000Kt3zXIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Kt3zXIAR/view)

### Scenario 6: Auditing Without Database Auditing Enabled
- **Symptoms**: Customer inquires about auditing SQL Server activities without enabling database auditing.
- **Solution**: Inform the customer that database auditing must be enabled for SQL Server activities to be monitored by Netwrix Access Analyzer.
- **Reference Case**: [500Qk00000OxrthIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OxrthIAB/view)

## Detailed Case Studies
### Case Study 1: Missing Hostlist Records
- **Ticket ID**: [500Qk00000CLEInIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CLEInIAP/view)
- **Symptoms**: SQL job stopped running due to missing hostlist records.
- **Diagnostic Steps**: Reviewed hostlist configuration, checked job logs, and identified scheduling conflicts.
- **Resolution**: Reworked login collection process and ensured hostlist records were complete.
- **Key Takeaways**: Regularly review hostlist configurations and monitor job schedules for conflicts.

### Case Study 2: "Invalid Object Name" Error
- **Ticket ID**: [500Qk00000ETqMaIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ETqMaIAL/view)
- **Symptoms**: SQL jobs failed with "Invalid Object Name" errors.
- **Diagnostic Steps**: Reviewed audit settings and hostlist configurations.
- **Resolution**: Installed Sensitive Data Discovery add-on and reconfigured hostlist.
- **Key Takeaways**: Ensure audit settings are correctly configured and hostlists are accurate.

### Case Study 3: Host Marked Offline
- **Ticket ID**: [500Qk00000Kt3zXIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Kt3zXIAR/view)
- **Symptoms**: Host marked offline despite successful query validation.
- **Diagnostic Steps**: Verified ping settings and connectivity.
- **Resolution**: Disabled "Skip host if cannot Ping" option.
- **Key Takeaways**: Review ping settings during job configuration.

### Case Study 4: SQL Permission Scans Failing
- **Ticket ID**: [500Qk00000OfohQIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OfohQIAR/view)
- **Symptoms**: Permission scans succeeded on one server but failed on others.
- **Diagnostic Steps**: Conducted UDL tests and verified access settings.
- **Resolution**: Corrected access settings and reconfigured hostlist.
- **Key Takeaways**: Consistently apply access settings across all servers.

### Case Study 5: Auditing Without Database Auditing Enabled
- **Ticket ID**: [500Qk00000OxrthIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OxrthIAB/view)
- **Symptoms**: Customer requested auditing capabilities without enabling database auditing.
- **Diagnostic Steps**: Reviewed documentation and confirmed limitations.
- **Resolution**: Provided documentation explaining the requirement for database auditing.
- **Key Takeaways**: Clearly communicate prerequisites for auditing capabilities.

## Best Practices & Tips
- Regularly review hostlist configurations to ensure completeness and accuracy.
- Monitor job schedules for potential conflicts and adjust timing as needed.
- Use UDL tests to verify SQL server connectivity before troubleshooting further.
- Educate customers on prerequisites for auditing features, such as enabling database auditing.
- Redact sensitive information, such as passwords, when sharing connection strings or logs.

## Escalation Guidelines
### Criteria for Escalation
- Issues persist despite following standard troubleshooting steps.
- Problems involve advanced SQL configurations or require development team intervention.
- Customer impact is severe, such as prolonged downtime or critical job failures.

### Escalation Procedure
1. Document all troubleshooting steps taken and results.
2. Collect relevant logs, screenshots, and configuration details.
3. Submit a detailed escalation request to the appropriate team, including customer impact and urgency.
4. Follow up regularly to ensure timely resolution.