# Knowledge Base Reference Guide: Troubleshooting SharePoint Online Activity Auditing Issues in Netwrix Enterprise Auditor

## Overview
This guide provides a comprehensive reference for troubleshooting issues related to SharePoint Online (SPO) activity auditing in Netwrix Enterprise Auditor (NEA), specifically within the StealthAUDIT for SharePoint component. It covers common problems, diagnostic methodologies, resolution strategies, and best practices to ensure consistent and effective support for customers. Understanding and resolving these issues is critical for maintaining accurate activity monitoring, compliance reporting, and data integrity in SharePoint Online environments.

---

## Technical Background
### Key Concepts
- **Netwrix Enterprise Auditor (NEA):** A platform for auditing and monitoring IT environments, including SharePoint Online.
- **StealthAUDIT for SharePoint (SPAC):** A component of NEA that collects and analyzes SharePoint activity data.
- **Activity Auditing:** The process of capturing and mapping user and system activities in SharePoint Online for reporting and compliance purposes.
- **SharePointActivityMappings.xml:** A configuration file that maps SharePoint Online event types to their corresponding activity categories in NEA.
- **SPAA/SPSEEK Jobs:** Scans that collect permissions and activity data from SharePoint Online resources.
- **SPAC Bulk Import:** A process that ingests collected activity data into the NEA database for analysis and reporting.

### Common Terminology
- **Event Type:** A specific activity or action logged in SharePoint Online (e.g., `SharingLinkCreated`, `DLPRuleMatch`).
- **Resource ID:** A unique identifier for a SharePoint resource (e.g., site, file, or folder) associated with an activity.
- **Foreign Key Constraint:** A database rule that enforces relationships between tables, ensuring data integrity.
- **Hotfix:** A software update that addresses specific issues or adds new functionality.

---

## Issue Recognition & Triage
### Identifying Common Symptoms
- **Unknown Event Type Warnings:** Messages indicating unmapped event types in SharePointActivityMappings.xml.
- **Database Errors:** Issues such as foreign key constraint conflicts during SPAC Bulk Import.
- **NULL Resource IDs:** Missing resource identifiers in activity records, leading to incomplete data in the Access Information Center (AIC).
- **Invalid URI Errors:** Errors related to incorrect URL formats in the SPAC database.
- **Activity Gaps:** Missing or incomplete activity data in reports.

### Assessing Priority
- **High Priority:** Issues causing data loss, such as failed SPAC Bulk Imports or missing activity records.
- **Medium Priority:** Warnings about unknown event types that do not immediately impact data collection.
- **Low Priority:** Configuration issues or minor warnings that do not affect core functionality.

---

## Diagnostic Methodology
### Systematic Troubleshooting Approach
1. **Reproduce the Issue:**
   - Run the relevant SPAC job (e.g., System Scan, Bulk Import) and observe the behavior.
   - Collect logs and error messages for analysis.

2. **Analyze Logs:**
   - Review SPAC logs (e.g., `3-SPAC_SystemScans_Log.tsv`) for error messages or warnings.
   - Search for keywords such as "Unknown event type," "Foreign key constraint," or "Invalid URI."

3. **Verify Configuration:**
   - Check the SharePointActivityMappings.xml file for missing event type mappings.
   - Ensure SPAC job settings (e.g., Activity Logs path) are correctly configured.

4. **Inspect Databases:**
   - Use tools like DB Browser for SQLite to examine SPAC.db3 or related databases.
   - Look for anomalies such as missing prefixes in URLs or NULL values in critical fields.

5. **Consult Documentation:**
   - Refer to Netwrix product documentation for guidance on configuration and known issues.

6. **Engage R&D (if needed):**
   - Escalate unresolved issues to the development team for further investigation or hotfix development.

---

## Information Collection
### Key Questions for Customers
- What version of NEA and StealthAUDIT for SharePoint are you using?
- When did the issue first occur, and has it been consistent?
- Have there been any recent upgrades, hotfixes, or configuration changes?
- Are there specific error messages or warnings in the logs?

