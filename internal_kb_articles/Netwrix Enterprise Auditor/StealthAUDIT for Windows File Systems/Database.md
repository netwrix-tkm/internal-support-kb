# Knowledge Base Reference Guide: Troubleshooting Database Issues in StealthAUDIT for Windows File Systems

## Overview

This guide provides a comprehensive reference for diagnosing and resolving database-related issues in the StealthAUDIT for Windows File Systems component of Netwrix Enterprise Auditor (NEA). Database issues can impact critical functionalities such as bulk imports, scans, and data management, making it essential for support engineers to understand common patterns, root causes, and resolution strategies. This document outlines systematic approaches, real-world case studies, and best practices to ensure consistent and effective troubleshooting.

---

## Technical Background

### Key Concepts
- **StealthAUDIT Database Architecture**: StealthAUDIT uses a multi-tier database structure (Tier 1 and Tier 2) to store and process data. Tier 1 handles raw data, while Tier 2 processes and aggregates it for reporting.
- **Bulk Import Jobs**: These jobs import data into the database for analysis. They are sensitive to database integrity, file path lengths, and system configurations.
- **Retention Policies**: Define how long data is stored in the database. Mismanagement can lead to excessive database growth.
- **Database Maintenance**: Includes tasks like truncating tables, shrinking databases, and repairing corrupted tables to ensure optimal performance.

### Common Terminology
- **T1/T2 Databases**: Tier 1 and Tier 2 databases used in StealthAUDIT.
- **FSAA**: File System Access Analysis, a key feature for auditing file system permissions.
- **AccessGUID**: A unique identifier for access data in the database.
- **SQL Logic Errors**: Errors related to database queries or schema mismatches.
- **Database Shrink Operation**: A process to reclaim unused disk space after data truncation.

---

## Issue Recognition & Triage

### Symptoms of Database Issues
- Bulk import job failures with specific error messages (e.g., "database disk image is malformed").
- Excessive database growth leading to storage issues.
- Errors during scans, such as schema mismatches or missing root elements.
- Incorrect reporting of file shares or permissions.

### Priority Assessment
- **High Priority**: Database corruption, bulk import failures, or critical scan errors affecting production environments.
- **Medium Priority**: Data management issues, such as stale data or excessive database size.
- **Low Priority**: Non-critical discrepancies in reporting or minor configuration issues.

---

## Diagnostic Methodology

1. **Initial Assessment**:
   - Review the problem description and error messages.
   - Confirm the NEA version and environment details.

2. **Log Analysis**:
   - Collect and analyze logs from the affected jobs or scans.
   - Enable debug mode if necessary to capture detailed logs.

3. **Database Inspection**:
   - Check the size and integrity of the T1/T2 databases.
   - Identify any schema mismatches or corrupted tables.

4. **Configuration Review**:
   - Verify job settings, retention policies, and database configurations.
   - Check for external factors like antivirus interference.

5. **Reproduction**:
   - Attempt to reproduce the issue in a controlled environment to isolate the root cause.

---

## Information Collection

### Questions to Ask Customers
- What specific error messages are being encountered?
- When did the issue first occur, and were there any recent changes (e.g., upgrades)?
- Are there any third-party tools (e.g., antivirus) running on the server?
- What is the current size of the database, and are there storage constraints?

### Logs and Data to Collect
- Bulk import and scan logs.
- SQL Server logs and database schema details.
- Screenshots or descriptions of error messages.
- Configuration files for the affected jobs.

---

## Common Scenarios & Solutions

### Scenario 1: Bulk Import Failures
- **Symptoms**: Errors like "The specified path, file name, or both are too long" or "SQL logic error unknown database StrucMap."
- **Resolution**:
  1. Shorten job names to avoid path length issues.
  2. Drop and repair T2 databases for affected hosts.
  3. Increase database size if space constraints are identified.

### Scenario 2: Excessive Database Growth
- **Symptoms**: Database size exceeding storage limits, leading to errors like "Root element is missing."
- **Resolution**:
  1. Disable unnecessary jobs (e.g., `FS_FileTags`).
  2. Truncate large tables (e.g., `SA_FS_TagsMapped`).
  3. Perform a database shrink operation to reclaim disk space.

### Scenario 3: Schema Mismatches After Upgrade
- **Symptoms**: Errors indicating that the 'Create Schema Job' needs to be run.
- **Resolution**:
  1. Run the 'Create Schema Job' to update database tables.
  2. Verify that all NEA servers have been updated to the same version.

### Scenario 4: Corrupted Databases
- **Symptoms**: Errors like "database disk image is malformed."
- **Resolution**:
  1. Back up the T1/T2 databases.
  2. Drop corrupted tables and rerun jobs.
  3. Implement antivirus exclusions to prevent interference.

---

## Detailed Case Studies

### Case Study 1: Bulk Import Failures ([Ticket ID: 500Qk00000CZNVxIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CZNVxIAP/view))
- **Symptoms**: Bulk import jobs failed with path length and SQL logic errors.
- **Diagnostic Steps**:
  - Reviewed logs and identified long file paths and insufficient database space.
  - Dropped T2 databases and repaired affected servers.
- **Resolution**:
  - Shortened job names and increased database size.
  - Deleted the "Reports" folder to resolve reporting issues.
- **Key Takeaways**:
  - Monitor path lengths and database space proactively.
  - Always rerun jobs after making database changes.

### Case Study 2: Excessive Database Growth ([Ticket ID: 500Qk00000JMv3AIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JMv3AIAT/view))
- **Symptoms**: Database size exceeded 250GB, causing application errors.
- **Diagnostic Steps**:
  - Identified the `SA_FS_TagsMapped` table as the primary contributor.
  - Disabled the `FS_FileTags` job and truncated the table.
- **Resolution**:
  - Performed a database shrink operation to reclaim disk space.
- **Key Takeaways**:
  - Regularly monitor database size and disable unnecessary jobs.
  - Truncation alone does not reclaim disk space; shrinking is required.

### Case Study 3: Schema Mismatches After Upgrade ([Ticket ID: 500Qk00000HNR5lIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HNR5lIAH/view))
- **Symptoms**: FSAA scans failed due to missing schema tables.
- **Diagnostic Steps**:
  - Verified that the 'Create Schema Job' was disabled.
  - Consulted documentation and confirmed the need to run the job.
- **Resolution**:
  - Ran the 'Create Schema Job' to create missing tables.
- **Key Takeaways**:
  - Always run schema update jobs after upgrading NEA.
  - Ensure all servers are updated to the same version.

---

## Best Practices & Tips

1. **Proactive Monitoring**:
   - Regularly check database size and job configurations.
   - Monitor for antivirus interference and implement exclusions.

2. **Efficient Troubleshooting**:
   - Use debug logs to capture detailed error information.
   - Reproduce issues in a test environment to isolate root causes.

3. **Database Maintenance**:
   - Perform regular truncation and shrink operations.
   - Back up databases before making significant changes.

4. **Customer Communication**:
   - Clearly explain the impact of actions like truncation or schema updates.
   - Provide step-by-step instructions for recurring tasks.

---

## Escalation Guidelines

- **When to Escalate**:
  - Database corruption that cannot be resolved by dropping tables.
  - Persistent issues after following standard resolution steps.
  - Errors related to unsupported configurations or third-party tools.

- **How to Escalate**:
  - Provide detailed logs, screenshots, and configuration files.
  - Document all troubleshooting steps taken and their outcomes.
  - Include a clear description of the impact on the customer's environment.