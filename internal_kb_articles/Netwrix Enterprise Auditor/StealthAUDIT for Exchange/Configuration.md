# Knowledge Base Reference Guide: Troubleshooting StealthAUDIT for Exchange Configuration Issues

## Overview

This guide provides a comprehensive reference for troubleshooting configuration issues related to the StealthAUDIT for Exchange component of Netwrix Enterprise Auditor. These issues typically involve problems with job configurations, permissions, connectivity, or data collection. Understanding and resolving these issues is critical to ensuring accurate reporting and maintaining system functionality.

## Technical Background

StealthAUDIT for Exchange is a collector within Netwrix Enterprise Auditor designed to gather data from Exchange environments, including on-premises and Exchange Online. Key components include:

- **Delegate Jobs**: Collect information about mailbox permissions and delegate access.
- **Exchange Online EWS**: Uses Exchange Web Services to retrieve mailbox and folder data.
- **Credential Profiles**: Define authentication methods for accessing Exchange environments.
- **Autodiscover Service**: Automatically locates Exchange server settings for connectivity.

Common challenges include misconfigurations, permission issues, and connectivity errors. Understanding the underlying systems (Exchange, PowerShell, SQL, and Netwrix job configurations) is essential for effective troubleshooting.

## Issue Recognition & Triage

### Symptoms
- Missing or incomplete delegate information in reports.
- Errors connecting to Exchange Online (e.g., PowerShell or SQL errors).
- Failure to collect data from Exchange Online EWS.
- Jobs skipping hosts or reporting them as offline.

### Priority Assessment
- **High Priority**: Issues affecting critical reporting or compliance data.
- **Medium Priority**: Errors causing partial data collection but not impacting compliance.
- **Low Priority**: Configuration warnings or minor discrepancies.

## Diagnostic Methodology

### Step-by-Step Approach
1. **Verify Symptoms**: Confirm the issue reported by the customer (e.g., missing data, connection errors).
2. **Review Job Configuration**: Check settings for delegate jobs, credential profiles, and host lists.
3. **Test Connectivity**: Use PowerShell commands and tools to verify Exchange connectivity.
4. **Examine Permissions**: Ensure proper permissions are assigned in Exchange and EntraID.
5. **Check Logs**: Review Netwrix logs and job execution results for error messages.
6. **Validate External Dependencies**: Confirm Autodiscover and Exchange endpoints are correctly configured.

## Information Collection

### Customer Questions
- What specific data is missing or incorrect?
- Are there any recent changes to the Exchange environment or permissions?
- Have any updates been applied to Netwrix Enterprise Auditor or Exchange?

### Logs and Data to Collect
- Netwrix job execution logs.
- PowerShell command outputs (e.g., `Get-MailboxPermission` results).
- Configuration files (e.g., `WebServer.exe.config`).
- Screenshots of job settings and error messages.

## Common Scenarios & Solutions

### Scenario 1: Missing Delegate Information
**Symptoms**: Delegate job results do not match expected outputs from Exchange commands.

**Resolution**:
1. Compare job results with PowerShell output:
   ```powershell
   Get-Mailbox -RecipientTypeDetails SharedMailbox -ResultSize Unlimited |
   Get-MailboxPermission |
   Select-Object Identity, User, AccessRights |
   Where-Object { $_.User -like '*@*' } |
   Export-Csv -Path C:Tempsharedfolders.csv -NoTypeInformation
   ```
2. Adjust job configuration to ensure all delegate information is captured.
3. Merge Exchange permissions into a consolidated report.

**Reference Case**: [Ticket ID 500Qk00000C0GvWIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C0GvWIAV/view)

---

### Scenario 2: Exchange Online Connectivity Errors
**Symptoms**: PowerShell and SQL errors when connecting to Exchange Online.

