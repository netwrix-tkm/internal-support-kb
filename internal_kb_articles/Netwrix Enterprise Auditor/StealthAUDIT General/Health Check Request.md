# Knowledge Base Reference Guide: Handling Health Check Requests in StealthAUDIT General

## Overview
This guide provides a comprehensive reference for support engineers handling issues related to Health Check Requests in the StealthAUDIT General component of Netwrix Enterprise Auditor. Health Check Requests often involve post-installation configuration guidance, database maintenance, and system health optimization. Understanding these issues is critical to ensuring customer satisfaction and maintaining system performance.

## Technical Background
### Key Concepts
- **Health Check Requests**: These are customer-initiated inquiries seeking guidance on system configuration, database optimization, or general health assessments of the Netwrix Enterprise Auditor environment.
- **StealthAUDIT Database**: The core repository for audit data, often hosted on MS SQL Server. Proper maintenance is essential for performance and data integrity.
- **Transaction Logs**: Logs that track database changes. Inadequate management can lead to bloating and system failures.
- **Domains and Connections**: Configuration settings in StealthAUDIT that define the scope of auditing. Misconfigured or outdated entries can cause confusion or errors.

### System Context
- **Netwrix Enterprise Auditor Version**: Issues in this category typically involve version 11.6.
- **Database Environment**: MS SQL Server is the standard database platform, with configurations such as Simple Recovery Mode impacting troubleshooting steps.
- **Installation Types**: Clean installations may require additional configuration to align with customer requirements.

## Issue Recognition & Triage
### Identifying Health Check Requests
- **Common Symptoms**:
  - Requests for post-installation configuration guidance.
  - Reports of unused database tables or outdated domain connections.
  - Notifications of database transaction log issues or low disk space.
- **Categorization**:
  - **Configuration Assistance**: Requests for setup guidance after installation.
  - **Database Maintenance**: Issues related to unused tables, transaction log bloating, or low disk space.
  - **System Optimization**: Requests for health checks to improve performance.

### Assessing Priority
- **High Priority**: Issues causing system downtime or job failures (e.g., bloated transaction logs).
- **Medium Priority**: Requests for database cleanup or domain removal.
- **Low Priority**: General configuration guidance without immediate impact on functionality.

## Diagnostic Methodology
1. **Clarify the Request**:
   - Determine whether the issue involves configuration, database maintenance, or system optimization.
   - Confirm the scope of support services with the customer.
2. **Gather Environment Details**:
   - Product version, database type, and installation type.
   - Symptoms and error messages.
3. **Analyze Logs and Data**:
   - Review SQL Server logs, StealthAUDIT database tables, and system settings.
4. **Identify Root Cause**:
   - Look for patterns such as unused tables, outdated domains, or transaction log bloating.
5. **Develop a Resolution Plan**:
   - Tailor the solution to the specific issue while ensuring data integrity and system stability.

## Information Collection
### Questions to Ask Customers
- What specific guidance or assistance is being requested?
- Are there any error messages or system notifications?
- What is the current configuration of the database and connections?
- Has a backup of the database been performed recently?

### Logs and Data to Collect
- SQL Server logs and database size metrics.
- List of tables in the StealthAUDIT database.
- Configuration details from Settings > Connections.
- Disk space availability on relevant drives.

## Common Scenarios & Solutions
### Scenario 1: Post-Installation Configuration Guidance
- **Symptoms**: Customer requests assistance after a clean installation.
- **Resolution**:
  - Coordinate with the account manager to arrange a health check.
  - Clearly communicate the scope of support services to the customer.
  - Follow up to ensure the customer receives the necessary assistance.

### Scenario 2: Unused Database Tables
- **Symptoms**: Accumulation of obsolete SQL tables created by previous administrators.
- **Resolution**:
  - Provide backup instructions for the StealthAUDIT database.
  - Guide the customer in identifying and dropping unused tables using SQL queries.
  - Example SQL commands:
    ```sql
    SELECT * INTO StealthAudit.[dbo].[SA_Messages_BAK] FROM StealthAudit.[dbo].[SA_Messages] WHERE JobRunTimeKey >= '2024-01-01';
    DROP TABLE StealthAudit.[dbo].[SA_Messages];
    EXEC sp_rename 'SA_Messages_BAK', 'SA_Messages';
    ```

### Scenario 3: Transaction Log Bloating
- **Symptoms**: Transaction log for 'tempdb' is full, causing job failures.
- **Resolution**:
  - Advise the customer to involve their DBA team for manual cleanup.
  - Ensure adequate disk space is available on the affected drive.
  - Recommend monitoring transaction log size and implementing alerts.

## Detailed Case Studies
### Case Study 1: Post-Installation Configuration ([Ticket ID 500Qk00000Hs2xZIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Hs2xZIAR/view))
- **Symptoms**: Customer requested configuration guidance after a clean installation.
- **Diagnostic Steps**:
  - Confirmed the request and clarified the scope of support services.
  - Contacted the account manager to arrange a health check.
- **Resolution**:
  - Facilitated communication between the customer and the account manager.
  - Ensured the customer received the necessary assistance.
- **Key Takeaways**:
  - Clearly communicate the scope of support services.
  - Follow up with account managers to ensure timely resolution.

### Case Study 2: Unused Database Tables ([Ticket ID 500Qk00000K97GTIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000K97GTIAZ/view))
- **Symptoms**: Customer reported unused SQL tables and outdated domains.
- **Diagnostic Steps**:
  - Provided backup instructions for the database.
  - Guided the customer in identifying and dropping unused tables.
  - Directed the customer to documentation for removing outdated domains.
- **Resolution**:
  - Customer successfully cleaned up the database and removed unwanted domains.
- **Key Takeaways**:
  - Always perform a backup before making database changes.
  - Regularly review and clean up unused tables to maintain performance.

### Case Study 3: Transaction Log Bloating ([Ticket ID 500Qk00000KdazTIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KdazTIAR/view))
- **Symptoms**: Transaction log for 'tempdb' was full, causing job failures.
- **Diagnostic Steps**:
  - Confirmed the error message and analyzed the transaction log.
  - Identified uncommitted transactions as the root cause.
- **Resolution**:
  - Advised the customer to involve their DBA team for cleanup.
  - Recommended monitoring disk space and transaction log size.
- **Key Takeaways**:
  - Proactively monitor transaction logs and disk space.
  - Implement alerts to prevent similar issues in the future.

## Best Practices & Tips
- **Backup First**: Always ensure a database backup is performed before making changes.
- **Clear Communication**: Clearly define the scope of support services to customers.
- **Proactive Monitoring**: Implement alerts for disk space and transaction log thresholds.
- **Regular Maintenance**: Encourage customers to periodically review and clean up unused database tables.
- **Collaborate with Account Managers**: Ensure seamless coordination for health check requests.

## Escalation Guidelines
- **When to Escalate**:
  - Issues involving critical system downtime or data loss.
  - Requests requiring advanced database expertise beyond the support team’s scope.
- **How to Escalate**:
  - Document all troubleshooting steps and findings.
  - Provide detailed logs and environment information.
  - Notify the appropriate team or account manager promptly.