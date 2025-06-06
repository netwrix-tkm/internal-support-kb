# Knowledge Base Reference Guide: Troubleshooting Sensitive Data Discovery (SDD) Credential Issues in Netwrix Enterprise Auditor

## Overview
Sensitive Data Discovery (SDD) is a critical feature of Netwrix Enterprise Auditor that helps organizations identify and manage sensitive information, such as passwords, across their IT environments. Proper configuration and troubleshooting of SDD are essential to ensure accurate reporting and compliance with data protection policies. This guide focuses on resolving issues related to false positives in sensitive data reports and memory errors when accessing SDD settings.

## Technical Background
### Key Concepts
- **Sensitive Data Discovery (SDD):** A feature that scans file systems and network shares to identify sensitive data, such as passwords, credit card numbers, and other regulated information.
- **False Positives:** Data entries incorrectly identified as sensitive. These can be excluded using exclusion filters.
- **Exclusion Filters:** Rules that prevent specific files or paths from being flagged as sensitive data in reports.
- **SA_FSDLP_MatchesView:** A database view used by SDD to store matches for sensitive data.
- **IsExcluded Column:** A field in the database that indicates whether a match has been excluded from reports.

### System Context
- **Netwrix Enterprise Auditor Version:** 11.6
- **Component:** StealthAUDIT Sensitive Data Discovery
- **Feature:** Credentials
- **Database Tables:** `SA_WS_OpenShares_SDD_Details`, `SA_FSDLP_MatchesView`

Understanding the database structure and query logic is essential for diagnosing and resolving issues related to SDD.

## Issue Recognition & Triage
### Symptoms
- False positives for sensitive data (e.g., passwords) appear in reports despite being marked for exclusion.
- "Out of memory" errors occur when accessing the Sensitive Data object under Settings.

### Priority Assessment
- **High Priority:** Memory errors that prevent access to SDD settings.
- **Medium Priority:** False positives in sensitive data reports that do not impact scanning but affect report accuracy.

## Diagnostic Methodology
### Step-by-Step Approach
1. **Confirm Product Version:** Verify that the customer is using the latest version of Netwrix Enterprise Auditor and SDD.
2. **Review Exclusion Filters:** Check the configuration of exclusion filters to ensure they are correctly defined.
3. **Analyze Database Queries:** Examine the SQL queries used in reports to identify missing conditions or logic errors.
4. **Reproduce the Issue:** Attempt to replicate the problem in a controlled environment to isolate the root cause.
5. **Check System Resources:** Investigate memory usage and system performance for "Out of memory" errors.

## Information Collection
### Customer Questions
- What version of Netwrix Enterprise Auditor are you using?
- Can you provide examples of the false positives appearing in reports?
- Have you configured exclusion filters? If so, what paths or patterns are included?
- When did the "Out of memory" error first occur? Was it after a specific change or update?

### Logs and Data to Collect
- Screenshots of the sensitive data reports showing false positives.
- Configuration details for exclusion filters.
- SQL query logs for the affected reports.
- System performance logs during the time of the "Out of memory" error.

## Common Scenarios & Solutions
### Scenario 1: False Positives in Sensitive Data Reports
**Cause:** The report query does not account for the `IsExcluded` column in the `SA_FSDLP_MatchesView` table.  
**Solution:** Modify the SQL query to include the exclusion condition:
```sql
AND mv.IsExcluded = 0
```
This ensures that only non-excluded entries are displayed in the report.

### Scenario 2: "Out of Memory" Error in SDD Settings
**Cause:** Insufficient system resources or a large volume of sensitive data matches.  
**Solution:** Optimize system resources by increasing memory allocation or reducing the scope of the SDD scan. Consider archiving old data to improve performance.

## Detailed Case Studies
### Case Study: False Positives and Memory Error (Ticket ID: [500Qk00000MwHANIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MwHANIA3/view))
#### Initial Symptoms
- False positives for passwords appeared in sensitive data reports despite being marked for exclusion.
- "Out of memory" error occurred when accessing the Sensitive Data object under Settings.

#### Diagnostic Steps
1. Verified the product version (Netwrix Enterprise Auditor 11.6).
2. Reviewed exclusion filter configuration and identified that only UNC paths were supported.
3. Analyzed the SQL query for the affected report and found that the `IsExcluded` column was not included.
4. Added the following line to the report query:
   ```sql
   AND mv.IsExcluded = 0
   ```
5. Investigated system performance logs and advised the customer to optimize memory allocation.

#### Resolution
- The SQL query modification resolved the false positives issue.
- The customer confirmed that the changes resolved their issue, and the case was closed.

#### Key Takeaways
- Always verify that exclusion filters are correctly configured and supported formats are used.
- Ensure that report queries include conditions for excluded entries.
- Optimize system resources to prevent memory-related errors.

#### Efficiency Improvements
- Update documentation to clarify supported exclusion filter formats.
- Provide pre-validated SQL query templates for common reports.

## Best Practices & Tips
- **Exclusion Filters:** Use UNC paths directly to the file (e.g., `\\Host\Share\Folder\File.txt`) for exclusions. Local file paths (e.g., `C:\Folder\File.txt`) are not supported.
- **SQL Query Validation:** Regularly review and test report queries to ensure they account for exclusion conditions.
- **System Resource Monitoring:** Monitor memory usage and optimize system resources to prevent performance issues.
- **Customer Communication:** Clearly explain the limitations of exclusion filters and provide guidance on supported formats.

## Escalation Guidelines
### Criteria for Escalation
- The issue persists after applying recommended solutions.
- The customer encounters additional errors or unexpected behavior.
- The problem involves unsupported configurations or requires development intervention.

### Escalation Procedure
1. Document all troubleshooting steps and findings.
2. Collect relevant logs, screenshots, and configuration details.
3. Submit a detailed escalation request to the development team, including the SQL query and database structure.

By following this guide, support engineers can systematically diagnose and resolve issues related to Sensitive Data Discovery in Netwrix Enterprise Auditor, ensuring accurate reporting and optimal system performance.