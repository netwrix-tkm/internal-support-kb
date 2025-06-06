# Knowledge Base Reference Guide: Troubleshooting Data Collection Issues in StealthAUDIT for NetApp

## Overview
This guide provides a comprehensive reference for troubleshooting data collection issues in the StealthAUDIT for NetApp component of Netwrix Enterprise Auditor. It is designed to help support engineers systematically diagnose and resolve common problems, ensuring efficient and consistent handling of customer cases. The guide covers key concepts, diagnostic methodologies, common scenarios, and best practices, with detailed case studies to illustrate real-world applications.

---

## Technical Background
### Key Concepts
- **StealthAUDIT for NetApp**: A component of Netwrix Enterprise Auditor designed to collect data from NetApp storage systems for auditing and reporting purposes.
- **Data Collection**: The process of scanning file systems, permissions, and activity logs on NetApp storage devices.
- **FSAA (File System Access Auditing)**: A specific type of scan that collects detailed access and permission data.
- **Proxy Servers**: Intermediate servers used to facilitate data collection from NetApp devices.
- **Tier 2 Databases**: Temporary databases used during data collection and bulk import processes.

### System Context
- **NetApp ONTAP**: The operating system for NetApp storage devices, with specific versions supported by StealthAUDIT.
- **Bulk Import**: A process that consolidates scan data into the central database for reporting and analysis.
- **fpolicy**: A NetApp feature that enables external engines like StealthAUDIT to monitor file operations.

---

## Issue Recognition & Triage
### Symptoms of Data Collection Issues
- Scans failing with "out of memory" errors or insufficient storage warnings.
- SQL database disk space running out unexpectedly.
- Scans running indefinitely or failing to complete.
- Errors related to permissions or communication between proxy servers and NetApp devices.
- Compatibility inquiries for specific NetApp ONTAP versions.

### Priority Assessment
- **High Priority**: Scans failing across multiple targets, critical errors affecting business operations.
- **Medium Priority**: Single scan failures, disk space warnings, or configuration issues.
- **Low Priority**: Compatibility inquiries or non-critical feature limitations.

---

## Diagnostic Methodology
### Systematic Approach
1. **Initial Assessment**:
   - Review the problem description and environment details provided by the customer.
   - Confirm the product version and NetApp ONTAP version in use.
2. **Log Analysis**:
   - Collect and analyze relevant logs, including scan logs, proxy logs, and SQL error logs.
3. **Configuration Review**:
   - Verify fpolicy settings, retention policies, and proxy server configurations.
4. **Replication in Lab**:
   - Reproduce the issue in a controlled lab environment if possible.
5. **Escalation**:
   - Escalate to Tier 2 or R&D if the issue involves a suspected product defect or requires a hotfix.

---

## Information Collection
### Questions to Ask Customers
- What specific error messages are being encountered?
- What is the version of StealthAUDIT and NetApp ONTAP in use?
- Are there any recent changes to the environment (e.g., upgrades, configuration changes)?
- What is the retention policy for data collection?
- Are antivirus or firewall settings potentially interfering with scans?

### Logs and Data to Collect
- Scan logs and bulk import job logs.
- Proxy server logs.
- SQL Server logs and database size details.
- Memory dump files (if applicable).
- Screenshots or error messages.

---

## Common Scenarios & Solutions
### Scenario 1: Out of Memory Errors During Scans
- **Root Cause**: Memory leak in the product.
- **Solution**: Apply the hotfix provided in [this article](https://nwxcorp.lightning.force.com/lightning/r/General__kav/ka0Qk0000004vsXIAQ/view). Monitor memory usage during scans to identify potential leaks early.

### Scenario 2: SQL Database Disk Space Issues
- **Root Cause**: Retention policy not enforced due to incomplete FS jobs.
- **Solution**: Upgrade to the latest version and ensure FS jobs end cleanly. Regularly verify retention settings and data storage.

### Scenario 3: Scan Running Indefinitely
- **Root Cause**: Incorrect fpolicy configuration.
- **Solution**: Validate and update the fpolicy using the following command:
  ```bash
  vserver fpolicy policy external-engine create -vserver [SVM_NAME] -engine-name StealthAUDITEngine -primary-servers [IP_ADDRESS,…] -port 9999 -extern-engine-type asynchronous -ssl-option no-auth
  ```

### Scenario 4: Compatibility Inquiries
- **Root Cause**: Lack of official testing for specific NetApp ONTAP versions.
- **Solution**: Refer to the compatibility documentation and recommend upgrades to supported versions.

### Scenario 5: Tier 2 Database Errors
- **Root Cause**: Corruption caused by residual scripts or processes.
- **Solution**: Disable problematic scripts and archive Tier 2 databases to reset the environment.

---

## Detailed Case Studies
### Case Study 1: Out of Memory Errors ([Ticket 500Qk00000CaKfiIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CaKfiIAF/view))
- **Symptoms**: Scans failing with "out of memory" errors.
- **Diagnostic Steps**: Reviewed logs, confirmed storage availability, collected memory dumps.
- **Resolution**: Applied a hotfix to resolve the memory leak.
- **Key Takeaways**: Monitor memory usage during scans and ensure antivirus settings do not interfere.

### Case Study 2: SQL Database Disk Space Issues ([Ticket 500Qk00000D4vufIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000D4vufIAB/view))
- **Symptoms**: SQL database running out of disk space.
- **Diagnostic Steps**: Verified retention policy, escalated to R&D.
- **Resolution**: Upgraded software and implemented bulk import workarounds.
- **Key Takeaways**: Regularly check retention settings and monitor FS job completion.

### Case Study 3: Scan Running Indefinitely ([Ticket 500Qk00000DRJByIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DRJByIAP/view))
- **Symptoms**: SVM scan running for 6 days without completion.
- **Diagnostic Steps**: Validated fpolicy, adjusted schedules, configured bulk imports.
- **Resolution**: Updated fpolicy settings to resolve the issue.
- **Key Takeaways**: Ensure fpolicy is correctly configured for all SVM targets.

### Case Study 4: Tier 2 Database Errors ([Ticket 500Qk00000M4x4vIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000M4x4vIAB/view))
- **Symptoms**: Errors during FSAA Bulk Import process.
- **Diagnostic Steps**: Analyzed logs, escalated to Tier 2, tested in lab.
- **Resolution**: Applied a hotfix to resolve database conflicts.
- **Key Takeaways**: Monitor for database conflicts after upgrades and collect detailed logs.

---

## Best Practices & Tips
- **Proactive Monitoring**: Regularly monitor scan durations, memory usage, and database sizes to identify potential issues early.
- **Configuration Validation**: Ensure fpolicy, retention policies, and proxy server settings are correctly configured.
- **Customer Communication**: Provide clear explanations of root causes and solutions, and share relevant documentation.
- **Log Analysis**: Collect and analyze logs systematically to pinpoint issues.
- **Escalation Readiness**: Escalate complex issues promptly with detailed logs and environment information.

---

## Escalation Guidelines
### When to Escalate
- Suspected product defects or memory leaks.
- Compatibility issues requiring R&D confirmation.
- Persistent errors despite following standard troubleshooting steps.

### How to Escalate
1. Collect all relevant logs and data.
2. Document the troubleshooting steps already taken.
3. Submit the case to Tier 2 or R&D with a detailed summary of findings.

