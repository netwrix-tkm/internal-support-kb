# Knowledge Base Reference Guide: Troubleshooting Access Information Center (AIC) Resource Audit Issues

## Overview

The **Access Information Center (AIC)** within Netwrix Enterprise Auditor is a critical component for monitoring and auditing resource access. It provides detailed insights into user activity, permissions, and access patterns across various resources. Effective troubleshooting of AIC issues ensures accurate reporting, optimal performance, and compliance with organizational policies. This guide serves as a comprehensive reference for diagnosing and resolving issues related to the **Resource Audit** feature in AIC.

---

## Technical Background

### Key Concepts
- **Access Information Center (AIC):** A module in Netwrix Enterprise Auditor that consolidates and displays resource access data.
- **Resource Audit:** A feature within AIC that tracks user activity, permissions, and access changes for monitored resources.
- **StealthAUDIT (SA):** A component that collects and processes data for AIC.
- **FSAC (File System Activity Collector):** A subsystem responsible for scanning and importing file system activity data.
- **T2 Database:** A temporary database used for storing scan and import data before it is processed into the main database.

### Terminology
- **SAMAccountName:** A unique identifier for user accounts in Active Directory.
- **AuthSessionTimeout:** A configuration parameter that determines the session timeout duration for AIC queries.
- **ExpirationState:** A database field used to track the state of expired permissions in AIC.
- **Host Mapping:** A feature that maps hosts to specific agents for scanning.

### System Context
- AIC relies on accurate data collection from various sources, including file systems, Active Directory, and external storage devices (e.g., Isilon, Nasuni).
- Proper configuration of scan jobs, permissions, and database settings is essential for AIC to function correctly.

---

## Issue Recognition & Triage

### Common Symptoms
- Incorrect or incomplete activity details in AIC.
- Query results displaying data for incorrect dates or users.
- Performance issues, such as long query times or timeouts.
- Errors in logs related to expired permissions or missing user accounts.
- Missing or outdated scan data for specific resources.

### Priority Assessment
- **High Priority:** Issues causing data inaccuracy, such as incorrect activity details or missing scan data.
- **Medium Priority:** Performance-related issues, such as timeouts or slow queries.
- **Low Priority:** Configuration requests, such as customizing views or enabling specific features.

---

## Diagnostic Methodology

### Systematic Approach
1. **Reproduce the Issue:** Attempt to replicate the problem in a lab environment using the same AIC version and configuration.
2. **Verify Configuration:** Check scan job settings, permissions, and database entries.
3. **Analyze Logs:** Review relevant logs (e.g., `aic.log`, FSAC logs) for errors or anomalies.
4. **Check Versions:** Confirm the versions of AIC, StealthAUDIT, and other components to identify potential compatibility issues.
5. **Test Workarounds:** Implement temporary solutions, such as SQL queries or configuration changes, to isolate the root cause.

---

## Information Collection

### Questions to Ask Customers
- What specific issue are you experiencing (e.g., incorrect data, timeouts)?
- What version of AIC and StealthAUDIT are you using?
- Are there any recent changes to your environment (e.g., upgrades, new devices)?
- Can you provide logs, screenshots, or examples of the issue?

### Logs and Data to Collect
- **AIC Logs:** `aic.log` for error messages and activity details.
- **SQL Queries:** Data from relevant tables (e.g., `SA_FSAC_ActivityEventsView`, `SA_AIC_ResourceAccessRequests`).
- **Configuration Files:** Settings for scan jobs, timeout parameters, and permissions.
- **Screenshots:** Visual evidence of the issue for comparison.

---

## Common Scenarios & Solutions

### Scenario 1: Incorrect Activity Details Displayed
- **Symptoms:** Activity for a child share displayed under a parent share despite "Include subfolders" being unchecked.
- **Solution:** Upgrade to the latest AIC build to resolve the bug. Reference: [Case 500Qk00000CbRYeIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CbRYeIAN/view).

