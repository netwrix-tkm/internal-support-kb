# Netwrix Enterprise Auditor Knowledge Base Reference Guide  
## StealthAUDIT for SQL - Database Issues  

### Overview  
This guide addresses common issues encountered with the StealthAUDIT for SQL component of Netwrix Enterprise Auditor (NEA), specifically related to database functionality. It provides support engineers with a systematic approach to diagnosing and resolving problems, ensuring consistent and effective troubleshooting. Understanding this category is critical for maintaining customer satisfaction and minimizing downtime in environments where SQL database auditing is essential for compliance and operational monitoring.  

### Technical Background  
StealthAUDIT for SQL is a powerful module within NEA designed to audit SQL Server environments. Key features include scanning database permissions, generating reports, and identifying security risks. However, certain limitations and environmental factors can lead to issues such as scanning offline databases, long-running SQL jobs, stale data in reports, and errors during job execution.  

#### Key Concepts  
- **SQL_PermissionScan Job**: A job that scans database permissions and can be configured to filter specific database objects.  
- **State of Databases**: SQL databases can be in various states (e.g., online, offline). The state is identified using the `sys.databases` table.  
- **Blocking Processes**: SQL jobs may fail or hang due to resource locks caused by other processes.  
- **Stale Data**: SQL Solution Set reports may contain outdated information from decommissioned or migrated servers.  
- **Extended Events Sessions**: These are used for monitoring SQL Server activity and can sometimes interfere with job execution.  

### Issue Recognition & Triage  
#### Symptoms  
- Scanning offline databases causing errors or unnecessary resource usage.  
- SQL jobs running indefinitely or failing due to blocking processes.  
- Reports containing stale data from decommissioned or migrated servers.  
- Errors during job execution related to size limitations or configuration issues.  

#### Priority Assessment  
- **High Priority**: Issues causing system-wide disruptions, such as blocking processes or long-running jobs.  
- **Medium Priority**: Errors affecting specific jobs or reports but not impacting overall system functionality.  
- **Low Priority**: Configuration questions or minor inconveniences, such as filtering database objects.  

### Diagnostic Methodology  
1. **Identify the Problem**: Review customer reports and logs to pinpoint the issue.  
2. **Categorize the Issue**: Determine whether the problem is related to scanning, job execution, stale data, or configuration.  
3. **Gather Information**: Collect relevant logs, database states, and job configurations.  
4. **Apply Resolution Strategies**: Use targeted approaches based on the issue type.  
5. **Test and Validate**: Ensure the solution resolves the issue without introducing new problems.  

### Information Collection  
#### Questions to Ask Customers  
- What specific error messages or symptoms are you encountering?  
- Are there any recent changes to the SQL environment (e.g., migrations, decommissioning)?  
- What version of NEA and SQL Server are you using?  
- Are there any blocking processes or resource locks in the database?  

#### Logs and Data to Collect  
- SQL Server logs and error messages.  
- State of databases (`sys.databases` query).  
- Job configurations and execution history.  
- Extended events sessions related to the affected jobs.  

### Common Scenarios & Solutions  
#### Scenario 1: Scanning Offline Databases  
**Symptoms**: Errors or unnecessary resource usage when scanning offline databases.  
**Solution**:  
- Use the query `SELECT name FROM sys.databases WHERE state = 0;` to identify online databases.  
- Configure the SQL_PermissionScan job to filter out offline databases in the Query settings.  

#### Scenario 2: Long-Running SQL Jobs  
**Symptoms**: SQL jobs running indefinitely or failing due to blocking processes.  
**Solution**:  
- Identify blocking processes using SQL Server logs.  
- Kill the blocking tasks and re-execute the job.  
- Implement alerts for long-running jobs to proactively address similar issues.  

#### Scenario 3: Stale Data in Reports  
**Symptoms**: Reports contain outdated information from decommissioned or migrated servers.  
**Solution**:  
- Create a job using the SQL Data Collector Configuration Wizard to remove stale data.  
- Test the job in a non-production environment before executing in production.  

#### Scenario 4: Errors During Job Execution  
**Symptoms**: Errors related to size limitations or configuration issues.  
**Solution**:  
- Increase size limit values in job configurations.  
- Delete extended events sessions interfering with the job.  
- Create and test a new job for the required functionality.  

### Detailed Case Studies  
#### Case Study 1: Scanning Offline Databases  
**Ticket ID**: [500Qk00000E5IaYIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000E5IaYIAV/view)  
**Symptoms**: Customer requested clarification on scanning only online databases.  
**Diagnostic Steps**:  
- Verified database states using `sys.databases`.  
- Explained NEA's limitation in automatically excluding offline databases.  
**Resolution**: Configured SQL_PermissionScan job to filter offline databases.  
**Key Takeaways**: Manual configuration is required to exclude offline databases.  

#### Case Study 2: Long-Running SQL Jobs  
**Ticket ID**: [500Qk00000IOJOvIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IOJOvIAP/view)  
**Symptoms**: SQL job "JOB_0-SQL DROP" ran for over 20 hours due to blocking processes.  
**Diagnostic Steps**:  
- Identified blocking processes using SQL Server logs.  
- Involved DBA team to kill the blocking tasks.  
**Resolution**: Cleared blocking processes and re-executed the job successfully.  
**Key Takeaways**: Monitor SQL jobs for blocking issues and implement alerts for long-running jobs.  

#### Case Study 3: Stale Data in Reports  
**Ticket ID**: [500Qk00000IzsSYIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IzsSYIAZ/view)  
**Symptoms**: Reports contained stale data from decommissioned servers.  
**Diagnostic Steps**:  
- Confirmed presence of stale data.  
- Created a job to remove stale data using the SQL Data Collector Configuration Wizard.  
**Resolution**: Successfully executed the job to clear stale data.  
**Key Takeaways**: Regularly review and clean up SQL data to prevent stale data accumulation.  

#### Case Study 4: Errors During Job Execution  
**Ticket ID**: [500Qk00000JOXZOIA5](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JOXZOIA5/view)  
**Symptoms**: Error executing SQL Server Logins job.  
**Diagnostic Steps**:  
- Increased size limit value and deleted extended events session.  
- Created and tested a new job for login reporting.  
**Resolution**: New job executed successfully without errors.  
**Key Takeaways**: Review job configurations and extended events sessions for potential conflicts.  

### Best Practices & Tips  
- **Database Filtering**: Use SQL queries to identify and exclude offline databases from scans.  
- **Job Monitoring**: Implement alerts for long-running jobs to address issues proactively.  
- **Data Cleanup**: Regularly review and remove stale data from reports.  
- **Testing**: Always test new jobs or configurations in a non-production environment before deploying in production.  
- **Documentation**: Maintain detailed records of job configurations and changes for future reference.  

### Escalation Guidelines  
- **Escalate to Tier 2 Support**: If the issue involves complex SQL configurations or requires custom scripting.  
- **Escalate to Development Team**: For product limitations or bugs requiring code changes.  
- **Provide Detailed Logs**: Include SQL Server logs, job configurations, and error messages when escalating.  
- **Customer Communication**: Keep the customer informed about escalation progress and expected timelines.  