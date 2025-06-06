# Netwrix Enterprise Auditor Knowledge Base Reference Guide  
## Component: StealthAUDIT for Windows File Systems  
## Feature: Sensitive Data  

---

## Overview  

Sensitive Data Discovery (SDD) is a critical feature of Netwrix Enterprise Auditor (NEA) that enables organizations to identify and manage sensitive information within their file systems. This functionality is essential for compliance, data security, and risk mitigation. However, issues related to SDD can disrupt workflows, compromise data integrity, and delay critical processes. This guide provides a systematic approach to diagnosing, resolving, and preventing issues within this category, ensuring consistent and efficient support for customers.

---

## Technical Background  

### Key Concepts  
- **Sensitive Data Discovery (SDD):** A feature that scans file systems to identify sensitive information based on predefined patterns or rules.  
- **SEEK Scans:** A type of scan used to collect file system metadata and sensitive data matches.  
- **Bulk Import:** The process of importing scan results into the database for reporting and analysis.  
- **Tier 1 Database:** The primary database used by NEA to store scan results and metadata.  
- **Libraries:** Essential DLL files (e.g., `System.Data.SQLite.dll`) required for scan execution and data processing.  

### Terminology  
- **FSAA:** StealthAUDIT for Windows File Systems component.  
- **DLP:** Data Loss Prevention, often tied to sensitive data scans.  
- **Primary Key Constraint:** A database rule ensuring unique entries in specific tables.  
- **Differential Scanning:** A method that scans only changes since the last scan.  

### System Context  
Sensitive Data scans rely on a combination of file system metadata collection, database operations, and library dependencies. Issues can arise due to misconfigurations, outdated libraries, resource constraints, or software bugs. Understanding the interplay between these components is crucial for effective troubleshooting.

---

## Issue Recognition & Triage  

### Symptoms  
- Scan jobs fail or stop unexpectedly.  
- Errors related to database constraints (e.g., primary key violations).  
- Missing or outdated library files causing runtime errors.  
- Sensitive data reports missing expected fields (e.g., filepath).  
- Excessive scan durations or resource consumption.  

### Priority Assessment  
- **High Priority:** Issues causing scan failures, database corruption, or security vulnerabilities.  
- **Medium Priority:** Performance degradation or incomplete scan results.  
- **Low Priority:** Cosmetic issues, such as error categorization in logs.  

---

## Diagnostic Methodology  

### Systematic Approach  
1. **Verify Environment Details:** Confirm software versions, scan configurations, and affected components.  
2. **Review Logs:** Examine applet logs, database logs, and scan job logs for error messages.  
3. **Reproduce the Issue:** Attempt to replicate the problem in a controlled environment.  
4. **Check Dependencies:** Validate the presence and version of required libraries.  
5. **Analyze Database:** Investigate constraints, duplicate entries, and schema compatibility.  
6. **Test Configuration Changes:** Adjust scan settings (e.g., threading, exclusions) and monitor results.  

### Decision Points  
- If the issue is related to outdated libraries, proceed with library replacement.  
- If scan durations are excessive, optimize threading and scope settings.  
- If database errors persist, consider dropping affected data and rerunning scans.  

---

## Information Collection  

### Customer Questions  
- What is the exact error message or behavior observed?  
- What version of NEA and related components are installed?  
- Were any recent upgrades or configuration changes made?  
- Are specific folders or files consistently causing issues?  

### Logs to Collect  
- Applet logs (`C:\Program Files (x86)\STEALTHbits\StealthAUDIT\Logs`).  
- Database logs for Tier 1 and Tier 2.  
- Scan job logs (SEEK, Bulk Import).  
- System event logs for resource-related errors.  

---

## Common Scenarios & Solutions  

### Scenario 1: File Tagging Alters Timestamps  
**Symptoms:** Customer requests tagging files without modifying timestamps.  
**Solution:** Inform the customer that file attribute modifications inherently change timestamps. This behavior is by design to ensure data integrity.  

