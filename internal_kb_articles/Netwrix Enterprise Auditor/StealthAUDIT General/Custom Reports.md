# Comprehensive Knowledge Base Guide: Troubleshooting Custom Reports in Netwrix Enterprise Auditor (StealthAUDIT General)

## Overview
Custom reports in Netwrix Enterprise Auditor (NEA) are a powerful feature that allows organizations to extract tailored insights from their data. However, issues with custom reports can arise due to misconfigurations, environmental factors, or limitations in the underlying system. This guide provides a systematic approach to diagnosing and resolving issues related to custom reports in the StealthAUDIT General component, ensuring support engineers can address these problems effectively and consistently.

---

## Technical Background
### Key Concepts
- **Custom Reports**: Reports created to meet specific organizational requirements, often involving SQL queries, custom jobs, or tailored configurations.
- **StealthAUDIT General**: A core component of NEA that handles data collection, analysis, and reporting across various modules, including File System Access Audit (FSAA), Active Directory (AD), and more.
- **Data Sources**: Tables and views within the NEA database, such as `SA_FSAA_ResourceView`, `SA_ADInventory_GroupMembersView`, and `SA_FSAA_PermissionsView`, which provide the raw data for reports.
- **Report Configuration**: Includes filters, SQL scripts, and job settings that determine the scope and output of a report.

### Common Terminology
- **FSAA**: File System Access Audit, used for analyzing file permissions and access.
- **NAM**: Netwrix Activity Monitor, used for tracking file activity.
- **AIC**: Access Information Center, a module for reviewing effective permissions.
- **GUID**: Globally Unique Identifier, used to track reports and jobs within the system.

---

## Issue Recognition & Triage
### Symptoms
- Reports fail to generate or display incomplete data.
- Errors such as "Sequence contains more than one matching element" or "No columns available for display."
- Missing or outdated data in reports.
- Reports disappearing from the NEA web portal.
- Performance issues during report generation.

### Priority Assessment
- **High Priority**: Errors affecting critical business operations (e.g., missing audit reports, failed job notifications).
- **Medium Priority**: Reports generating incorrect or incomplete data but not impacting immediate operations.
- **Low Priority**: Cosmetic issues or requests for new report configurations.

---

## Diagnostic Methodology
### Systematic Approach
1. **Verify Report Configuration**:
   - Check filters, SQL scripts, and data sources.
   - Ensure the correct tables/views are being queried.
2. **Review Logs**:
   - Examine job logs, SQL error logs, and debug logs for anomalies.
3. **Test in Isolation**:
   - Run the report independently to rule out interference from other jobs.
4. **Check Environmental Factors**:
   - Verify database integrity, TempDB storage, and host availability.
5. **Recreate or Modify Report**:
   - If the issue persists, recreate the report or adjust its configuration.

---

## Information Collection
### Customer Questions
- What specific issue are you experiencing with the report?
- Are there any error messages? If so, provide screenshots or logs.
- What data or fields are missing or incorrect in the report?
- Have there been any recent changes to the environment (e.g., upgrades, server migrations)?
- What is the urgency of resolving this issue?

### Logs and Data to Collect
- **Job Logs**: Located in `%SAInstallDir%\Logs`.
- **SQL Queries**: Scripts used for report generation.
- **System Information**: TempDB storage capacity, host availability, and permissions.
- **Screenshots**: Error messages and report outputs.

---

## Common Scenarios & Solutions
### Scenario 1: Report Fails to Generate
- **Symptoms**: Errors such as "Sequence contains more than one matching element."
- **Solution**:
  - Check for duplicate job names or unsupported structures in `Reports.xml`.
  - Backup and delete the `Reports.xml` file, then restart NEA.
  - Reference [Ticket ID: 500Qk00000GtGHSIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GtGHSIA3/view).

### Scenario 2: Missing Data in Reports
- **Symptoms**: Reports do not display expected fields or data.
- **Solution**:
  - Verify the SQL script and ensure the correct tables/views are queried.
  - Adjust filters to include the desired data range.
  - Reference [Ticket ID: 500Qk00000Jcf0EIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Jcf0EIAR/view).

### Scenario 3: Reports Disappear from Web Portal
- **Symptoms**: Custom reports temporarily disappear after regeneration.
- **Solution**:
  - Use standard copy/paste methods to maintain GUID integrity.
  - Reference [Ticket ID: 500Qk00000LQ1h8IAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LQ1h8IAD/view).

### Scenario 4: Performance Issues
- **Symptoms**: Reports take too long to generate or fail due to resource constraints.
- **Solution**:
  - Increase TempDB storage capacity.
  - Optimize SQL queries by targeting efficient tables/views.
  - Reference [Ticket ID: 500Qk00000J49zUIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000J49zUIAR/view).

---

## Detailed Case Studies
### Case Study 1: Missing Accounts in Password Expiry Report
- **Ticket ID**: [500Qk00000OScEDIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OScEDIA1/view)
- **Symptoms**: Accounts with passwords that never expire were missing from the report.
- **Diagnostic Steps**:
  - Reviewed SQL query and logs.
  - Identified issues with the referenced table.
- **Resolution**:
  - Fixed the problematic table, restoring complete report results.
- **Key Takeaways**:
  - Monitor database table integrity regularly.
  - Collect detailed logs for faster troubleshooting.

### Case Study 2: Report Disappears After Upgrade
- **Ticket ID**: [500Qk00000ONRsvIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ONRsvIAH/view)
- **Symptoms**: Custom analysis disappeared after upgrading to version 11.6.
- **Diagnostic Steps**:
  - Copied archived job folder to active directory.
  - Repaired StealthAUDIT installation.
- **Resolution**:
  - Restored analysis visibility by repairing the installation.
- **Key Takeaways**:
  - Use "Upgrade in Place" to avoid losing custom configurations.

---

## Best Practices & Tips
1. **SQL Optimization**:
   - Use efficient tables/views like `SA_FSAA_ResourceView` for better performance.
   - Avoid complex joins unless necessary.
2. **Backup Critical Files**:
   - Always back up `Reports.xml` and job folders before making changes.
3. **Monitor Database Health**:
   - Regularly check TempDB storage and table integrity.
4. **Customer Communication**:
   - Provide clear instructions and set realistic expectations for resolution timelines.
5. **Documentation**:
   - Maintain detailed records of report configurations and troubleshooting steps.

---

## Escalation Guidelines
### Criteria for Escalation
- Issues involving database corruption or missing tables.
- Requests for custom reports requiring advanced SQL scripting.
- Problems persisting after standard troubleshooting steps.

### Escalation Procedure
1. Collect all relevant logs, screenshots, and SQL queries.
2. Document steps already taken and their outcomes.
3. Submit a detailed escalation request to the Professional Services team.

--- 

End of Guide.