# Comprehensive Knowledge Base Reference Guide: PingCastle General Issues

## Overview
This guide covers troubleshooting and resolution strategies for issues related to PingCastle General under the PC Standard component. PingCastle is a security auditing tool for Active Directory environments, and understanding its functionality and common issues is critical for ensuring accurate scans, resolving errors, and maintaining customer satisfaction. This document provides a systematic approach to diagnosing and resolving issues, along with real-world case studies and best practices.

---

## Technical Background
### Key Concepts
- **PingCastle**: A tool designed to audit Active Directory environments for security risks and vulnerabilities.
- **Collector Code**: Refers to the specific configuration used for data collection during scans.
- **Health Check Rules**: Predefined checks that PingCastle performs to identify risks in Active Directory environments.
- **License Management**: PingCastle requires valid licenses for full functionality, including health checks and advanced features.
- **Azure AD Scanning**: PingCastle supports scanning Azure Active Directory environments, but requires specific permissions and configurations.

### Terminology
- **SYSVOL and NETLOGON**: Shared folders used by Active Directory for Group Policy and logon scripts.
- **Hardened UNC Paths**: Security settings that enforce mutual authentication and integrity for SYSVOL and NETLOGON shares.
- **LastLogon vs. LastLogonTimestamp**: Attributes in Active Directory that track user logon activity. `LastLogon` is not replicated, while `LastLogonTimestamp` is replicated every 14 days.
- **Graph API**: The modern API for Azure AD, replacing older APIs like MSOnline and AzureAD.

---

## Issue Recognition & Triage
### Symptoms
- Errors during scans (e.g., timeout, missing data, false positives).
- Licensing issues (e.g., invalid or unrecognized licenses).
- Problems with Azure AD scans (e.g., incomplete data or permissions errors).
- Configuration issues (e.g., Hardened UNC Paths, LDAP signing).
- Portal access problems (e.g., missing licenses or download errors).

### Priority Assessment
- **High Priority**: Issues affecting production environments, security vulnerabilities, or critical scans.
- **Medium Priority**: Errors in non-production environments or minor functionality issues.
- **Low Priority**: Documentation requests or inquiries about features.

---

## Diagnostic Methodology
### Systematic Approach
1. **Verify Environment Details**: Confirm the PingCastle version, platform, and configuration.
2. **Reproduce the Issue**: Attempt to replicate the problem using the customer's setup or a lab environment.
3. **Analyze Logs**: Use trace logs (`--log` switch) to identify errors or anomalies.
4. **Check Configuration**: Review settings like licenses, permissions, and Group Policy configurations.
5. **Consult Documentation**: Refer to PingCastle manuals, GitHub repositories, and community forums.
6. **Test Solutions**: Apply potential fixes and verify their effectiveness.

---

## Information Collection
### Customer Questions
- What version of PingCastle are you using?
- Are you scanning Active Directory or Azure AD?
- Have there been recent changes to your environment (e.g., updates, policy changes)?
- Are you encountering specific error messages? If so, provide screenshots or logs.

### Logs and Data to Collect
- **Trace Logs**: Generated using the `--log` switch.
- **Configuration Files**: `PingCastle.exe.config` or `web.config`.
- **Screenshots**: Error messages or portal issues.
- **Reports**: XML or HTML output from scans.

---

## Common Scenarios & Solutions
### Scenario 1: Licensing Issues
#### Symptoms
- License not recognized or software running in free edition.
#### Resolution
- Verify the license key in the configuration file.
- Test the license in a lab environment.
- If invalid, request a new license from the licensing team.

### Scenario 2: Azure AD Scanning Problems
#### Symptoms
- Incomplete data or missing rules during scans.
#### Resolution
- Assign necessary permissions (`Directory.Read.All`, `Security.Read.All`).
- Download Azure AD rules separately from the PingCastle repository.
- Monitor updates for migration to the Graph API.

### Scenario 3: Hardened UNC Paths Configuration
#### Symptoms
- Security risks flagged for SYSVOL and NETLOGON shares.
#### Resolution
- Apply the following Group Policy settings:
  ```
  SYSVOL  RequireMutualAuthentication=1, RequireIntegrity=1
  NETLOGON  RequireMutualAuthentication=1, RequireIntegrity=1
  ```
- Execute `gpupdate /force` and verify access controls.

### Scenario 4: Portal Access Issues
#### Symptoms
- Missing licenses or download functionality in the Netwrix portal.
#### Resolution
- Verify account association in Salesforce.
- Ensure users have active Netwrix accounts.
- Escalate to the web team for portal fixes.

---

## Detailed Case Studies
### Case Study 1: Licensing Issue
#### Ticket ID: [500Qk00000NAndMIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NAndMIAT/view)
- **Symptoms**: PingCastle running in free edition despite applying a license.
- **Diagnostic Steps**: Verified configuration file, tested license in lab environment.
- **Resolution**: Issued a new license key, confirmed functionality.
- **Key Takeaways**: Always test licenses in a controlled environment before escalation.

### Case Study 2: Azure AD Scanning
#### Ticket ID: [500Qk00000NeL6wIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NeL6wIAF/view)
- **Symptoms**: No data returned during Azure AD scans.
- **Diagnostic Steps**: Verified permissions, reviewed deprecated APIs.
- **Resolution**: Advised customer to monitor updates for Graph API migration.
- **Key Takeaways**: Ensure permissions align with the latest API requirements.

### Case Study 3: Hardened UNC Paths
#### Ticket ID: [500Qk00000MHjIeIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MHjIeIAL/view)
- **Symptoms**: Security risks flagged for SYSVOL and NETLOGON shares.
- **Diagnostic Steps**: Reviewed Group Policy settings, applied recommended configurations.
- **Resolution**: Enforced Hardened UNC Paths policy, verified access controls.
- **Key Takeaways**: Regularly review Group Policy settings for security compliance.

### Case Study 4: Portal Access Issue
#### Ticket ID: [500Qk00000O1JvfIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O1JvfIAF/view)
- **Symptoms**: Missing licenses in the Netwrix portal.
- **Diagnostic Steps**: Checked account association in Salesforce.
- **Resolution**: Linked account to company, restored portal access.
- **Key Takeaways**: Verify account associations during portal-related issues.

---

## Best Practices & Tips
- **License Management**: Always verify licenses in the configuration file and test them in a lab environment.
- **Azure AD Scanning**: Assign permissions carefully and monitor updates for API migrations.
- **Group Policy Settings**: Regularly review and enforce security configurations like Hardened UNC Paths.
- **Portal Access**: Ensure all users have active Netwrix accounts and verify account associations.
- **Documentation**: Maintain links to relevant resources, including GitHub repositories and community forums.

---

## Escalation Guidelines
### Criteria for Escalation
- Issues affecting production environments or critical scans.
- Problems requiring intervention from the licensing or web teams.
- Errors related to deprecated APIs or unsupported configurations.

### Escalation Procedure
1. Gather all relevant logs, screenshots, and configuration files.
2. Document troubleshooting steps taken and results.
3. Submit a detailed escalation request to the appropriate team (e.g., licensing, web, development).
4. Follow up regularly to ensure timely resolution.

--- 

End of Document.