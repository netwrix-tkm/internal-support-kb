# Comprehensive Knowledge Base Guide: Troubleshooting Activity Auditing Issues in StealthAUDIT for Windows File Systems

## Overview

This guide provides a systematic approach to understanding, diagnosing, and resolving issues related to Activity Auditing in the StealthAUDIT for Windows File Systems component of Netwrix Enterprise Auditor (NEA). Activity Auditing is critical for tracking file system changes, user activity, and permissions, enabling organizations to maintain security and compliance. This document is designed to equip support engineers with the knowledge and tools needed to handle these issues effectively.

---

## Technical Background

### Key Concepts
- **Activity Auditing**: Tracks file system changes, user activity, and permissions to provide actionable insights.
- **FSAC (File System Activity Collection)**: A core feature that collects activity data from file servers.
- **NAM (Netwrix Activity Monitor)**: A component that monitors file system activity and generates logs.
- **StealthIntercept**: A tool for real-time monitoring and alerting on file system changes.
- **SQL Views**: Predefined database views that store collected activity data for reporting and analysis.

### Terminology
- **T2 Folder**: A directory used by StealthAUDIT to store temporary data during scans.
- **SIDs (Security Identifiers)**: Unique identifiers for user accounts or groups in Windows environments.
- **VSS (Volume Shadow Copy Service)**: A Windows feature used for creating backups and snapshots.

### System Context
- **Data Flow**: Activity data is collected by agents, processed by StealthAUDIT, and stored in SQL databases for reporting.
- **Common Components**: StealthAUDIT agents, SQL databases, and reporting tools like Power BI or Netwrix Access Information Center (AIC).

---

## Issue Recognition & Triage

### Common Symptoms
- Missing or incomplete activity logs.
- Errors during FSAC scans (e.g., "Unknown protocol VSS," "GetSessions failed").
- Data retention settings not being respected.
- Issues with SQL views or database imports.
- Configuration mismatches (e.g., hostname formats, log file paths).

### Priority Assessment
- **High Priority**: Data loss, inability to monitor critical file servers, or errors affecting compliance reporting.
- **Medium Priority**: Warnings or non-critical errors (e.g., "Unknown protocol VSS").
- **Low Priority**: Informational queries or minor configuration issues.

---

## Diagnostic Methodology

### Step-by-Step Approach
1. **Understand the Problem**: Gather detailed information from the customer, including error messages, affected systems, and desired outcomes.
2. **Verify Configuration**: Check settings in StealthAUDIT, NAM, and related components.
3. **Analyze Logs**: Review debug logs, SQL views, and system event logs for clues.
4. **Test Scenarios**: Replicate the issue in a controlled environment if possible.
5. **Implement Fixes**: Apply configuration changes, update software, or resolve database issues.
6. **Validate Resolution**: Confirm that the issue is resolved and document the steps taken.

---

## Information Collection

### Questions to Ask Customers
- What specific issue are you experiencing (e.g., missing logs, scan errors)?
- What is the scope of the problem (e.g., specific servers, date ranges)?
- Have there been any recent changes (e.g., upgrades, configuration updates)?
- Are there any error messages or warnings? If so, provide screenshots or logs.

### Logs and Data to Collect
- Debug logs from StealthAUDIT and NAM.
- SQL database logs and views (e.g., `SA_FSAC_ActivityEventsView`).
- Configuration files (e.g., `SBTFileMon.ini`).
- System event logs from affected servers.

---

## Common Scenarios & Solutions

### Scenario 1: Missing Activity Logs
- **Root Cause**: Misconfigured log file paths or expired licenses.
- **Solution**: Correct the log file path (e.g., `C:\Program Files\Stealthbits\StealthAUDITFSAC\SBTFileMon_Logs\<SERVER_NAME>_Log_.tsv`) and renew licenses.

### Scenario 2: FSAC Scan Errors
- **Root Cause**: Permission issues, outdated proxies, or configuration mismatches.
- **Solution**: Verify permissions, update proxies, and ensure hostname formats match between the Activity Monitor and configuration files.

### Scenario 3: Data Retention Issues
- **Root Cause**: Malfunctioning database cleanup jobs.
- **Solution**: Redeploy NEA on a new server and monitor retention settings for 60 days.

### Scenario 4: SQL View or Import Errors
- **Root Cause**: Missing data due to unexecuted FSAC scans.
- **Solution**: Run the FSAC Scan Job before attempting imports.

### Scenario 5: "Unknown Protocol VSS" Warning
- **Root Cause**: Informational message related to VSS monitoring.
- **Solution**: Inform the customer that the warning is non-critical or disable VSS monitoring.

---

## Detailed Case Studies

### Case Study 1: Missing Data in Power BI Report
- **Ticket**: [500Qk00000CPRz1IAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CPRz1IAH/view)
- **Symptoms**: Customer could not locate SQL tables for Power BI integration.
- **Diagnostic Steps**: Identified the relevant SQL view (`SA_FSAC_ActivityEventsView`).
- **Resolution**: Provided the SQL view details, enabling successful integration.
- **Key Takeaways**: Always document available SQL views for customer reference.

### Case Study 2: Permission Changes Not Monitored
- **Ticket**: [500Qk00000DpvBGIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DpvBGIAZ/view)
- **Symptoms**: File share permissions were altered without alerts.
- **Diagnostic Steps**: Enabled monitoring in StealthIntercept and configured alerts.
- **Resolution**: Set up FSAC scans and monthly reports to track changes.
- **Key Takeaways**: Ensure monitoring is enabled and credentials are available.

### Case Study 3: FSAC Job Fails After Upgrade
- **Ticket**: [500Qk00000EfWFBIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EfWFBIA3/view)
- **Symptoms**: FSAC jobs failed due to certificate issues.
- **Diagnostic Steps**: Fixed certificates, dropped old host data, and renamed T2 folders.
- **Resolution**: Successfully ran the FSAC job after cleanup.
- **Key Takeaways**: Address certificate and T2 folder issues post-upgrade.

---

## Best Practices & Tips

1. **Configuration Management**: Regularly review and document configurations, including log file paths, hostname formats, and retention settings.
2. **Proactive Monitoring**: Enable alerts for critical events and monitor system health (e.g., disk space, licenses).
3. **Documentation**: Maintain up-to-date documentation for SQL views, permissions, and common troubleshooting steps.
4. **Customer Communication**: Clearly explain technical concepts and provide actionable guidance.
5. **Testing Environment**: Use test environments to replicate and resolve complex issues.

---

## Escalation Guidelines

### When to Escalate
- Issues involving data corruption or loss.
- Persistent errors after applying standard fixes.
- Requests for new features or unsupported configurations.

### How to Escalate
1. Gather all relevant logs, screenshots, and configuration details.
2. Document the steps already taken and their outcomes.
3. Submit a detailed escalation request to the appropriate team or vendor.

---

This guide serves as a comprehensive reference for troubleshooting Activity Auditing issues in StealthAUDIT for Windows File Systems, enabling support engineers to resolve problems efficiently and consistently.