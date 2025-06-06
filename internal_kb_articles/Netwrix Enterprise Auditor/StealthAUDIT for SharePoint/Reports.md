# Knowledge Base Reference Guide: Troubleshooting StealthAUDIT for SharePoint Reports in Netwrix Enterprise Auditor

## Overview
This guide provides a comprehensive reference for troubleshooting issues related to the **Reports** feature in the **StealthAUDIT for SharePoint** component of **Netwrix Enterprise Auditor**. It is designed to help support engineers systematically diagnose, resolve, and escalate issues, ensuring consistent and effective customer support. The guide covers common scenarios, diagnostic methodologies, and best practices, with insights drawn from real-world cases.

---

## Technical Background
### Key Concepts
- **StealthAUDIT for SharePoint**: A component of Netwrix Enterprise Auditor designed to audit and report on SharePoint environments, including permissions, activity, and sensitive data.
- **Reports Feature**: Provides insights into SharePoint environments through pre-configured and customizable reports.
- **tempdb Database**: A system database in SQL Server used for temporary storage during query execution.
- **Pivot Analysis**: A feature that aggregates and organizes data into a tabular format for reporting.
- **Active Directory Permissions Analyzer**: A solution for analyzing permissions granted through AD groups.

### System Context
- **SQL Server Dependency**: Many reporting features rely on SQL Server for data storage and processing.
- **SharePoint Online (SPO) and On-Premises**: Reports may involve data from both cloud and on-premises SharePoint environments.
- **Professional Services (ProServe)**: Handles advanced customizations and complex reporting requirements beyond standard support.

---

## Issue Recognition & Triage
### Symptoms to Look For
- Errors related to insufficient database space (e.g., `tempdb` full).
- Missing or incomplete data in reports.
- High CPU usage during job execution.
- Requests for advanced report customizations.
- Issues with permissions analysis or AD group usage reporting.

### Priority Assessment
- **High Priority**: Performance issues causing server outages or critical job failures.
- **Medium Priority**: Missing data or inaccuracies in reports.
- **Low Priority**: Requests for customizations or enhancements.

---

## Diagnostic Methodology
### Systematic Approach
1. **Understand the Problem**: Gather detailed information about the issue from the customer.
2. **Reproduce the Issue**: Attempt to replicate the problem in a test environment if possible.
3. **Analyze Logs**: Review job logs, SQL Server logs, and application logs for errors or anomalies.
4. **Check Dependencies**: Verify database configurations, permissions, and system resources.
5. **Isolate the Cause**: Narrow down potential root causes using diagnostic tools and queries.
6. **Implement Fixes**: Apply targeted solutions and test their effectiveness.
7. **Monitor Results**: Ensure the issue is resolved and does not recur.

---

## Information Collection
### Questions to Ask Customers
- What specific report or job is failing?
- Are there any error messages or logs available?
- Has the issue occurred before? If so, what was done to resolve it?
- Are there any recent changes to the environment (e.g., updates, configuration changes)?
- What is the impact of the issue on business operations?

### Logs and Data to Collect
- Job logs from StealthAUDIT for SharePoint.
- SQL Server logs, including `tempdb` usage statistics.
- Screenshots or exports of error messages.
- Configuration details for SharePoint and SQL Server.
- Historical data or trends related to the issue.

---

## Common Scenarios & Solutions
### Scenario 1: `tempdb` Database Full
- **Symptoms**: Job fails with an error indicating insufficient space in `tempdb`.
- **Solution**:
  1. Verify `tempdb` autogrowth settings and available disk space.
  2. Delete unneeded files or add additional files to the `tempdb` filegroup.
  3. Monitor `tempdb` usage during job execution to ensure stability.
- **Reference Case**: [500Qk00000GF8yXIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GF8yXIAT/view)

### Scenario 2: Advanced Report Customization Requests
- **Symptoms**: Customer requests custom reports beyond standard capabilities.
- **Solution**:
  1. Inform the customer that advanced customizations require Professional Services.
  2. Loop in the Account Executive (AE) and Solutions Engineer (SE) to facilitate ProServe engagement.
  3. Provide documentation links and schedule follow-ups to ensure customer satisfaction.
- **Reference Case**: [500Qk00000HDvUxIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HDvUxIAL/view)

### Scenario 3: Missing Data in Pivot Analysis
- **Symptoms**: Pivot analysis table is not populated despite source table having data.
- **Solution**:
  1. Increase the character limit for the relevant field from 128 to 256.
  2. Verify that the source table contains the necessary data.
  3. Test the changes and confirm that the issue is resolved.
- **Reference Case**: [500Qk00000NrQ3xIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NrQ3xIAF/view)

### Scenario 4: High CPU Usage During Job Execution
- **Symptoms**: Server CPU usage spikes to 100% during job execution.
- **Solution**:
  1. Optimize SQL queries by creating temporary tables before inserting data.
  2. Add unnamed primary keys to temporary tables for faster processing.
  3. Test the modified job in a controlled environment.
- **Reference Case**: [500Qk00000O22b0IAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O22b0IAB/view)

### Scenario 5: AD Group Permissions Reporting
- **Symptoms**: Customer requests a report on AD group permissions but lacks the necessary solution.
- **Solution**:
  1. Confirm whether the Active Directory Permissions Analyzer solution is enabled.
  2. Engage Professional Services to create the requested report.
  3. Schedule a call to finalize requirements and deliverables.
- **Reference Case**: [500Qk00000O4VozIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O4VozIAF/view)

---

## Detailed Case Studies
### Case Study 1: `tempdb` Database Full
- **Symptoms**: `SP_ProbableOwners` job fails with a `tempdb` full error.
- **Diagnostic Steps**: Checked `tempdb` configuration and autogrowth settings.
- **Resolution**: Increased `tempdb` space and addressed related scan issues.
- **Key Takeaways**: Regularly monitor `tempdb` usage and configure autogrowth appropriately.
- **Reference**: [500Qk00000GF8yXIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GF8yXIAT/view)

### Case Study 2: High CPU Usage During Job Execution
- **Symptoms**: CPU spikes during the SharePoint Broken Inheritance Job.
- **Diagnostic Steps**: Reviewed SQL queries and identified inefficiencies in `SELECT...INTO` statements.
- **Resolution**: Optimized queries by creating and indexing temporary tables.
- **Key Takeaways**: Optimize SQL queries to reduce resource consumption.
- **Reference**: [500Qk00000O22b0IAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O22b0IAB/view)

---

## Best Practices & Tips
1. **Monitor System Resources**: Regularly check `tempdb` usage, CPU load, and disk space.
2. **Optimize SQL Queries**: Use indexed temporary tables and avoid inefficient query patterns.
3. **Engage Professional Services**: For advanced customizations, involve ProServe early.
4. **Maintain Backups**: Always back up jobs and configurations before making changes.
5. **Communicate Clearly**: Set realistic expectations with customers regarding timelines and support scope.

---

## Escalation Guidelines
- **When to Escalate**:
  - Issues involving critical outages or data loss.
  - Requests for advanced customizations beyond standard support.
  - Persistent performance issues despite optimization efforts.
- **How to Escalate**:
  1. Document all diagnostic steps and findings.
  2. Provide relevant logs and configuration details.
  3. Loop in the Account Executive and escalate to Professional Services or Development as needed.