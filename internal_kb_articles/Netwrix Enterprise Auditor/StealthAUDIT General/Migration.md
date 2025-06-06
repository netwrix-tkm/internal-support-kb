# Netwrix Enterprise Auditor: StealthAUDIT General - Migration Reference Guide

## Overview

This guide provides a comprehensive reference for troubleshooting and resolving migration-related issues in the **StealthAUDIT General** component of **Netwrix Enterprise Auditor (NEA)**. Migration tasks often involve transitioning databases, servers, or configurations to new environments, which can introduce challenges such as compatibility issues, configuration mismatches, and operational disruptions. Understanding these issues is critical to ensuring smooth transitions and maintaining system functionality.

This document outlines key concepts, diagnostic methodologies, common scenarios, and best practices to equip support engineers with the tools and knowledge needed to handle migration-related cases effectively.

---

## Technical Background

### Key Concepts
- **StealthAUDIT**: A component of NEA used for auditing and reporting on IT infrastructure. It relies on SQL databases, service accounts, and scheduled jobs for its operations.
- **Migration**: The process of moving StealthAUDIT components, databases, or configurations to new servers or environments, often involving upgrades or domain changes.
- **Collation**: A database setting that determines how string data is sorted and compared. Collation mismatches can cause SQL errors during migrations.
- **Service Accounts**: Accounts used by StealthAUDIT for running jobs and accessing resources. Password changes or misconfigurations can disrupt operations.
- **Access Information Center (AIC)**: A web-based interface for accessing reports and managing configurations in NEA.

### Common Migration Scenarios
1. **Database Migration**: Moving SQL databases to newer versions or different servers.
2. **Server Migration**: Transitioning StealthAUDIT installations to new Windows servers.
3. **Domain Migration**: Reconfiguring NEA components to operate in a new domain.
4. **Version Upgrades**: Upgrading StealthAUDIT or NEA to newer versions during migration.

### System Context
- **SQL Server**: Hosts the StealthAUDIT database and requires proper configuration for connectivity and collation.
- **Windows Server**: Hosts the StealthAUDIT application and associated components.
- **Proxy Servers**: Used for scanning file systems or sensitive data.

---

## Issue Recognition & Triage

### Symptoms of Migration Issues
- Errors during job execution (e.g., collation conflicts, connection failures).
- Inability to launch the StealthAUDIT application or AIC.
- Missing configurations or data after migration.
- Certificate errors or SSL/TLS issues.
- Scheduled jobs failing to start or execute.

### Priority Assessment
- **High Priority**: Issues affecting production environments, such as job failures or application downtime.
- **Medium Priority**: Errors in non-production environments (e.g., DEV/QA) or during pre-migration testing.
- **Low Priority**: Documentation requests or minor configuration adjustments.

---

## Diagnostic Methodology

### Systematic Approach
1. **Understand the Environment**:
   - Identify the source and target environments (e.g., SQL versions, Windows Server versions).
   - Confirm the scope of the migration (e.g., database, server, or domain).

2. **Reproduce the Issue**:
   - Attempt to replicate the reported error in a controlled environment.
   - Review error messages and logs for specific details.

3. **Isolate the Root Cause**:
   - Check for configuration mismatches (e.g., collation settings, service account credentials).
   - Verify connectivity between components (e.g., SQL server, proxy server).

4. **Implement and Test Solutions**:
   - Apply fixes incrementally and validate functionality after each change.
   - Test critical operations such as job execution and report generation.

---

## Information Collection

### Questions to Ask Customers
- What is the source and target environment for the migration (e.g., SQL versions, server OS)?
- Are there any error messages or logs available?
- Have any configurations (e.g., service accounts, certificates) been changed recently?
- Was the migration performed during production hours or in a test environment?

### Logs and Data to Collect
- SQL Server logs and error messages.
- StealthAUDIT application logs.
- Screenshots of error messages or failed configurations.
- Details of scheduled jobs and their statuses.
- Network connectivity test results (e.g., `Test-NetConnection`).

---

## Common Scenarios & Solutions

### Scenario 1: Collation Conflicts
- **Symptoms**: SQL errors indicating collation conflicts during job execution or application launch.
- **Resolution**:
  1. Verify the collation settings of the source and target databases.
  2. Align the collation of the target database with the source database.
  3. Re-run jobs and validate functionality.

### Scenario 2: Service Account Password Reset
- **Symptoms**: Jobs fail to execute after a service account password change.
- **Resolution**:
  1. Update the password in all relevant configurations within the StealthAUDIT console.
  2. Manually verify job statuses and error messages.

### Scenario 3: Database Migration
- **Symptoms**: Connection errors or missing data after migrating the database to a new SQL server.
- **Resolution**:
  1. Ensure the SQL server is configured to accept connections on the correct port.
  2. Grant necessary permissions (e.g., `VIEW ANY DEFINITION`) to the service account.
  3. Update the database connection settings in the StealthAUDIT console.

### Scenario 4: Domain Migration
- **Symptoms**: Configuration mismatches or certificate errors after migrating to a new domain.
- **Resolution**:
  1. Update URL paths, certificates, and service account configurations.
  2. Re-scan the environment to ensure accurate data collection.

---

## Detailed Case Studies

### Case Study 1: Collation Conflict During Migration
- **Ticket**: [500Qk00000H9bUoIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000H9bUoIAJ/view)
- **Symptoms**: SQL collation conflict error during job execution.
- **Key Information**: Source database collation was "Latin1_General_CI_AS," while the target server used "SQL_Latin1_General_CP1_CI_AS."
- **Resolution**:
  1. Changed the collation of the target database to match the source.
  2. Re-ran jobs, resolving the conflict.
- **Takeaways**: Always verify collation settings before migration.

### Case Study 2: SQL Server Migration with Connection Issues
- **Ticket**: [500Qk00000NllcXIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NllcXIAR/view)
- **Symptoms**: "Remote server refused connection" error when changing the storage profile.
- **Key Information**: Missing `VIEW ANY DEFINITION` permission on the SQL server.
- **Resolution**:
  1. Granted the necessary permissions.
  2. Updated the storage profile and validated the connection.
- **Takeaways**: Ensure proper permissions are granted to service accounts during migration.

### Case Study 3: Domain Migration with Certificate Errors
- **Ticket**: [500Qk00000LYlWgIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LYlWgIAL/view)
- **Symptoms**: Certificate errors and missing configurations after domain migration.
- **Key Information**: Required updates to URL paths, certificates, and service accounts.
- **Resolution**:
  1. Updated configurations and re-scanned the environment.
  2. Verified functionality post-migration.
- **Takeaways**: Schedule migrations during off-peak hours and back up configurations.

---

## Best Practices & Tips

1. **Pre-Migration Planning**:
   - Document all configurations, including service accounts, scheduled jobs, and database settings.
   - Perform a pre-flight checklist to ensure readiness.

2. **Testing**:
   - Conduct thorough testing in DEV/QA environments before migrating to production.
   - Validate all critical operations post-migration.

3. **Communication**:
   - Keep customers informed throughout the migration process.
   - Provide clear documentation and follow-up support.

4. **Backup and Recovery**:
   - Always back up databases and configurations before initiating migration.
   - Have a rollback plan in case of unexpected issues.

---

## Escalation Guidelines

### When to Escalate
- Persistent issues after applying standard troubleshooting steps.
- Errors involving unsupported configurations or environments.
- Requests for new features or enhancements.

### How to Escalate
- Collect all relevant logs, screenshots, and error messages.
- Document the steps already taken and their outcomes.
- Submit a detailed escalation request to the development or product team.

--- 

End of Document.