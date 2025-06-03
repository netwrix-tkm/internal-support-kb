# Netwrix Endpoint Protector: Content-Aware Protection (Custom Content - Custom PII)

## Overview
Netwrix Endpoint Protector's Content-Aware Protection (CAP) feature enables organizations to monitor, detect, and control the transfer of sensitive data, including custom Personally Identifiable Information (PII). This feature is highly configurable, allowing users to define custom content policies tailored to their specific needs. However, misconfigurations, knowledge gaps, and product limitations can lead to issues that require troubleshooting.

This article provides a comprehensive guide to common issues, troubleshooting steps, root causes, and tested solutions related to the CAP feature for custom PII. It also includes best practices to prevent recurring problems and advanced topics for complex scenarios.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Emails blocked within the same domain | Emails to specific users blocked despite domain allowlist | Verify allowlist, enable DPI, refresh policies | Add "Exchange Administrative Group" to allowlist | [Blocked Emails in Same Domain](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BfbDNIAZ/view) |
| Custom PII implementation guidance | Customer unsure how to configure custom PII policies | Schedule remote session, provide step-by-step guidance | Conduct remote session to demonstrate implementation | [Custom PII Implementation](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CCfIFIA1/view) |
| CAP policies not applied | Policies not enforced despite configuration | Collect logs, test with new build | Provide test build to resolve defect | [CAP Policies Not Applied](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EzP36IAF/view) |
| Blocking PII and donor info in Outlook | Need to block donor info without triggering regular PII alerts | Configure regex + PII items, set Global Threshold | Create custom policy with threshold of 5 | [Blocking Donor Info in Outlook](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FI88AIAT/view) |
| Special character detection failure | "şeker" not detected in CAP policies | Test with larger text files, analyze encoding | Use larger text samples to resolve encoding issues | [Special Character Detection](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000I9ONKIA3/view) |
| Monitoring WhatsApp and Google Drive | Unable to monitor WhatsApp web due to encryption | Block `web.whatsapp` domain, apply CAP to desktop app | Block domain, configure CAP for desktop app | [WhatsApp and Google Drive Monitoring](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IbQafIAF/view) |
| PDF custom properties not scanned | CAP fails to detect tags in PDF custom properties | Test across file types, escalate to development | Apply code fix to enable PDF scanning | [PDF Custom Properties Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JJs8GIAT/view) |
| URL blocklist not working on macOS | Blocked URL accessible on macOS | Verify DPI certificate import | Import and trust DPI certificate | [URL Blocklist on macOS](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000L9FIHIA3/view) |
| Master list for sensitive data | Customer unsure how to create master list for PII | Explain custom content list creation | Guide customer on creating and referencing custom lists | [Master List for Sensitive Data](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LbrIzIAJ/view) |
| Empty user list in MAC policy | Unable to select users in MAC policy | Verify IP/port settings, update deployment scripts | Deploy updated scripts with correct IP/port | [Empty User List in MAC Policy](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LHg0LIAT/view) |
| Policy creation guidance | Customer unsure how to implement policies | Conduct Q&A session, review requirements | Provide detailed guidance during session | [Policy Creation Guidance](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000M9KEAIA3/view) |
| CAP behavior in Outlook | Customer needs confirmation of CAP behavior | Review test scenarios, confirm expected behavior | Provide official confirmation of expected behavior | [CAP Behavior in Outlook](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NAlwUIAT/view) |
| Keyword detection in Arsys webmail | Unable to detect keywords in email subject/body | Confirm product limitation, suggest feature request | Advise customer to submit feature request | [Keyword Detection in Arsys Webmail](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ose9BIAR/view) |
| Incorrect alert for attachments | Alert triggered for single attachment instead of 5 | Verify threat threshold configuration | Clarify threshold applies to PII, not attachment count | [Incorrect Alert for Attachments](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OuNc7IAF/view) |

---

## Detailed Issues

### 1. Blocked Emails in Same Domain
**Symptoms:** Emails to specific users within the same domain were blocked despite the domain being whitelisted.  
**Troubleshooting Steps:**
1. Verify that the email domain is whitelisted in Endpoint Protector settings.
2. Add "Exchange Administrative Group" to the allowlist.
3. Ensure the allowlist is included in the Content-Aware Policy (CAP).
4. Enable Deep Packet Inspection (DPI) in global settings.
5. Refresh policies on client machines.  
**Root Cause:** The lack of proper whitelisting for the Exchange domain.  
**Solution:** Add "Exchange Administrative Group" to the allowlist and include it in the CAP.  
**Source Ticket:** [Blocked Emails in Same Domain](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BfbDNIAZ/view)

---

### 2. Custom PII Implementation
**Symptoms:** Customer required guidance on implementing custom PII policies.  
**Troubleshooting Steps:**
1. Schedule a remote session to demonstrate implementation.
2. Provide step-by-step instructions for creating custom PII policies.  
**Root Cause:** Knowledge gap in configuring custom PII policies.  
**Solution:** Conduct a remote session to guide the customer through the process.  
**Source Ticket:** [Custom PII Implementation](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CCfIFIA1/view)

---

### 3. CAP Policies Not Applied
**Symptoms:** CAP policies were not enforced despite configuration.  
**Troubleshooting Steps:**
1. Collect logs from affected clients.
2. Test with a new build to identify defects.  
**Root Cause:** A defect in the existing build prevented policy application.  
**Solution:** Provide a test build to resolve the defect.  
**Source Ticket:** [CAP Policies Not Applied](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EzP36IAF/view)

---

### 4. Blocking Donor Info in Outlook
**Symptoms:** Customer needed to block donor info without triggering alerts for regular PII.  
**Troubleshooting Steps:**
1. Create a policy combining regex and PII items.
2. Set the Global Threshold to 5 violations.  
**Root Cause:** Requirement for a custom policy to differentiate between regular PII and donor info.  
**Solution:** Configure a custom policy with a threshold of 5.  
**Source Ticket:** [Blocking Donor Info in Outlook](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FI88AIAT/view)

---

## Best Practices
- **Regular Updates:** Keep Endpoint Protector server and client versions up to date to avoid known defects.
- **Policy Testing:** Test policies in a controlled environment before deploying them organization-wide.
- **DPI Certificate Deployment:** Ensure DPI certificates are imported and trusted on all devices.
- **Custom Content Validation:** Use larger text samples for testing custom content with special characters.
- **Documentation:** Maintain detailed documentation of custom PII lists and policies for future reference.

---

## Advanced Topics

### Special Character Detection
**Scenario:** Detection of special characters like "şeker" fails due to encoding issues.  
**Solution:** Use larger text samples to improve encoding detection accuracy.  
**Source Ticket:** [Special Character Detection](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000I9ONKIA3/view)

### Monitoring Encrypted Platforms
**Scenario:** Monitoring WhatsApp web is not feasible due to encryption.  
**Solution:** Block the `web.whatsapp` domain and apply CAP to the desktop app.  
**Source Ticket:** [WhatsApp and Google Drive Monitoring](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IbQafIAF/view)