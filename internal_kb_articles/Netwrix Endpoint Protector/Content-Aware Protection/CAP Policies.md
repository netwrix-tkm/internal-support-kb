# Netwrix Endpoint Protector Knowledge Base: Content-Aware Protection (CAP) Policies

## Overview

Netwrix Endpoint Protector's Content-Aware Protection (CAP) Policies are designed to monitor, block, and report sensitive data transfers across various endpoints and exit points, including applications, devices, and protocols. CAP Policies are critical for enforcing data security and compliance, but they can encounter issues due to misconfigurations, software limitations, or environmental factors. This article provides a comprehensive guide to troubleshooting CAP Policy-related issues, identifying root causes, and implementing tested solutions.

---

## Common Issues and Solutions

### Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Incorrect CAP policy triggered for excluded user | Excluded user affected by CAP policy | Collect logs, reinstall client, re-register certificates | Apply hotfix and re-register certificates | [Incorrect CAP Policy Triggered](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bh2eXIAR/view) |
| File location denylist limitations | Unable to selectively block USB transfers from specific folders | Confirm limitations, suggest logging activities | Block USB devices entirely or submit feature request | [File Location Denylist Limitations](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BpzhTIAR/view) |
| Screenshot blocking on specific websites | Screenshots blocked globally instead of per-website | Test OCR, confirm limitations | Submit feature request for selective blocking | [Screenshot Blocking Limitations](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BR0QcIAL/view) |
| GitHub Client domain allowlisting | Unable to allow specific domains for GitHub | Update to latest version, test DPI allowlists | Upgrade to version 5.9.4.1 for enhanced CAP handling | [GitHub Client Allowlisting](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BWJduIAH/view) |
| Differentiating uploaded vs downloaded files | Logs do not distinguish uploads from downloads | Enable DPI, add DPI certificate to MacOS Keychain | Enable DPI and configure certificate | [Upload vs Download Differentiation](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CGK3uIAH/view) |
| Logs not received after server hotfix | CAP logs missing post-hotfix | Verify hotfix functionality, apply PHP patch | Apply PHP patch to restore log transmission | [Logs Missing Post-Hotfix](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CVeNHIA1/view) |
| Recognizing TOR traffic | TOR traffic not monitored effectively | Mark TOR traffic as exit point, clarify eDiscovery limitations | Configure CAP policies for TOR traffic monitoring | [TOR Traffic Monitoring](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Cz5IPIAZ/view) |
| CAP reports show "No matching records found" | Reports fail when policy name contains "&" | Test filtering with different policy names | Avoid "&" in policy names until hotfix is applied | [CAP Reports Filtering Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000D4xq1IAB/view) |
| PAN and Passport numbers not masked | Sensitive data visible in logs | Upgrade client to latest version | Upgrade to version 2.4.3.1007 for masking support | [Sensitive Data Masking](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DgmqMIAR/view) |
| Missing OTP Entry Option | OTP entry option missing in CAP tab | Confirm absence, investigate bug, send patch | Apply offline patch | [Missing OTP Entry Option](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LECzhIAH/view) |
| False positives for credit card detection | Frequent pop-ups for blocked credit card data | Enable extended logging, create contextual detection rule | Adjust CAP policy | [False Positives for Credit Card Detection](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LfiQpIAJ/view) |
| CAP policy issues on Ubuntu | File transfer problems on Ubuntu | Enable DPI, update EPP client | Enable DPI and update client | [CAP Policy Issues on Ubuntu](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LJHM6IAP/view) |
| DNS resolution failure | Client unable to communicate with server | Verify DNS settings, check logs | Correct DNS settings | [DNS Resolution Failure](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Lmh8FIAR/view) |
| CAP rule blocking emails | Emails blocked without notification | Review CAP rule settings, disable rule | Disable CAP rule | [CAP Rule Blocking Emails](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LqA2PIAV/view) |
| Metadata scanning false positives | Web uploads blocked incorrectly | Turn off Metadata Scanning | Disable Metadata Scanning | [Metadata Scanning False Positives](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LRHOsIAP/view) |
| Missing destination logs | Destination not logged during data exfiltration | Enable Reporting V2 | Enable Reporting V2 | [Missing Destination Logs](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LSCVHIA5/view) |
| Excluding items from CAP policy | Confusion about excluding file types | Provide exclusion instructions | Update CAP policy settings | [Excluding Items from CAP Policy](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MEGmcIAH/view) |
| Websites blocked incorrectly | All websites blocked except denylist entries | Correct denylist formatting, enable network extension | Update denylist and enable network extension | [Websites Blocked Incorrectly](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MZr4rIAD/view) |

