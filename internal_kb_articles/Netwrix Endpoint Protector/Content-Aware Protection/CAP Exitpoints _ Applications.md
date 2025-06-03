# Netwrix Endpoint Protector: Content-Aware Protection (CAP) Exitpoints / Applications

## Overview
Netwrix Endpoint Protector's Content-Aware Protection (CAP) Exitpoints / Applications feature is designed to monitor and control data transfers through various applications and exit points. This functionality ensures sensitive data is protected from unauthorized sharing or leakage. However, certain configurations, compatibility issues, or environmental factors can lead to unexpected behavior. This article provides a comprehensive guide to common issues, troubleshooting steps, root causes, and tested solutions.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Tally application errors | Errors in Tally after EPP client installation | Verify compatibility and collect debug logs | Ensure compatibility and analyze logs | [Tally Errors](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000D4gE6IAJ/view) |
| Policy not blocking Brave/Tor | Brave and Tor not blocked despite policy | Verify policy settings and test on endpoints | Confirm policy application and test functionality | [Policy Not Blocking Brave/Tor](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DRkX8IAL/view) |
| Network Share behavior with Total Commander | Transfers logged despite "Network Share" disabled | Review CAP policy and logs | Clarify expected behavior for Total Commander | [Network Share Behavior](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DubtVIAR/view) |
| OneDrive misclassification | OneDrive for Business classified as Personal | Enable DPI and test with updated build | Update to version 5.9.4.1 with DPI enabled | [OneDrive Misclassification](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DVM1aIAH/view) |
| CAP not blocking Python/PHP on WhatsApp | Python/PHP files not blocked on WhatsApp Desktop | Test blocking rules and collect logs | Monitor CAP functionality and update WhatsApp | [WhatsApp Blocking Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EjhX1IAJ/view) |
| WhatsApp Desktop not blocked | Denylist ineffective for WhatsApp Desktop | Add wildcard entries to denylist | Use `*` wildcard for Microsoft Store apps | [WhatsApp Desktop Denylist](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EyWRaIAN/view) |
| Certificate issue affecting CAP | CAP functionality disrupted by certificate error | Verify and renew certificate | Renew and install valid certificate | [Certificate Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FidMpIAJ/view) |
| Excel prompts on Google Drive | Frequent authorization prompts in Excel | Add wildcard to allowlist for dynamic URLs | Use `*.blob.core.windows.net` in allowlist | [Excel Prompts on Google Drive](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FJwMFIA1/view) |
| Outlook email blocking | Emails blocked due to process name conflict | Test with updated EPP client | Update to version 5941 to resolve conflict | [Outlook Email Blocking](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GmNPKIA3/view) |
| Adobe Acrobat Reader crash | Acrobat Reader crashes with EPP agent active | Add exception for Acrobat Reader | Configure Advanced Scanning Exception | [Adobe Acrobat Reader Crash](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000H5zh2IAB/view) |
| File transfers in WSL | EPP not blocking file transfers in WSL | Confirm logging and raise feature request | Inform customer of non-GUI limitations | [WSL File Transfers](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ItTmzIAF/view) |
| Git errors after policy change | Git errors after removing GitHub from policy | Review policy changes and logs | Uninstall GitHub client and reset system | [Git Errors](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JoD5ZIAV/view) |
| PNG signature blocking emails | Emails blocked due to PNG signature | Add PNG to allowlist and adjust CAP policy | Modify CAP policy to allow PNG format | [PNG Signature Blocking Emails](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000K1mLdIAJ/view) |
| SSH uploads blocked | SSH uploads blocked by CAP policy | Update EPP client and verify logs | Upgrade to version 6.2.3.1 | [SSH Uploads Blocked](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Kau3RIAR/view) |
| Hyperlink slowness in Outlook | Slow or incorrect hyperlink behavior | Exclude .ost/.pst files from scanning | Adjust policy to exclude archive files | [Hyperlink Slowness in Outlook](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KdqEcIAJ/view) |
| PII detection failure in OneDrive | PII not detected during OneDrive transfers | Remove affected computer from allowlist | Remove computer from allowlist | [PII Detection Failure](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000M0DwiIAF/view) |
| Media file blocking in Chrome | MP4 downloads blocked in Chrome | Verify policies and adjust denylist | Adjust policy to allow MP4 downloads | [Media File Blocking in Chrome](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NDCm5IAH/view) |
| Brazilian PII not blocked in Outlook | PII not blocked in old Outlook version | Test regex patterns and upgrade EPP | Upgrade to version 5.9.4.1 | [Brazilian PII Not Blocked](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NOq1rIAD/view) |
| AI tool exit points | Inquiry about ChatGPT exit points | Confirm feature absence and consult roadmap | Inform customer of planned feature | [AI Tool Exit Points](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000P74OjIAJ/view) |
| CiscoVPN disconnects | CiscoVPN disconnects intermittently | Add CiscoVPN process to exception list | Add process to exception list | [CiscoVPN Disconnects](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PSLMYIA5/view) |

