# Comprehensive Knowledge Base Guide: Troubleshooting Access Auditing Issues in StealthAUDIT for SharePoint

## Overview

This guide provides a systematic approach to diagnosing and resolving issues related to Access Auditing in the StealthAUDIT for SharePoint component of Netwrix Enterprise Auditor (NEA). Access Auditing is critical for ensuring visibility into permissions, access requests, and resource reviews across SharePoint environments, including SharePoint Online (SPO) and OneDrive. Understanding and addressing these issues is essential for maintaining data security, compliance, and operational efficiency.

---

## Technical Background

### Key Concepts
- **Access Auditing**: Tracks and reports on permissions, access requests, and resource reviews for SharePoint and OneDrive.
- **StealthAUDIT for SharePoint**: A module within NEA designed to audit SharePoint environments, including on-premises and cloud-based deployments.
- **Access Intelligence Center (AIC)**: Provides centralized visibility into access requests and resource reviews.
- **SPAA (SharePoint Access Auditing)**: A specific feature within StealthAUDIT that scans SharePoint environments for access-related data.
- **SPAC (SharePoint Activity Collection)**: Collects activity logs from SharePoint environments, including SPO.

### Common Components
- **Database Dependencies**: StealthAUDIT relies on SQL databases (e.g., `tempdb`, `StealthauditDB`) for storing and processing data.
- **Microsoft Graph API**: Used for accessing SharePoint Online and OneDrive data.
- **Event Type Mapping**: Ensures that new SharePoint event types are recognized and processed correctly.

### Typical Challenges
- Integration with cloud platforms like OneDrive and SPO.
- Compatibility with third-party software (e.g., anti-virus programs).
- Handling new or unknown SharePoint event types introduced by Microsoft.
- Database constraints and configuration issues.

---

## Issue Recognition & Triage

### Symptoms to Watch For
- Scans hanging or timing out (e.g., SPAA scans not completing).
- Errors related to database constraints (e.g., foreign key violations).
- Missing or unrecognized SharePoint event types.
- Connectivity issues with Microsoft Graph API.
- Storage-related errors in SQL databases (e.g., `tempdb` full).

### Priority Assessment
- **High Priority**: Issues causing data loss, inability to collect critical access data, or complete scan failures.
- **Medium Priority**: Errors affecting specific features (e.g., Access Requests) but not the overall functionality.
- **Low Priority**: Minor errors or warnings that do not impact core operations.

---

## Diagnostic Methodology

### Systematic Approach
1. **Reproduce the Issue**: Confirm the problem by replicating the reported behavior.
2. **Review Logs**: Examine relevant logs (e.g., SPAA logs, SQL logs) for error messages and patterns.
3. **Check Configuration**: Verify system settings, including database configurations, permissions, and module versions.
4. **Isolate Variables**: Determine if the issue is environment-specific (e.g., on-premises vs. cloud).
5. **Engage Development**: For unresolved issues, escalate to the development team with detailed logs and findings.

### Decision Points
- **Is the issue related to third-party software?** Investigate potential interference (e.g., anti-virus settings).
- **Is the issue environment-specific?** Check for differences in configuration between affected and unaffected environments.
- **Are there recent updates or changes?** Review recent hotfixes, patches, or system updates.

---

## Information Collection

### Key Questions for Customers
- What is the scope of the issue (e.g., specific scans, all scans)?
- Are there any recent changes to the environment (e.g., migrations, updates)?
- Is the issue intermittent or consistent?
- Are there any third-party tools (e.g., anti-virus) in use?

### Logs and Data to Collect
- SPAA logs and SPAC logs.
- SQL logs, particularly for `tempdb` and `StealthauditDB`.
- Screenshots of error messages.
- Details of recent updates or hotfixes applied.

---

## Common Scenarios & Solutions

### Scenario 1: SPAA Scans Hanging
- **Symptoms**: Scans do not complete and hang until timeout.
- **Root Cause**: Anti-virus interference.
- **Solution**: Adjust anti-virus settings to exclude StealthAUDIT processes. Perform a repair installation and apply the latest cumulative updates.
- **Reference Case**: [500Qk00000FK62HIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FK62HIAT/view)

### Scenario 2: Foreign Key Constraint Violations
- **Symptoms**: Errors during bulk imports due to database constraints.
- **Root Cause**: High USN values and DLL errors from a previous hotfix.
- **Solution**: Upgrade to the latest NEA version, reset USN values, and unblock DLLs.
- **Reference Case**: [500Qk00000HZVyTIAX](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HZVyTIAX/view)

### Scenario 3: `tempdb` Full Errors
- **Symptoms**: SQL `tempdb` runs out of space during scans.
- **Root Cause**: Concurrent jobs filling up `tempdb`.
- **Solution**: Monitor and limit concurrent jobs. Configure `tempdb` autogrowth settings.
- **Reference Case**: [500Qk00000JXhZVIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JXhZVIA1/view)

### Scenario 4: Unknown SharePoint Event Types
- **Symptoms**: Missing activity events in SPO scans.
- **Root Cause**: New event types not mapped in NEA.
- **Solution**: Apply the latest hotfix with updated event mappings.
- **Reference Case**: [500Qk00000O9ytZIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O9ytZIAR/view)

### Scenario 5: Microsoft Graph API Connection Errors
- **Symptoms**: Failure to connect to Graph API during app registration.
- **Root Cause**: Incorrect connection profile configuration.
- **Solution**: Use PowerShell to manually connect to Graph API and pre-authenticate.
- **Reference Case**: [500Qk00000OwQxCIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OwQxCIAV/view)

---

## Detailed Case Studies

### Case Study: SPAA Scans Hanging
- **Ticket ID**: [500Qk00000FK62HIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FK62HIAT/view)
- **Symptoms**: Scans hung until timeout.
- **Diagnostic Steps**: Checked anti-virus settings, performed repair installation, and applied updates.
- **Resolution**: Adjusted anti-virus settings and confirmed successful scans.
- **Key Takeaways**: Always verify third-party software interactions.

### Case Study: Foreign Key Constraint Violations
- **Ticket ID**: [500Qk00000HZVyTIAX](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HZVyTIAX/view)
- **Symptoms**: Bulk import errors due to foreign key violations.
- **Diagnostic Steps**: Investigated USN values and DLL errors.
- **Resolution**: Upgraded NEA version and reset USN values.
- **Key Takeaways**: Ensure hotfixes are applied correctly and monitor database constraints.

---

## Best Practices & Tips

1. **Proactive Monitoring**: Set up alerts for database usage and scan performance.
2. **Regular Updates**: Keep NEA and its modules updated to the latest versions.
3. **Documentation**: Maintain detailed records of configurations and changes.
4. **Customer Communication**: Clearly explain troubleshooting steps and solutions.
5. **Collaboration**: Engage development early for complex issues.

---

## Escalation Guidelines

### When to Escalate
- Issues persist after applying standard troubleshooting steps.
- Errors involve unrecognized event types or require development fixes.
- Critical functionality (e.g., Access Requests) is completely unavailable.

### How to Escalate
1. Collect all relevant logs and screenshots.
2. Document steps already taken and their outcomes.
3. Submit a detailed escalation request to the development team.

--- 

This guide serves as a comprehensive reference for troubleshooting Access Auditing issues in StealthAUDIT for SharePoint, enabling consistent and effective resolution of customer cases.