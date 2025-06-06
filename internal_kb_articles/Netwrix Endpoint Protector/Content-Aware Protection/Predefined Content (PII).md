# Comprehensive Knowledge Base Guide: Troubleshooting Content-Aware Protection (Predefined Content - PII)

## Overview

Content-Aware Protection (CAP) with Predefined Content (PII) in Netwrix Endpoint Protector is a critical feature designed to prevent unauthorized sharing or exposure of sensitive data. This feature enables organizations to detect and block Personally Identifiable Information (PII) across various endpoints and communication channels. Understanding and troubleshooting issues in this category is essential to ensure compliance with data protection regulations and to maintain the integrity of sensitive information.

This guide provides a systematic approach to diagnosing and resolving issues related to CAP with Predefined Content (PII). It includes technical background, diagnostic methodologies, common scenarios, and best practices to empower support engineers to handle these cases effectively.

---

## Technical Background

### Key Concepts
- **Content-Aware Protection (CAP):** A feature that scans data in motion (e.g., file transfers, email attachments) and at rest (e.g., local files) to detect sensitive content.
- **Predefined Content:** Pre-configured patterns for detecting specific types of sensitive data, such as Social Security Numbers (SSNs), credit card numbers, or regional identification formats (e.g., Brazilian CPF, UK bank accounts).
- **Deep Packet Inspection (DPI):** A technology used to analyze data packets for sensitive content.
- **Optical Character Recognition (OCR):** A feature that scans text within images or PDFs to detect sensitive information.

### System Context
- **Server-Client Architecture:** The Netwrix Endpoint Protector server manages policies, while the client enforces them on endpoints.
- **Policy Configuration:** CAP policies define what content to monitor, block, or report, and can include logical operators (AND/OR) for complex rules.
- **Exit Points:** Channels where data can leave the organization, such as email, web uploads, or external devices.

---

## Issue Recognition & Triage

### Symptoms of CAP Issues
- Alerts not being triggered for sensitive data transfers.
- False positives or false negatives in PII detection.
- Inconsistent behavior across file types or communication channels.
- Issues with email alerts or reporting functionality.
- Compatibility problems with specific applications (e.g., Outlook, WhatsApp).

### Priority Assessment
- **High Priority:** Data leakage risks, such as undetected sensitive data transfers or inability to block critical PII.
- **Medium Priority:** False positives affecting productivity or minor reporting discrepancies.
- **Low Priority:** Configuration inquiries or feature clarifications.

---

## Diagnostic Methodology

### Systematic Approach
1. **Understand the Problem:**
   - Gather detailed information from the customer about the issue.
   - Identify the affected components (e.g., email alerts, file uploads, specific applications).

2. **Verify Configuration:**
   - Check CAP policy settings, including predefined content patterns, thresholds, and exit points.
   - Ensure DPI and OCR features are enabled if required.

3. **Reproduce the Issue:**
   - Attempt to replicate the problem in a controlled environment using test data.

4. **Analyze Logs:**
   - Review relevant logs (e.g., CAP logs, mail logs) for errors or anomalies.

5. **Test Solutions:**
   - Apply configuration changes or updates incrementally and test their impact.

6. **Escalate if Necessary:**
   - If the issue persists, escalate to R&D with detailed logs and findings.

---

## Information Collection

### Questions to Ask Customers
- What specific data or file types are not being detected or blocked?
- Which applications or channels are affected (e.g., email, web uploads)?
- Are there any recent changes to the environment (e.g., upgrades, policy changes)?
- What is the expected behavior versus the observed behavior?

### Logs and Data to Collect
- CAP logs and mail logs.
- Screenshots or recordings of the issue.
- Policy configuration exports.
- Sample data that reproduces the issue (e.g., test files, email formats).

---

## Common Scenarios & Solutions

### Scenario 1: Email Alerts Not Received
- **Root Cause:** Invalid sender email address or misconfigured SMTP settings.
- **Solution:** Reconfigure the email server with a valid sender address and verify SMTP relay settings. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BjpstIAB/view)

### Scenario 2: False Positives in PII Detection
- **Root Cause:** Overly broad detection patterns or algorithm limitations.
- **Solution:** Refine detection rules and use custom regex patterns to minimize false positives. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000F0SIEIA3/view)

### Scenario 3: Undetected Sensitive Data in Specific Formats
- **Root Cause:** Unsupported file types or incorrect data formats.
- **Solution:** Update CAP policies to include the specific file types and ensure OCR is enabled. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NJ08jIAD/view)

### Scenario 4: Compatibility Issues with Applications
- **Root Cause:** Limitations in client functionality with newer application versions.
- **Solution:** Use older application versions or test custom builds provided by R&D. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ORVnDIAX/view)

---

## Detailed Case Studies

### Case Study 1: Email Alerts Not Triggered
- **Ticket ID:** [500Qk00000BjpstIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BjpstIAB/view)
- **Symptoms:** Alerts not received after implementing a WhatsApp blocking policy.
- **Diagnostic Steps:** Verified SMTP settings, reinstalled EPP software, and analyzed mail logs.
- **Resolution:** Changed the sender email address and folder ownership, ensuring alerts were sent successfully.
- **Key Takeaways:** Always use valid email addresses and verify mail server configurations.

### Case Study 2: False Positives for Brazilian CPF
- **Ticket ID:** [500Qk00000KwZTOIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KwZTOIA3/view)
- **Symptoms:** Non-CPF content flagged as sensitive.
- **Diagnostic Steps:** Reviewed detection patterns and engaged R&D for a custom build.
- **Resolution:** Deployed a custom build with refined CPF detection rules.
- **Key Takeaways:** Tailor detection algorithms to regional data formats to reduce false positives.

### Case Study 3: Undetected TCIDs in Email Body
- **Ticket ID:** [500Qk00000ORVnDIAX](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ORVnDIAX/view)
- **Symptoms:** TCIDs in email bodies not detected in the new Outlook application.
- **Diagnostic Steps:** Tested detection across different Outlook versions and formats.
- **Resolution:** Advised using the old Outlook version until a new client release.
- **Key Takeaways:** Monitor application compatibility and communicate known limitations to customers.

---

## Best Practices & Tips

1. **Policy Configuration:**
   - Regularly review and update CAP policies to align with organizational needs.
   - Use logical operators (AND/OR) for complex detection criteria.

2. **Testing and Validation:**
   - Test policies with real-world data to ensure accuracy.
   - Validate detection capabilities across all relevant file types and formats.

3. **Customer Communication:**
   - Provide clear instructions and examples for testing.
   - Set realistic expectations regarding feature limitations and timelines for fixes.

4. **Proactive Monitoring:**
   - Monitor logs for anomalies and address issues before they escalate.
   - Stay informed about new releases and updates to the Netwrix Endpoint Protector.

---

## Escalation Guidelines

### When to Escalate
- Issues persist after applying standard troubleshooting steps.
- Detection failures involve critical data or high-risk scenarios.
- Compatibility issues with widely used applications (e.g., Outlook, Chrome).

### How to Escalate
- Collect comprehensive logs, screenshots, and test data.
- Document all troubleshooting steps taken and their outcomes.
- Submit a detailed escalation request to R&D, referencing relevant case IDs.

---

This guide serves as a definitive reference for troubleshooting Content-Aware Protection (Predefined Content - PII) issues, enabling support engineers to resolve cases efficiently and consistently.