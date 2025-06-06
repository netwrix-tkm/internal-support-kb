# Comprehensive Knowledge Base Guide: Troubleshooting Database Issues in Netwrix Enterprise Auditor (StealthAUDIT for Active Directory)

## Overview
This guide provides a systematic approach to diagnosing and resolving database-related issues in Netwrix Enterprise Auditor (NEA) with a focus on the StealthAUDIT for Active Directory component. Database issues can disrupt critical auditing and reporting functions, making it essential to understand their root causes and resolution strategies. This document equips support engineers with the knowledge and tools to handle these issues effectively.

---

## Technical Background
### Key Concepts
- **StealthAUDIT for Active Directory**: A component of NEA that collects and analyzes Active Directory (AD) data for auditing and reporting purposes.
- **Database Dependencies**: NEA relies on SQL Server databases to store and process collected data. Proper configuration and maintenance of these databases are critical.
- **Recovery Models**: SQL Server databases can use different recovery models (e.g., Full, Simple) that impact transaction log growth and performance.
- **Collation Settings**: NEA requires case-insensitive collation for SQL Server databases to ensure compatibility with its queries and operations.

### Common Terminology
- **Jobs**: Automated tasks in NEA that collect, process, and analyze data.
- **Temporary Tables**: Intermediate storage structures used during job execution.
- **Foreign Key Constraints**: Database rules that enforce relationships between tables.
- **Threshold Parameters**: Configurable values that determine job behavior (e.g., stale user thresholds).

---

## Issue Recognition & Triage
### Symptoms
- Job failures with SQL errors (e.g., invalid column names, missing objects).
- Excessive database growth or resource consumption.
- Errors during upgrades or database operations (e.g., foreign key conflicts).
- Unexpected behavior in reports or data collection.

### Priority Assessment
- **High Priority**: Database crashes, job failures affecting critical business operations, or issues causing significant resource consumption.
- **Medium Priority**: Errors in non-critical jobs or reports.
- **Low Priority**: Configuration requests or minor discrepancies in reports.

---

## Diagnostic Methodology
### Systematic Approach
1. **Reproduce the Issue**: Attempt to replicate the problem by running the affected job or operation.
2. **Analyze Logs**: Review job logs, SQL error messages, and system event logs for clues.
3. **Verify Environment**: Check database configuration, permissions, and collation settings.
4. **Isolate the Problem**: Identify whether the issue is related to database configuration, job logic, or environmental changes.
5. **Test Solutions**: Apply fixes incrementally and verify their impact.

---

## Information Collection
### Questions to Ask Customers
- What is the impact of the issue on your operations?
- Have there been any recent changes to the environment (e.g., upgrades, migrations)?
- What steps have you already taken to troubleshoot the issue?
- Are there any specific error messages or logs available?

### Logs and Data to Collect
- Job logs from the NEA console.
- SQL Server error logs.
- Screenshots or descriptions of error messages.
- Details of the database configuration (e.g., collation, recovery model).
- Version numbers of NEA and related components.

---

## Common Scenarios & Solutions
### Scenario 1: Job Fails with Invalid Column/Object Name Errors
- **Root Cause**: Duplicate entries in the database or outdated software versions.
- **Solution**: Clean up duplicate entries, upgrade to the latest version, and rerun the job.
- **Reference Case**: [Case 413163](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CLO0PIAX/view)

### Scenario 2: Excessive Database Growth
- **Root Cause**: Full recovery model causing transaction log bloating or inefficient SQL queries.
- **Solution**: Switch to Simple recovery model, truncate bloated tables, and optimize queries.
- **Reference Case**: [Case 414497](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Cq5ZQIAZ/view)

### Scenario 3: Foreign Key Constraint Errors During Deletion
- **Root Cause**: Decommissioned domains with unresolved foreign key dependencies.
- **Solution**: Apply relevant hotfixes and rerun the deletion job.
- **Reference Case**: [Case 418210](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ETBT8IAP/view)

### Scenario 4: Errors Post-Upgrade
- **Root Cause**: Invalid database objects or missing tables after an upgrade.
- **Solution**: Delete problematic tables and rerun jobs to recreate them.
- **Reference Case**: [Case 425418](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HcpCiIAJ/view)

### Scenario 5: Database Collation Issues
- **Root Cause**: Case-sensitive collation incompatible with NEA requirements.
- **Solution**: Reinstall SQL Server with case-insensitive collation and reconfigure NEA.
- **Reference Case**: [Case 440332](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NR20cIAD/view)

---

## Detailed Case Studies
### Case Study 1: Duplicate Entries Causing Job Failures
- **Symptoms**: Errors referencing invalid column and object names.
- **Diagnostic Steps**: Identified duplicate entries, upgraded software, and verified job queries.
- **Resolution**: Cleaned up database, upgraded to version 11.5.0.276, and reran jobs successfully.
- **Key Takeaways**: Regular database maintenance and timely upgrades prevent such issues.
- **Reference**: [Case 413163](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CLO0PIAX/view)

### Case Study 2: Transaction Log Bloating
- **Symptoms**: Job running for over 10 hours and consuming 800 GB of disk space.
- **Diagnostic Steps**: Truncated bloated tables, switched recovery model, and optimized queries.
- **Resolution**: Reduced transaction log size and improved job performance.
- **Key Takeaways**: Monitor database recovery models and optimize resource-intensive jobs.
- **Reference**: [Case 414497](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Cq5ZQIAZ/view)

### Case Study 3: Foreign Key Conflicts During Domain Deletion
- **Symptoms**: SQL exceptions related to foreign key constraints.
- **Diagnostic Steps**: Applied hotfix and reran the drop domain job.
- **Resolution**: Successfully deleted decommissioned domains.
- **Key Takeaways**: Apply hotfixes proactively and ensure proper domain decommissioning.
- **Reference**: [Case 418210](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ETBT8IAP/view)

---

## Best Practices & Tips
1. **Database Maintenance**: Regularly clean up duplicate entries and monitor transaction log growth.
2. **Configuration Checks**: Verify SQL Server collation and recovery model settings during installation.
3. **Upgrade Testing**: Test upgrades in a staging environment to identify potential issues.
4. **Proactive Monitoring**: Use debug logging and scheduled tasks to detect anomalies early.
5. **Customer Communication**: Gather detailed information about the environment and recent changes to expedite troubleshooting.

---

## Escalation Guidelines
### When to Escalate
- Issues persist after applying known fixes.
- Database crashes or critical job failures affecting business operations.
- Complex SQL errors requiring advanced expertise.

### How to Escalate
- Provide detailed logs, error messages, and environment information.
- Document all troubleshooting steps taken and their outcomes.
- Use the internal escalation process to involve senior engineers or developers.

--- 

This guide serves as a comprehensive reference for diagnosing and resolving database-related issues in Netwrix Enterprise Auditor, ensuring consistent and effective support for customers.