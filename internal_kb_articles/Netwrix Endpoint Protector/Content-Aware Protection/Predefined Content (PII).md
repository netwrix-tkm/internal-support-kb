# Netwrix Endpoint Protector Knowledge Base: Content-Aware Protection (Predefined Content - PII)

## Overview
Netwrix Endpoint Protector's Content-Aware Protection (CAP) feature enables organizations to detect, block, and remediate sensitive data transfers based on predefined content policies. This includes Personally Identifiable Information (PII) such as Social Security Numbers (SSNs), credit card numbers, and regional identification formats like Brazilian CPF or Turkish ID numbers. Common issues include misconfigurations, detection limitations, false positives, and compatibility challenges with specific applications or environments.

This article provides a structured guide to troubleshooting and resolving issues related to CAP's predefined content functionality.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Email alerts not received | Alerts not triggered for PII-related WhatsApp messages; SMTP errors | Verify email server settings, check logs, reconfigure sender address | Change sender email to valid address, adjust folder ownership | [Email Alerts Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BjpstIAB/view) |
| Sensitive data not detected in WhatsApp | PII not flagged when copied/pasted into WhatsApp | Adjust threat threshold, create "Report Only" policy | Lower threshold to 1 for detection | [WhatsApp Detection Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BTF29IAH/view) |
| Report discrepancies | Reports show more flagged files than actual detections | Review CAP and eDiscovery configurations | Adjust scanning/reporting settings | [Report Discrepancies](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BxJLFIA3/view) |
| Twitter access blocked | CAP policy incorrectly flags Twitter requests | Review logs, whitelist domain, test build | Ignore flagged requests via custom build | [Twitter Blocking Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DFptzIAD/view) |
| Missing remediation logs | "Content Remediation Session Active" not logged | Test file transfer post-remediation | Clarify logging behavior | [Remediation Logs Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DHTuBIAX/view) |
| False positives for Brazilian CPF | Non-CPF data flagged as PII | Analyze detection patterns, enable "Ignore Trust" | Adjust detection algorithm via custom build | [Brazilian CPF False Positives](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KwZTOIA3/view) |
| OCR not functioning for SSNs | OCR fails to detect SSNs in text/images | Verify OCR settings, test configurations | Adjust OCR settings, install EPP certificate | [OCR Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LCuvCIAT/view) |
| Daily block report setup | Unable to generate automated block reports | Configure reporting and email notifications | Enable report generation and email settings | [Daily Block Report Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LNsTSIA1/view) |
| Printing blocked | Unable to print email due to outdated client | Upgrade EPP client, reboot system | Update client to latest version | [Printing Block Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MaYEiIAN/view) |
| Trial license expired | Unable to back up policies after trial expiration | Export policies before expiration | Provide backup instructions | [Trial License Expiration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MX4WPIA1/view) |
| Blocking JPG files | OCR detects PNG but not JPG files | Verify CAP policy settings, test file uploads | Configure CAP to include JPG files | [JPG Blocking Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NJ08jIAD/view) |
| URL-specific PII blocking | Unable to restrict PII uploads to specific websites | Enable DPI, configure URL categories | Use URL categories in CAP policies | [URL-Specific Blocking](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NWyGmIAL/view) |
| Turkish ID detection in emails | TCIDs in email body not detected | Test old vs. new Outlook, enable debug mode | Use old Outlook until new client release | [Turkish ID Detection](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ORVnDIAX/view) |

---

## Detailed Issues

### Email Alerts Not Received
**Symptoms:** Alerts not triggered for PII-related WhatsApp messages; SMTP errors due to invalid sender address.  
**Troubleshooting Steps:**  
1. Verify email server settings and sender address (`root@eppserver`).  
2. Check mail logs for errors like "unable to qualify my own domain name."  
3. Change ownership of the Mailer folder to `www-data`.  
4. Clear pending emails from the database and restart mailer alerts.  
**Root Cause:** Invalid sender email address rejected by SMTP server.  
**Solution:**  
- Reconfigure sender email to a valid address.  
- Adjust folder ownership to `www-data`.  
**Source Ticket:** [Email Alerts Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BjpstIAB/view)

---

### Sensitive Data Not Detected in WhatsApp
**Symptoms:** PII not flagged when copied/pasted into WhatsApp Web/Desktop.  
**Troubleshooting Steps:**  
1. Verify CAP policy settings and threat threshold.  
2. Create a "Report Only" policy to monitor file transfers.  
3. Lower threat threshold to 1 for detection.  
**Root Cause:** Threshold set too high, preventing detection of sensitive data.  
**Solution:** Adjust threat threshold to 1 to flag any sensitive data.  
**Source Ticket:** [WhatsApp Detection Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BTF29IAH/view)

---

### Report Discrepancies
**Symptoms:** Reports show more flagged files than actual detections.  
**Troubleshooting Steps:**  
1. Review CAP and eDiscovery configurations.  
2. Test file uploads and regex expressions for false positives.  
**Root Cause:** Misconfigured CAP settings affecting detection accuracy.  
**Solution:** Adjust scanning and reporting configurations.  
**Source Ticket:** [Report Discrepancies](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BxJLFIA3/view)

---

### Turkish ID Detection in Emails
**Symptoms:** TCIDs in email body not detected in new Outlook; attachments detected correctly.  
**Troubleshooting Steps:**  
1. Test detection in old vs. new Outlook.  
2. Enable debug mode and gather logs.  
**Root Cause:** Known limitation in EPP client with new Outlook.  
**Solution:** Use old Outlook until new client release (expected May).  
**Source Ticket:** [Turkish ID Detection](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ORVnDIAX/view)

---

## Best Practices
- **Email Alerts:** Always configure valid sender addresses to avoid SMTP rejections.  
- **CAP Policies:** Regularly review and adjust threat thresholds to align with organizational needs.  
- **OCR Settings:** Test OCR functionality for all relevant file types (e.g., PNG, JPG, PDF).  
- **Client Updates:** Ensure EPP clients are updated to maintain compatibility with server versions.  
- **Policy Backups:** Export policies before license expiration to preserve configurations.  
- **URL Categories:** Enable DPI when applying URL-specific CAP policies.  

---

## Advanced Topics

### Custom Builds for Regional PII Detection
For cases involving regional identification formats (e.g., Brazilian CPF, Turkish ID), custom builds may be required to refine detection algorithms. These builds should be tested on limited machines before deployment. Monitor logs for bypass events and validate detection accuracy.

### Debugging DPI and Text Inspection
When CAP fails to detect sensitive data in specific applications (e.g., new Outlook), enable debug mode and collect extended logs. This helps identify limitations in DPI or text inspection capabilities.

---

End of Article.