---

## Detailed Issues

### Tally Application Errors
**Symptoms:** Continuous errors in Tally after EPP client installation.  
**Troubleshooting Steps:**
1. Verify compatibility between EPP client and Tally version.
2. Collect debug logs using EPPSupportTool.  
**Root Cause:** Compatibility issue or specific machine configuration.  
**Solution:** Ensure compatibility and analyze logs for further insights.  
**Source Ticket:** [Tally Errors](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000D4gE6IAJ/view)

---

### Policy Not Blocking Brave/Tor
**Symptoms:** Brave and Tor applications not blocked despite policy.  
**Troubleshooting Steps:**
1. Verify policy settings and application inclusion.
2. Test policy on endpoints.  
**Root Cause:** Temporary glitch or miscommunication in policy enforcement.  
**Solution:** Confirm policy application and test functionality.  
**Source Ticket:** [Policy Not Blocking Brave/Tor](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DRkX8IAL/view)

---

### Network Share Behavior with Total Commander
**Symptoms:** Transfers logged as "Network Share" despite being disabled.  
**Troubleshooting Steps:**
1. Review CAP policy settings.
2. Analyze logs for transfer details.  
**Root Cause:** Default behavior of recognizing Total Commander transfers as network share operations.  
**Solution:** Clarify expected behavior and adjust policy if needed.  
**Source Ticket:** [Network Share Behavior](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DubtVIAR/view)

---

### OneDrive Misclassification
**Symptoms:** OneDrive for Business classified as Personal.  
**Troubleshooting Steps:**
1. Enable DPI for accurate classification.
2. Test with updated build.  
**Root Cause:** Detection mechanism misinterpreted domain type.  
**Solution:** Update to version 5.9.4.1 with DPI enabled.  
**Source Ticket:** [OneDrive Misclassification](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DVM1aIAH/view)

---

## Best Practices
- **Regular Updates:** Keep the EPP client and server updated to the latest versions.
- **Policy Testing:** Test policies in a controlled environment before deployment.
- **Log Monitoring:** Regularly review logs for anomalies or errors.
- **Wildcard Usage:** Use wildcards in allowlists/denylists for dynamic URLs or applications.
- **Certificate Management:** Monitor and renew certificates before expiration.

---

## Advanced Topics

### Handling Non-GUI Environments
In terminal-only environments (e.g., WSL), user notifications are unavailable, but actions are logged on the EPP server. Inform customers of this limitation and suggest feature requests for enhanced functionality.  
**Source Ticket:** [WSL File Transfers](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ItTmzIAF/view)

### AI Tool Exit Points
Netwrix Endpoint Protector currently lacks dedicated exit points for AI tools like ChatGPT. This feature is planned for future releases. Customers can track updates via the [Netwrix Public Roadmap](https://portal.productboard.com/rqqgx2aos1cf9enrezvrre6a/tabs/56-planned).  
**Source Ticket:** [AI Tool Exit Points](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000P74OjIAJ/view)