### Logs and Data to Collect
- **SPAC Logs:** `3-SPAC_SystemScans_Log.tsv`, `SPAC_BulkImport_Log.tsv`
- **Database Snapshots:** SPAC.db3 and related tables (e.g., ActivitySiteCollections)
- **Configuration Files:** SharePointActivityMappings.xml
- **Screenshots:** Error messages or warnings in the NEA interface

---

## Common Scenarios & Solutions
### Scenario 1: Unknown Event Types
- **Symptoms:** Warnings about unmapped event types (e.g., `SharingLinkCreated`, `DLPRuleMatch`).
- **Solution:** Update the SharePointActivityMappings.xml file or apply the latest hotfix that includes mappings for new event types. Example: [Case 500Qk00000DwAYzIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DwAYzIAN/view).

### Scenario 2: Foreign Key Constraint Conflicts
- **Symptoms:** SPAC Bulk Import fails with database errors.
- **Solution:** Remove affected tables, rerun SPAA/SPSEEK jobs, and verify data integrity. Example: [Case 500Qk00000FKtEFIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FKtEFIA1/view).

### Scenario 3: NULL Resource IDs
- **Symptoms:** Missing resource IDs in activity records, leading to incomplete data in AIC.
- **Solution:** Ensure SPAA/SPSEEK scans are completed before SPAC scans. Example: [Case 500Qk00000GvnUIIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GvnUIIAZ/view).

### Scenario 4: Invalid URI Errors
- **Symptoms:** Errors related to incorrect URL formats in the SPAC database.
- **Solution:** Correct URL formats using SQL commands in DB Browser for SQLite. Example: [Case 500Qk00000NGVU7IAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NGVU7IAP/view).

---

## Detailed Case Studies
### Case Study 1: Unknown Event Types
- **Ticket ID:** [500Qk00000DwAYzIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DwAYzIAN/view)
- **Symptoms:** Warnings about unmapped event types (`SharingLinkUsed`, `DLPRuleMatch`).
- **Diagnostic Steps:** Reviewed logs, identified missing mappings, consulted R&D.
- **Resolution:** Applied hotfix 11.6.0.052 and upgraded to NEA 11.6.0.112.
- **Key Takeaways:** Monitor for new event types and ensure timely updates to mappings.

### Case Study 2: Foreign Key Constraint Conflicts
- **Ticket ID:** [500Qk00000FKtEFIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FKtEFIA1/view)
- **Symptoms:** SPAC Bulk Import failed due to database constraint errors.
- **Diagnostic Steps:** Investigated table relationships, removed affected tables, reran scans.
- **Resolution:** Successfully repopulated tables and completed the import.
- **Key Takeaways:** Understand database relationships and retention policies.

### Case Study 3: Invalid URI Errors
- **Ticket ID:** [500Qk00000NGVU7IAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NGVU7IAP/view)
- **Symptoms:** SPAC System Scan failed with "Invalid URI" errors.
- **Diagnostic Steps:** Identified incorrect URL formats, applied SQL fixes.
- **Resolution:** Corrected URLs and reran the scan successfully.
- **Key Takeaways:** Validate database integrity after upgrades.

---

## Best Practices & Tips
- **Proactive Monitoring:** Regularly review logs for warnings about unknown event types.
- **Database Backups:** Always back up databases before making changes.
- **Timely Updates:** Apply hotfixes and upgrades promptly to address known issues.
- **Customer Communication:** Clearly explain the root cause and resolution steps to customers.
- **Documentation:** Maintain up-to-date internal documentation on common issues and solutions.

---

## Escalation Guidelines
- **When to Escalate:**
  - Unresolved issues after applying known fixes.
  - New event types or errors requiring development team input.
  - Critical data loss or system failures.
- **How to Escalate:**
  - Provide detailed logs, database snapshots, and configuration files.
  - Include a clear description of the issue and steps already taken.
  - Reference similar resolved cases for context.

--- 

This guide serves as a definitive resource for handling SharePoint Online activity auditing issues in Netwrix Enterprise Auditor, enabling support engineers to resolve cases efficiently and consistently.