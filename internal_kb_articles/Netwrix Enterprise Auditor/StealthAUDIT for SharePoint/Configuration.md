# Knowledge Base Reference Guide: Troubleshooting StealthAUDIT for SharePoint Configuration Issues

## Overview
This guide provides a comprehensive reference for troubleshooting configuration issues related to the StealthAUDIT for SharePoint component of Netwrix Enterprise Auditor (NEA). These issues often involve connectivity, authentication, and configuration challenges when integrating with SharePoint Online. Understanding and resolving these problems is critical to ensuring successful data collection and auditing in SharePoint environments.

## Technical Background
StealthAUDIT for SharePoint is a component of NEA designed to audit and monitor SharePoint environments. Key elements include:
- **Azure App Authentication**: Used to establish secure connections between NEA and SharePoint Online.
- **SP_RegisterAzureAppAuth Job**: Automates Azure app registration for SharePoint Online.
- **Connection Profiles**: Define the parameters for connecting to SharePoint, including host URLs, credentials, and permissions.
- **Certificates**: Used for authentication when connecting to Azure and SharePoint Online.
- **Scan Depth**: Determines the level of detail in SharePoint scans.

Common challenges arise from misconfigurations in Azure app registration, incorrect host URLs, missing database tables, or insufficient permissions.

## Issue Recognition & Triage
### Symptoms
- Errors during SharePoint connection attempts (e.g., "ACCESS DENIED").
- Authentication failures with Azure apps (e.g., AADSTS700027 errors).
- Failed SharePoint scans or incomplete data collection.
- Configuration errors in connection profiles or job settings.

### Priority Assessment
- **High Priority**: Issues preventing all SharePoint data collection or causing critical authentication failures.
- **Medium Priority**: Errors affecting specific jobs or scans but not the overall functionality.
- **Low Priority**: Documentation discrepancies or minor warnings.

## Diagnostic Methodology
1. **Verify Configuration**: Check host URLs, connection profiles, and Azure app settings.
2. **Test Connectivity**: Use PowerShell commands (e.g., `Test-NetConnection`) to confirm network access.
3. **Review Logs**: Examine job logs, error messages, and PowerShell outputs for clues.
4. **Validate Permissions**: Ensure Azure apps have the required API permissions.
5. **Check Certificates**: Confirm that certificates are correctly configured and registered.
6. **Inspect Database**: Verify the presence of necessary tables and stored procedures.

## Information Collection
### Questions to Ask Customers
- What version of NEA are you using?
- What is the SharePoint Online URL?
- Have you configured an Azure app for authentication? If so, what are the app ID and permissions?
- Are there any recent changes to certificates or connection profiles?
- Can you provide logs or screenshots of the error messages?

### Data to Collect
- PowerShell outputs (e.g., `Test-NetConnection`, Azure AD module commands).
- Job logs from the NEA console.
- Screenshots of Azure app configurations.
- SQL database structure (if applicable).

## Common Scenarios & Solutions
### Scenario 1: Incorrect Host URL Configuration
- **Symptoms**: Token request failures during Azure app registration.
- **Solution**: Update the host URL in the configuration to the correct format (e.g., `*.sharepoint.com` instead of `*.onmicrosoft.com`). Use the SP_RegisterAzureAppAuth job for automated setup.
- **Reference Case**: [500Qk00000Cu9JRIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Cu9JRIAZ/view)

### Scenario 2: Azure App Authentication Failures
- **Symptoms**: Errors related to Azure Client ID or certificate thumbprints.
- **Solution**: Verify API permissions, update connection profile credentials, and ensure certificates are properly registered in Azure.
- **Reference Case**: [500Qk00000PSn4DIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PSn4DIAT/view)

### Scenario 3: Missing Database Tables
- **Symptoms**: "ACCESS DENIED" errors due to missing database tables.
- **Solution**: Execute scripts provided by R&D to manually create the required tables and stored procedures.
- **Reference Case**: [500Qk00000GzgQwIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GzgQwIAJ/view)

### Scenario 4: Misconfigured Connection Profiles
- **Symptoms**: Failed SharePoint scans or connection attempts.
- **Solution**: Create a new connection profile, provision necessary permissions, and assign settings to all child objects.
- **Reference Case**: [500Qk00000KYiCpIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KYiCpIAL/view)

### Scenario 5: Certificate Configuration Errors
- **Symptoms**: Authentication errors after uploading a new certificate.
- **Solution**: Recreate the Azure app with the correct configuration and update the connection profile credentials.
- **Reference Case**: [500Qk00000PSn4DIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PSn4DIAT/view)

## Detailed Case Studies
### Case Study 1: Incorrect Host URL Configuration
- **Ticket**: [500Qk00000Cu9JRIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Cu9JRIAZ/view)
- **Symptoms**: Token request failures during Azure app registration.
- **Diagnostic Steps**: Reviewed documentation, identified incorrect host URL, and corrected it.
- **Resolution**: Updated the host URL to `*.sharepoint.com` and used SP_RegisterAzureAppAuth for setup.
- **Key Takeaways**: Ensure documentation specifies the correct host URL format.

### Case Study 2: Missing Database Tables
- **Ticket**: [500Qk00000GzgQwIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GzgQwIAJ/view)
- **Symptoms**: "ACCESS DENIED" errors during SharePoint connection attempts.
- **Diagnostic Steps**: Verified database structure and identified missing tables.
- **Resolution**: Executed R&D-provided scripts to create the necessary tables.
- **Key Takeaways**: Document the manual table creation process for environments without on-prem AD.

### Case Study 3: Certificate Configuration Errors
- **Ticket**: [500Qk00000PSn4DIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PSn4DIAT/view)
- **Symptoms**: Authentication errors after uploading a new certificate.
- **Diagnostic Steps**: Reviewed Azure app configuration and identified a mismatch in the certificate thumbprint.
- **Resolution**: Recreated the Azure app and updated connection profile credentials.
- **Key Takeaways**: Always verify certificate registration and update credentials after changes.

## Best Practices & Tips
- **Documentation Accuracy**: Regularly review and update documentation to reflect the latest configurations and procedures.
- **Azure App Permissions**: Ensure all required API permissions are provisioned before running jobs.
- **Certificate Management**: Maintain a clear process for updating and registering certificates.
- **Connection Profiles**: Periodically review and validate connection profiles to prevent misconfigurations.
- **Customer Communication**: Provide clear instructions and request detailed logs to expedite troubleshooting.

## Escalation Guidelines
- **When to Escalate**:
  - Issues involving product defects or missing database tables.
  - Persistent authentication failures despite following documented procedures.
  - Complex cases requiring R&D intervention.
- **How to Escalate**:
  - Provide a detailed summary of the issue, including logs, screenshots, and diagnostic steps taken.
  - Include relevant ticket references and customer environment details.
  - Use the internal escalation process to notify the appropriate teams.