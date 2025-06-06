# Knowledge Base Reference Guide: Server Access Errors in Netwrix Endpoint Protector

## Overview

Server Access Errors in Netwrix Endpoint Protector typically occur when users are unable to access the application’s UI or services due to misconfigurations, expired certificates, or network restrictions. These issues can disrupt critical operations, making it essential for support engineers to diagnose and resolve them efficiently. This guide provides a systematic approach to identifying, troubleshooting, and resolving such issues, ensuring minimal downtime and optimal customer satisfaction.

---

## Technical Background

### Key Concepts
- **SSL Certificates**: Secure Sockets Layer (SSL) certificates are used to establish encrypted connections between servers and clients. Expired or improperly configured certificates can block access to secure endpoints.
- **Port 443**: This port is the default for HTTPS traffic. If it is blocked or misconfigured in network rules, users cannot access the application’s UI.
- **Azure Network Rules**: Azure environments often use Network Security Groups (NSGs) to control inbound and outbound traffic. Misconfigured rules can inadvertently block required ports.

### System Context
Netwrix Endpoint Protector is often deployed in cloud environments like Azure. Access to the application relies on proper SSL certificate configuration and open network ports. Any disruption in these components can lead to server access errors.

---

## Issue Recognition & Triage

### Symptoms
- Users report being unable to access the Endpoint Protector UI.
- Error messages indicating SSL certificate issues or connection timeouts.
- Services appear operational, but the UI remains inaccessible.

### Priority Assessment
- **High Priority**: If the issue affects multiple users or critical business operations.
- **Medium Priority**: If the issue is isolated to a single user or non-critical environment.

---

## Diagnostic Methodology

1. **Initial Assessment**:
   - Confirm the reported symptoms with the customer.
   - Verify if the issue is reproducible.

2. **Certificate Validation**:
   - Check if the SSL certificate is expired or improperly configured.
   - Validate the certificate chain using tools like OpenSSL or browser inspection.

3. **Network Configuration**:
   - Verify that port 443 is open and allowed in the Azure Network Security Group (NSG) rules.
   - Check for any recent changes to network configurations.

4. **Service Health**:
   - Ensure all required services are running on the server.
   - Check server logs for errors related to SSL or network connectivity.

5. **Environment-Specific Checks**:
   - If hosted on Azure, confirm that the VM is accessible via SSH or RDP for further troubleshooting.

---

## Information Collection

### Questions to Ask the Customer
- When did the issue start, and were there any recent changes (e.g., certificate updates, network changes)?
- Is the issue affecting all users or specific ones?
- What error messages are displayed when attempting to access the UI?

### Data to Collect
- SSL certificate details (expiration date, issuer, etc.).
- Azure NSG configuration (inbound and outbound rules).
- Server logs (e.g., IIS logs, application logs).
- Screenshots or error messages from the customer.

---

## Common Scenarios & Solutions

### Scenario 1: Expired SSL Certificate
- **Symptoms**: Users see a browser warning about an expired certificate.
- **Resolution**:
  1. Replace the expired SSL certificate with a valid one.
  2. Restart the web server to apply the changes.

### Scenario 2: Port 443 Blocked in Azure NSG
- **Symptoms**: Connection timeouts when accessing the UI.
- **Resolution**:
  1. Add an inbound rule in the Azure NSG to allow traffic on port 443.
  2. Verify connectivity using tools like `telnet` or `curl`.

### Scenario 3: Misconfigured Certificate Chain
- **Symptoms**: SSL errors despite a valid certificate.
- **Resolution**:
  1. Verify the certificate chain and ensure all intermediate certificates are installed.
  2. Test the configuration using SSL validation tools.

---

## Detailed Case Studies

### Case Study 1: Port 443 Blocked in Azure NSG
- **Ticket ID**: [500Qk00000INm6PIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000INm6PIAT/view)
- **Initial Symptoms**: Customer reported inability to access the Endpoint Site after updating an expired SSL certificate.
- **Diagnostic Steps**:
  1. Verified that the SSL certificate was replaced correctly.
  2. Checked Azure NSG rules and identified that port 443 was not allowed.
  3. Confirmed that all services were operational on the server.
- **Resolution**:
  1. Added port 443 to the Azure NSG inbound rules.
  2. Replaced the expired SSL certificate.
  3. Verified that the UI was accessible and functioning.
- **Key Takeaways**:
  - Always verify network rules when diagnosing access issues.
  - Proactively monitor SSL certificate expiration dates to prevent downtime.
- **Efficiency Improvements**:
  - Develop a checklist for SSL certificate updates, including network rule verification.

---

## Best Practices & Tips

1. **Proactive Monitoring**:
   - Use monitoring tools to track SSL certificate expiration dates.
   - Regularly audit Azure NSG rules to ensure required ports are open.

2. **Standardized Procedures**:
   - Create a step-by-step guide for replacing SSL certificates, including post-update validation.
   - Maintain a template for collecting customer information during initial triage.

3. **Communication**:
   - Clearly explain the root cause and resolution steps to the customer.
   - Provide guidance on preventing similar issues in the future.

4. **Documentation**:
   - Document all changes made during troubleshooting for future reference.
   - Update internal knowledge base articles with lessons learned from resolved cases.

---

## Escalation Guidelines

### When to Escalate
- The issue persists despite following all diagnostic and resolution steps.
- The root cause involves complex Azure configurations or third-party integrations.
- The customer requests escalation due to business impact.

### How to Escalate
1. Gather all relevant information, including logs, screenshots, and configuration details.
2. Document the steps already taken and their outcomes.
3. Escalate to the appropriate team or senior engineer with a detailed summary of the case.

--- 

This guide serves as a comprehensive reference for diagnosing and resolving server access errors in Netwrix Endpoint Protector. By following the outlined methodologies and best practices, support engineers can address these issues effectively and consistently.