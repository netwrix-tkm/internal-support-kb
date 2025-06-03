# Netwrix Endpoint Protector: Content-Aware Protection - Upload Not Blocked

## Overview

The Content-Aware Protection (CAP) feature in Netwrix Endpoint Protector is designed to monitor and block unauthorized file uploads across various platforms and applications. However, misconfigurations, environmental factors, or software limitations can lead to scenarios where uploads are not blocked as expected. This document provides a comprehensive guide to troubleshooting and resolving such issues, along with best practices to prevent them.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| CAP policy not blocking email attachments | File attachments blocked on web URLs but not in email clients | Verify CAP policy configuration and enable "Report Only" action for monitoring | Confirm CAP policy configuration and enable monitoring | [Upload Not Blocked in Email Clients](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BeCNVIA3/view) |
| Inconsistent blocking on WhatsApp | File uploads partially blocked on WhatsApp | Check CAP settings and network connectivity | Adjust CAP settings for consistent blocking | [WhatsApp Upload Blocking Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BhMGfIAN/view) |
| Uploads bypass CAP in New Outlook on macOS | Files not blocked despite CAP policy | Verify known limitations with New Outlook and Microsoft Sync Technology | Inform customer of limitation and monitor for updates | [New Outlook Limitation](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BjuXZIAZ/view) |
| JPEG uploads bypass OCR policy in Teams | JPEG files not blocked during uploads to Teams | Verify OCR and DPI settings for Teams exit point | Enable Text Inspection and DPI for Teams | [OCR Policy Issue in Teams](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bk20TIAR/view) |
| PRT files not blocked | PRT files uploaded without remediation | Test with larger files and verify file classification | Install updated client version with fix | [PRT File Blocking Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CJJuVIAX/view) |
| Gmail reporting confusion | CAP reports show "webbrowser" instead of email details | Enable EPP network extension and clarify reporting behavior | Educate customer on EPP limitations for drafts | [Gmail Reporting Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CmCuPIAV/view) |
| DPI misconfiguration for Teams | Files not blocked in Teams but blocked on WeTransfer | Verify DPI settings and allowlist configuration | Adjust DPI settings and allowlist | [DPI Misconfiguration for Teams](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CvVszIAF/view) |
| Skype uploads not blocked | Files uploaded via Skype desktop app | Add missing process name to monitored list | Update to version 5.9.4.1 with fix | [Skype Blocking Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EqBQjIAN/view) |
| DPI certificate inactive on Ubuntu | File uploads bypass CAP on Ubuntu | Restart browser and verify DPI certificate | Inform users to reboot after updates | [DPI Certificate Issue on Ubuntu](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FieadIAB/view) |
| CAP instability in MS Teams | Inconsistent blocking in Teams | Test with "Restrict Content Detection" option | Upgrade to version 5.9.4.1 with fix | [CAP Instability in Teams](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FJGrgIAH/view) |
| CAP rules not effective in Teams | File uploads bypass CAP in Teams | Enable DPI and Stealthy DPI settings | Activate DPI settings for Teams | [CAP Rules Not Effective in Teams](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FoOrJIAV/view) |
| Gsuite uploads bypass CAP | Files not blocked on Gsuite | Enable File Hash option in Global settings | Adjust CAP configuration for Gsuite | [Gsuite Upload Blocking Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GEWA8IAP/view) |
| VPN conflicts on macOS | CAP not blocking uploads on macOS | Disable conflicting VPNs or proxies | Ensure EPP is primary traffic handler | [VPN Conflicts on macOS](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Gj1unIAB/view) |
| Teams desktop app bypasses CAP | Teams desktop app uploads not blocked | Verify DPI and rights functionality | Upgrade to version 6.2.4.0031 | [Teams Desktop App Bypasses CAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GXRY8IAP/view) |
| Encryption bypass in web apps | WhatsApp Web uploads bypass CAP | Verify encryption status of web apps | Block access via URL Denylist | [Encryption Bypass in Web Apps](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HwpgHIAR/view) |
| Regex denylist not blocking | Specific URLs bypass denylist | Test regex on supported sites | Inform customer of text inspection limitations | [Regex Denylist Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000I3JqAIAV/view) |
| License expiry disables CAP | CAP logging stops after license expiry | Verify license status and renew | Apply license extension key | [License Expiry Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000I8U3NIAV/view) |
| OneDrive uploads bypass CAP | Files uploaded to OneDrive via Teams | Apply allowlist twice in CAP policy | Await fix in next update | [OneDrive Uploads Bypass CAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IFGQIIA5/view) |
| Web Outlook uploads bypass CAP | CAP not blocking uploads in Web Outlook | Verify browser compatibility and CAP settings | Confirm CAP configuration | [Web Outlook Uploads Bypass CAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IuG4XIAV/view) |
| Taiwan SSN not detected | Taiwan SSN bypasses CAP | Test detection with DPI enabled | Investigate detection limitations | [Taiwan SSN Detection Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000J7RN8IAN/view) |
| MiP policy conflicts on macOS | CAP fails after MiP policy integration | Reinstall EPP client and restart | Ensure network extension is active | [MiP Policy Conflicts on macOS](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JGilKIAT/view) |
| CAP inconsistency in Teams | Teams uploads inconsistently blocked | Restart Teams after policy changes | Await fix in version 5.9.4.3 | [CAP Inconsistency in Teams](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JXzJZIA1/view) |
| OneDrive uploads bypass CAP | Sensitive data not blocked in OneDrive | Include OneDrive in CAP exit points | Create new policy with correct settings | [OneDrive Uploads Bypass CAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KOoMlIAL/view) |
| Ubuntu CAP policy not working | CAP policy not generating reports | Verify EPP client compatibility | Provide updated EPP client | [Ubuntu CAP Policy Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Lt3kMIAR/view) |
| Slack URLs bypass denylist | Lightshot URLs not blocked in Slack | Modify detection logic for Slack URLs | Await fix in version 5943 | [Slack URLs Bypass Denylist](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MGRZ5IAP/view) |
| CAP fails on specific Mac | CAP not detecting SSNs on one Mac | Disable DPI and test uploads | Adjust bypass rule in settings | [CAP Fails on Specific Mac](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OJUCfIAP/view) |
| File size threshold misconfiguration | CAP not blocking uploads as expected | Disable "Apply Policy if File Size Threshold is Matched" | Adjust CAP policy settings | [File Size Threshold Misconfiguration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OJUCfIAP/view) |

