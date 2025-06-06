# Comprehensive Reference Guide: Troubleshooting Data Collection Issues in Access Information Center (AIC)

## Overview

This guide provides a systematic approach to identifying, diagnosing, and resolving issues related to data collection in the Access Information Center (AIC) of Netwrix Enterprise Auditor. The AIC is a critical component for delivering actionable insights into permissions, effective access, and attribute changes. Ensuring its proper functionality is essential for maintaining accurate reporting and compliance.

This document is designed to help support engineers troubleshoot common issues, recognize patterns, and apply proven resolution strategies. It also includes escalation guidelines and best practices to ensure consistent and efficient handling of cases.

---

## Technical Background

### Key Concepts
- **Access Information Center (AIC):** A module in Netwrix Enterprise Auditor that provides detailed reports on permissions, effective access, and changes to Active Directory attributes.
- **Effective Access Reports:** These reports calculate and display the actual access rights of users and groups to specific resources, considering both direct and inherited permissions.
- **Differential Scans:** A method of scanning that captures incremental changes in Active Directory or file system permissions, ensuring up-to-date reporting.
- **FSAA (File System Access Auditing):** A scanning mechanism that collects permissions and access data from file systems.

### System Context
- **Data Collection Workflow:** Data is collected via FSAA scans or Active Directory Inventory scans, processed, and stored in the database. The AIC queries this data to generate reports.
- **Dependencies:** Proper configuration of scans, database health, and accurate permissions collection are prerequisites for AIC functionality.

---

## Issue Recognition & Triage

### Symptoms
- **Blank Effective Access Reports:** Reports fail to display user or group access details despite permissions being configured.
- **Missing Attribute Change Data:** Known changes to Active Directory attributes are not reflected in AIC reports.

### Priority Assessment
- **High Priority:** Issues affecting compliance reporting or critical business operations.
- **Medium Priority:** Issues impacting non-critical reports or test environments.
- **Low Priority:** Configuration questions or minor discrepancies in non-production environments.

---

## Diagnostic Methodology

### Step-by-Step Approach
1. **Verify Configuration:**
   - Confirm that FSAA scans or Active Directory Inventory scans are enabled and properly configured.
   - Check that the AIC is set up to track the relevant data (e.g., permissions, attribute changes).

2. **Review Reports:**
   - Examine the Permissions Report to ensure user/group memberships are being captured.
   - Check for any existing data in the Effective Access or Attribute Change reports.

3. **Validate Scans:**
   - Confirm the health and status of FSAA scans or Active Directory Inventory scans.
   - Ensure differential scans are enabled for Active Directory Inventory.

4. **Inspect Database Health:**
   - Investigate whether the database views (e.g., `dbo.SA_FSAA_EffectiveAccessView`) are updating correctly.
   - Look for any anomalies in the database records related to the affected reports.

5. **Collect Logs:**
   - Gather relevant logs from the Netwrix system and database for further analysis.

6. **Engage Customer:**
   - If necessary, schedule a meeting to review the environment and configuration in detail.

---

## Information Collection

### Questions to Ask Customers
- What specific reports are affected (e.g., Effective Access, Attribute Changes)?
- Have there been recent changes to the environment (e.g., server configurations, permissions)?
- Are FSAA scans or Active Directory Inventory scans running as expected?
- Is the issue occurring in production, test, or both environments?

### Logs and Data to Collect
- FSAA scan logs and status reports.
- Active Directory Inventory scan settings and logs.
- Database logs and query results for affected views (e.g., `dbo.SA_FSAA_EffectiveAccessView`).
- Screenshots or exports of affected reports.

---

## Common Scenarios & Solutions

### Scenario 1: Blank Effective Access Reports
- **Symptoms:** Effective Access reports are blank despite permissions being configured.
- **Root Cause:** Database records for Effective Access were not updating due to incorrect configuration.
- **Solution:** Delete the affected records from the database to allow proper population of Effective Access reports.
- **Reference Case:** [500Qk00000DNCgvIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DNCgvIAH/view)

### Scenario 2: Missing Attribute Change Data
- **Symptoms:** Attribute changes for Active Directory users are not displayed in the AIC.
- **Root Cause:** Differential scans for Active Directory Inventory were not enabled.
- **Solution:** Enable differential scans to capture incremental changes.
- **Reference Case:** [500Qk00000FNTYYIA5](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FNTYYIA5/view)

---

## Detailed Case Studies

### Case Study 1: Blank Effective Access Reports
- **Ticket ID:** [500Qk00000DNCgvIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DNCgvIAH/view)
- **Initial Symptoms:** Effective Access reports were blank in the AIC.
- **Diagnostic Steps:**
  1. Verified user permissions and group memberships.
  2. Checked FSAA scan health and database views.
  3. Identified that `dbo.SA_FSAA_EffectiveAccessView` was not updating.
- **Resolution:** Deleted the affected database records, allowing the Effective Access reports to populate correctly.
- **Key Takeaways:** Ensure FSAA scans and database views are functioning correctly. Document configuration changes to prevent recurrence.

### Case Study 2: Missing Attribute Change Data
- **Ticket ID:** [500Qk00000FNTYYIA5](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FNTYYIA5/view)
- **Initial Symptoms:** Attribute changes for AD users were not displayed in the AIC.
- **Diagnostic Steps:**
  1. Verified AIC configuration and scanning settings.
  2. Confirmed that changes were made to AD users.
  3. Identified that differential scans were not enabled.
- **Resolution:** Enabled differential scans for Active Directory Inventory, resolving the issue.
- **Key Takeaways:** Differential scans are essential for capturing incremental changes. Verify scanning settings during initial troubleshooting.

---

## Best Practices & Tips

1. **Regularly Monitor Scans:**
   - Ensure FSAA and Active Directory Inventory scans are running as scheduled and without errors.

2. **Enable Differential Scans:**
   - For Active Directory Inventory, always enable differential scans to capture incremental changes.

3. **Document Configuration Changes:**
   - Maintain a record of any changes made to the environment or Netwrix configuration.

4. **Proactive Database Maintenance:**
   - Periodically review database health and clean up outdated or corrupted records.

5. **Customer Communication:**
   - Clearly explain the root cause and resolution steps to customers. Provide guidance on preventing similar issues.

---

## Escalation Guidelines

### When to Escalate
- The issue persists despite following standard troubleshooting steps.
- Database anomalies cannot be resolved without advanced intervention.
- The problem affects multiple customers or appears to be a systemic issue.

### How to Escalate
1. Collect all relevant logs, screenshots, and configuration details.
2. Document the steps already taken and their outcomes.
3. Submit the case to the appropriate escalation team with a detailed summary.