**Resolution**:
1. Assign the correct "Credential Profile" to Exchange jobs.
2. Modify permissions for the App Registration in EntraID.
3. Install the ExchangeManagementOnline PowerShell module.
4. Update host lists to use "office365.outlook.com".
5. Adjust job properties to disable skipping unresponsive hosts.
6. Enable Windows Authentication in `WebServer.exe.config`.

**Reference Case**: [Ticket ID 500Qk00000HPsQ1IAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HPsQ1IAL/view)

---

### Scenario 3: Exchange Online EWS Data Collection Failure
**Symptoms**: Exchange Online EWS fails to collect data despite correct settings.

**Resolution**:
1. Verify Autodiscover settings and correct any misconfigurations.
2. Test connectivity to Exchange Online endpoints.
3. Re-run the job after fixing Autodiscover.

**Reference Case**: [Ticket ID 500Qk00000KjmBSIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KjmBSIAZ/view)

## Detailed Case Studies

### Case Study 1: Missing Delegate Information
**Ticket ID**: [500Qk00000C0GvWIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C0GvWIAV/view)

**Initial Symptoms**: Delegate job results were incomplete compared to PowerShell outputs.

**Diagnostic Steps**:
1. Reviewed job results and compared them with PowerShell outputs.
2. Modified delegate results to test job functionality.
3. Consulted documentation on shared mailbox permissions.

**Key Information**: Job configuration was filtering out certain delegates.

**Resolution**:
- Adjusted job settings to capture all delegate information.
- Merged permissions into a new report.

**Takeaways**:
- Always test job configurations against expected outputs.
- Regularly review settings to align with organizational policies.

---

### Case Study 2: Exchange Online Connectivity Errors
**Ticket ID**: [500Qk00000HPsQ1IAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HPsQ1IAL/view)

**Initial Symptoms**: PowerShell and SQL errors when connecting to Exchange Online.

**Diagnostic Steps**:
1. Verified credential profiles and permissions.
2. Installed necessary PowerShell modules.
3. Updated host lists and job properties.

**Key Information**: Incorrect credential profiles and permissions caused connectivity issues.

**Resolution**:
- Correctly configured credential profiles and permissions.
- Updated host lists and enabled Windows Authentication.

**Takeaways**:
- Ensure proper training for new users on credential profiles.
- Review configurations thoroughly before deployment.

---

### Case Study 3: Exchange Online EWS Data Collection Failure
**Ticket ID**: [500Qk00000KjmBSIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KjmBSIAZ/view)

**Initial Symptoms**: Exchange Online EWS failed to collect data.

**Diagnostic Steps**:
1. Verified settings and host configurations.
2. Tested Autodiscover functionality.

**Key Information**: Autodiscover service was misconfigured.

**Resolution**:
- Fixed Autodiscover settings to enable data collection.

**Takeaways**:
- Regularly verify Autodiscover settings during setup.
- Include Autodiscover checks in routine maintenance.

## Best Practices & Tips

1. **Configuration Validation**: Always test job configurations against expected outputs before deployment.
2. **Permission Management**: Ensure credential profiles and permissions are correctly set up and regularly reviewed.
3. **Connectivity Testing**: Use PowerShell commands to verify Exchange connectivity and troubleshoot errors.
4. **Documentation Reference**: Familiarize yourself with Netwrix documentation for specific features and permissions.
5. **Routine Maintenance**: Regularly review Autodiscover settings, host lists, and job properties to prevent issues.
6. **Customer Communication**: Clearly explain troubleshooting steps and resolutions to customers to build trust and confidence.

## Escalation Guidelines

### Criteria for Escalation
- Issues persist after following all troubleshooting steps.
- Errors involve complex dependencies (e.g., third-party integrations).
- Customer requests escalation due to urgency or impact.

### Escalation Procedure
1. Document all troubleshooting steps and findings.
2. Collect relevant logs, screenshots, and configuration files.
3. Submit a detailed escalation request to the appropriate team or tier.
4. Communicate escalation status to the customer and provide updates as needed.