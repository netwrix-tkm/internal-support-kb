# Knowledge Base Reference Guide: Troubleshooting Database Issues in Netwrix Enterprise Auditor

## Overview
This guide focuses on troubleshooting database-related issues in Netwrix Enterprise Auditor (NEA), specifically within the context of StealthAUDIT for NetApp. Database issues can significantly impact the functionality of scheduled jobs, data imports, and overall system performance. Understanding these issues is critical for maintaining system reliability and ensuring seamless operations in customer environments.

## Technical Background
### Key Concepts
- **SQL Jobs**: Automated tasks executed on SQL Server, often used for maintenance, data migration, and schema updates.
- **Indexes**: Database structures that improve query performance. Missing or corrupted indexes can lead to job failures.
- **TempDB**: A system database in SQL Server used for temporary storage. Issues with TempDB can disrupt SQL operations.
- **Column Data Types**: The type of data a column can store (e.g., `int`, `BIGINT`). Mismatched data types can cause errors during data processing.
- **Schema Migration**: The process of updating database structures during upgrades or configuration changes.

### System Context
- **Netwrix Enterprise Auditor**: A platform for IT auditing and compliance, relying on SQL Server databases for data storage and processing.
- **StealthAUDIT for NetApp**: A module within NEA designed for auditing NetApp file shares, requiring robust database configurations to handle large-scale data imports and scans.

## Issue Recognition & Triage
### Symptoms
- SQL job failures with specific error messages (e.g., missing indexes, data type mismatches).
- Excessive warnings or errors during scans or imports.
- Jobs hanging indefinitely during execution.
- Performance degradation or timeouts in database operations.

### Priority Assessment
- **High Priority**: Issues causing complete job failures or system downtime.
- **Medium Priority**: Errors or warnings that degrade performance but do not halt operations.
- **Low Priority**: Non-critical warnings or minor inefficiencies.

## Diagnostic Methodology
1. **Identify the Failing Component**: Determine which SQL job, table, or operation is failing.
2. **Review Logs**: Analyze SQL Server logs, job logs, and application logs for error messages.
3. **Reproduce the Issue**: Attempt to replicate the problem in a controlled environment.
4. **Isolate the Root Cause**: Use error messages and logs to pinpoint the underlying issue.
5. **Test Solutions**: Implement potential fixes in a test environment before applying them to production.

## Information Collection
### Customer Questions
- What is the exact error message or symptom observed?
- When did the issue first occur?
- Were there any recent changes to the database or environment (e.g., upgrades, schema changes)?
- Is the issue reproducible? If so, what steps trigger it?

### Logs and Data to Collect
- SQL Server job logs.
- Application logs from Netwrix Enterprise Auditor.
- Database schema and configuration details.
- Screenshots or exports of error messages.

## Common Scenarios & Solutions
### Scenario 1: SQL Job Fails Due to Missing Index
- **Symptoms**: Job failure with an error indicating a missing index.
- **Root Cause**: Index was dropped, either intentionally or unintentionally.
- **Resolution**:
  1. Confirm the missing index using SQL Server Management Studio (SSMS).
  2. Recreate the index using the appropriate SQL script.
  3. Monitor the job during its next scheduled execution.
- **Reference Case**: [500Qk00000CzMhUIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CzMhUIAV/view)

### Scenario 2: Data Type Mismatch in `SA_Messages` Table
- **Symptoms**: FSAA/SEEK imports fail with excessive warnings and errors.
- **Root Cause**: `MSGID` column type set to `int`, insufficient for the volume of data.
- **Resolution**:
  1. Update the `MSGID` column type to `BIGINT` manually.
  2. Apply the latest cumulative updates (CUs) to ensure future compatibility.
  3. Verify database configurations post-update.
- **Reference Case**: [500Qk00000Ni2aLIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ni2aLIAR/view)

### Scenario 3: FS Create Schema Job Hangs Indefinitely
- **Symptoms**: Job hangs during the Data Migration phase, causing downstream failures.
- **Root Cause**: FS_MigrateSchema job not executed prior to FS Create Schema job.
- **Resolution**:
  1. Execute the FS_MigrateSchema job.
  2. Run the FS Create Schema job after FS_MigrateSchema completes.
  3. Monitor job progress and verify successful completion.
- **Reference Case**: [500Qk00000OgP7RIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OgP7RIAV/view)

## Detailed Case Studies
### Case Study 1: Missing Index Causes SQL Job Failure
- **Ticket ID**: [500Qk00000CzMhUIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CzMhUIAV/view)
- **Symptoms**: SQL job failed with error "Cannot find index 'IDX_SA_ADInventory_Principals_DisplayName'."
- **Diagnostic Steps**:
  1. Reviewed job logs and confirmed the missing index.
  2. Verified with the DBA team that the DROP operation was unintentional.
- **Resolution**:
  - Cleaned up TempDB to resolve cleanup operation issues.
  - Recreated the missing index.
- **Key Takeaways**:
  - Regularly monitor SQL jobs and indexes.
  - Document and communicate database changes.

### Case Study 2: Data Type Mismatch in `SA_Messages` Table
- **Ticket ID**: [500Qk00000Ni2aLIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ni2aLIAR/view)
- **Symptoms**: FSAA/SEEK imports failed with over 1,000 warnings per host/share.
- **Diagnostic Steps**:
  1. Analyzed error messages related to the `MSGID` column.
  2. Confirmed the column type was set to `int`.
- **Resolution**:
  - Updated the column type to `BIGINT`.
  - Ensured future updates included this change.
- **Key Takeaways**:
  - Align database configurations with expected data types.
  - Monitor warnings and errors during scans for early detection.

### Case Study 3: FS Create Schema Job Hangs
- **Ticket ID**: [500Qk00000OgP7RIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OgP7RIAV/view)
- **Symptoms**: Job hung during Data Migration > SQL script 1 of 3.
- **Diagnostic Steps**:
  1. Confirmed the job was stuck in SSMS.
  2. Investigated logs and identified the missing FS_MigrateSchema step.
- **Resolution**:
  - Executed FS_MigrateSchema job before FS Create Schema job.
  - Verified successful completion of both jobs.
- **Key Takeaways**:
  - Follow post-upgrade procedures in sequence.
  - Use debug logs for additional insights.

## Best Practices & Tips
- **Monitor SQL Jobs**: Regularly check job statuses and logs to identify issues early.
- **Document Changes**: Maintain a record of database modifications to prevent unintended consequences.
- **Validate Configurations**: Ensure database settings align with product requirements, especially after updates.
- **Perform Regular Maintenance**: Clean up TempDB and optimize indexes to prevent performance issues.
- **Follow Upgrade Procedures**: Adhere to documented steps during upgrades to avoid job failures or hangs.

## Escalation Guidelines
- **When to Escalate**:
  - Issues persist despite following documented resolution steps.
  - Root cause cannot be identified or resolved within a reasonable timeframe.
  - Problems involve product defects or require development team intervention.
- **How to Escalate**:
  1. Gather all relevant logs, error messages, and diagnostic findings.
  2. Document steps already taken and their outcomes.
  3. Submit a detailed escalation request to the development or product team.

