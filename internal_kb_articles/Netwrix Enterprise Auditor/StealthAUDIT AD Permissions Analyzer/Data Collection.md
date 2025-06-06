# Knowledge Base Reference Guide: Troubleshooting StealthAUDIT AD Permissions Analyzer Data Collection Issues

## Overview

The StealthAUDIT AD Permissions Analyzer is a critical feature within Netwrix Enterprise Auditor, designed to collect and analyze Active Directory permissions data. Proper functionality of this feature is essential for ensuring accurate reporting and compliance. This guide provides a systematic approach to diagnosing and resolving issues related to data collection within the AD Permissions Analyzer, enabling support engineers to address customer concerns efficiently and effectively.

---

## Technical Background

### Key Concepts
- **Active Directory Permissions Analyzer**: A tool that collects and analyzes permissions data from Active Directory to identify potential security risks.
- **Prerequisite Jobs**: Specific jobs that must be executed in sequence to ensure the Permissions Analyzer functions correctly.
- **Data Collection**: The process of gathering information from Active Directory and associated systems, which is critical for generating accurate reports.

### System Context
- **Netwrix Enterprise Auditor**: A platform for auditing and monitoring IT environments, including Active Directory.
- **StealthAUDIT**: A component within Netwrix Enterprise Auditor that provides advanced data collection and analysis capabilities.
- **SQL Database**: Stores configuration and collected data, which is queried during troubleshooting.

---

## Issue Recognition & Triage

### Symptoms
- Permissions Analyzer returns no results.
- Logs indicate warnings related to SQL Server or job queue threads.
- Customer requests detailed information about specific accounts but reports incomplete or unclear data.

### Priority Assessment
- **High Priority**: Permissions Analyzer fails to return results, impacting compliance reporting.
- **Medium Priority**: Customer requests detailed account information but lacks clarity on how to access it.

---

## Diagnostic Methodology

### Step-by-Step Approach
1. **Review Logs**: Examine error logs for warnings or errors related to SQL Server, job execution, or data collection.
2. **Verify Job Execution Order**: Confirm that prerequisite jobs have been executed in the correct sequence.
3. **Check Configuration Settings**: Ensure the Permissions Analyzer and associated jobs are configured correctly.
4. **Run SQL Queries**: Query the database to verify data integrity and identify missing information.
5. **Validate Permissions**: Confirm that the necessary permissions are in place for data collection.

---

## Information Collection

### Customer Questions
- What specific issue are you experiencing (e.g., missing results, incomplete data)?
- Have you executed any prerequisite jobs before running the Permissions Analyzer?
- Are there any warnings or errors in the logs?

### Logs and Data to Collect
- **Error Logs**: From the Netwrix Enterprise Auditor platform.
- **Job Queue Logs**: To verify execution order and status.
- **SQL Query Results**: For detailed account or permissions data.
- **Configuration Settings**: Screenshots or exported settings for the Permissions Analyzer.

---

## Common Scenarios & Solutions

### Scenario 1: Permissions Analyzer Returns No Results
- **Root Cause**: Prerequisite jobs were not executed in the correct order.
- **Solution**:
  1. Execute the following jobs in sequence:
     - ADInventory Job
     - AD_SensitiveSecurityGroups Job
     - AD_AdminSDHolder Job
     - AD_DomainReplication Job
     - AD_ResetPasswordPermissions Job
     - AD_GroupMembershipPermissions Job
  2. Rerun the Permissions Analyzer after completing these jobs.

### Scenario 2: Customer Requests Detailed Account Information
- **Root Cause**: Separation of user attributes and activity data within the Netwrix system.
- **Solution**:
  1. Use the Active Directory Inventory feature to gather user attributes.
  2. Run SQL queries to extract additional details, such as account creation dates and UserAccountControl settings.
  3. Provide guidance on interpreting data from separate reports.

---

## Detailed Case Studies

### Case Study 1: Permissions Analyzer Fails to Return Results
- **Ticket ID**: [500Qk00000GpASMIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GpASMIA3/view)
- **Initial Symptoms**: Permissions Analyzer returned no results; logs indicated SQL Server warnings.
- **Diagnostic Steps**:
  1. Reviewed error logs and identified warnings related to job queue threads.
  2. Verified job execution order and found prerequisite jobs were missing.
  3. Checked configuration settings for accuracy.
- **Resolution**:
  - Executed prerequisite jobs in the correct sequence.
  - Reran the Permissions Analyzer, which returned results as expected.
- **Key Takeaways**:
  - Always verify job execution order before troubleshooting further.
  - Regularly monitor logs for warnings or errors.
- **Efficiency Improvements**:
  - Create a checklist for prerequisite job execution to streamline troubleshooting.

---

### Case Study 2: Customer Requests Detailed Account Information
- **Ticket ID**: [500Qk00000MlYO9IAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MlYO9IAN/view)
- **Initial Symptoms**: Customer needed detailed information about three accounts but reported incomplete data.
- **Diagnostic Steps**:
  1. Reviewed existing reports and user attributes.
  2. Conducted a search for user activity using the Search Activity tool.
  3. Ran SQL queries to extract additional account details.
  4. Compiled findings and discussed them with the customer.
- **Resolution**:
  - Provided account creation dates, last logon information, and UserAccountControl settings.
  - Guided the customer on using the Active Directory Inventory feature for further details.
- **Key Takeaways**:
  - Clarify the distinction between user attributes and activity data to customers.
  - Use SQL queries to supplement data collection when reports are insufficient.
- **Efficiency Improvements**:
  - Develop a standardized report template for common account inquiries.

---

## Best Practices & Tips

1. **Verify Job Execution Order**: Always ensure prerequisite jobs are completed before running the Permissions Analyzer.
2. **Monitor Logs Regularly**: Check for warnings or errors that may indicate configuration or execution issues.
3. **Clarify Data Separation**: Educate customers on the distinction between user attributes and activity data to avoid confusion.
4. **Use SQL Queries**: Leverage SQL queries to extract detailed information when standard reports are insufficient.
5. **Standardize Processes**: Create checklists and templates for common troubleshooting scenarios to improve efficiency.

---

## Escalation Guidelines

### Criteria for Escalation
- Permissions Analyzer continues to fail after executing prerequisite jobs and verifying configuration settings.
- SQL queries or logs indicate database corruption or other critical issues.
- Customer requests data that cannot be retrieved using standard tools or queries.

### Escalation Procedure
1. Document all troubleshooting steps taken, including logs and SQL query results.
2. Provide a detailed description of the issue and its impact on the customer.
3. Escalate to the development or database team for further investigation, including all collected data and findings.

--- 

End of Document.