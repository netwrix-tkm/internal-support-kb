# Comprehensive Knowledge Base Guide: Troubleshooting Active Directory Inventory Issues in Netwrix Enterprise Auditor

## Overview

This guide provides a systematic approach to identifying, diagnosing, and resolving issues related to the Active Directory Inventory (ADI) feature in Netwrix Enterprise Auditor (NEA), specifically within the StealthAUDIT for Active Directory component. ADI is a critical feature for organizations to maintain accurate Active Directory (AD) data, ensure compliance, and support operational tasks such as licensing and reporting. Understanding and resolving issues in this category is essential to maintaining system integrity and minimizing disruptions.

---

## Technical Background

### Key Concepts
- **Active Directory Inventory (ADI):** A feature in StealthAUDIT that collects and analyzes AD data, including user accounts, groups, permissions, and custom attributes.
- **Differential vs. Full Scans:** Differential scans collect only changes since the last scan, while full scans collect all data from the AD environment.
- **Custom Attributes:** Schema extensions in AD that may be required for specific inventory tasks.
- **Access Control Lists (ACLs):** Permissions structures in AD that can impact inventory scans if they exceed size limits.
- **SQL Server Integration:** ADI relies on SQL Server for data storage and processing, making database connectivity and configuration critical.

### Terminology
- **SA_ADInventory_ExtendedAttributes:** A table in the database that stores extended attribute data collected during scans.
- **Pivot Views:** SQL views used to organize and present collected data for reporting.
- **LDAP:** Protocol used for accessing and maintaining distributed directory information services like AD.
- **FQDN:** Fully Qualified Domain Name, used to identify domain controllers and other network resources.

### System Context
- **StealthAUDIT Installation Directory:** `%SAInstallDir%\Jobs` contains job configurations and output files.
- **SQL Server Dependencies:** ADI jobs require proper SQL Server authentication and connectivity.
- **Version Upgrades:** Upgrades to NEA or StealthAUDIT can introduce changes to job configurations, database schemas, or compatibility.

---

## Issue Recognition & Triage

### Common Symptoms
- Missing or incomplete AD scan results.
- Errors or warnings during ADI job execution.
- Discrepancies in user or group data (e.g., active users marked as deleted).
- SQL errors related to authentication or data integrity.
- Performance issues or job failures due to schema or configuration changes.

### Priority Assessment
- **High Priority:** Issues causing job failures, data loss, or incorrect user/group status (e.g., [500Qk00000Bg2dPIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bg2dPIAR/view)).
- **Medium Priority:** Warnings or errors that do not prevent job completion but indicate potential data discrepancies (e.g., [500Qk00000CdjrCIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CdjrCIAR/view)).
- **Low Priority:** Cosmetic or non-critical issues, such as warnings about unused custom attributes.

---

## Diagnostic Methodology

### Step-by-Step Approach
1. **Reproduce the Issue:**
   - Run the ADI job manually to confirm the reported behavior.
   - Collect error messages and logs for analysis.

2. **Review Configuration:**
   - Check job settings (e.g., differential vs. full scan).
   - Verify SQL Server connection profiles and authentication methods.

3. **Analyze Logs:**
   - Examine logs in `%SAInstallDir%\Jobs\GROUP_.Active Directory Inventory\JOB_1-AD_Scan\OUTPUT`.
   - Review SQL Server logs for database-related errors.

4. **Validate Environment:**
   - Confirm AD schema and custom attributes are correctly configured.
   - Check for network or LDAP connectivity issues.

5. **Identify Root Cause:**
   - Use error messages, logs, and configuration details to pinpoint the issue.

---

## Information Collection

### Key Questions for Customers
- What version of NEA and StealthAUDIT are you using?
- Was the issue observed after an upgrade or configuration change?
- Are there any custom attributes or schema extensions in your AD environment?
- Have there been recent changes to your SQL Server or domain controllers?

### Logs and Data to Collect
- ADI job output logs from `%SAInstallDir%\Jobs`.
- SQL Server logs and error messages.
- Screenshots of error messages or warnings in the NEA console.
- Details of any recent upgrades or migrations.

---

## Common Scenarios & Solutions

### Scenario 1: Missing Analysis After Upgrade
- **Symptoms:** Custom AD scan analysis disappears after upgrading to a new version.
- **Solution:** Restore the job folder from backup, ensure it is not blocked or read-only, and repair the StealthAUDIT installation. ([500Qk00000Bg2dPIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bg2dPIAR/view))

### Scenario 2: Warnings About Custom Attributes
- **Symptoms:** ADI job generates warnings about missing custom attributes.
- **Solution:** Remove unused attributes from the scan configuration or ensure they are implemented in the AD schema. ([500Qk00000CdjrCIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CdjrCIAR/view))

### Scenario 3: SQL Errors During Job Execution
- **Symptoms:** "Login failed. The login is from an untrusted domain."
- **Solution:** Switch to SQL Server authentication for cross-domain connections. ([500Qk00000Jf3BuIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Jf3BuIAJ/view))

### Scenario 4: Users Incorrectly Marked as Deleted
- **Symptoms:** Active users are flagged as deleted in ADI reports.
- **Solution:** Run a full ADI scan to correct synchronization issues. ([500Qk00000FfvktIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FfvktIAB/view))

### Scenario 5: ACL Size Limit Exceeded
- **Symptoms:** ADI job fails with "Length of the access control list exceeds the allowed maximum."
- **Solution:** Apply a hotfix to handle large ACLs gracefully and clean up excessive permissions. ([500Qk00000GCmdzIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GCmdzIAD/view))

---

## Detailed Case Studies

### Case Study: Missing Analysis After Upgrade
- **Ticket ID:** [500Qk00000Bg2dPIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bg2dPIAR/view)
- **Symptoms:** Custom AD scan analysis disappeared post-upgrade.
- **Diagnostic Steps:** Verified job folder location, repaired installation.
- **Resolution:** Restored job folder and repaired StealthAUDIT.
- **Key Takeaways:** Always upgrade jobs in place to avoid configuration loss.

### Case Study: SQL Authentication Error
- **Ticket ID:** [500Qk00000Jf3BuIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Jf3BuIAJ/view)
- **Symptoms:** SQL login failed due to untrusted domain.
- **Diagnostic Steps:** Reviewed authentication method and domain trust settings.
- **Resolution:** Switched to SQL Server authentication.
- **Key Takeaways:** Use SQL authentication for cross-domain connections.

---

## Best Practices & Tips

1. **Upgrade Planning:**
   - Always back up job configurations before upgrading.
   - Verify that all jobs are upgraded in place to retain settings.

2. **Configuration Management:**
   - Regularly review ADI job settings, especially after upgrades or migrations.
   - Use full scans sparingly to minimize performance impact.

3. **Data Integrity:**
   - Monitor for malformed data or invalid characters in AD attributes.
   - Validate custom attributes across all domains to avoid warnings.

4. **Proactive Monitoring:**
   - Enable debug logging for critical jobs to capture detailed error information.
   - Regularly review logs for early detection of potential issues.

---

## Escalation Guidelines

### When to Escalate
- Persistent job failures despite following standard troubleshooting steps.
- Issues involving product bugs or unresolvable configuration conflicts.
- Errors requiring database schema changes or custom hotfixes.

### How to Escalate
- Collect all relevant logs, screenshots, and configuration details.
- Document steps already taken and their outcomes.
- Submit a detailed escalation request to R&D or the appropriate support team.