# Netwrix Enterprise Auditor: Troubleshooting SharePoint Online Permissions and Credential Issues

## Overview

This guide provides a comprehensive reference for troubleshooting issues related to SharePoint Online permissions and credential configurations in Netwrix Enterprise Auditor (NEA). These issues often arise during migrations, updates, or misconfigurations and can impact the ability to generate accurate permissions reports or execute scans. Understanding and resolving these problems is critical to maintaining accurate auditing and compliance reporting.

## Technical Background

### Key Concepts
- **Netwrix Enterprise Auditor (NEA):** A platform for auditing IT infrastructure, including SharePoint Online, to ensure security and compliance.
- **SharePoint Online Permissions Job:** A job in NEA that collects permissions data from SharePoint Online sites.
- **Azure App Registration:** A mechanism to authenticate NEA with SharePoint Online using either certificates or app secrets.
- **Microsoft Graph API:** Used by NEA to interact with SharePoint Online for data collection.
- **Resource Contention:** Overlapping jobs or misconfigured schedules can lead to resource contention, causing incomplete scans or failures.

### Terminology
- **Zero-Level Job:** A baseline scan that collects minimal data to verify connectivity and configuration.
- **App Secret vs. Certificate:** NEA requires certificates for authentication with Azure services, not app secrets.
- **SPAC_SystemScans Profile:** A configuration profile in NEA for managing SharePoint Online scans.

### System Context
NEA interacts with SharePoint Online through Azure App Registrations, leveraging Microsoft Graph API permissions. Proper configuration of credentials, permissions, and job schedules is essential for successful data collection.

## Issue Recognition & Triage

### Symptoms
- Incomplete permissions reports (e.g., missing subdirectories).
- Scan failures with connection errors.
- Errors after migrations or updates.

### Priority Assessment
- **High Priority:** Scans fail entirely, impacting compliance reporting.
- **Medium Priority:** Partial data collection, such as missing subdirectories.
- **Low Priority:** Non-critical warnings or errors that do not affect data integrity.

## Diagnostic Methodology

1. **Verify Configuration:**
   - Check Azure App Registration settings (certificate, permissions).
   - Confirm job schedules to avoid overlapping.

2. **Test Connectivity:**
   - Run a Zero-Level Job to validate the connection.

3. **Review Logs:**
   - Examine NEA logs for errors related to SharePoint Online jobs.

4. **Reproduce the Issue:**
   - Attempt to replicate the problem in a controlled environment.

5. **Isolate Variables:**
   - Test individual components (e.g., Azure App, Microsoft Graph API).

## Information Collection

### Customer Questions
- When did the issue start?
- Were there any recent migrations, updates, or configuration changes?
- Are all SharePoint Online sites affected or only specific ones?

### Data to Collect
- NEA logs (e.g., `Netwrix_Auditor.log`).
- Azure App Registration details (permissions, certificates).
- Job configuration settings in NEA.
- Screenshots of errors or incomplete reports.

## Common Scenarios & Solutions

### Scenario 1: Incomplete Permissions Reports After Migration
- **Symptoms:** Missing subdirectories in reports.
- **Root Cause:** Misconfigured SharePoint Online permissions job and overlapping schedules.
- **Resolution:**
  1. Correct job configuration settings.
  2. Schedule jobs sequentially to avoid resource contention.
  3. Test with a Zero-Level Job to confirm resolution.

### Scenario 2: Scan Failures Due to Expired App Secret
- **Symptoms:** Connection errors after updating the app secret.
- **Root Cause:** NEA requires certificates, not app secrets, for authentication.
- **Resolution:**
  1. Replace the app secret with a valid certificate.
  2. Update the connection string in NEA.
  3. Test connectivity using Microsoft Graph API.

## Detailed Case Studies

### Case Study 1: Incomplete Permissions Reports After Migration
- **Ticket ID:** [500Qk00000JsatDIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JsatDIAR/view)
- **Initial Symptoms:** Missing subdirectories in permissions reports after migrating user home directories to OneDrive.
- **Diagnostic Steps:**
  1. Identified overlapping jobs causing resource contention.
  2. Corrected SharePoint Online permissions job configuration.
  3. Tested with a Zero-Level Job.
- **Resolution:** Adjusted job schedules and configurations. Verified successful scans.
- **Key Takeaways:**
  - Always verify job configurations after migrations.
  - Avoid overlapping job schedules to prevent resource contention.

### Case Study 2: Scan Failures Due to Expired App Secret
- **Ticket ID:** [500Qk00000NXaAlIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NXaAlIAL/view)
- **Initial Symptoms:** Connection failure after updating the app secret.
- **Diagnostic Steps:**
  1. Renewed the app secret and updated it in NEA.
  2. Replaced the app secret with a certificate.
  3. Verified Microsoft Graph API permissions.
- **Resolution:** Configured NEA to use certificates for authentication. Tested and confirmed successful scans.
- **Key Takeaways:**
  - NEA requires certificates, not app secrets, for Azure authentication.
  - Ensure proper Microsoft Graph API permissions are assigned.

## Best Practices & Tips

1. **Configuration Management:**
   - Document all changes to Azure App Registrations and NEA job settings.
   - Use certificates for authentication with Azure services.

2. **Job Scheduling:**
   - Avoid overlapping jobs to prevent resource contention.
   - Stagger job schedules for optimal performance.

3. **Testing & Validation:**
   - Run Zero-Level Jobs after configuration changes to validate connectivity.
   - Test Microsoft Graph API permissions independently.

4. **Proactive Monitoring:**
   - Regularly review NEA logs for warnings or errors.
   - Monitor certificate expiration dates and renew them proactively.

5. **Customer Communication:**
   - Clearly explain the root cause and resolution steps.
   - Provide documentation for recurring tasks, such as renewing certificates.

## Escalation Guidelines

### When to Escalate
- Persistent scan failures despite following troubleshooting steps.
- Issues involving unsupported configurations or third-party dependencies.
- Critical impact on compliance reporting with no immediate resolution.

### How to Escalate
- Collect all relevant logs, screenshots, and configuration details.
- Document steps already taken and their outcomes.
- Escalate to the Netwrix development or product team with a detailed summary.

