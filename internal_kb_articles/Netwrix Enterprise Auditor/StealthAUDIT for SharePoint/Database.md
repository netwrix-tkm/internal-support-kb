# Knowledge Base Reference Guide: Troubleshooting Database Issues in Netwrix Enterprise Auditor

## Overview
This guide focuses on troubleshooting database-related issues in Netwrix Enterprise Auditor (NEA), specifically within the StealthAUDIT for SharePoint component. Database issues can impact critical functionalities such as DLP scans and bulk import operations, leading to delays, incomplete data imports, or system errors. Understanding these issues is essential for maintaining system performance and ensuring data integrity.

## Technical Background
### Key Concepts
- **Netwrix Enterprise Auditor (NEA):** A platform for auditing and monitoring IT environments, including SharePoint on-premises and SharePoint Online.
- **StealthAUDIT for SharePoint:** A module within NEA designed for auditing SharePoint environments, including permissions, activity, and sensitive data discovery.
- **Database Integration:** NEA relies on SQL databases to store audit data, scan results, and configuration settings. Proper database configuration is critical for system functionality.
- **DLP Scans:** Data Loss Prevention scans identify sensitive data within SharePoint environments. Results are imported into the database for reporting and analysis.
- **Bulk Import Jobs:** Used to import large datasets, such as SharePoint Online audit logs, into the NEA database.

### Common Terminology
- **Endpoint Protection Software:** Antivirus or security software that may interfere with file access during scans.
- **SQL Server Memory Configuration:** Settings that control how much RAM the SQL server can use, impacting performance and stability.
- **SPAA Tables:** Database tables specific to SharePoint audit data.

## Issue Recognition & Triage
### Symptoms
- **DLP Scans:** Long scan durations, missing scan results in the database, or errors indicating file access conflicts.
- **Bulk Import Jobs:** Failed imports with SQL-related errors, such as "connection's current state is closed."

### Priority Assessment
- **High Priority:** Issues causing data loss, system downtime, or critical functionality failures.
- **Medium Priority:** Performance degradation or delays in non-critical operations.
- **Low Priority:** Minor errors or warnings that do not impact functionality.

## Diagnostic Methodology
### Systematic Approach
1. **Confirm Environment Details:** Verify the NEA version, build number, and database configuration.
2. **Review Logs:** Examine debug logs for error messages related to scans or imports.
3. **Check Resource Allocation:** Analyze SQL server memory settings and endpoint protection software configurations.
4. **Test Scenarios:** Temporarily disable endpoint protection or adjust SQL server settings to isolate the issue.
5. **Validate Repairs:** Run system repairs or database table resets as needed.

### Decision Points
- If logs indicate file access conflicts, focus on endpoint protection software.
- If SQL errors are present, investigate memory allocation and server performance.

## Information Collection
### Customer Queries
- What version/build of NEA and SQL server are being used?
- Have there been recent upgrades or configuration changes?
- Are endpoint protection or backup processes running during scans or imports?

### Logs and Data
- Debug logs from NEA and SQL server.
- Event logs from the operating system.
- Screenshots or descriptions of error messages.

## Common Scenarios & Solutions
### Scenario 1: DLP Scan Results Missing from Database
- **Symptoms:** Long scan durations, missing DLP data, "file is used by another process" errors.
- **Root Cause:** File access conflicts caused by endpoint protection software.
- **Resolution:**
  - Add exclusions to endpoint protection software for NEA-related files.
  - Temporarily disable endpoint protection during scans to confirm interference.
  - Run system repairs to address damaged T2 files.
- **Reference Case:** [Ticket ID 500Qk00000CVKpzIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CVKpzIAH/view)

### Scenario 2: Bulk Import Jobs Failing with SQL Errors
- **Symptoms:** Failed imports, "connection's current state is closed" errors.
- **Root Cause:** SQL server memory configuration set to unlimited RAM, causing performance issues.
- **Resolution:**
  - Adjust SQL server memory settings to use a maximum of 75% of total RAM.
  - Monitor SQL server performance during bulk import operations.
- **Reference Case:** [Ticket ID 500Qk00000K9KX9IAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000K9KX9IAN/view)

## Detailed Case Studies
### Case Study 1: DLP Scan Results Missing
- **Initial Symptoms:** Customer reported missing DLP scan results despite permissions being imported correctly.
- **Diagnostic Steps:**
  - Verified NEA version and build number.
  - Reviewed logs for file access errors.
  - Suggested disabling endpoint protection temporarily.
  - Requested debug logs for deeper analysis.
- **Key Information:** Logs revealed "file is used by another process" errors.
- **Resolution:** Added exclusions to endpoint protection software and repaired damaged T2 files.
- **Key Takeaways:** Endpoint protection software can interfere with file access during scans. Adding exclusions and running repairs resolved the issue efficiently.

### Case Study 2: Bulk Import Jobs Failing
- **Initial Symptoms:** Customer reported SQL-related errors after upgrading NEA.
- **Diagnostic Steps:**
  - Reviewed SQL server logs and debug logs from NEA.
  - Confirmed no external issues with SQL server.
  - Suggested checking SQL server memory allocation.
- **Key Information:** SQL server was set to use unlimited RAM, causing connection issues.
- **Resolution:** Adjusted SQL server memory settings to use 75% of total RAM.
- **Key Takeaways:** Proper SQL server resource allocation is critical for stable performance during bulk imports.

## Best Practices & Tips
- **Endpoint Protection:** Always add exclusions for NEA-related files and processes to prevent interference.
- **SQL Server Configuration:** Set memory limits to avoid performance degradation during high-load operations.
- **Log Analysis:** Enable debug mode for detailed logs when troubleshooting complex issues.
- **System Updates:** Keep NEA and SQL server updated to the latest versions to ensure compatibility and stability.
- **Proactive Monitoring:** Regularly review system performance and resource allocation to prevent issues.

## Escalation Guidelines
### Criteria for Escalation
- Issues persist despite following resolution steps.
- Errors indicate potential software bugs or compatibility issues.
- Customer environment includes unsupported configurations.

### Escalation Procedures
1. Collect all relevant logs, screenshots, and environment details.
2. Document troubleshooting steps already taken.
3. Submit the case to the development or product team for further analysis.
4. Communicate escalation status and expected timelines to the customer.

End of Document.