### Scenario 2: Query Results for Incorrect Dates
- **Symptoms:** Activity details for one date displayed under another due to timezone discrepancies.
- **Solution:** Upgrade to AIC version 11.6.0.132 to fix timezone handling. Reference: [Case 500Qk00000Da12vIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Da12vIAB/view).

### Scenario 3: Customizing Views for Unique Identifiers
- **Symptoms:** User names displayed instead of unique SAMAccountNames.
- **Solution:** Add the `TrusteeAccount` column to the Resource Audit view. Reference: [Case 500Qk00000ELIjTIAX](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ELIjTIAX/view).

### Scenario 4: Query Timeouts
- **Symptoms:** AIC queries fail due to session timeouts.
- **Solution:** Increase the `AuthSessionTimeout` parameter to 90 minutes. Reference: [Case 500Qk00000GJcoMIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GJcoMIAT/view).

### Scenario 5: Errors Related to Expired Permissions
- **Symptoms:** Logs overwhelmed with errors for expired permissions of deleted AD accounts.
- **Solution:** Set `ExpirationState` to 2 in the `SA_AIC_ResourceAccessRequests` table. Reference: [Case 500Qk00000HgOoyIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HgOoyIAF/view).

### Scenario 6: Missing Activity Data for Specific Devices
- **Symptoms:** Activity data missing for some Nasuni devices.
- **Solution:** Remove host mapping and ensure proper permissions for the connection profile account. Reference: [Case 500Qk00000LAT9ZIAX](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LAT9ZIAX/view).

### Scenario 7: Outdated Scan Data
- **Symptoms:** AIC displays old scan dates for specific servers.
- **Solution:** Delete or rename stale T2 database data and reconfigure scan jobs. Reference: [Case 500Qk00000O23AYIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O23AYIAZ/view).

### Scenario 8: Missing Features After Upgrade
- **Symptoms:** Manual group membership changes unavailable after upgrading to version 12.0.
- **Solution:** Enable the "Allow this account to make changes to group membership" setting. Reference: [Case 500Qk00000P9vqIIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000P9vqIIAR/view).

---

## Detailed Case Studies

### Case Study: Incorrect Activity Details Displayed
- **Ticket ID:** [500Qk00000CbRYeIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CbRYeIAN/view)
- **Symptoms:** Activity for a child share displayed under a parent share.
- **Diagnostic Steps:** Verified configuration, reproduced issue in lab, reviewed SQL data.
- **Resolution:** Upgraded AIC to the latest build.
- **Key Takeaways:** Always check for known bugs in specific versions.

### Case Study: Query Timeouts
- **Ticket ID:** [500Qk00000GJcoMIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GJcoMIAT/view)
- **Symptoms:** AIC queries failed due to session timeouts.
- **Diagnostic Steps:** Reviewed query performance, adjusted timeout settings.
- **Resolution:** Increased `AuthSessionTimeout` to 90 minutes.
- **Key Takeaways:** Monitor query performance and adjust timeout settings as needed.

---

## Best Practices & Tips

1. **Keep Software Updated:** Regularly upgrade to the latest versions to benefit from bug fixes and new features.
2. **Monitor Logs:** Increase log retention periods for better troubleshooting.
3. **Document Changes:** Maintain records of configuration changes and upgrades.
4. **Educate Customers:** Provide guidance on customizing views and understanding feature limitations.
5. **Optimize Scans:** Schedule scans and imports in the correct sequence to avoid data inconsistencies.

---

## Escalation Guidelines

### Criteria for Escalation
- Issues involving unresolved bugs or product defects.
- Problems requiring changes to core functionality or database schema.
- Cases where standard troubleshooting steps fail to resolve the issue.

### Escalation Process
1. Gather all relevant logs, screenshots, and configuration details.
2. Document the troubleshooting steps already taken.
3. Submit the case to the R&D team with a detailed description of the issue and findings.
4. Follow up regularly to ensure timely resolution.