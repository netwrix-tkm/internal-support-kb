# Netwrix Enterprise Auditor: Troubleshooting StealthAUDIT for Windows File Systems Configuration Issues

## Overview
This guide provides a comprehensive reference for troubleshooting configuration issues related to the StealthAUDIT for Windows File Systems component in Netwrix Enterprise Auditor (NEA). Configuration issues in this category can impact data collection, job execution, server connectivity, and overall system performance. Understanding and resolving these issues is critical to maintaining accurate auditing and ensuring the integrity of collected data.

## Technical Background
### Key Concepts
- **StealthAUDIT for Windows File Systems (FSAA):** A module within NEA designed to scan file systems, collect access data, and monitor activity.
- **File System Activity Collector (FSAC):** A subcomponent responsible for collecting file system activity data.
- **NAM (Netwrix Activity Monitor):** A tool used for monitoring and collecting activity events.
- **Connection Profiles:** Configuration settings that define how NEA connects to target hosts for scanning.
- **Job Groups:** Logical collections of scan jobs that execute specific tasks, such as permissions audits or activity monitoring.

### Terminology
- **FSDFS:** File System Distributed File System job, used for scanning DFS servers.
- **DropFSHostData:** A job designed to remove data for decommissioned hosts from the NEA database.
- **SBTFileMon.ini:** A configuration file used by FSAC to monitor file system activity.
- **NLog.config:** A configuration file that controls logging levels for NEA components.

### System Context
NEA relies on accurate configuration of jobs, hosts, and permissions to perform scans and collect data. Misconfigurations, missing permissions, or outdated settings can lead to errors, incomplete scans, or performance degradation.

## Issue Recognition & Triage
### Symptoms
- Access denied errors during scans.
- Failed job execution with specific error messages (e.g., "Job connection profile is not available").
- Missing or incomplete data in reports.
- Excessive log sizes due to incorrect logging levels.
- Errors related to database schema or foreign key constraints.

### Priority Assessment
- **High Priority:** Issues preventing data collection or causing system-wide failures (e.g., corrupt database, failed schema creation).
- **Medium Priority:** Configuration errors affecting specific jobs or hosts (e.g., missing permissions, incorrect job settings).
- **Low Priority:** Performance-related issues or minor logging discrepancies.

## Diagnostic Methodology
### Systematic Approach
1. **Identify the Issue:** Review customer reports and logs to pinpoint the problem.
2. **Verify Configuration:** Check job settings, host lists, and connection profiles for accuracy.
3. **Analyze Logs:** Examine relevant logs (e.g., FSAA logs, SQL logs) for error messages and patterns.
4. **Test Connectivity:** Use tools like ping and WMI calls to confirm communication with target hosts.
5. **Replicate the Issue:** Attempt to reproduce the problem in a sandbox environment.
6. **Apply Fixes:** Implement configuration changes or execute repair tasks as needed.
7. **Validate Resolution:** Run test jobs to confirm the issue is resolved.

## Information Collection
### Customer Questions
- What version of NEA is being used?
- What specific error messages or symptoms are being observed?
- Are there any recent changes to the environment (e.g., new servers, upgrades)?
- What permissions have been configured for the affected hosts?

### Logs to Examine
- FSAA logs (`C:\Program Files (x86)\STEALTHbits\StealthAUDIT\Logs`).
- SQL logs for database-related errors.
- NAM logs for activity monitoring issues.
- Configuration files (`NLog.config`, `SBTFileMon.ini`).

