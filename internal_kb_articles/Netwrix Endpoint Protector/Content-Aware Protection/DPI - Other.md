# Netwrix Endpoint Protector: Deep Packet Inspection (DPI) - Common Issues and Resolutions

## Overview
Deep Packet Inspection (DPI) is a critical feature of the Netwrix Endpoint Protector (EPP) that enables advanced content filtering and monitoring for data loss prevention. DPI inspects network traffic to enforce Content-Aware Protection (CAP) policies, ensuring sensitive data is not transmitted in violation of organizational policies. However, DPI can sometimes encounter issues due to misconfigurations, environmental factors, or software limitations. This article provides a comprehensive guide to troubleshooting and resolving common DPI-related issues.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| DPI not functioning for Mac users | No alerts for sensitive text input in Chrome; file uploads blocked correctly | Verify DPI settings, check URL categories for trailing spaces | Remove trailing spaces from URL categories | [DPI not functioning for Mac users](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BXMHyIAP/view) |
| DPI blocks client certificates on smart cards | Unable to access `https://public.cyber.mil/` with DPI enabled | Enable Peer Certificate Validation and DPI Bypass, add domain to allowlist | Upgrade EPP client and configure DPI settings | [DPI blocks client certificates on smart cards](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C1d0SIAR/view) |
| CAP logs missing in reports | CAP logs not visible in reports despite successful communication | Verify server communication, check CAP report logs | Apply Hotfix 1.1 to resolve logging bug | [CAP logs missing in reports](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CcI1pIAF/view) |
| DPI bypassed traffic events | Excessive bypass logs generated | Review DPI bypass settings in Device Control | Adjust bypass settings to reduce logs | [DPI bypassed traffic events](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CgcUzIAJ/view) |
| Audit logs not downloadable | Unable to download audit logs for a specific month | Verify audit backup process | Check audit backups and provide guidance | [Audit logs not downloadable](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CvVjJIAV/view) |
| Deprecated TLS versions enabled with DPI | DPI allows weak cipher suites and deprecated TLS versions | Test with updated OpenSSL library | Upgrade to OpenSSL 3.0 LTS in test builds | [Deprecated TLS versions enabled with DPI](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000D4eLyIAJ/view) |
| Amazon Workspaces client fails with DPI | Amazon Workspaces client does not load with DPI enabled | Test with Stealthy DPI enabled | Enable Stealthy DPI to resolve conflict | [Amazon Workspaces client fails with DPI](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000D7wPZIAZ/view) |
| Users can delete files despite monitoring | EPP cannot block file deletions | Enable File Tracing to monitor deletions | Use File Tracing for visibility | [Users can delete files despite monitoring](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DB5RVIA1/view) |
| Browsing blocked with DPI enabled | Websites inaccessible with DPI enabled | Check `eppsplit.log` for errors, test with updated build | Apply fix in build 5941 | [Browsing blocked with DPI enabled](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DEaAbIAL/view) |
| SSL Inspection bypasses DPI | DPI bypassed for all websites with SSL Inspection enabled | Regenerate SSL Inspection certificate | Ensure compatibility with DPI | [SSL Inspection bypasses DPI](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DhGhxIAF/view) |

---

## Detailed Issues

### DPI Not Functioning for Mac Users
**Symptoms:**  
- No alerts generated for sensitive text input in Chrome.  
- File uploads containing sensitive information are blocked correctly.

**Troubleshooting Steps:**  
1. Verify DPI settings for affected users.  
2. Test functionality with the latest EPP agent version.  
3. Check URL categories for trailing spaces.  
4. Gather logs during testing to analyze DPI behavior.

**Root Cause:**  
Trailing spaces in URL category names caused DPI to malfunction.

**Solution:**  
- Remove trailing spaces from URL categories in the EPP configuration.  
- Retest DPI functionality to confirm resolution.

**Source Ticket:** [DPI not functioning for Mac users](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BXMHyIAP/view)

---

### DPI Blocks Client Certificates on Smart Cards
**Symptoms:**  
- Unable to access `https://public.cyber.mil/` with DPI enabled.  
- Client certificate stored on a smart card is not recognized.

**Troubleshooting Steps:**  
1. Upgrade EPP client to the latest version.  
2. Enable Peer Certificate Validation and DPI Bypass in DPI settings.  
3. Add the domain to the DPI allowlist.  
4. Collect diagnostic logs for further analysis.

**Root Cause:**  
DPI configuration prevented proper use of client certificates.

**Solution:**  
- Upgrade to EPP client version 6.2.2.1.  
- Configure DPI settings to allow the domain and enable Peer Certificate Validation.

**Source Ticket:** [DPI blocks client certificates on smart cards](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C1d0SIAR/view)

---

### CAP Logs Missing in Reports
**Symptoms:**  
- CAP logs not visible in reports despite successful server communication.  

**Troubleshooting Steps:**  
1. Verify server communication and CAP policy application.  
2. Check CAP report logs for missing entries.  
3. Apply relevant hotfixes to address known issues.

**Root Cause:**  
A bug in CoSoSys Endpoint Protector Hotfix #1 caused CAP logs to stop processing.

**Solution:**  
- Apply Hotfix 1.1 to resolve the logging issue.  
- Confirm logs appear in CAP reports after applying the fix.

**Source Ticket:** [CAP logs missing in reports](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CcI1pIAF/view)

---

### DPI Bypassed Traffic Events
**Symptoms:**  
- Excessive DPI bypass logs generated.  

**Troubleshooting Steps:**  
1. Review DPI bypass settings in Device Control.  
2. Adjust settings to reduce unnecessary bypass logs.

**Root Cause:**  
DPI bypass logs are generated for connections deemed irrelevant to the EPP client.

**Solution:**  
- Modify bypass settings in Device Control to manage log visibility.  

**Source Ticket:** [DPI bypassed traffic events](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CgcUzIAJ/view)

---

## Best Practices
1. **Regular Configuration Audits:** Periodically review DPI and CAP policy settings to ensure proper functionality.  
2. **Log Management:** Monitor log sizes and implement rotation to prevent disk space issues.  
3. **Certificate Management:** Use the correct certificate file types (.pem) for deployment and ensure they are trusted.  
4. **Testing in Controlled Environments:** Test updates, patches, and configuration changes in a non-production environment before deployment.  
5. **Enable Stealthy DPI:** Use Stealthy DPI for applications that conflict with standard DPI settings.  
6. **Avoid Trailing Spaces:** Ensure URL categories and other configuration fields do not contain trailing spaces.  

---

## Advanced Topics

### DPI and SSL Inspection Compatibility
**Scenario:** DPI bypasses all traffic when SSL Inspection is enabled on a Fortigate device.  
**Solution:**  
- Regenerate the SSL Inspection certificate to ensure compatibility with DPI.  
- Test DPI functionality after applying the new certificate.  

**Source Ticket:** [SSL Inspection bypasses DPI](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DhGhxIAF/view)

---

### DPI and VPN Traffic
**Scenario:** DPI does not function correctly when users are connected via VPN.  
**Solution:**  
- Enable "Intercept VPN Traffic" in the console settings.  
- Verify DPI functionality with test websites.  

**Source Ticket:** [DPI and VPN Traffic](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000F6ZqbIAF/view)