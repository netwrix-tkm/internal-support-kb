# Comprehensive Knowledge Base Guide: Troubleshooting Content-Aware Protection (Custom Content - PII) in Netwrix Endpoint Protector

## Overview
This guide provides a systematic approach to understanding, diagnosing, and resolving issues related to the **Content-Aware Protection (CAP)** feature in **Netwrix Endpoint Protector**, specifically focusing on **Custom Content (custom PII)**. CAP is a critical component for organizations aiming to enforce data loss prevention (DLP) policies by monitoring and controlling sensitive data, such as Personally Identifiable Information (PII). This guide equips support engineers with the knowledge and tools to handle these issues effectively, ensuring consistent and efficient resolutions.

---

## Technical Background
### Key Concepts
- **Content-Aware Protection (CAP):** A feature that scans data for predefined or custom patterns (e.g., PII) and enforces policies to block, allow, or alert based on violations.
- **Custom Content:** User-defined patterns or keywords (e.g., regex for Aadhaar numbers, credit card details) that CAP policies monitor.
- **Deep Packet Inspection (DPI):** A mechanism that inspects data packets for policy violations, requiring a DPI certificate for HTTPS traffic monitoring.
- **Global Threshold:** A configurable value that determines the number of violations required to trigger a policy action.

### System Context
- **Server-Client Architecture:** CAP policies are configured on the server and pushed to client machines.
- **Supported Platforms:** Windows, macOS, and specific applications like Outlook and Google Drive.
- **Limitations:** Certain platforms (e.g., web versions of WhatsApp) and functionalities (e.g., keyword detection in email subject lines) may have inherent restrictions.

---

## Issue Recognition & Triage
### Symptoms
- Policies not applying or triggering incorrectly.
- Specific keywords or patterns not being detected.
- Issues with DPI functionality (e.g., blocked URLs still accessible).
- Misunderstandings about CAP policy configurations (e.g., thresholds, exclusions).

### Priority Assessment
- **High Priority:** Data breaches, inability to enforce critical DLP policies.
- **Medium Priority:** Detection failures for specific patterns or keywords.
- **Low Priority:** Configuration guidance or feature clarification.

---

## Diagnostic Methodology
### Systematic Approach
1. **Understand the Problem:**
   - Gather detailed information about the issue (e.g., symptoms, affected users, environment details).
   - Confirm the version of the Endpoint Protector server and client.

2. **Verify Configuration:**
   - Check CAP policy settings (e.g., thresholds, exit points, allowlists/denylists).
   - Ensure DPI is enabled and the certificate is imported on all devices.

3. **Reproduce the Issue:**
   - Attempt to replicate the problem in a controlled environment using test data.

4. **Analyze Logs:**
   - Collect and review logs from the server and client machines to identify errors or misconfigurations.

5. **Engage Development (if needed):**
   - For unresolved issues, escalate to the R&D team with detailed findings.

---

## Information Collection
### Key Questions for Customers
- What specific issue are you experiencing (e.g., detection failure, policy misbehavior)?
- What data types or patterns are involved (e.g., Aadhaar numbers, keywords)?
- Are DPI and CAP policies enabled and configured correctly?
- What is the environment setup (e.g., OS, email platform, browser)?

### Logs and Data to Collect
- CAP policy configuration files.
- DPI settings and certificate status.
- Client and server logs.
- Screenshots or videos demonstrating the issue.

---

## Common Scenarios & Solutions
### Scenario 1: Policies Not Applying
- **Root Cause:** Misconfigured IP/port settings or outdated deployment scripts.
- **Solution:** Update deployment scripts and verify IP/port configurations. Ensure policies are refreshed on client machines.

### Scenario 2: Detection Failures for Specific Keywords
- **Root Cause:** Character encoding issues or insufficient text context.
- **Solution:** Test with larger text samples and verify encoding settings.

### Scenario 3: DPI Certificate Not Imported
- **Root Cause:** DPI functionality not working due to missing certificates.
- **Solution:** Import and trust the DPI certificate on all devices.

### Scenario 4: Misunderstanding of Thresholds
- **Root Cause:** Confusion about how thresholds apply to PII versus file types.
- **Solution:** Clarify that thresholds are based on PII violations, not attachment counts.

---

## Detailed Case Studies
### Case Study 1: Email Blocking Issue  
**[Ticket ID: 500Qk00000BfbDNIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BfbDNIAZ/view)**  
- **Symptoms:** Emails to specific users were blocked despite being in the same domain.  
- **Diagnostic Steps:** Verified allowlist configuration, DPI settings, and policy refresh.  
- **Resolution:** Added "Exchange Administrative Group" to the allowlist and refreshed policies.  
- **Key Takeaways:** Always include entire administrative groups in allowlists for Exchange environments.

### Case Study 2: Custom PII Implementation  
**[Ticket ID: 500Qk00000CCfIFIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CCfIFIA1/view)**  
- **Symptoms:** Customer needed guidance on implementing custom PII protection.  
- **Diagnostic Steps:** Conducted a remote session to demonstrate policy creation.  
- **Resolution:** Provided step-by-step instructions for configuring custom PII policies.  
- **Key Takeaways:** Remote sessions are highly effective for complex configurations.

### Case Study 3: Keyword Detection Failure  
**[Ticket ID: 500Qk00000I9ONKIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000I9ONKIA3/view)**  
- **Symptoms:** The word "şeker" was not detected in text files.  
- **Diagnostic Steps:** Tested with various file types and sizes, identified encoding issues.  
- **Resolution:** Advised testing with larger text samples to ensure proper encoding detection.  
- **Key Takeaways:** Short text samples may lead to encoding misidentification.

### Case Study 4: DPI Certificate Issue  
**[Ticket ID: 500Qk00000L9FIHIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000L9FIHIA3/view)**  
- **Symptoms:** Blocked URLs were still accessible on macOS devices.  
- **Diagnostic Steps:** Verified DPI settings and identified missing certificates.  
- **Resolution:** Imported and trusted the DPI certificate on macOS devices.  
- **Key Takeaways:** DPI certificates must be deployed and trusted on all devices.

---

## Best Practices & Tips
- **Policy Configuration:** Regularly review and test CAP policies to ensure they align with organizational requirements.
- **DPI Deployment:** Always deploy and verify DPI certificates across all devices in the environment.
- **Custom Content:** Use regex patterns for precise detection and test with realistic data samples.
- **Documentation:** Maintain detailed records of configurations and resolutions for future reference.
- **Customer Communication:** Clearly explain limitations and expected behavior to manage expectations.

---

## Escalation Guidelines
### When to Escalate
- Issues involving product defects or unresolvable bugs.
- Requests for unsupported features or enhancements.
- Persistent problems despite following standard troubleshooting steps.

### How to Escalate
1. Collect all relevant logs, configurations, and test results.
2. Document the issue, including steps taken and findings.
3. Submit a detailed report to the R&D team via the appropriate escalation channel.

---

This guide serves as a comprehensive reference for handling Content-Aware Protection (Custom Content - PII) issues in Netwrix Endpoint Protector. By following the outlined methodologies and leveraging the case studies, support engineers can ensure consistent and effective resolutions.