---

## Detailed Issues

### Issue: CAP Policy Not Blocking Email Attachments
**Symptoms:** File attachments blocked on web URLs but not in email clients.  
**Troubleshooting Steps:**
1. Verify CAP policy configuration.
2. Enable "Report Only" action to monitor file types.  
**Root Cause:** CAP policy was configured to block based on file extensions but not email attachments.  
**Solution:** Confirm CAP policy configuration and enable monitoring.  
**Source Ticket:** [Upload Not Blocked in Email Clients](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BeCNVIA3/view)

---

## Best Practices

- **Policy Testing:** Always test CAP policies in all intended environments (e.g., web, email clients, desktop apps) before deployment.
- **Regular Updates:** Keep the Endpoint Protector server and client software updated to the latest versions.
- **DPI Configuration:** Ensure DPI and Stealthy DPI settings are enabled for all relevant exit points.
- **User Education:** Train users on CAP policy configurations and limitations to avoid misunderstandings.
- **System Reboots:** Encourage regular system reboots after updates to ensure proper functionality.

---

## Advanced Topics

### Handling Encrypted Web Applications
Encrypted platforms like WhatsApp Web and Telegram Web may bypass CAP due to end-to-end encryption. In such cases:
- Use a URL Denylist to block access to these platforms.
- Educate users on the limitations of monitoring encrypted traffic.

### Debugging DPI Certificate Issues
If the DPI certificate is inactive:
1. Restart the browser or system.
2. Verify the certificate is installed in the browser's certificate store.
3. Inform users about the importance of reboots after updates.

