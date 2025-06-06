# Comprehensive Knowledge Base Guide: Troubleshooting Custom Reports in StealthAUDIT for Active Directory

## Overview
Custom reports in StealthAUDIT for Active Directory are a powerful feature of Netwrix Enterprise Auditor, enabling organizations to extract tailored insights from Active Directory (AD) and Azure AD environments. However, issues with custom reports can arise due to configuration errors, environmental changes, or limitations in the software. This guide provides a systematic approach to diagnosing and resolving issues related to custom reports, ensuring support engineers can handle these cases efficiently and consistently.

---

## Technical Background
### Key Concepts
- **Custom Reports**: Reports created to meet specific organizational needs, often involving SQL views or job configurations.
- **StealthAUDIT**: A module within Netwrix Enterprise Auditor used for auditing and reporting on AD environments.
- **SQL Views**: Custom queries used to extract data from the StealthAUDIT database.
- **Active Directory Inventory (ADI) Jobs**: Scanning jobs that collect data from AD for reporting purposes.
- **Path Length Limitations**: Windows restrictions on file and directory name lengths, which can impact report generation.

### Terminology
- **SAMAccountName**: The logon name used by AD accounts.
- **DistinguishedName**: The unique name identifying an object in AD.
- **Group Policy Objects (GPOs)**: Policies applied to AD users and computers.
- **Extension Attributes**: Custom attributes in AD used for specific organizational needs.

---

## Issue Recognition & Triage
### Identifying Common Symptoms
- Errors during report generation (e.g., SQL binding errors, path length violations).
- Missing data in reports (e.g., groups or users not appearing).
- Reports failing after environmental changes (e.g., server migrations or domain decommissioning).

### Categorizing Issues
1. **Configuration Errors**: Problems with SQL scripts, job settings, or report filters.
2. **Environmental Changes**: Issues arising from migrations, updates, or attribute collection settings.
3. **Software Limitations**: Features not supported out-of-the-box or requiring custom development.

### Assessing Priority
- **High Priority**: Issues impacting critical business operations or compliance reporting.
- **Medium Priority**: Errors causing delays but not affecting essential functions.
- **Low Priority**: Feature requests or minor inconveniences.

---

## Diagnostic Methodology
### Systematic Approach
1. **Understand the Problem**: Gather detailed information about the issue and its impact.
2. **Reproduce the Issue**: Attempt to replicate the problem in a controlled environment.
3. **Analyze Logs and Scripts**: Review SQL scripts, debug logs, and job configurations.
4. **Test Solutions**: Implement changes incrementally and verify results.
5. **Document Findings**: Record the root cause, solution, and any lessons learned.

---

## Information Collection
### Questions to Ask Customers
- What is the specific issue or error message?
- What changes have been made to the environment recently?
- Are there specific requirements for the report (fields, filters, etc.)?
- What is the impact of the issue on business operations?

### Logs and Data to Collect
- SQL scripts used in custom jobs.
- Debug logs and application logs from Netwrix Enterprise Auditor.
- Screenshots or exported job configurations.
- Details of the affected environment (e.g., AD structure, server setup).

---

## Common Scenarios & Solutions
### Scenario 1: Missing Data in Reports
**Symptoms**: Groups or users not appearing in reports.  
**Solution**: Verify the presence of data in AD and adjust SQL views or filters accordingly. Example: [Case 500Qk00000LnbPsIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LnbPsIAJ/view).

---

### Scenario 2: Path Length Errors
**Symptoms**: Errors related to file or directory name lengths.  
**Solution**: Shorten job names or paths to comply with Windows limitations. Example: [Case 500Qk00000CuRYBIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CuRYBIA3/view).

---

### Scenario 3: SQL Binding Errors
**Symptoms**: Multi-part identifiers cannot be bound.  
**Solution**: Ensure all identifiers are correctly aliased to existing tables. Example: [Case 500Qk00000DrxlhIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DrxlhIAB/view).

---

### Scenario 4: Attribute Collection Issues
**Symptoms**: Reports fail due to missing attributes.  
**Solution**: Update ADI job settings to include necessary attributes. Example: [Case 500Qk00000IHTxkIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IHTxkIAH/view).

---

### Scenario 5: Bulk Reporting Limitations
**Symptoms**: Unable to query multiple groups simultaneously.  
**Solution**: Modify existing jobs or involve Professional Services for custom development. Example: [Case 500Qk00000MXIUZIA5](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MXIUZIA5/view).

---

## Detailed Case Studies
### Case Study 1: Path Length Error ([Case 500Qk00000CuRYBIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CuRYBIA3/view))
- **Symptoms**: Report generation failed due to path length restrictions.
- **Diagnostic Steps**: Verified path lengths and registry settings for LongPaths.
- **Solution**: Shortened job names to comply with Windows limits.
- **Key Takeaways**: Monitor job names and paths during report creation.

---

### Case Study 2: SQL Binding Error ([Case 500Qk00000DrxlhIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DrxlhIAB/view))
- **Symptoms**: Multi-part identifiers could not be bound in SQL scripts.
- **Diagnostic Steps**: Reviewed SQL scripts and identified missing table aliases.
- **Solution**: Removed incorrect aliases and validated the script.
- **Key Takeaways**: Validate SQL scripts for syntax and binding errors before execution.

---

### Case Study 3: Attribute Collection Issue ([Case 500Qk00000IHTxkIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IHTxkIAH/view))
- **Symptoms**: Missing attribute prevented report generation.
- **Diagnostic Steps**: Confirmed attribute collection settings in ADI jobs.
- **Solution**: Updated settings to include the required attribute.
- **Key Takeaways**: Verify attribute collection settings during migrations.

---

## Best Practices & Tips
1. **Validate SQL Scripts**: Test scripts for syntax and binding errors before execution.
2. **Monitor Path Lengths**: Ensure job names and paths comply with Windows restrictions.
3. **Document Custom Jobs**: Maintain detailed records of job configurations and SQL scripts.
4. **Engage Professional Services**: For complex requirements, consider custom development.
5. **Proactive Communication**: Keep customers informed about limitations and alternative solutions.

---

## Escalation Guidelines
### Criteria for Escalation
- Issues requiring custom development or Professional Services.
- Problems impacting critical business operations or compliance.
- Errors that cannot be resolved through standard troubleshooting.

### Escalation Process
1. **Document the Issue**: Include logs, scripts, and customer impact details.
2. **Engage Professional Services**: Coordinate with the team for custom solutions.
3. **Communicate Costs**: Inform customers about potential charges for advanced support.

---

This guide serves as a definitive reference for troubleshooting custom reports in StealthAUDIT for Active Directory, equipping support engineers with the tools and methodologies needed to resolve issues effectively.