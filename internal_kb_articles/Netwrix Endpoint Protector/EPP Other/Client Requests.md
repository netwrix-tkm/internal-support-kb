# Comprehensive Knowledge Base Guide: Handling "Client Requests" for Netwrix Endpoint Protector (EPP Other)

## Overview

This guide provides a systematic approach to handling "Client Requests" for the Netwrix Endpoint Protector (EPP Other) component. These requests often involve inquiries about product features, installation files, configuration assistance, troubleshooting, and compliance-related issues. Understanding and resolving these requests efficiently is critical to maintaining customer satisfaction and ensuring the proper functionality of the Endpoint Protector system.

---

## Technical Background

### Key Concepts
- **Netwrix Endpoint Protector (EPP):** A Data Loss Prevention (DLP) solution designed to protect sensitive data across endpoints, networks, and storage.
- **Components:** Includes features like Content Aware Protection (CAP), Deep Packet Inspection (DPI), and device control.
- **Client Requests:** Typically involve feature inquiries, installation assistance, configuration changes, or troubleshooting specific issues.

### Terminology
- **DPI (Deep Packet Inspection):** A feature that analyzes network traffic for security purposes.
- **CAP (Content Aware Protection):** Monitors and controls sensitive data transfers.
- **Offline Agents:** Installation files for environments without internet access.
- **Audit Logs:** Records of system activities for compliance and troubleshooting.
- **Regex Patterns:** Used for identifying sensitive data in compliance with regulations like LGPD.

### System Context
- **Hosting Environments:** EPP can be deployed on-premises or in cloud environments (AWS, Azure, etc.).
- **Supported Platforms:** Includes various Linux distributions (e.g., Ubuntu, RHEL), Windows, and macOS.
- **Policy Management:** Policies control data access, encryption, and device usage.

---

## Issue Recognition & Triage

### Common Symptoms
- Requests for installation files or offline agents.
- Inquiries about feature compatibility or compliance (e.g., DPDP Act, LGPD).
- Issues with policy creation, role management, or configuration.
- Troubleshooting errors (e.g., "500 Internal Server Error," uninstallation issues).
- Requests for backend access or migration assistance.

### Priority Assessment
- **High Priority:** Issues affecting system functionality (e.g., inability to log in, policy creation errors).
- **Medium Priority:** Requests for installation files or feature clarifications.
- **Low Priority:** General inquiries about product capabilities or compliance.

---

## Diagnostic Methodology

### Systematic Approach
1. **Understand the Request:**
   - Clarify the customer's requirements or issue.
   - Confirm the affected environment (e.g., OS version, hosting platform).

2. **Gather Information:**
   - Request logs, screenshots, or error messages.
   - Confirm product version and configuration details.

3. **Analyze the Problem:**
   - Cross-reference the issue with known scenarios.
   - Check compatibility or configuration settings.

4. **Provide a Solution:**
   - Share relevant resources (e.g., download links, documentation).
   - Guide the customer through configuration or troubleshooting steps.

5. **Follow Up:**
   - Confirm resolution with the customer.
   - Document the case for future reference.

---

## Information Collection

### Key Questions to Ask
- What is the specific issue or request?
- What version of the Endpoint Protector Server or agent is being used?
- What operating system and version are affected?
- Are there any error messages or logs available?
- Has the issue been reproduced, and under what conditions?

### Logs and Data to Collect
- **System Logs:** For errors like "500 Internal Server Error."
- **Policy Configuration:** For issues with policy creation or enforcement.
- **Network Traffic Logs:** For DPI-related issues.
- **Screenshots:** To understand error messages or UI issues.

---

## Common Scenarios & Solutions

### Scenario 1: Request for Installation Files
- **Example Case:** [500Qk00000C7r2NIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C7r2NIAR/view)
- **Solution:** Provide download links for the requested OS versions. Confirm compatibility with the customer's environment.

### Scenario 2: Policy Creation Errors
- **Example Case:** [500Qk00000HGqfCIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HGqfCIAT/view)
- **Solution:** Increase the policy limit or adjust existing policies to accommodate new requirements.

### Scenario 3: Compliance-Related Requests
- **Example Case:** [500Qk00000I32vrIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000I32vrIAB/view)
- **Solution:** Refine regex patterns or implement contextual detection to reduce false positives.

### Scenario 4: Connectivity Issues
- **Example Case:** [500Qk00000ORSs4IAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ORSs4IAH/view)
- **Solution:** Disable DPI settings if they interfere with network connectivity.

### Scenario 5: Migration Assistance
- **Example Case:** [500Qk00000NJ6R6IAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NJ6R6IAL/view)
- **Solution:** Use Audit Log Backup to retain logs and shadows during migration.

---

## Detailed Case Studies

### Case Study 1: Installation File Request
- **Ticket ID:** [500Qk00000C7r2NIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C7r2NIAR/view)
- **Symptoms:** Customer requested setup files for Ubuntu distributions.
- **Diagnostic Steps:** Verified server version and OS compatibility.
- **Resolution:** Provided download links for the requested versions.
- **Key Takeaways:** Always confirm server version and OS compatibility before sharing resources.

### Case Study 2: Policy Limit Issue
- **Ticket ID:** [500Qk00000HGqfCIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HGqfCIAT/view)
- **Symptoms:** Customer unable to create new policies due to a limit.
- **Diagnostic Steps:** Verified the existing policy limit and system logs.
- **Resolution:** Increased the policy limit from 48 to 80.
- **Key Takeaways:** Monitor policy limits for customers with complex setups.

### Case Study 3: Regex False Positives
- **Ticket ID:** [500Qk00000I32vrIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000I32vrIAB/view)
- **Symptoms:** Regex pattern generated false positives.
- **Diagnostic Steps:** Reviewed the regex and implemented contextual detection.
- **Resolution:** Refined the regex and added contextual detection rules.
- **Key Takeaways:** Contextual detection can significantly reduce false positives.

---

## Best Practices & Tips

1. **Proactive Communication:**
   - Confirm all details before providing solutions.
   - Follow up to ensure customer satisfaction.

2. **Documentation:**
   - Maintain detailed records of resolved cases for future reference.
   - Share common solutions in internal knowledge bases.

3. **Regular Updates:**
   - Keep track of product updates and new features.
   - Inform customers about upcoming releases that may address their needs.

4. **Efficient Troubleshooting:**
   - Use systematic diagnostic approaches to save time.
   - Leverage tools like the EPPSupportTool for log collection.

5. **Customer Education:**
   - Provide clear instructions and documentation for common tasks.
   - Educate customers on best practices for using the Endpoint Protector.

---

## Escalation Guidelines

### When to Escalate
- Issues involving product defects or limitations.
- Requests requiring development team input (e.g., feature enhancements).
- Cases where standard troubleshooting fails to resolve the issue.

### How to Escalate
1. Document all diagnostic steps and findings.
2. Include relevant logs, screenshots, and customer communications.
3. Submit the case to the appropriate escalation team with a clear summary of the issue.

---

This guide serves as a comprehensive reference for handling "Client Requests" in the Netwrix Endpoint Protector system. By following the outlined methodologies and leveraging the provided case studies, support engineers can resolve issues efficiently and consistently.