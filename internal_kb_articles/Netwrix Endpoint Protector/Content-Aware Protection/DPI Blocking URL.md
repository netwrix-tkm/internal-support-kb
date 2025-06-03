# Netwrix Endpoint Protector: DPI Blocking URL Knowledge Base

## Overview

The **DPI Blocking URL** feature in Netwrix Endpoint Protector (EPP) is a powerful tool for managing web access and enforcing security policies. It leverages Deep Packet Inspection (DPI) to block or allow specific URLs, domains, or web-based applications based on predefined policies. While highly effective, this feature can sometimes lead to unexpected behavior due to misconfigurations, compatibility issues, or environmental factors.

This knowledge base article provides a comprehensive guide to common issues, troubleshooting steps, root causes, and tested solutions related to the DPI Blocking URL feature. It also includes best practices to prevent recurring problems and ensure smooth operation.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Compatibility issue with MacOS Sonoma 14.5 | Web access blocked for iOS virtual machines | Test with previous agent version and collect logs | Revert to EPP agent version 3.0.2.2 | [Compatibility Issue with MacOS Sonoma](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bdnk5IAB/view) |
| DPI Denylist overrides CAP exclusions | Denylisted URLs blocked despite exclusions | Verify global DPI Denylist behavior | Remove computer from CAP policy | [DPI Denylist Overrides CAP Exclusions](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bduf7IAB/view) |
| Events not registered in Content Aware Report | Missing events in reports | Analyze logs and verify recent patches | Apply vulnerability fix | [Events Missing in Content Aware Report](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CcOATIA3/view) |
| Certificate errors on Mac devices | Webpages inaccessible due to certificate errors | Verify certificate installation in keychain | Push certificate via Jamf with "allow all" trust | [Certificate Errors on Mac](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CoUTpIAN/view) |
| Allowlist not functioning | Data transfers to allowlisted servers blocked | Review allowlist configuration and logs | Correct allowlist settings | [Allowlist Not Functioning](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Dk6PXIAZ/view) |
| DPI blocking Cloudflare challenge | Unable to access ChatGPT due to Cloudflare check | Add related domains to allowlist | Allowlist `*.logr-ingest.com` and clear browser cache | [DPI Blocking Cloudflare Challenge](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JMNkcIAH/view) |

---

## Detailed Issues

### Compatibility Issue with MacOS Sonoma 14.5
**Symptoms:**  
After updating to MacOS Sonoma 14.5, iOS virtual machines experienced blocked web access.

**Troubleshooting Steps:**  
1. Confirm the issue by testing web access on affected virtual machines.  
2. Collect logs during a remote session.  
3. Test a new build of the EPP agent.  
4. Reinstall the previous version of the EPP agent (3.0.2.2).  

**Root Cause:**  
The new EPP agent version was incompatible with MacOS Sonoma 14.5, causing DPI to block web access.

**Solution:**  
Revert to EPP agent version 3.0.2.2 to restore functionality. Monitor future updates for compatibility.

**Source Ticket:** [Compatibility Issue with MacOS Sonoma](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bdnk5IAB/view)

---

### DPI Denylist Overrides CAP Exclusions
**Symptoms:**  
URLs on the DPI Denylist were blocked even when the affected computer was excluded from CAP policies.

**Troubleshooting Steps:**  
1. Verify if the computer is bound to any CAP policy.  
2. Check the global DPI Denylist configuration.  
3. Test access after removing the computer from CAP policies.  

**Root Cause:**  
The DPI Denylist operates independently of CAP policies, overriding exclusions.

**Solution:**  
Remove the computer from CAP policies to regain access to denylisted URLs.

**Source Ticket:** [DPI Denylist Overrides CAP Exclusions](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bduf7IAB/view)

---

### Events Missing in Content Aware Report
**Symptoms:**  
Events were not being registered in the Content Aware Report for several days.

**Troubleshooting Steps:**  
1. Schedule a remote session to analyze the issue.  
2. Investigate recent patches applied to the EPP server.  
3. Communicate with the customer about ongoing fixes.  

**Root Cause:**  
A vulnerability patch inadvertently disrupted event registration.

**Solution:**  
Apply a fix to resolve the issue and confirm functionality with the customer.

**Source Ticket:** [Events Missing in Content Aware Report](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CcOATIA3/view)

---

### Certificate Errors on Mac
**Symptoms:**  
Mac users encountered certificate errors when accessing webpages after applying URL restriction policies.

**Troubleshooting Steps:**  
1. Verify if the certificate was added to the keychain and set to "allow all" trust.  
2. Provide instructions for certificate deployment via Jamf.  

**Root Cause:**  
The required certificate was not installed in the Mac keychain.

**Solution:**  
Push the certificate to all Macs using Jamf, ensuring it is trusted.

**Source Ticket:** [Certificate Errors on Mac](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CoUTpIAN/view)

---

### Allowlist Not Functioning
**Symptoms:**  
Data transfers to allowlisted servers were blocked.

**Troubleshooting Steps:**  
1. Verify allowlist configuration.  
2. Check for conflicting policies.  
3. Re-enable DPI and test functionality.  

**Root Cause:**  
Misconfiguration in the allowlist settings or DPI not being properly enabled.

**Solution:**  
Correct the allowlist configuration and re-enable DPI.

**Source Ticket:** [Allowlist Not Functioning](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Dk6PXIAZ/view)

---

### DPI Blocking Cloudflare Challenge
**Symptoms:**  
Users were unable to access ChatGPT due to interference with the Cloudflare challenge.

**Troubleshooting Steps:**  
1. Add `*.logr-ingest.com` to the allowlist.  
2. Clear browser cache to apply changes.  

**Root Cause:**  
DPI inspection interfered with the Cloudflare challenge.

**Solution:**  
Allowlist `*.logr-ingest.com` and ensure browser cache is cleared.

**Source Ticket:** [DPI Blocking Cloudflare Challenge](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JMNkcIAH/view)

---

## Best Practices

1. **Test Compatibility:** Always test new EPP agent versions with the latest operating systems before deployment.  
2. **Monitor DPI Settings:** Regularly review allowlists and denylists to ensure they align with organizational needs.  
3. **Certificate Management:** Ensure certificates are properly installed and trusted on all devices.  
4. **Log Collection:** Enable debug logging during troubleshooting to capture detailed information.  
5. **Clear Browser Cache:** After making changes to DPI settings, clear browser caches to avoid residual issues.  
6. **Communicate Changes:** Inform users about potential impacts of DPI policies on web access and provide clear reporting channels.

---

## Advanced Topics

### Selective Blocking for Microsoft Teams
**Scenario:** Customers requested selective blocking of personal Microsoft Teams accounts while allowing business accounts.  

**Limitation:** The DPI Blocking URL feature does not support account-based differentiation. Blocking applies universally to all accounts.  

**Recommendation:** Inform customers of this limitation and suggest alternative approaches, such as separate policies for personal and business devices.  

**Source Ticket:** [Selective Blocking for Microsoft Teams](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OQfmbIAD/view)  

--- 

End of Article.