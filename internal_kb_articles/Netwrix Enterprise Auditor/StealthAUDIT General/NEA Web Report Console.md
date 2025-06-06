# Comprehensive Knowledge Base Guide: Troubleshooting NEA Web Report Console Issues

## Overview

The **NEA Web Report Console** is a critical component of the Netwrix Enterprise Auditor (NEA) platform, enabling users to access, publish, and manage reports securely. This guide provides a systematic approach to diagnosing and resolving issues related to the NEA Web Report Console, including Single Sign-On (SSO), SSL certificate management, report generation, and web server configuration. Understanding and addressing these issues is essential to maintaining uninterrupted access to reporting functionality, ensuring compliance, and supporting business operations.

---

## Technical Background

### Key Concepts
- **NEA Web Report Console**: A web-based interface for accessing published reports and managing reporting configurations.
- **Service Principal Name (SPN)**: Used for Kerberos authentication in SSO configurations.
- **SSL Certificates**: Ensure secure communication between the web server and clients.
- **Binding URLs**: Configuration settings that define how the web server listens for incoming connections.
- **Roles and Permissions**: Access to reports is controlled via roles such as "Report Viewer" in NEA settings.
- **Microsoft HTTP API**: Starting from version 11.6, NEA uses Microsoft HTTP API instead of IIS for servicing web requests.

### Common Components
- **Web Server Service**: Handles requests to the NEA Web Report Console.
- **Access Information Center (AIC)**: Provides additional reporting and access management capabilities.
- **Configuration Files**: Key files such as `WebServer.exe.config` and `AccessInformationCenter.service.exe.config` control web server behavior.

---

## Issue Recognition & Triage

### Symptoms
- **Access Issues**: Users unable to log in, receiving 500/503 errors, or being prompted for credentials repeatedly.
- **SSL Errors**: Warnings about expired or misconfigured certificates.
- **Report Generation Failures**: Errors during report export or incomplete data in reports.
- **Port Conflicts**: Web server not listening on the expected port.
- **Configuration Errors**: Incorrect binding URLs, SPN misconfigurations, or missing roles.

### Priority Assessment
- **High Priority**: Issues affecting multiple users, critical reports, or compliance deadlines.
- **Medium Priority**: Single-user access issues or non-critical report errors.
- **Low Priority**: Configuration inquiries or cosmetic issues.

---

## Diagnostic Methodology

### Systematic Approach
1. **Verify Symptoms**: Confirm the issue by replicating the reported behavior.
2. **Check Service Status**: Ensure the NEA Web Server service is running.
3. **Review Logs**: Examine logs in `%SAInstallDir%SADatabaseLogsApplication` or `%SAInstallDir%Web`.
4. **Validate Configuration**: Inspect configuration files for errors or inconsistencies.
5. **Test Connectivity**: Use `netstat` to check if the expected ports are listening.
6. **Check Permissions**: Verify service account roles and database access.
7. **Reproduce in Test Environment**: If possible, replicate the issue in a controlled environment.

---

## Information Collection

### Customer Questions
- What is the exact error message or behavior observed?
- When did the issue start, and were there any recent changes (e.g., updates, migrations)?
- What is the affected NEA version and build number?
- Are all users affected, or only specific accounts?
- What troubleshooting steps have already been attempted?

### Logs and Data to Collect
- **Service Logs**: `%SAInstallDir%SADatabaseLogsApplication`
- **Configuration Files**: `WebServer.exe.config`, `AccessInformationCenter.service.exe.config`
- **SSL Certificate Details**: Thumbprints, expiration dates, and bindings.
- **Network Information**: Output of `netstat -aob` and firewall rules.
- **Screenshots**: Error messages or configuration settings.

---

## Common Scenarios & Solutions

### Scenario 1: SSO Prompts for Credentials
- **Root Cause**: SPN misconfiguration or incorrect service account permissions.
- **Solution**:
  1. Run `Setspn –S HTTP/[FQDN] [domain][servername]$` to register the SPN.
  2. Restart the NEA Web Server service.
  3. Verify service account permissions in Active Directory.

