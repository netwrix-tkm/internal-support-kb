# Knowledge Base Reference Guide: Troubleshooting SSL Certificate Installation Issues in Netwrix Enterprise Auditor

## Overview
This guide focuses on troubleshooting issues related to SSL certificate installation in Netwrix Enterprise Auditor, specifically within the Access Information Center component. These issues often stem from incorrect server configurations, which can prevent SSL certificates from being properly installed or updated. Understanding and resolving these problems is critical for ensuring secure communication and maintaining system functionality.

## Technical Background
### Key Concepts
- **Access Information Center**: A component of Netwrix Enterprise Auditor that provides self-service access to audit data and reports.
- **IIS (Internet Information Services)**: A web server used to host sites and services, including the StealthAudit site for Netwrix Enterprise Auditor.
- **SSL Certificates**: Digital certificates that enable secure communication over HTTPS by encrypting data between the server and client.
- **Ports**: Specific communication endpoints (e.g., port 8082 for published reports and port 481 for the Access Information Center).

### System Context
Netwrix Enterprise Auditor relies on IIS to host its web-based components. SSL certificates must be correctly configured within IIS to secure these components. Misconfigurations can lead to issues such as site invisibility in IIS or failed certificate installations.

## Issue Recognition & Triage
### Symptoms
- Inability to locate the StealthAudit site in IIS.
- Errors or failures during SSL certificate installation.
- Customer reports of insecure communication or inability to access web-based components.

### Priority Assessment
- **High Priority**: Issues affecting SSL certificate installation should be treated as urgent due to their impact on security and accessibility.
- **Low Priority**: Non-critical configuration errors that do not affect system functionality.

## Diagnostic Methodology
### Systematic Approach
1. **Verify IIS Configuration**: Check if the StealthAudit site is visible and properly configured in IIS.
2. **Review SSL Certificate Settings**: Confirm the certificate details and ensure it matches the intended configuration.
3. **Check Port Assignments**: Validate that the correct ports (e.g., 8082 and 481) are being used for the respective components.
4. **Analyze Logs**: Examine IIS logs and Netwrix Enterprise Auditor logs for errors or warnings related to SSL configuration.
5. **Engage Team Members**: Collaborate with colleagues for insights or precedents related to similar issues.

## Information Collection
### Customer Queries
- What error messages or symptoms are being observed?
- Has the SSL certificate been successfully installed on other servers?
- Are there any recent changes to the server configuration or IIS settings?

### Logs and Data
- IIS configuration files and logs.
- Netwrix Enterprise Auditor logs related to the Access Information Center.
- Screenshots or recordings of the issue (if available).

## Common Scenarios & Solutions
### Scenario 1: StealthAudit Site Not Visible in IIS
#### Cause
The site may not have been properly configured during installation or may have been inadvertently removed.

#### Resolution
- Reconfigure the StealthAudit site in IIS.
- Verify that the site is bound to the correct ports and SSL certificate.

---

### Scenario 2: Incorrect Port Configuration
#### Cause
SSL certificates may fail to install if the wrong ports are used for the Access Information Center or published reports.

#### Resolution
- Update the SSL certificate bindings for port 8082 (published reports) and port 481 (Access Information Center).
- Restart IIS to apply the changes.

---

### Scenario 3: Certificate Mismatch
#### Cause
The SSL certificate being installed does not match the server's configuration or hostname.

#### Resolution
- Ensure the certificate matches the server's hostname and intended use.
- Reinstall the certificate and verify its bindings in IIS.

## Detailed Case Studies
### Case Study: Ticket ID [500Qk00000GqBCiIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GqBCiIAN/view)
#### Initial Symptoms
The customer reported an inability to locate the StealthAudit site in IIS while attempting to install an SSL certificate.

#### Diagnostic Steps
1. Attempted to locate the StealthAudit site in IIS.
2. Reviewed the SSL certificate configuration and port bindings.
3. Scheduled a meeting with the customer, which was not attended.

#### Key Information Leading to Resolution
The issue was traced to incorrect port configurations for the Access Information Center and published reports.

#### Resolution
- Updated the SSL certificate bindings for port 8082 and port 481.
- Verified the configuration and confirmed successful installation.

#### Key Takeaways
- Always verify IIS site visibility and port configurations before attempting SSL certificate installations.
- Maintain clear communication with customers to ensure timely resolution.

#### Efficiency Improvements
- Develop a checklist for SSL certificate installations, including site visibility and port verification steps.

## Best Practices & Tips
- **Pre-Installation Checklist**: Create a standardized checklist for SSL certificate installations to ensure all prerequisites are met.
- **Port Verification**: Always confirm the correct ports are being used for the Access Information Center and published reports.
- **Collaborative Troubleshooting**: Engage team members early for insights and precedents related to similar issues.
- **Customer Communication**: Schedule meetings with customers and ensure attendance to avoid delays in resolution.
- **Documentation**: Maintain detailed records of configurations and changes for future reference.

## Escalation Guidelines
### Criteria for Escalation
- Issues that cannot be resolved after following the diagnostic methodology.
- Problems involving complex server configurations or third-party dependencies.
- Cases where customer communication is insufficient to gather necessary information.

### Escalation Procedure
1. Document all troubleshooting steps and findings.
2. Provide detailed logs and screenshots to the escalation team.
3. Notify the customer of the escalation and provide an estimated timeline for resolution.