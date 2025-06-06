# Comprehensive Knowledge Base Guide: Troubleshooting PingCastle General Issues

## Overview

This guide provides a systematic approach to troubleshooting issues related to PingCastle's PC Professional component under the "PingCastle General" feature. It is designed to help support engineers effectively diagnose, resolve, and prevent common problems encountered by customers. The guide covers key concepts, diagnostic methodologies, common scenarios, and best practices, with detailed case studies for reference.

---

## Technical Background

### Key Concepts
- **PingCastle Pro**: A professional-grade tool for Active Directory security health checks and reporting.
- **Core Features**: Includes scheduling scans, generating reports, importing/exporting configurations, and integrating with Azure AD.
- **Dependencies**: Relies on specific .NET versions, SQL databases, and proper configuration of application settings.
- **Common Components**:
  - **Scheduler**: Automates scans and report generation.
  - **License Management**: Ensures the correct application of Pro licenses.
  - **Database Integration**: Stores scan results and configurations.
  - **Authentication**: Supports Azure AD and local domain authentication.

### Terminology
- **`appsettings.production.json`**: Configuration file for PingCastle, including license and database settings.
- **`GrantApplicationPoolToSql.ps1`**: Script used during installation to configure SQL permissions.
- **`LastLogonTimeStamp`**: AD attribute used for calculating inactive accounts.
- **RODC**: Read-Only Domain Controller, which caches credentials for specific users.

### System Context
PingCastle operates in environments with Active Directory and Azure AD integrations. It requires specific versions of .NET and ASP.NET Core Hosting Bundles for compatibility. Misconfigurations or outdated dependencies often lead to operational issues.

---

## Issue Recognition & Triage

### Common Symptoms
- **Scheduler Failures**: Reports not sent or tasks not executed.
- **License Issues**: Application defaults to the free version despite a valid Pro license.
- **Installation Errors**: Failures during database creation or missing files.
- **Authentication Failures**: Blank dialogs or errors in Azure AD integration.
- **Report Discrepancies**: Missing data or incorrect calculations in reports.

### Priority Assessment
- **High Priority**: Issues causing complete application failure (e.g., HTTP 500 errors, crashes).
- **Medium Priority**: Functional issues affecting specific features (e.g., scheduler not sending emails).
- **Low Priority**: Cosmetic or minor discrepancies in reports.

---

## Diagnostic Methodology

### Step-by-Step Approach
1. **Understand the Problem**:
   - Review the customer's description and logs.
   - Identify the affected feature (e.g., scheduler, licensing, reporting).
2. **Verify the Environment**:
   - Check software versions (PingCastle, .NET, ASP.NET).
   - Confirm system prerequisites (e.g., SQL database, hosting bundle).
3. **Reproduce the Issue**:
   - Attempt to replicate the problem in a test environment.
   - Use provided logs and error messages for clues.
4. **Analyze Logs**:
   - Review application logs, scheduler logs, and system event logs.
   - Look for specific error codes or stack traces.
5. **Apply Known Solutions**:
   - Refer to common scenarios and resolution paths.
   - Test fixes in a controlled environment before advising the customer.
6. **Escalate if Necessary**:
   - If the issue is unresolved, escalate to R&D with detailed findings.

---

## Information Collection

### Questions to Ask Customers
- What version of PingCastle are you using?
- What .NET and ASP.NET versions are installed?
- Are there any recent changes to the environment (e.g., updates, configuration changes)?
- Can you provide logs or screenshots of the error?

### Logs and Data to Collect
- **Application Logs**: Located in the PingCastle directory.
- **Scheduler Logs**: For issues related to automated tasks.
- **System Event Logs**: For installation or runtime errors.
- **Configuration Files**: `appsettings.production.json`, `pingcastle.config`.

---

## Common Scenarios & Solutions

### Scenario 1: Scheduler Not Sending Emails
- **Symptoms**: Scheduler runs but emails are not sent.
- **Root Cause**: Outdated software version or configuration issues.
- **Solution**: Upgrade to the latest version and verify email settings. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Dvxv7IAB)

### Scenario 2: License Defaults to Free Version
- **Symptoms**: Pro features unavailable despite a valid license.
- **Root Cause**: Incorrect or missing license key in `appsettings.production.json`.
- **Solution**: Update the configuration file with the correct license key. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EcETKIA3)

### Scenario 3: Installation Errors
- **Symptoms**: Errors during database creation or missing files.
- **Root Cause**: Missing scripts or incorrect .NET version.
- **Solution**: Ensure all prerequisites are met and use the latest installer. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LDDTEIA5)

### Scenario 4: Authentication Failures
- **Symptoms**: Blank dialogs or errors in Azure AD integration.
- **Root Cause**: Proxy misconfiguration or missing permissions.
- **Solution**: Adjust proxy settings and verify Azure AD permissions. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LVJjsIAH)

### Scenario 5: Report Discrepancies
- **Symptoms**: Missing or incorrect data in reports.
- **Root Cause**: Misinterpretation of data or incomplete scans.
- **Solution**: Re-run scans with the `--full` parameter and clarify report details. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MfRyrIAF)

---

## Detailed Case Studies

### Case Study 1: Scheduler Email Failure
- **Ticket**: [500Qk00000Dvxv7IAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Dvxv7IAB)
- **Symptoms**: Scheduler stopped sending emails.
- **Diagnostic Steps**:
  1. Reviewed logs indicating unsupported software version.
  2. Verified the installed version was outdated.
- **Resolution**: Upgraded to the latest version, restoring functionality.
- **Key Takeaway**: Regular updates prevent compatibility issues.

### Case Study 2: Installation Error 26021
- **Ticket**: [500Qk00000LDDTEIA5](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LDDTEIA5)
- **Symptoms**: Installation failed during database creation.
- **Diagnostic Steps**:
  1. Reviewed logs showing missing `GrantApplicationPoolToSql.ps1`.
  2. Confirmed script was inaccessible.
- **Resolution**: Released a new installer version to fix the issue.
- **Key Takeaway**: Ensure all installation scripts are included and accessible.

### Case Study 3: Authentication Failure in Azure AD
- **Ticket**: [500Qk00000LVJjsIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LVJjsIAH)
- **Symptoms**: Blank authentication dialog in interactive mode.
- **Diagnostic Steps**:
  1. Verified proxy settings in Internet Settings.
  2. Adjusted settings to resolve the issue.
- **Resolution**: Corrected proxy configuration, enabling authentication.
- **Key Takeaway**: Proxy settings are critical for Azure AD integration.

---

## Best Practices & Tips

1. **Keep Software Updated**: Regularly check for new PingCastle versions to avoid known bugs.
2. **Verify Prerequisites**: Ensure all dependencies (e.g., .NET, ASP.NET) are installed and compatible.
3. **Backup Configurations**: Before updates or changes, back up critical files like `appsettings.production.json`.
4. **Use Comprehensive Scans**: Always include the `--full` parameter for detailed reporting.
5. **Document Changes**: Maintain a log of updates and configurations for troubleshooting.

---

## Escalation Guidelines

### When to Escalate
- Issues unresolved after applying known solutions.
- Bugs requiring development team intervention.
- Critical failures affecting multiple customers.

### How to Escalate
- Provide detailed logs, error messages, and reproduction steps.
- Include environment details (software versions, configurations).
- Use the internal escalation process to notify R&D.

--- 

This guide serves as a definitive reference for handling PingCastle General issues, enabling support engineers to resolve problems efficiently and consistently.