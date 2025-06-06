# Comprehensive Knowledge Base Reference Guide: PingCastle General Issues

## Overview

This guide provides a systematic approach to diagnosing and resolving issues related to PingCastle Enterprise under the "PingCastle General" feature. It covers common problems, troubleshooting methodologies, and best practices for handling customer inquiries effectively. The goal is to equip support engineers with the tools and knowledge to address these issues confidently and consistently.

## Technical Background

PingCastle is a security assessment tool designed to evaluate Active Directory environments for vulnerabilities and misconfigurations. Key components include:
- **PC Enterprise**: The enterprise version of PingCastle, offering advanced features such as API integrations, centralized reporting, and claims-based authentication.
- **Features**: Includes health checks, rule scans, reporting, and API capabilities.
- **Key Terminology**:
  - **Rules**: Predefined checks that identify vulnerabilities or misconfigurations.
  - **Claims**: Attributes used for authentication and authorization in PingCastle.
  - **API**: Interfaces for automating tasks and retrieving data programmatically.
  - **Configuration Files**: Files such as `PingCastle.exe.config` and `appsettings.Production.json` used for customizing PingCastle behavior.

Understanding these components is essential for diagnosing and resolving issues effectively.

## Issue Recognition & Triage

### Common Symptoms
- Errors during installation (e.g., missing prerequisites, error codes like 26201).
- Incorrect or incomplete scan results (e.g., false positives, missing data).
- API-related issues (e.g., authentication failures, incomplete data retrieval).
- Problems with claims-based authentication or role assignments.
- Reporting discrepancies (e.g., missing Azure data, incorrect domain scores).
- Configuration challenges (e.g., custom rules, exclusions, migration).

### Priority Assessment
- **High Priority**: Issues affecting production environments, such as installation failures or critical scan errors.
- **Medium Priority**: Problems with reporting accuracy or API functionality.
- **Low Priority**: Configuration inquiries or requests for documentation.

## Diagnostic Methodology

### Step-by-Step Approach
1. **Understand the Problem**:
   - Review the customer's description and environment details.
   - Identify whether the issue is related to installation, configuration, scanning, or reporting.

2. **Reproduce the Issue**:
   - Attempt to replicate the problem in a lab environment using similar configurations.

3. **Collect Logs and Data**:
   - Gather relevant logs, screenshots, and configuration files from the customer.
   - Use tools like PowerShell or Event Viewer to validate Active Directory attributes and system settings.

4. **Analyze Root Cause**:
   - Compare collected data against expected behavior.
   - Check for missing prerequisites, incorrect configurations, or software bugs.

5. **Implement Resolution**:
   - Apply fixes based on the identified root cause.
   - Test the solution in the customer's environment to confirm resolution.

6. **Document Findings**:
   - Record the issue, resolution steps, and any lessons learned for future reference.

## Information Collection

### Key Questions to Ask Customers
- What version of PingCastle are you using?
- Are you encountering errors during installation or runtime?
- Have you verified prerequisites (e.g., SQL Server, .NET framework)?
- Are you using claims-based authentication or API integrations?
- Can you provide logs, screenshots, or configuration files?

### Logs and Data to Collect
- **PingCastle Logs**: Found in the installation directory.
- **Active Directory Attributes**: Use PowerShell commands to retrieve `pwdLastSet`, `lastLogonTimestamp`, etc.
- **Configuration Files**: `PingCastle.exe.config`, `appsettings.Production.json`.
- **Event Viewer Logs**: Check for .NET runtime errors or application stop events.

## Common Scenarios & Solutions

### Scenario 1: Installation Errors (e.g., Error Code 26201)
- **Symptoms**: Installation fails due to missing prerequisites.
- **Solution**: Ensure SQL Server Management Studio (SSMS) and other prerequisites are installed. Retry installation.

### Scenario 2: Incorrect Scan Results
- **Symptoms**: False positives or missing data in reports.
- **Solution**: Verify domain controller replication and time synchronization. Check for future timestamps in Active Directory attributes.

### Scenario 3: API Authentication Failures
- **Symptoms**: `(405) Method Not Allowed` errors or incomplete data retrieval.
- **Solution**: Confirm API endpoint accessibility and authentication method. Address certificate or firewall issues.

### Scenario 4: Claims-Based Authentication Issues
- **Symptoms**: Users unable to access domains or dashboards.
- **Solution**: Verify claims configuration and role assignments. Update PingCastle to the latest version if necessary.

### Scenario 5: Reporting Discrepancies
- **Symptoms**: Missing Azure data or incorrect domain scores.
- **Solution**: Adjust domain statuses in the PingCastle console. Ensure scan accounts have Global Admin privileges.

## Detailed Case Studies

### Case Study 1: Installation Error (Ticket ID: [500Qk00000OvsAjIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OvsAjIAJ/view))
- **Symptoms**: Error code 26201 during MSI installation.
- **Diagnostic Steps**:
  - Verified prerequisites (SSMS was missing).
  - Installed SSMS and retried installation.
- **Resolution**: Installation succeeded after prerequisites were met.
- **Key Takeaways**: Always verify prerequisites before installation.

### Case Study 2: Claims Configuration Issue (Ticket ID: [500Qk00000NdfZ7IAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NdfZ7IAJ/view))
- **Symptoms**: Users unable to access domains despite correct role assignments.
- **Diagnostic Steps**:
  - Reviewed claims configuration and role mappings.
  - Updated PingCastle to version 3.3.0.11.
- **Resolution**: Claims propagation issue resolved in the updated version.
- **Key Takeaways**: Ensure claims configuration matches expected attributes and use the latest software version.

### Case Study 3: Reporting Discrepancies (Ticket ID: [500Qk00000LKfsaIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LKfsaIAD/view))
- **Symptoms**: Missing Azure data in reports.
- **Diagnostic Steps**:
  - Verified scan account permissions (Global Admin privileges were missing).
  - Updated permissions and reran the scan.
- **Resolution**: Azure data populated correctly after permissions were adjusted.
- **Key Takeaways**: Ensure scan accounts have sufficient privileges.

## Best Practices & Tips

1. **Verify Prerequisites**:
   - Ensure all required software (e.g., SSMS, .NET framework) is installed before starting PingCastle installation.

2. **Maintain Configuration Files**:
   - Regularly review and update configuration files to reflect changes in the environment.

3. **Monitor Domain Controllers**:
   - Check replication and time synchronization to prevent scan inaccuracies.

4. **Use Claims Effectively**:
   - Map claims correctly and ensure role assignments are consistent with user requirements.

5. **Leverage API Documentation**:
   - Familiarize yourself with PingCastle API endpoints to streamline data retrieval and automation.

## Escalation Guidelines

### When to Escalate
- Issues persist despite following troubleshooting steps.
- Bugs or defects in PingCastle are suspected.
- Customer requests features not currently supported by PingCastle.

### How to Escalate
- Provide detailed logs, screenshots, and configuration files.
- Document all troubleshooting steps taken.
- Submit a feature request or bug report to the Netwrix community or development team.

### Escalation Example
- **Ticket ID**: [500Qk00000PKjiYIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PKjiYIAT/view)
- **Issue**: Database creation errors during installation.
- **Escalation Steps**:
  - Provided logs and configuration details to the development team.
  - Assisted customer with manual installation as a temporary workaround.

By following this guide, support engineers can systematically address PingCastle General issues, ensuring efficient and effective resolutions.