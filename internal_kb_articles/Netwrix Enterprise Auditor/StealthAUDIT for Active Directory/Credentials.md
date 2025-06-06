# Netwrix Enterprise Auditor: Troubleshooting StealthAUDIT for Active Directory Credential Issues

## Overview
This guide focuses on troubleshooting credential-related issues in the StealthAUDIT for Active Directory component of Netwrix Enterprise Auditor (NEA). Credential issues can manifest as job failures, performance degradation, or authentication errors, often impacting critical functionality such as Active Directory scans, self-service features, and domain controller discovery. Understanding and resolving these issues is essential to maintaining the integrity and performance of the NEA environment.

## Technical Background
### Key Concepts
- **Active Directory Integration (ADI):** A core feature of StealthAUDIT that enables data collection and analysis from Active Directory environments.
- **Group Managed Service Accounts (gMSA):** Special accounts designed to provide automatic password management and simplified service account administration.
- **PrincipalsAllowedToRetrieveManagedPassword:** A property that defines which accounts or services can retrieve the password for a gMSA.
- **Replication Permissions:** Permissions such as "Replicating Directory Changes" and "Replicating Directory Changes All" are required for certain AD-related jobs.

### Common Terminology
- **Connection Profile:** Configuration settings that define how NEA connects to Active Directory or other data sources.
- **Discovery Query:** A job or query designed to identify and collect data from domain controllers or other AD objects.
- **Dynamic Accounts:** Temporary accounts created and deleted programmatically, often requiring special handling in inventory scans.

### System Context
Credential issues often arise due to misconfigurations, permission changes, or environmental factors such as password updates or domain policy changes. These issues can disrupt data collection, authentication, and job execution, necessitating a systematic approach to diagnosis and resolution.

## Issue Recognition & Triage
### Symptoms
- Job failures with errors such as `System.UnauthorizedAccessException` or "Access Denied."
- Prolonged scan times or incomplete data collection.
- Authentication errors, including Kerberos failures or account lockouts.
- Missing or incorrect data in inventory scans.

### Priority Assessment
- **High Priority:** Issues causing service disruptions, such as account lockouts or failed critical jobs.
- **Medium Priority:** Performance degradation or partial functionality loss.
- **Low Priority:** Non-critical errors or warnings that do not impact core functionality.

## Diagnostic Methodology
### Systematic Approach
1. **Reproduce the Issue:** Attempt to replicate the problem to confirm its scope and gather error details.
2. **Review Logs:** Examine job logs, event logs, and debug logs for error messages and timestamps.
3. **Verify Configuration:** Check connection profiles, credential formats, and job settings.
4. **Test Permissions:** Validate that the service account has the necessary permissions for the task.
5. **Engage Development Team:** If the issue persists, escalate with detailed logs and findings.

### Decision Points
- If the issue is related to gMSA, focus on the `PrincipalsAllowedToRetrieveManagedPassword` property.
- For job failures, verify credential formats and permissions.
- For performance issues, analyze scan configurations and environmental factors.

## Information Collection
### Questions to Ask Customers
- What specific error messages are being observed?
- When did the issue first occur, and were there any recent changes (e.g., upgrades, password updates)?
- What account is being used for the affected job or feature?
- Are there any related account lockouts or authentication failures?

### Logs and Data to Collect
- Job logs and debug logs from NEA.
- Event logs from affected domain controllers.
- PowerShell outputs for gMSA properties and permissions.
- Screenshots or exports of connection profile settings.

## Common Scenarios & Solutions
### Scenario 1: Self-Service Functionality Fails After Upgrade
- **Symptoms:** Self-service features stop working; scans take longer than expected.
- **Root Cause:** Improper configuration of ADI scans after an upgrade.
- **Solution:** Verify and reconfigure ADI scans to ensure proper functionality.
- **Reference Case:** [500Qk00000HbjZ4IAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HbjZ4IAJ/view)

### Scenario 2: gMSA Fails with "Access Denied"
- **Symptoms:** Job fails with `System.UnauthorizedAccessException` when using gMSA.
- **Root Cause:** Missing permissions in the `PrincipalsAllowedToRetrieveManagedPassword` property.
- **Solution:** Update the property using PowerShell to include all necessary accounts.
- **Reference Case:** [500Qk00000KAlAGIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KAlAGIA1/view)

### Scenario 3: Incorrect Credential Format Causes Job Failure
- **Symptoms:** Job fails with replication access denied errors.
- **Root Cause:** Incorrect credential format in the connection profile.
- **Solution:** Update the credential format to `DOMAINusername`.
- **Reference Case:** [500Qk00000KHJKTIA5](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KHJKTIA5/view)

### Scenario 4: Authentication Errors Due to Password Mismatch
- **Symptoms:** Kerberos login errors; service account authentication fails.
- **Root Cause:** Inconsistent password updates across the environment.
- **Solution:** Ensure the service account password is updated in all relevant locations.
- **Reference Case:** [500Qk00000MjNgbIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MjNgbIAF/view)

### Scenario 5: Account Lockouts During Host Discovery
- **Symptoms:** Service account locks out during domain controller discovery.
- **Root Cause:** Improper scoping of discovery queries.
- **Solution:** Scope discovery queries appropriately and delete problematic queries.
- **Reference Case:** [500Qk00000OOzyzIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OOzyzIAD/view)

### Scenario 6: Dynamic Accounts Not Marked as Deleted
- **Symptoms:** Dynamic accounts remain active in NEA despite being deleted in AD.
- **Root Cause:** "Collect only updates since the last scan" setting prevents full inventory.
- **Solution:** Deselect the setting and run a full inventory scan.
- **Reference Case:** [500Qk00000PdT74IAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PdT74IAF/view)

## Detailed Case Studies
### Case Study: [500Qk00000KAlAGIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KAlAGIA1/view)
- **Symptoms:** "AD_WeakPasswords" job fails with "Access Denied."
- **Diagnostic Steps:** Verified gMSA permissions, updated `PrincipalsAllowedToRetrieveManagedPassword` property.
- **Resolution:** Added required accounts to the property using PowerShell.
- **Key Takeaways:** Use security groups for easier management of permissions.

### Case Study: [500Qk00000KHJKTIA5](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KHJKTIA5/view)
- **Symptoms:** Replication access denied error due to incorrect credential format.
- **Diagnostic Steps:** Reviewed connection profile settings, identified incorrect format.
- **Resolution:** Updated credential format to `DOMAINusername`.
- **Key Takeaways:** Always verify credential formats in connection profiles.

## Best Practices & Tips
- **Credential Management:** Use security groups to manage permissions for gMSA accounts.
- **Configuration Verification:** Regularly review connection profiles and job settings after upgrades or policy changes.
- **Logging:** Enable DEBUG logging for detailed diagnostics during troubleshooting.
- **Documentation:** Maintain clear records of service account configurations and permissions.
- **Communication:** Proactively inform customers about potential impacts of upgrades or policy changes.

## Escalation Guidelines
- **When to Escalate:**
  - Issues persist after following standard troubleshooting steps.
  - Errors indicate potential bugs or require development team intervention.
  - Critical functionality is impacted, and immediate resolution is needed.
- **How to Escalate:**
  - Provide detailed logs, error messages, and configuration screenshots.
  - Summarize diagnostic steps already taken and their outcomes.
  - Clearly define the impact on the customer's environment.