### Scenario 2: SSL Certificate Errors
- **Root Cause**: Expired or improperly bound SSL certificates.
- **Solution**:
  1. Use `netsh http show sslcert` to verify bindings.
  2. Re-bind the certificate using:
     ```bash
     netsh http add sslcert ipport=0.0.0.0:[port] appid={GUID} certhash={Thumbprint}
     ```
  3. Restart the NEA Web Server service.

### Scenario 3: 500/503 Errors on Login
- **Root Cause**: Missing roles or incorrect service account configuration.
- **Solution**:
  1. Assign the "Report Viewer" role to the affected user in NEA > Settings > Access.
  2. Ensure the service account has database access and is part of the "Pre-Windows 2000 Compatible Access" group.

### Scenario 4: Reports Not Updating After Migration
- **Root Cause**: DNS misconfiguration or incorrect certificate bindings.
- **Solution**:
  1. Update DNS settings to point to the correct server.
  2. Re-bind the SSL certificate and restart the web server.

### Scenario 5: Port Not Listening
- **Root Cause**: Port conflict or incorrect binding URL.
- **Solution**:
  1. Check for conflicts using `netstat -aob`.
  2. Update the `BindingURL` parameter in `WebServer.exe.config` to use an available port.

---

## Detailed Case Studies

### Case Study 1: SSO Configuration Issue
- **Ticket ID**: [500Qk00000BpV1pIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BpV1pIAF/view)
- **Symptoms**: Users prompted for credentials repeatedly.
- **Diagnostic Steps**:
  1. Verified SPN configuration using `Setspn`.
  2. Checked service account permissions.
- **Resolution**: Registered SPN and restarted the web server service.
- **Key Takeaways**: Always verify SPN and service account permissions during SSO setup.

### Case Study 2: SSL Certificate Binding Issue
- **Ticket ID**: [500Qk00000FvRdyIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FvRdyIAF/view)
- **Symptoms**: WebUI not responding after certificate update.
- **Diagnostic Steps**:
  1. Verified SSL bindings using `netsh`.
  2. Re-bound the certificate to the correct port.
- **Resolution**: Corrected SSL bindings and restarted the service.
- **Key Takeaways**: Regularly monitor certificate expiration and bindings.

### Case Study 3: Report Export Limitations
- **Ticket ID**: [500Qk00000GWZJEIA5](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GWZJEIA5/view)
- **Symptoms**: CSV export limited to 1000 rows.
- **Diagnostic Steps**:
  1. Reviewed export settings in the NEA Web Console.
  2. Adjusted settings to export all rows and columns.
- **Resolution**: Updated export settings to remove row limitations.
- **Key Takeaways**: Check export configurations for large datasets.

---

## Best Practices & Tips

1. **SPN Configuration**: Always verify SPN settings during SSO setup to avoid authentication issues.
2. **SSL Certificate Management**: Monitor expiration dates and ensure proper bindings to avoid service interruptions.
3. **Service Account Permissions**: Assign appropriate roles and group memberships to service accounts.
4. **Configuration Backups**: Regularly back up configuration files before making changes.
5. **Port Management**: Use `netstat` to identify conflicts and ensure ports are available.
6. **Documentation**: Maintain detailed records of configuration changes for future reference.

---

## Escalation Guidelines

### When to Escalate
- Issues persist after following standard troubleshooting steps.
- Errors indicate potential bugs or require development team intervention.
- Customer impact is critical, such as compliance deadlines or widespread outages.

### How to Escalate
1. Collect all relevant logs, screenshots, and configuration files.
2. Document all troubleshooting steps taken.
3. Submit a detailed escalation request to the appropriate team, including customer impact and urgency.

--- 

This guide serves as a comprehensive reference for diagnosing and resolving issues related to the NEA Web Report Console, ensuring consistent and effective support for customers.