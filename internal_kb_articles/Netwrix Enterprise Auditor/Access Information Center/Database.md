# Knowledge Base Reference Guide: Troubleshooting Database Issues in Access Information Center (AIC)

## Overview

This guide provides a comprehensive reference for troubleshooting database-related issues in the Access Information Center (AIC) component of Netwrix Enterprise Auditor (NEA). Database connectivity and performance are critical for AIC functionality, as it relies on SQL Server for data storage and retrieval. Understanding and resolving these issues ensures uninterrupted access to audit data and system operations.

This document is designed to help support engineers systematically diagnose, resolve, and prevent database-related issues in AIC, leveraging insights from real-world cases.

---

## Technical Background

### Key Concepts
- **Access Information Center (AIC):** A web-based interface for accessing audit data collected by Netwrix Enterprise Auditor.
- **SQL Server Database:** The backend database used by AIC to store and retrieve audit data.
- **Authentication Methods:** AIC supports both Windows Authentication and SQL Authentication for database connections.
- **Ports:** Common SQL Server ports include 1433 (default) and 1434 (browser service). AIC may also use custom ports for HTTPS (e.g., 481).
- **Database Maintenance:** Proper maintenance of SQL databases (e.g., NVMonitorData) is essential to avoid performance issues.

### Common Terminology
- **IsDeleted Flag:** A database field indicating whether a record is marked as deleted.
- **UNIQUE KEY Constraint:** A database rule that prevents duplicate entries in specific tables.
- **SQL Timeout:** A failure to execute a query within the allotted time, often due to high server load or connectivity issues.

### System Context
- AIC interacts with SQL Server for data storage, retrieval, and reporting.
- Configuration settings, such as authentication methods and database credentials, are critical for successful operation.
- Environmental factors, such as firewall rules, disk space, and server performance, can impact database connectivity.

---

## Issue Recognition & Triage

### Symptoms of Database Issues
- Error messages such as:
  - "No connection to DB in AIC"
  - "Unable to contact the SQL Server Database"
  - "SQL Error: Login failed for user"
  - "Violation of UNIQUE KEY constraint"
- Slow query performance or timeouts.
- Inability to log in to the AIC console or web portal.
- Missing or incomplete data in AIC reports.

### Priority Assessment
- **High Priority:** Issues affecting production environments, preventing access to AIC, or causing data loss.
- **Medium Priority:** Performance degradation or intermittent connectivity issues.
- **Low Priority:** Non-critical errors or warnings that do not impact functionality.

---

## Diagnostic Methodology

### Systematic Approach
1. **Verify the Error Message:**
   - Review logs and error messages to identify the specific issue.
   - Example: "SQL Error: Login failed for user" indicates authentication issues.

2. **Check Database Connectivity:**
   - Test connectivity using SQL Server Management Studio (SSMS) or a .udl file.
   - Verify that required ports (e.g., 1433, 1434) are open.

3. **Review Configuration Settings:**
   - Confirm authentication methods (Windows vs. SQL Authentication).
   - Check database credentials and permissions.

4. **Analyze Server Performance:**
   - Monitor CPU, memory, and disk space on the SQL server.
   - Identify excessive connections or high resource utilization.

5. **Inspect Database Integrity:**
   - Check for missing or corrupted tables.
   - Look for duplicate entries or constraint violations.

6. **Test AIC Functionality:**
   - Attempt to log in to the AIC console or web portal.
   - Verify data visibility and report generation.

---

## Information Collection

### Questions to Ask Customers
- What error messages are being displayed?
- When did the issue first occur?
- Have there been any recent changes to the environment (e.g., database migrations, password updates)?
- What authentication method is being used (Windows or SQL)?
- Are there any firewall rules or antivirus software that could impact connectivity?

### Logs and Data to Collect
- AIC logs (e.g., `AIC.log`).
- SQL Server logs and error messages.
- Screenshots of error messages.
- Details of recent changes (e.g., database migrations, configuration updates).
- Network configuration details (e.g., firewall rules, open ports).

---

## Common Scenarios & Solutions

