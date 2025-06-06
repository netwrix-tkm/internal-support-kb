# Knowledge Base Reference Guide: Troubleshooting Data Collection Issues in StealthAUDIT for Exchange

## Overview
This guide focuses on troubleshooting data collection issues within the **StealthAUDIT for Exchange** component of **Netwrix Enterprise Auditor**. These issues typically involve incomplete or inaccurate data retrieval from Exchange environments, such as mailbox folder counts or permissions. Understanding and resolving these issues is critical for ensuring accurate reporting and maintaining customer confidence in the product.

## Technical Background
### Key Concepts
- **StealthAUDIT for Exchange**: A module within Netwrix Enterprise Auditor designed to collect and analyze data from Microsoft Exchange environments.
- **Data Collection Jobs**: SQL-based processes that retrieve specific data (e.g., mailbox details, folder counts) from Exchange servers and store it in SQL tables for reporting.
- **SQL Tables**: Data collected by StealthAUDIT is stored in SQL tables, which can be queried for analysis and reporting.
- **PowerShell Integration**: In some cases, PowerShell scripts are used to supplement or validate data collection.

### Terminology
- **Mailbox Folder Count**: The total number of folders within a mailbox.
- **SQL Query Scope**: The range of data retrieved by a SQL query, determined by filtering criteria such as user attributes or mailbox status.
- **Feature Request (FR)**: A formal request to enhance product functionality based on customer needs.

### System Context
StealthAUDIT for Exchange relies on SQL queries to extract data from Exchange environments. Misconfigured queries or environmental factors (e.g., permissions, filtering criteria) can lead to incomplete data collection.

## Issue Recognition & Triage
### Symptoms
- SQL tables return incomplete data (e.g., fewer mailboxes or folder counts than expected).
- Discrepancies between reported data and the actual environment.
- Errors or warnings during data collection jobs.

### Priority Assessment
- **High Priority**: Data critical for compliance or reporting is missing or inaccurate.
- **Medium Priority**: Non-critical data discrepancies that do not impact immediate operations.
- **Low Priority**: Minor inconsistencies or cosmetic issues.

## Diagnostic Methodology
### Systematic Approach
1. **Verify the Environment**:
   - Confirm the version of Netwrix Enterprise Auditor and StealthAUDIT.
   - Check the Exchange environment configuration (e.g., number of mailboxes, permissions).

2. **Review SQL Queries**:
   - Examine the SQL query used in the data collection job.
   - Identify potential filtering criteria or scope limitations.

3. **Validate Data Sources**:
   - Cross-check SQL table data with PowerShell scripts or Exchange Management Shell outputs.

4. **Reproduce the Issue**:
   - Run the data collection job in a test environment to replicate the problem.

5. **Analyze Logs**:
   - Review StealthAUDIT logs for errors or warnings related to the data collection job.

6. **Engage the Customer**:
   - Clarify requirements and expectations for the data being collected.

## Information Collection
### Questions to Ask the Customer
- How many mailboxes are in the environment?
- Are there any specific mailboxes or folders missing from the results?
- Have there been recent changes to the Exchange environment (e.g., mailbox migrations, deletions)?
- What is the intended use case for the data (e.g., reporting, compliance)?

### Logs and Data to Collect
- StealthAUDIT job logs.
- SQL query used in the data collection job.
- Sample outputs from PowerShell scripts for comparison.
- Screenshots or reports highlighting the discrepancy.

## Common Scenarios & Solutions
### Scenario 1: Incomplete Mailbox Data
- **Symptoms**: SQL table returns fewer mailboxes than expected.
- **Root Cause**: SQL query scope is limited by filtering criteria (e.g., excluding certain users or mailboxes).
- **Resolution**: Modify the SQL query to expand the scope. For example:
  ```sql
  SELECT DisplayName, COUNT(*) AS FolderCount 
  FROM StealthAudit.dbo.[SA_EX_Perms_EXO_Details_EXO] 
  WHERE EmailAddressSMTP NOT LIKE 'Departed%' 
  GROUP BY DisplayName;
  ```

### Scenario 2: Missing Folder Counts
- **Symptoms**: Folder counts are missing for some mailboxes.
- **Root Cause**: Permissions issues or mailbox-specific anomalies.
- **Resolution**: Validate permissions and rerun the job. Use PowerShell scripts to verify folder counts.

### Scenario 3: SQL Table Not Updating
- **Symptoms**: Data in the SQL table does not reflect recent changes in the environment.
- **Root Cause**: Data collection job not running or failing silently.
- **Resolution**: Check job schedules and logs. Restart the job if necessary.

## Detailed Case Studies
### Case Study: Ticket [500Qk00000LYF5OIAX](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LYF5OIAX/view)
#### Initial Symptoms
The SQL table `SA_EX_Folderdetails_DEFAULT` returned folder counts for only 1,600 mailboxes out of over 3,000 in the environment.

#### Diagnostic Steps
1. Verified the SQL query used in the data collection job.
2. Discussed requirements with the customer to clarify the desired output.
3. Created a new SQL job to populate a custom table (`SA_EX_FolderCount`) with the required data.

#### Key Information
- The original SQL query had implicit filtering criteria that excluded some mailboxes.
- A new query was written to include all relevant mailboxes and count their folders.

#### Resolution
A new SQL job was created with the following query:
```sql
IF OBJECT_ID('SA_EX_Perms_EXO_Details_EXO', 'U') IS NOT NULL 
BEGIN 
    DROP TABLE SA_EX_Perms_EXO_Details_EXO; 
END;

SELECT DisplayName, COUNT(*) AS FolderCount 
INTO SA_EX_FolderCount 
FROM StealthAudit.dbo.[SA_EX_Perms_EXO_Details_EXO] 
WHERE UserName LIKE 'default' 
AND EmailAddressSMTP NOT LIKE 'Departed%' 
GROUP BY DisplayName;
```
This resolved the issue by accurately counting folders for all mailboxes.

#### Key Takeaways
- Always review SQL queries for implicit filtering criteria.
- Engage customers to clarify requirements before implementing changes.
- Document custom jobs for future reference.

#### Efficiency Improvements
- Develop a library of reusable SQL queries for common data collection scenarios.
- Automate validation of SQL query outputs against PowerShell scripts.

## Best Practices & Tips
- **SQL Query Design**: Ensure queries are comprehensive and account for all relevant data.
- **Validation**: Cross-check SQL outputs with PowerShell or Exchange Management Shell to ensure accuracy.
- **Documentation**: Maintain detailed records of custom jobs and their purposes.
- **Customer Communication**: Clearly explain limitations and proposed solutions to customers.
- **Proactive Monitoring**: Regularly review data collection jobs and logs to identify potential issues early.

## Escalation Guidelines
- **When to Escalate**:
  - The issue persists despite following standard troubleshooting steps.
  - The customer requests a feature enhancement or customization beyond the product's current capabilities.
  - Logs indicate a potential bug or product limitation.

- **How to Escalate**:
  - Gather all relevant information (logs, SQL queries, customer requirements).
  - Submit a detailed escalation request to the development or product management team.
  - Provide a clear summary of the issue, steps taken, and proposed next steps.