### Scenario 2: Vulnerability in Outdated Libraries  
**Symptoms:** Errors related to `log4j` or outdated DLL files.  
**Solution:** Replace outdated libraries (e.g., `System.Data.SQLite.dll`) with updated versions. Ensure all dependencies are compatible with the current NEA version.  

### Scenario 3: Excessive Scan Durations  
**Symptoms:** Sensitive data scans take significantly longer than expected.  
**Solution:** Optimize threading settings in SEEK job XML (`MAXTHREADS`, `MAXFOLDERTHREADS`). Exclude unnecessary folders from the scan scope.  

### Scenario 4: Primary Key Constraint Violations  
**Symptoms:** Bulk import fails due to duplicate entries in the database.  
**Solution:** Drop affected data using FS_SDD_DELETE job and rerun scans without differential scanning.  

### Scenario 5: Missing Filepath in Reports  
**Symptoms:** Filepath field in sensitive data reports is empty.  
**Solution:** Update NEA to a version that resolves known bugs affecting filepath visibility. Reset affected hosts and rerun scans.  

---

## Detailed Case Studies  

### Case Study 1: [Ticket ID: 500Qk00000CK9bPIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CK9bPIAT/view)  
**Symptoms:** Customer requested tagging files without altering timestamps.  
**Diagnostic Steps:** Investigated file attribute behavior and consulted development team.  
**Resolution:** Communicated that timestamp changes are unavoidable due to system design.  
**Key Takeaways:** Set clear expectations for customers regarding file attribute modifications.  

### Case Study 2: [Ticket ID: 500Qk00000CwdOhIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CwdOhIAJ/view)  
**Symptoms:** Vulnerability due to outdated `log4j` files.  
**Diagnostic Steps:** Identified outdated files and manually removed them.  
**Resolution:** Guided customer through updating NEA and related components.  
**Key Takeaways:** Ensure full admin access before performing updates.  

### Case Study 3: [Ticket ID: 500Qk00000D9R9aIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000D9R9aIAF/view)  
**Symptoms:** Sensitive data scans took 6 days instead of 3 hours.  
**Diagnostic Steps:** Adjusted threading settings and excluded unnecessary folders.  
**Resolution:** Optimized SEEK job XML settings to reduce scan duration.  
**Key Takeaways:** Monitor scan performance after configuration changes.  

### Case Study 4: [Ticket ID: 500Qk00000DgwePIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DgwePIAR/view)  
**Symptoms:** Bulk import failure due to primary key constraint violation.  
**Diagnostic Steps:** Dropped DLP data and reran scans.  
**Resolution:** Resolved database issues by resetting hosts and deleting affected data.  
**Key Takeaways:** Monitor for duplicate entries before bulk imports.  

---

## Best Practices & Tips  

1. **Library Management:** Ensure all dependent libraries are updated during upgrades.  
2. **Thread Optimization:** Adjust threading settings for SEEK scans to balance performance and resource usage.  
3. **Exclusions:** Use scoping options to exclude known error-generating objects.  
4. **Database Integrity:** Regularly monitor for duplicate entries and schema compatibility.  
5. **Customer Communication:** Set clear expectations regarding system limitations and required actions.  
6. **Documentation:** Maintain detailed records of configuration changes and troubleshooting steps.  

---

## Escalation Guidelines  

### Criteria for Escalation  
- Persistent scan failures despite configuration changes.  
- Database corruption or unresolved primary key violations.  
- Issues requiring development team intervention (e.g., software bugs).  

### Escalation Procedure  
1. Collect detailed logs and artifacts from the customer.  
2. Document all troubleshooting steps taken.  
3. Submit a detailed escalation request to the development team, including logs, configuration details, and observed behavior.  
4. Communicate escalation status and expected timelines to the customer.  

---  

This guide serves as a comprehensive reference for handling Sensitive Data issues within Netwrix Enterprise Auditor. By following the outlined methodologies, support engineers can ensure efficient and consistent resolution of customer problems.