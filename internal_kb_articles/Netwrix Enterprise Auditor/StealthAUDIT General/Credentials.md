# Comprehensive Knowledge Base Guide: Troubleshooting Credential Issues in Netwrix Enterprise Auditor (StealthAUDIT General)

## Overview

Credential-related issues in Netwrix Enterprise Auditor (NEA) and its StealthAUDIT component are critical to address as they directly impact the functionality of scheduled tasks, authentication, and integration with external systems. These issues often arise due to misconfigurations, password changes, or insufficient permissions. This guide provides a systematic approach to diagnosing and resolving credential-related problems, ensuring minimal downtime and maintaining system integrity.

---

## Technical Background

### Key Concepts
- **Service Accounts**: Accounts used by NEA and StealthAUDIT to perform scheduled tasks, access databases, and integrate with external systems.
- **Connection Profiles**: Configuration settings in NEA that store credentials for accessing monitored systems and services.
- **Password Vault Integration**: Integration with tools like CyberArk or BeyondTrust for secure credential management.
- **Group Managed Service Accounts (gMSA)**: A secure method for managing service account credentials in Active Directory environments.
- **Authentication Methods**: NEA supports NTLM and Kerberos authentication, with Kerberos being the preferred method for security.

### Common Credential Storage Locations
1. **Global Settings**:
   - Connection Profiles
   - Notification Settings (Mail Server)
   - Schedule
   - Storage Authentication
2. **System Services**:
   - NEA Web Server
   - Access Information Center (AIC)
   - Vault
3. **Activity Monitor**:
   - Agent Settings
   - Monitored Hosts
4. **External Integrations**:
   - CyberArk or other password vaults
   - ServiceNow (if enabled)

---

## Issue Recognition & Triage

### Symptoms of Credential Issues
- Scheduled jobs fail to run or return authentication errors.
- Users are unable to log into the NEA console or Access Information Center.
- Integration with external systems (e.g., CyberArk, ServiceNow) fails.
- Account lockouts or repeated failed login attempts.
- Errors such as "Default storage profile is missing" or "Invalid credentials."

### Priority Assessment
- **High Priority**: Issues causing system-wide failures, such as all scheduled jobs failing or inability to access the NEA console.
- **Medium Priority**: Problems affecting specific integrations or isolated tasks.
- **Low Priority**: Non-critical errors, such as warnings in logs without immediate impact.

---

## Diagnostic Methodology

1. **Verify Symptoms**:
   - Confirm the reported issue (e.g., job failures, login errors).
   - Check if the issue is reproducible.

2. **Identify Scope**:
   - Determine if the issue affects all users, specific accounts, or particular tasks.

3. **Review Configuration**:
   - Inspect Connection Profiles, scheduled tasks, and service configurations for incorrect or outdated credentials.

4. **Check Logs**:
   - Collect logs from NEA, Windows Event Viewer, and external systems (e.g., CyberArk).

5. **Test Credentials**:
   - Manually test the credentials in the affected configuration to confirm validity.

6. **Isolate Changes**:
   - Identify recent changes, such as password updates, migrations, or upgrades.

---

## Information Collection

### Questions to Ask Customers
- What specific error messages are you encountering?
- Have there been any recent password changes or system updates?
- Which accounts are affected, and where are they used?
- Are you using a password vault (e.g., CyberArk)? If so, which version?
- Can you provide screenshots or logs of the issue?

### Logs to Collect
- **NEA Logs**: Located in the installation directory.
- **Windows Event Logs**: Security and Application logs.
- **CyberArk Logs** (if applicable): For integration-related issues.
- **SPProfiles.xml**: For storage profile configurations.

---

## Common Scenarios & Solutions

### Scenario 1: Password Rotation Issues
- **Symptoms**: Scheduled jobs fail after a password change.
- **Resolution**:
  1. Update the password in all relevant locations:
     - Connection Profiles
     - Notification Settings
     - Schedule
     - Storage Authentication
     - System Services
  2. Verify that the updated credentials are correct.
  3. Test scheduled jobs to confirm functionality.

### Scenario 2: Account Lockouts
- **Symptoms**: Service accounts repeatedly lock out.
- **Resolution**:
  1. Use auditing tools (e.g., NTP) to track failed login attempts.
  2. Identify and update all instances where the account is used.
  3. Ensure the account is not being used by unauthorized systems.

### Scenario 3: Integration Failures with CyberArk
- **Symptoms**: NEA fails to retrieve credentials from CyberArk.
- **Resolution**:
  1. Verify the AppID and Folder values in the configuration files.
  2. Ensure the CyberArk integration is correctly configured.
  3. Test credential retrieval manually.

### Scenario 4: Missing Storage Profile
- **Symptoms**: "Default storage profile is missing" error.
- **Resolution**:
  1. Reinstall NEA and reboot the server.
  2. Verify SQL permissions for the service account.
  3. Check the `SPProfiles.xml` file for corruption.

---

## Detailed Case Studies

### Case Study 1: Password Rotation Across Multiple Locations
- **Ticket**: [500Qk00000Ez15gIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ez15gIAB/view)
- **Symptoms**: Customer needed guidance on updating a service account password.
- **Key Steps**:
  1. Provided a comprehensive list of locations for password updates.
  2. Verified updates in Connection Profiles, System Services, and Activity Monitor.
- **Resolution**: Customer successfully updated the password in all locations.
- **Takeaway**: Maintain a checklist of all credential storage locations.

### Case Study 2: CyberArk Integration Failure
- **Ticket**: [500Qk00000H4shZIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000H4shZIAR/view)
- **Symptoms**: Credentials could not be retrieved from CyberArk after an upgrade.
- **Key Steps**:
  1. Updated the `StealthAUDITGlobalOptions.xml` file with the correct AppID.
  2. Restored the Folder value in the Credential Profile.
- **Resolution**: Credentials were successfully retrieved, and scans resumed.
- **Takeaway**: Always verify configuration files after upgrades.

### Case Study 3: Account Lockout Investigation
- **Ticket**: [500Qk00000KSj5EIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KSj5EIAT/view)
- **Symptoms**: A domain account repeatedly locked out.
- **Key Steps**:
  1. Monitored failed login attempts using NTP.
  2. Isolated the issue to an external system using the account.
- **Resolution**: Customer resolved the issue after identifying the source.
- **Takeaway**: Use auditing tools to track account activity.

---

## Best Practices & Tips

1. **Maintain Documentation**:
   - Keep a detailed record of all credential storage locations and update procedures.

2. **Use Password Vaults**:
   - Integrate with tools like CyberArk for secure and automated credential management.

3. **Plan Password Changes**:
   - Schedule password updates during maintenance windows to minimize disruptions.

4. **Enable Auditing**:
   - Use tools like NTP to monitor failed login attempts and account activity.

5. **Test After Changes**:
   - Verify functionality of scheduled jobs and integrations after updating credentials.

---

## Escalation Guidelines

### When to Escalate
- The issue persists despite following standard troubleshooting steps.
- Errors indicate potential bugs or undocumented behavior.
- Integration with third-party systems fails due to compatibility issues.

### How to Escalate
1. Collect all relevant logs and configuration files.
2. Document the troubleshooting steps already taken.
3. Submit a detailed escalation request to the R&D or product management team.

--- 

This guide serves as a comprehensive reference for diagnosing and resolving credential-related issues in Netwrix Enterprise Auditor. By following the outlined methodologies and leveraging the case studies, support engineers can efficiently address these problems and ensure system reliability.