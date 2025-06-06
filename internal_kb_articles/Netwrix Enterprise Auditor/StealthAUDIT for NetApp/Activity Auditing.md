# Netwrix Enterprise Auditor: StealthAUDIT for NetApp - Activity Auditing Troubleshooting Guide

## Overview
This guide provides a comprehensive reference for troubleshooting issues related to the **Activity Auditing** feature in **StealthAUDIT for NetApp**, a component of **Netwrix Enterprise Auditor**. Activity Auditing is critical for monitoring and analyzing user actions and system events on NetApp systems, ensuring compliance and security. Understanding and resolving issues in this category is essential for maintaining accurate auditing and uninterrupted system functionality.

## Technical Background
### Key Concepts
- **Activity Auditing**: Tracks user and system activities on NetApp systems, providing insights into file access, modifications, and other operations.
- **StealthAUDIT**: A module within Netwrix Enterprise Auditor designed for auditing file systems, including NetApp systems.
- **Proxy Server**: Acts as an intermediary for communication between Netwrix Enterprise Auditor and monitored systems.
- **FSAC System Scan**: A process that retrieves configuration and activity data from monitored systems.

### System Context
- **NetApp Systems**: Network-attached storage devices that require specific permissions and configurations for auditing.
- **Registry Keys**: Critical for storing configuration paths and settings used by Netwrix Enterprise Auditor.
- **Configuration Files**: Files such as `SBTFileMon.ini` store operational settings for StealthAUDIT.

## Issue Recognition & Triage
### Symptoms
- **Activity Bulk Import Failures**: Errors during data import from NetApp systems, often linked to proxy server transitions or misconfigurations.
- **Registry Access Errors**: Messages such as "Requested registry access is not allowed," indicating permission issues with registry keys.

### Priority Assessment
- **High Priority**: Issues that prevent auditing or data collection, impacting compliance and security monitoring.
- **Medium Priority**: Configuration errors that can be resolved without significant impact on auditing functionality.

## Diagnostic Methodology
### Systematic Approach
1. **Verify Environment Details**: Confirm product version, build number, and system configurations.
2. **Reproduce the Issue**: Attempt to replicate the error to understand its scope and impact.
3. **Review Permissions**: Check proxy server and registry key permissions against documentation.
4. **Analyze Logs**: Examine system logs for error messages and diagnostic clues.
5. **Consult Documentation**: Reference official Netwrix documentation for configuration requirements.

### Decision Points
- If permissions are misconfigured, proceed with correcting them.
- If the issue persists after configuration changes, escalate for deeper investigation.

## Information Collection
### Customer Queries
- What changes were made to the environment prior to the issue (e.g., proxy server transitions)?
- Are there specific error messages or logs available?
- What is the current configuration of the affected systems?

### Logs and Data
- **System Logs**: Collect logs from Netwrix Enterprise Auditor and affected NetApp systems.
- **Registry Key Details**: Verify permissions and values for relevant registry keys.
- **Configuration Files**: Review files such as `SBTFileMon.ini` for incorrect settings.

## Common Scenarios & Solutions
### Scenario 1: Activity Bulk Import Fails During Proxy Server Transition
#### Symptoms
- Bulk import fails for multiple NetApp systems.
- Proxy server permissions misaligned with documentation.

#### Resolution
1. Verify proxy server permissions against [Proxy Server Permissions Documentation](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Requirements/Solutions/FileSystem/ProxyModeServicePermissions.htm).
2. Correct permissions as specified.
3. Re-initiate the bulk import process.

#### Reference Case
[Ticket ID: 500Qk00000FfQfTIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FfQfTIAV/view)

---

### Scenario 2: FSAC System Scan Fails with Registry Access Error
#### Symptoms
- Error message: "Requested registry access is not allowed."
- Failure to retrieve `SBTFileMon.INI` path from registry.

#### Resolution
1. Navigate to `C:\ProgramData\Netwrix\Activity Monitor\Agent\SBTFileMon.ini`.
2. Under `[FILE_MONITOR1]`, change `STEALTHAUDIT=ON` to `STEALTHAUDIT=OFF`.
3. Save the file and re-initiate the FSAC System scan.

#### Reference Case
[Ticket ID: 500Qk00000PQdIiIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PQdIiIAL/view)

## Detailed Case Studies
### Case Study 1: Proxy Server Transition Issue
#### Initial Symptoms
- Bulk import failures during proxy server transition.
- Customer reported misaligned permissions.

#### Diagnostic Steps
1. Verified transition process and permissions.
2. Reviewed NetApp system configurations.

#### Key Information
- Proxy server permissions did not match documentation requirements.

#### Resolution
- Corrected permissions as per [Proxy Server Permissions Documentation](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Requirements/Solutions/FileSystem/ProxyModeServicePermissions.htm).

#### Key Takeaways
- Always verify permissions during proxy server transitions.
- Reference documentation to ensure compliance with requirements.

---

### Case Study 2: Registry Access Error During FSAC System Scan
#### Initial Symptoms
- FSAC System scan failed with "Requested registry access is not allowed."
- Error occurred while accessing `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SBTLogging\Parameters\ConfigPath`.

#### Diagnostic Steps
1. Investigated registry key permissions.
2. Reviewed `SBTFileMon.ini` configuration file.

#### Key Information
- Insufficient permissions for registry key access.
- Configuration file setting required adjustment.

#### Resolution
- Modified `SBTFileMon.ini` to disable StealthAUDIT (`STEALTHAUDIT=OFF`).
- Successfully completed FSAC System scan.

#### Key Takeaways
- Ensure registry key permissions are correctly configured.
- Monitor configuration file settings for potential conflicts.

## Best Practices & Tips
- **Permission Verification**: Always verify proxy server and registry key permissions during system transitions or configuration changes.
- **Documentation Reference**: Use official Netwrix documentation to ensure accurate configurations.
- **Configuration File Monitoring**: Regularly review files like `SBTFileMon.ini` for settings that may impact functionality.
- **Customer Communication**: Clearly explain resolution steps and preventive measures to customers.
- **Log Analysis**: Develop expertise in analyzing system logs for faster issue identification.

## Escalation Guidelines
### Criteria for Escalation
- Issues persist after following documented resolution steps.
- Errors indicate potential software defects or require development team intervention.
- Customer impact is high, such as prolonged auditing downtime.

### Escalation Procedure
1. Document all troubleshooting steps and findings.
2. Collect relevant logs, configuration files, and screenshots.
3. Submit a detailed escalation request to the appropriate team, including case history and diagnostic results.

End of Document.