---

## Detailed Troubleshooting and Solutions

### Incorrect CAP Policy Triggered for Excluded User
**Symptoms:** CAP policy triggered for a user explicitly excluded from the policy.  
**Solution:**  
- Apply hotfix `adv-2024-002`.  
- Re-register client certificates from the backend.  

---

### File Location Denylist Limitations
**Symptoms:** Unable to selectively block USB transfers from specific folders.  
**Solution:**  
- Block USB devices entirely or enable file trace logging for network shares.  
- Submit feature request for selective blocking functionality.  

---

### Screenshot Blocking on Specific Websites
**Symptoms:** Screenshots blocked globally instead of selectively for sensitive websites.  
**Solution:**  
- Submit feature request for selective blocking functionality.  

---

### GitHub Client Domain Allowlisting
**Symptoms:** Unable to allow specific domains for GitHub Client configurations.  
**Solution:**  
- Upgrade to version 5.9.4.1 for enhanced CAP handling.  

---

### Differentiating Uploaded vs Downloaded Files
**Symptoms:** Logs do not distinguish between uploaded and downloaded files.  
**Solution:**  
- Enable DPI and configure certificates for accurate monitoring.  

---

### Missing OTP Entry Option
**Symptoms:** OTP entry option missing in CAP tab.  
**Solution:**  
- Apply offline patch containing fixed agents.  

---

### False Positives for Credit Card Detection
**Symptoms:** Frequent pop-ups for blocked credit card data during web browsing.  
**Solution:**  
- Adjust CAP policy to refine detection rules and eliminate false positives.  

---

### CAP Policy Issues on Ubuntu
**Symptoms:** File transfer problems on Ubuntu systems.  
**Solution:**  
- Enable DPI for proper monitoring.  
- Update the EPP client to ensure compatibility.  

---

### DNS Resolution Failure
**Symptoms:** Client unable to communicate with the server due to DNS resolution failure.  
**Solution:**  
- Correct DNS settings on the customer's network.  

---

### CAP Rule Blocking Emails
**Symptoms:** Emails blocked without notification due to CAP rule settings.  
**Solution:**  
- Disable the CAP rule blocking emails.  

---

### Metadata Scanning False Positives
**Symptoms:** Web uploads blocked incorrectly due to metadata scanning.  
**Solution:**  
- Disable Metadata Scanning.  

---

### Missing Destination Logs
**Symptoms:** Destination not logged during data exfiltration.  
**Solution:**  
- Enable Reporting V2.  

---

### Websites Blocked Incorrectly
**Symptoms:** All websites blocked except denylist entries.  
**Solution:**  
- Correct denylist formatting and enable network extension.  

---

## Best Practices

1. **Regular Updates:** Ensure Endpoint Protector server and client versions are up-to-date to benefit from the latest features and fixes.  
2. **Policy Testing:** Test CAP policies in controlled environments before deploying them organization-wide.  
3. **Enable DPI:** Use Deep Packet Inspection for environments requiring detailed monitoring of file transfers.  
4. **Notification Systems:** Implement notifications for blocked actions to improve user experience and transparency.  
5. **Snapshot Configurations:** Take snapshots before performing updates to prevent data loss.  
6. **Review Logs:** Regularly review logs to identify and address anomalies promptly.  

---

## Advanced Topics

### Handling Encrypted Files
CAP policies can monitor encrypted files by their file type but cannot access their content due to encryption protocols. Use metadata-based detection for encrypted files.

### DPI Conflicts with Other Security Tools
Deep Packet Inspection (DPI) may conflict with other security tools like CrowdStrike or PaloAlto. Review DPI configurations to prevent unintended blocking of legitimate traffic.

### Virtualization Platforms
Blocking file transfers to virtual machines requires explicit recognition of platforms as exit points. Monitor updates for added support or submit feature requests for virtualization-specific policies.

---

End of Article.