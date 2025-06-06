# Knowledge Base Reference Guide: Troubleshooting Sensitive Data Issues in StealthAUDIT for SharePoint

## Overview

Sensitive Data issues in StealthAUDIT for SharePoint are critical to address as they directly impact the ability to scan, import, and analyze sensitive data within SharePoint environments. These issues can arise due to system resource constraints, database conflicts, licensing limitations, or software bugs. Understanding how to diagnose and resolve these problems ensures uninterrupted functionality and compliance with data governance requirements.

This guide provides a systematic approach to identifying, diagnosing, and resolving issues related to Sensitive Data functionality in StealthAUDIT for SharePoint.

---

## Technical Background

### Key Concepts
- **SPPEEK Scan**: A scheduled scan process used to identify sensitive data within SharePoint environments.
- **SPSEEK Bulk Import**: A job that imports sensitive data findings into the Netwrix Enterprise Auditor database for further analysis.
- **Sensitive Data Discovery (SDD)**: A licensed feature that enables scanning and reporting on sensitive data.
- **Foreign Key Constraints**: Database rules that enforce relationships between tables, ensuring data integrity.

### System Context
- **Netwrix Enterprise Auditor Database**: Central repository for storing audit data, including sensitive data findings.
- **StealthAUDIT for SharePoint**: A component of Netwrix Enterprise Auditor designed to audit SharePoint environments for sensitive data and other compliance-related metrics.

---

## Issue Recognition & Triage

### Symptoms
- Scheduled scans freezing or becoming unresponsive.
- Errors during bulk import jobs, such as database constraint violations.
- Licensing-related errors preventing the execution of sensitive data scans.

### Priority Assessment
- **High Priority**: Issues that prevent scans or imports from completing, impacting compliance reporting.
- **Medium Priority**: Errors that can be resolved with patches or configuration changes.
- **Low Priority**: Licensing-related issues that require clarification but do not involve technical failures.

---

## Diagnostic Methodology

### Systematic Approach
1. **Verify Symptoms**: Confirm the reported issue by reviewing logs, error messages, and system behavior.
2. **Check System Resources**: Assess CPU, memory, and disk usage to rule out resource constraints.
3. **Analyze Logs**: Examine debug logs and tier 2 files for error codes and patterns.
4. **Investigate Database Integrity**: Check for foreign key constraint violations or missing tables.
5. **Review Licensing**: Confirm the customer’s licensing status for Sensitive Data Discovery.
6. **Engage Development**: If the issue involves software bugs, escalate to the development team for analysis.

---

## Information Collection

### Customer Queries
- What is the exact error message or behavior observed?
- When did the issue first occur?
- Has any recent patch or hotfix been applied?
- Are there any changes to the SharePoint environment or database configuration?

### Logs and Data to Collect
- Debug logs and tier 2 files from the affected scan or import job.
- Database error messages and SQL logs.
- System resource utilization metrics during the scan or import process.
- Licensing details for Sensitive Data Discovery.

---

## Common Scenarios & Solutions

### Scenario 1: Scheduled Scan Freezing
**Symptoms**: Scan process becomes unresponsive, and attempts to restart fail.  
**Resolution**: Restart the scan process. Monitor system resources and implement alerts for scan failures.  
**Reference Case**: [Ticket ID 500Qk00000FJaYcIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FJaYcIAL/view)

---

### Scenario 2: Foreign Key Constraint Error During Bulk Import
**Symptoms**: Bulk import job fails with a database error indicating a conflict with a foreign key constraint.  
**Resolution**: Apply a patch to address the bug causing the database conflict. Monitor bulk import behavior after applying patches.  
**Reference Case**: [Ticket ID 500Qk00000KPkkBIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KPkkBIAT/view)

---

### Scenario 3: Licensing Error Preventing Bulk Import
**Symptoms**: Error indicating a missing table or licensing issue during bulk import.  
**Resolution**: Confirm licensing requirements with the customer. Provide documentation on feature-specific licensing.  
**Reference Case**: [Ticket ID 500Qk00000NmKIZIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NmKIZIA3/view)

---

## Detailed Case Studies

### Case Study 1: Scheduled Scan Freezing
**Ticket ID**: [500Qk00000FJaYcIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FJaYcIAL/view)  
**Symptoms**: Scheduled SPPEEK scan froze on server Y0185-APP0443-S.  
**Diagnostic Steps**: Verified scan status, checked system resources, attempted restart, consulted SA/NEA team.  
**Resolution**: Restarted the scan process, which resolved the issue.  
**Key Takeaways**: Monitor scan performance regularly and implement alerts for failures.  

---

### Case Study 2: Foreign Key Constraint Error
**Ticket ID**: [500Qk00000KPkkBIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KPkkBIAT/view)  
**Symptoms**: Bulk import job failed due to a foreign key constraint conflict in the database.  
**Diagnostic Steps**: Reviewed debug logs, analyzed error message, investigated hotfix impact, engaged development.  
**Resolution**: Applied a patch to fix the bug. Bulk imports functioned correctly post-patch.  
**Key Takeaways**: Monitor database behavior after applying patches and document similar errors for future analysis.  

---

### Case Study 3: Licensing Error
**Ticket ID**: [500Qk00000NmKIZIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NmKIZIA3/view)  
**Symptoms**: SQL logic error indicating a missing table due to licensing limitations.  
**Diagnostic Steps**: Ran SPAA system scan, executed bulk import, confirmed licensing issue.  
**Resolution**: Clarified licensing requirements with the customer.  
**Key Takeaways**: Ensure customers understand licensing requirements before using specific features.  

---

## Best Practices & Tips

1. **Proactive Monitoring**: Implement alerts for scan failures or freezes to enable quicker responses.
2. **Patch Management**: Test patches and hotfixes in a staging environment before deployment.
3. **Licensing Awareness**: Provide customers with clear documentation on feature-specific licensing requirements.
4. **Database Integrity Checks**: Regularly audit database constraints and relationships to prevent import errors.
5. **Customer Communication**: Maintain clear and concise communication with customers regarding troubleshooting steps and resolutions.

---

## Escalation Guidelines

### Criteria for Escalation
- Issues involving software bugs or unresolvable database conflicts.
- Persistent scan failures despite resource optimization.
- Licensing disputes requiring clarification from sales or licensing teams.

### Escalation Procedure
1. Document all troubleshooting steps and findings.
2. Attach relevant logs, error messages, and screenshots.
3. Submit the case to the appropriate development or licensing team with detailed notes.
4. Follow up regularly to ensure timely resolution.

--- 

End of Document.