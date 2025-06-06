# Netwrix Enterprise Auditor Knowledge Base Reference Guide  
## Component: StealthAUDIT for AzureAD  
### Feature: Credentials  

---

## Overview  
This guide addresses issues related to credential configuration and authentication errors when connecting to Azure Active Directory (Azure AD) using StealthAUDIT for AzureAD in Netwrix Enterprise Auditor. Proper credential setup is critical for ensuring seamless inventory scans and data collection from Azure AD environments. Misconfigurations can lead to access errors, impacting operational workflows and customer satisfaction.  

---

## Technical Background  
### Key Concepts  
- **Azure AD Inventory Scans**: StealthAUDIT for AzureAD performs inventory scans to collect data from Azure AD environments. These scans require proper authentication to access the directory.  
- **Authentication Methods**: Supported methods include Application (client) ID and Client Secret. Modern authentication with certificates is not supported for Azure AD Inventory scans.  
- **Credential Profiles**: Credential profiles in Netwrix Enterprise Auditor define the authentication parameters used to connect to external systems like Azure AD.  

### Terminology  
- **Application (client) ID**: A unique identifier for the application registered in Azure AD.  
- **Client Secret**: A password-like value used in conjunction with the Application ID for authentication.  
- **Connection URL**: The URL of the Azure AD tenant (e.g., `https://ALLSTATE365.ONMICROSOFT.COM`).  

---

## Issue Recognition & Triage  
### Symptoms  
- **Error Message**: "Access Denied" when attempting to connect to Azure AD Inventory scan.  
- **Environment**: Errors occur during authentication using Application ID and Client Secret.  

### Priority Assessment  
- **High Priority**: If the issue prevents inventory scans or data collection, it impacts operational workflows and must be resolved promptly.  

---

## Diagnostic Methodology  
### Systematic Approach  
1. **Verify Connection Parameters**: Confirm the connection URL and Application ID are correct.  
2. **Validate Credentials**: Ensure the Client Secret is accurate and up-to-date.  
3. **Check Authentication Method**: Confirm the credential profile is configured to use Application ID and Client Secret, not unsupported methods like certificates.  
4. **Review Configuration Settings**: Inspect the Azure AD connection settings in Netwrix Enterprise Auditor for discrepancies.  
5. **Test Connectivity**: Attempt a manual connection using PowerShell or other tools to validate the credentials outside the Netwrix platform.  

---

## Information Collection  
### Customer Queries  
- What is the connection URL being used?  
- What authentication method is configured in the credential profile?  
- Has the Client Secret been recently updated or expired?  

### Logs and Data to Collect  
- **Netwrix Logs**: Collect logs from the Netwrix Enterprise Auditor server to identify authentication errors.  
- **Azure AD Audit Logs**: Review Azure AD logs for failed authentication attempts.  
- **Credential Profile Configuration**: Export and review the credential profile settings.  

---

## Common Scenarios & Solutions  
### Scenario 1: Incorrect Authentication Method  
- **Symptoms**: "Access Denied" error when using modern authentication with a certificate.  
- **Resolution**: Reconfigure the credential profile to use Application ID and Client Secret.  

### Scenario 2: Expired Client Secret  
- **Symptoms**: Authentication fails despite correct Application ID and connection URL.  
- **Resolution**: Generate a new Client Secret in Azure AD and update the credential profile.  

### Scenario 3: Incorrect Connection URL  
- **Symptoms**: Authentication fails due to an invalid tenant URL.  
- **Resolution**: Verify the connection URL matches the Azure AD tenant domain.  

---

## Detailed Case Studies  
### Case Study: Ticket ID [500Qk00000FZqzJIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FZqzJIAT/view)  
#### Initial Symptoms  
The customer reported an "Access Denied" error when attempting to connect to Azure AD Inventory scan from server `Y0185-APP0443-S`.  

#### Diagnostic Steps  
1. Verified the connection URL and Application ID.  
2. Confirmed the credentials (Client Secret) were correct and up-to-date.  
3. Reviewed the credential profile configuration and identified the use of an unsupported authentication method (modern authentication with a certificate).  

#### Key Information Leading to Resolution  
The credential profile was incorrectly configured to use modern authentication with a certificate, which is not supported for Azure AD Inventory scans.  

#### Resolution  
Reconfigured the credential profile to use Application ID and Client Secret. Verified connectivity successfully.  

#### Key Takeaways  
- Always confirm the authentication method aligns with supported configurations.  
- Ensure credentials are validated before attempting connections.  

#### Efficiency Improvements  
- Implement pre-checks for credential profiles during initial setup to avoid unsupported configurations.  

---

## Best Practices & Tips  
1. **Credential Validation**: Always verify credentials (Application ID and Client Secret) before configuring connections.  
2. **Supported Authentication Methods**: Ensure credential profiles use only supported methods for Azure AD Inventory scans.  
3. **Regular Updates**: Periodically update Client Secrets to prevent expiration-related issues.  
4. **Pre-Deployment Testing**: Test connectivity using PowerShell or other tools before deploying configurations in Netwrix Enterprise Auditor.  
5. **Documentation**: Maintain detailed records of credential profiles and authentication settings for future reference.  

---

## Escalation Guidelines  
### Criteria for Escalation  
- Issue persists despite following diagnostic and resolution steps.  
- Authentication errors are caused by external factors (e.g., Azure AD tenant misconfigurations).  
- Logs indicate systemic issues within the Netwrix platform.  

### Escalation Procedure  
1. Collect all relevant logs and configuration details.  
2. Document the troubleshooting steps already performed.  
3. Escalate to the Netwrix development or product team with a detailed summary of findings.  

---  
End of Document  