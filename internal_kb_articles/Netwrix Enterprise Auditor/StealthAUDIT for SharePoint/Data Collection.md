# Netwrix Enterprise Auditor Knowledge Base Reference Guide  
## Component: StealthAUDIT for SharePoint  
## Feature: Data Collection  

---

## Overview  

### Purpose  
This guide provides a comprehensive reference for troubleshooting issues related to the **Data Collection** feature within the **StealthAUDIT for SharePoint** component of Netwrix Enterprise Auditor (NEA). It is designed to equip support engineers with the knowledge and tools necessary to systematically diagnose, resolve, and escalate issues in this category.  

### Scope  
The guide covers common problems encountered during SharePoint data collection, including bulk import errors, database locking, prolonged scan durations, disk I/O errors, and configuration issues. It also includes best practices for maintaining system performance and ensuring successful data collection.  

### Importance  
Effective troubleshooting of data collection issues is critical for ensuring accurate auditing and reporting within SharePoint environments. These issues can impact compliance, security, and operational efficiency, making it essential to address them promptly and systematically.  

---

## Technical Background  

### Key Concepts  
- **StealthAUDIT for SharePoint**: A component of NEA designed to collect and analyze SharePoint data for auditing purposes.  
- **Data Collection**: The process of gathering information from SharePoint sites, including files, folders, permissions, and activity logs.  
- **SPSEEK Scans**: SharePoint Online SEEK scans that identify sensitive data and audit SharePoint resources.  
- **SPAA Bulk Import**: A process for importing SharePoint data into the NEA database for analysis.  
- **Foreign Key Constraints**: Database rules that enforce relationships between tables, which can cause errors during bulk imports if violated.  
- **TempDB**: A temporary database used by SQL Server for storing intermediate results and uncommitted transactions during data collection.  

### Terminology  
- **USN**: Update Sequence Number, used to track changes in SharePoint hosts.  
- **FIPS Compliance**: Federal Information Processing Standards for cryptographic algorithms, which can impact system compatibility.  
- **Agent-less Scanning**: A method of scanning SharePoint resources without deploying agents on the target servers.  

---

## Issue Recognition & Triage  

### Symptoms  
- Errors during bulk import operations (e.g., foreign key constraint violations).  
- Database locking or deadlocks during scheduled jobs.  
- Excessive scan durations or jobs hanging indefinitely.  
- Disk I/O errors or SQLite exceptions during scans.  
- Missing SharePoint sites in audit reports.  

### Priority Assessment  
- **High Priority**: Issues causing system-wide impact, such as database locking or prolonged scan durations.  
- **Medium Priority**: Errors affecting specific jobs or scans, such as foreign key constraint violations.  
- **Low Priority**: Configuration issues or missing data that do not disrupt overall functionality.  

---

## Diagnostic Methodology  

### Systematic Approach  
1. **Identify Symptoms**: Review customer reports and logs to understand the issue.  
2. **Categorize the Problem**: Determine whether the issue is related to configuration, database performance, or product defects.  
3. **Reproduce the Issue**: Attempt to replicate the problem in a controlled environment.  
4. **Analyze Logs**: Examine debug logs, SQL error messages, and system performance metrics.  
5. **Implement Fixes**: Apply targeted solutions based on the root cause analysis.  
6. **Verify Resolution**: Confirm that the issue is resolved and document the steps taken.  

---

## Information Collection  

### Customer Questions  
- What version of NEA and StealthAUDIT for SharePoint are you using?  
- Are there specific error messages or codes?  
- What is the size and scope of the SharePoint environment (e.g., number of sites, data volume)?  
- Have there been recent changes to the SharePoint configuration or NEA settings?  
- Are there any network or infrastructure constraints (e.g., DMZ placement)?  

### Logs and Data to Collect  
- **Debug Logs**: From the SADatabase folder and SEEK scan job logs.  
- **SQL Error Messages**: Including stack traces for database-related issues.  
- **System Performance Metrics**: Disk usage, memory consumption, and TempDB statistics.  
- **Configuration Details**: SQL Server aliases, permissions, and scan settings.  