## Common Scenarios & Solutions
### Scenario 1: Access Denied During Scans
**Symptoms:** Access denied errors when scanning new servers.  
**Solution:** Ensure required permissions are configured for the target hosts. Refer to [StealthAUDIT Permissions Documentation](https://helpcenter.netwrix.com/bundle/StealthAUDIT_11.5/page/Content/Configuration/Windows_Config/SA_FS_Scan_(Windows).htm).  

### Scenario 2: Failed DropFSHostData Job
**Symptoms:** "Job connection profile is not available" error.  
**Solution:** Select a valid connection profile for the job and disable unnecessary analysis tasks to improve performance.  

### Scenario 3: Schema Creation Errors
**Symptoms:** Errors related to foreign key constraints during schema creation.  
**Solution:** Delete invalid records from affected tables using SQL queries and rerun the Create Schema job.  

### Scenario 4: Missing Data for DFS Servers
**Symptoms:** DFS servers not being scanned or reporting data.  
**Solution:** Update FSDFS job settings to reference a Domain Controller instead of a list of hosts.  

### Scenario 5: Excessive Log Sizes
**Symptoms:** Logs defaulting to DEBUG level, causing disk usage issues.  
**Solution:** Adjust logging levels in the `NLog.config` file to reduce verbosity.  

## Detailed Case Studies
### Case Study 1: Access Denied During Scans ([Ticket ID: 500Qk00000C1hwsIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C1hwsIAB/view))
- **Symptoms:** Access denied errors when scanning DEACMICS-APP01.  
- **Diagnostic Steps:** Verified permissions and recommended using a backup operator account.  
- **Resolution:** Configured global account access for the target host.  
- **Key Takeaways:** Always verify permissions before scanning new hosts.  

### Case Study 2: Failed DropFSHostData Job ([Ticket ID: 500Qk00000NIqNuIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NIqNuIAL/view))
- **Symptoms:** "Job connection profile is not available" error.  
- **Diagnostic Steps:** Identified missing connection profile and excessive execution time due to analysis tasks.  
- **Resolution:** Selected a valid connection profile and disabled unnecessary tasks.  
- **Key Takeaways:** Ensure connection profiles are configured for all jobs.  

### Case Study 3: Schema Creation Errors ([Ticket ID: 500Qk00000NLFwWIAX](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NLFwWIAX/view))
- **Symptoms:** Foreign key constraint errors during schema creation.  
- **Diagnostic Steps:** Verified table structures and executed SQL queries to delete invalid records.  
- **Resolution:** Deleted invalid records and reran the Create Schema job successfully.  
- **Key Takeaways:** Validate database integrity before upgrades or schema migrations.  

### Case Study 4: Missing Data for DFS Servers ([Ticket ID: 500Qk00000MYtJzIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MYtJzIAL/view))
- **Symptoms:** DFS server not being scanned.  
- **Diagnostic Steps:** Verified job settings and updated FSDFS job to reference a Domain Controller.  
- **Resolution:** Successfully scanned the DFS server after updating job settings.  
- **Key Takeaways:** Ensure DFS jobs are correctly configured to reference Domain Controllers.  

### Case Study 5: Excessive Log Sizes ([Ticket ID: 500Qk00000M1wjdIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000M1wjdIAB/view))
- **Symptoms:** Logs defaulting to DEBUG level.  
- **Diagnostic Steps:** Reviewed `NLog.config` file and adjusted logging levels.  
- **Resolution:** Reduced log verbosity to mitigate disk usage.  
- **Key Takeaways:** Configure logging levels appropriately to balance detail and performance.  

## Best Practices & Tips
- **Pre-scan Validation:** Verify permissions and host configurations before initiating scans.
- **Logging Configuration:** Adjust logging levels to avoid excessive disk usage while retaining necessary details.
- **Database Integrity Checks:** Perform regular checks to ensure foreign key relationships and table structures are intact.
- **Sandbox Testing:** Test configuration changes in a sandbox environment before applying them to production.
- **Documentation Reference:** Always consult the latest Netwrix documentation for guidance on configuration and troubleshooting.

## Escalation Guidelines
### Criteria for Escalation
- Issues involving corrupt databases or missing tables.
- Persistent errors after applying recommended fixes.
- Problems requiring development team intervention (e.g., custom SQL queries).

### Escalation Procedure
1. Collect all relevant logs and configuration files.
2. Document the steps taken and results observed.
3. Submit a detailed escalation request to the development team, including ticket references and supporting data.
4. Follow up regularly to ensure timely resolution.