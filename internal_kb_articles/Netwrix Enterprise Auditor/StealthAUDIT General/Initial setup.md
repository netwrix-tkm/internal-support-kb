# Knowledge Base Article: Initial Setup of StealthAUDIT General in Netwrix Enterprise Auditor

## Overview

This guide provides a comprehensive reference for the initial setup of the **StealthAUDIT General** component within the **Netwrix Enterprise Auditor (NEA)** platform. It consolidates troubleshooting steps, best practices, and solutions to common issues encountered during deployment. The goal is to ensure a smooth configuration process, minimize downtime, and maintain optimal functionality.

### Scope
- **Platform:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial Setup
- **Version Range:** 11.0 - 11.6

### Importance
The initial setup of StealthAUDIT is critical for enabling data collection, auditing, and reporting capabilities. Misconfigurations or compatibility issues during this phase can impact core functionality, making it essential to address them promptly and effectively.

---

## Technical Background

### Key Concepts
- **StealthAUDIT General:** A data collection and auditing tool that provides insights into permissions, activity, sensitive data, and system configurations.
- **Collector Code:** Modules or job groups responsible for data collection (e.g., FSAA, ADI, SEEK).
- **Connection Profiles:** Credentials and configurations used to access target systems for scanning and data collection.
- **Host Lists:** Lists of servers or endpoints targeted by specific jobs.
- **Bulk Import Jobs:** Processes that import collected data into the NEA database for analysis and reporting.
- **Database Configuration:** SQL Server settings that impact data storage, retention, and performance.

### Terminology
- **FSAA:** File System Access Auditor, responsible for scanning file system permissions.
- **SEEK:** Sensitive Data Discovery module for identifying sensitive information.
- **AIC:** Audit Intelligence Center, the web-based interface for managing NEA.
- **gMSA:** Group Managed Service Account, used for secure authentication in enterprise environments.
- **TempDB:** SQL Server temporary database used during job execution.
- **CDSA Job:** Compliance and Data Security Analysis job type.
- **Persistent Store:** A feature for caching events when fPolicy fails to send data.

### System Context
NEA operates within a complex environment that includes:
- **SQL Databases:** Used for storing audit data and configurations.
- **Active Directory:** Provides authentication and user/group management.
- **File Systems:** Scanned for permissions and activity data.
- **Cloud Services:** Integration with Azure, SharePoint Online, and Exchange Online.

---

## Issue Recognition & Triage

### Symptoms
- Errors during job execution (e.g., "Access Denied," "Timeout expired").
- Missing or stale data in reports.
- High memory utilization on SQL servers.
- Authentication failures with SQL databases or Active Directory.
- Compatibility issues after upgrades.

### Priority Assessment
- **High Priority:** Issues causing complete job failures or preventing critical functionality (e.g., database connection errors, bulk import failures).
- **Medium Priority:** Partial functionality loss or performance degradation (e.g., slow job execution, missing data).
- **Low Priority:** Minor configuration issues or cosmetic errors (e.g., incorrect timestamps, UI glitches).

---

## Diagnostic Methodology

### Systematic Approach
1. **Verify Environment Details:** Confirm NEA version, server OS, database configuration, and affected job groups.
2. **Reproduce the Issue:** Attempt to replicate the problem in a controlled environment.
3. **Analyze Logs:** Collect and review application logs, SQL logs, and job execution logs for error messages.
4. **Check Configuration:** Validate host lists, connection profiles, and job settings.
5. **Test Dependencies:** Ensure required permissions, network connectivity, and service account configurations are in place.
6. **Apply Fixes:** Implement targeted solutions based on findings.
7. **Monitor Results:** Verify that the issue is resolved and functionality is restored.

### Decision Points
- **Upgrade Required:** If the issue is related to outdated software, recommend upgrading to the latest version.
- **Escalation Needed:** If the issue involves custom configurations or unresolved errors, escalate to Professional Services.

---

## Information Collection

### Customer Queries
- What is the exact error message or behavior observed?
- Which job group or feature is affected?
- Have there been any recent changes to the environment (e.g., upgrades, server replacements)?
- What troubleshooting steps have already been attempted?

### Logs and Data to Collect
- **Application Logs:** Located in the NEA installation directory.
- **SQL Logs:** For database-related issues.
- **Job Execution Logs:** Accessible via the NEA console.
- **System Logs:** For server-level errors or resource contention.
- **PowerShell Outputs:** Collect installed software details using:
  ```powershell
  Get-CimInstance -Class Win32_Product | Where-Object {($_.Name -Like "Stealth*" -or $_.Name -like "Netwrix*" -or $_.Name -like "Postg*" -or $_.Name -like "Python*")} -ErrorAction SilentlyContinue
  ```

---

## Common Scenarios & Solutions

### Scenario 1: Database Growth Issues
**Symptoms:** SQL Server disk space alerts due to excessive database size.  
**Solution:**  
- Purge stale data using zSandBox jobs (e.g., FSAA Drop Data).  
- Shrink the database after cleanup.  
- Adjust retention settings for data collectors.  

---

### Scenario 2: Permission Errors
**Symptoms:** "Access Denied" errors during job execution.  
**Solution:**  
- Verify service account permissions.  
- Ensure gMSA accounts have proper access using PowerShell commands.  

---

### Scenario 3: Job Execution Failures
**Symptoms:** Jobs fail with timeout or memory errors.  
**Solution:**  
- Increase command timeout settings.  
- Adjust job schedules to prevent overlaps.  

---

### Scenario 4: Missing Data in Reports
**Symptoms:** Reports display "No data available."  
**Solution:**  
- Run Schema jobs and ensure proper host list assignments.  
- Verify connection profiles for scanning hosts.  

---

### Scenario 5: High SQL Server Memory Utilization
**Symptoms:** SQL server RAM usage exceeds 90%.  
**Solution:**  
- Set a memory cap in SQL Server Management Studio (SSMS).  

---

### Scenario 6: Authentication Failures
**Symptoms:** Unable to connect to SQL database or Active Directory.  
**Solution:**  
- Verify service account permissions.  
- Switch to SQL authentication if necessary.  

---

## Best Practices & Tips

### Configuration
- Assign host lists and connection profiles consistently across job groups.
- Use dedicated service accounts with least privilege access.

### Monitoring
- Regularly check database size and retention settings.
- Set alerts for connection pool thresholds and disk space usage.

### Troubleshooting
- Reproduce issues in a lab environment to isolate root causes.
- Maintain detailed logs and documentation for recurring issues.

### Upgrades
- Always recreate jobs after major upgrades to ensure compatibility.
- Upgrade to the latest NEA version to benefit from bug fixes and performance improvements.

---

## Escalation Guidelines

### Criteria for Escalation
- Issues persist after applying standard troubleshooting steps.
- Critical functionality is impacted (e.g., database connectivity, bulk imports).
- Errors involve unresolvable bugs or require development team intervention.

### Escalation Process
1. **Collect Evidence:** Gather logs, screenshots, and detailed descriptions of the issue.
2. **Document Attempts:** Record all troubleshooting steps taken.
3. **Submit Request:** Open a ticket with Professional Services, including all collected evidence.
4. **Follow Up:** Monitor the escalation process and provide updates to the customer.

---

End of Article.