---

## Common Scenarios & Solutions  

### Scenario 1: Foreign Key Constraint Errors During Bulk Import  
**Symptoms**: Errors during SPAA bulk import, often related to Probable Owner analysis.  
**Solution**: Reset the USN value for the host site using the SQL command:  
```sql  
UPDATE SA_SPAA_HOSTS  
SET USN = 0  
WHERE ID = <HostID>;  
```  
**Reference Case**: [500Qk00000ECruzIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ECruzIAD/view)  

---

### Scenario 2: Database Locking During Scheduled Jobs  
**Symptoms**: Deadlocks and table blocks during SharePoint collection jobs, preventing access to the NEA console.  
**Solution**: Adjust job scheduling to avoid simultaneous execution and disable conflicting jobs temporarily.  
**Reference Case**: [500Qk00000ESaZyIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ESaZyIAL/view)  

---

### Scenario 3: Prolonged Data Collection Durations  
**Symptoms**: Excessive scan times, often exceeding 100 hours.  
**Solution**: Apply hotfixes for product defects and optimize scan settings (e.g., reduce depth, limit file size).  
**Reference Case**: [500Qk00000HMH3dIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HMH3dIAH/view)  

---

### Scenario 4: Disk I/O Errors During Scans  
**Symptoms**: SQLite exceptions and disk I/O errors during system scans.  
**Solution**: Drop Tier 2s and rescan, ensuring sufficient disk space and permissions.  
**Reference Case**: [500Qk00000JknPQIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JknPQIAZ/view)  

---

### Scenario 5: Missing SharePoint Sites in Audit Reports  
**Symptoms**: SharePoint Online sites not appearing in Resource Audit.  
**Solution**: Remove scoping limitations, update certificates, and perform fresh SPSEEK scans.  
**Reference Case**: [500Qk00000OqVupIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OqVupIAF/view)  

---

## Detailed Case Studies  

### Case Study 1: Foreign Key Constraint Error  
**Ticket ID**: [500Qk00000ECruzIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ECruzIAD/view)  
**Symptoms**: Bulk import failure due to foreign key constraint violations.  
**Diagnostic Steps**: Reset USN value, reattempt bulk import.  
**Resolution**: SQL command executed to reset USN; import completed successfully.  
**Key Takeaways**: Monitor USN values and consider systemic fixes for recurring errors.  

---

### Case Study 2: Database Locking During Jobs  
**Ticket ID**: [500Qk00000ESaZyIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ESaZyIAL/view)  
**Symptoms**: Console locking due to deadlocks during SharePoint jobs.  
**Diagnostic Steps**: Reviewed logs, adjusted job scheduling.  
**Resolution**: Conflicting jobs rescheduled; console access restored.  
**Key Takeaways**: Regularly review job runtimes and configurations to prevent conflicts.  

---

## Best Practices & Tips  

1. **Optimize Scan Settings**: Limit file sizes and scan depths to improve performance.  
2. **Monitor TempDB Usage**: Prevent uncommitted transactions from filling TempDB.  
3. **Verify Permissions**: Ensure service accounts have appropriate access to SharePoint resources.  
4. **Update Regularly**: Keep NEA and related components up to date to avoid compatibility issues.  
5. **Document Changes**: Maintain detailed records of configuration adjustments and troubleshooting steps.  

---

## Escalation Guidelines  

### Criteria for Escalation  
- Issues involving product defects or requiring hotfix development.  
- Persistent errors despite applying documented solutions.  
- System-wide impact affecting multiple customers or environments.  

### Escalation Procedure  
1. Collect all relevant logs, error messages, and configuration details.  
2. Provide a detailed summary of troubleshooting steps taken.  
3. Submit the case to the engineering team with clear documentation of the issue.  
4. Maintain regular communication with the customer regarding escalation status.  

---  

End of Document.  