### Scenario 1: Database Connectivity Issues
- **Symptoms:** "No connection to DB in AIC" error.
- **Root Cause:** Firewall blocking SQL ports or SQL Server service not running.
- **Resolution:**
  1. Verify that SQL Server service is running.
  2. Ensure ports 1433 and 1434 are open in the firewall.
  3. Test connectivity using a .udl file.

### Scenario 2: UNIQUE KEY Constraint Violation
- **Symptoms:** Import process fails with a UNIQUE KEY constraint error.
- **Root Cause:** Duplicate entries in the database.
- **Resolution:**
  1. Identify and delete duplicate entries in the affected table.
  2. Update the `IsDeleted` flag for relevant records.
  3. Re-import the data.

### Scenario 3: Authentication Mismatch
- **Symptoms:** AIC set to Windows Authentication but attempts SQL Authentication.
- **Root Cause:** Misconfigured authentication settings.
- **Resolution:**
  1. Update AIC settings to match the desired authentication method.
  2. Reinstall AIC if necessary to reconfigure settings.

### Scenario 4: Slow Query Performance
- **Symptoms:** AIC queries are slow or time out.
- **Root Cause:** Excessive connections or high CPU usage on the SQL server.
- **Resolution:**
  1. Reduce the number of simultaneous connections.
  2. Optimize SQL server performance (e.g., index maintenance, query tuning).

### Scenario 5: Insufficient Disk Space
- **Symptoms:** "Unable to contact the SQL Server Database" error.
- **Root Cause:** Low disk space on SQL Server Data and Logs drives.
- **Resolution:**
  1. Add additional disk space.
  2. Configure database maintenance to manage growth.

---

## Detailed Case Studies

### Case Study 1: Connectivity Issue Due to Firewall
- **Ticket ID:** [500Qk00000CpppcIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CpppcIAB/view)
- **Symptoms:** "No connection to DB in AIC."
- **Diagnostic Steps:**
  1. Verified SQL Server service status.
  2. Tested port connectivity (1433, 1434).
- **Resolution:** Opened required ports in the firewall.
- **Key Takeaways:** Always verify firewall rules when diagnosing connectivity issues.

### Case Study 2: UNIQUE KEY Constraint Violation
- **Ticket ID:** [500Qk00000DUE1FIAX](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DUE1FIAX/view)
- **Symptoms:** Import process fails with a UNIQUE KEY constraint error.
- **Diagnostic Steps:**
  1. Reviewed logs for constraint violation details.
  2. Deleted duplicate entries in the database.
- **Resolution:** Updated `IsDeleted` flag and re-imported data.
- **Key Takeaways:** Regularly check for duplicate entries in critical tables.

### Case Study 3: Authentication Mismatch
- **Ticket ID:** [500Qk00000Fiv8QIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Fiv8QIAR/view)
- **Symptoms:** AIC set to Windows Authentication but attempts SQL Authentication.
- **Diagnostic Steps:**
  1. Reviewed AIC logs for authentication errors.
  2. Reinstalled AIC to reconfigure settings.
- **Resolution:** Aligned authentication settings with service account.
- **Key Takeaways:** Ensure authentication settings are consistent across components.

---

## Best Practices & Tips

1. **Verify Connectivity Early:** Use tools like SSMS or .udl files to test database connectivity before diving into complex diagnostics.
2. **Monitor SQL Server Performance:** Regularly check CPU, memory, and disk usage to prevent performance bottlenecks.
3. **Document Changes:** Maintain detailed records of configuration changes, migrations, and updates to facilitate troubleshooting.
4. **Use Admin Accounts for Configuration:** Always log in as an admin user when updating database credentials or settings.
5. **Schedule Maintenance Windows:** Plan regular maintenance to address disk space, database growth, and server reboots.
6. **Proactively Manage Tables:** Regularly review and clean up database tables to avoid constraint violations and duplicate entries.

---

## Escalation Guidelines

### When to Escalate
- The issue persists after following all diagnostic and resolution steps.
- Critical production environments are impacted, and immediate resolution is required.
- Complex database corruption or performance issues that require advanced expertise.

### How to Escalate
1. Collect all relevant logs, screenshots, and diagnostic data.
2. Document the steps already taken and their outcomes.
3. Escalate to the appropriate team or tier with a detailed summary of the issue.

--- 

End of Document.