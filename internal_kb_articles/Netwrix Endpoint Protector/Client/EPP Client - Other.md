# Netwrix Endpoint Protector Knowledge Base: EPP Client - Other

## Overview
The Netwrix Endpoint Protector (EPP) Client is a critical component for endpoint security, offering features such as Data Loss Prevention (DLP), Deep Packet Inspection (DPI), device control, and content-aware protection. This article consolidates common issues, troubleshooting procedures, root cause analyses, and tested solutions related to the EPP Client across various environments, including Windows, macOS, and Linux. It also includes best practices and advanced topics to help support engineers resolve issues efficiently and prevent recurring problems.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| USB keyboards blocked on Windows 11 | USB keyboards blocked by EPP on new PCs | Verify Minifilter settings and reinstall EPP client | Enable Minifilter option in EPP settings | [USB Keyboards Blocked](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BjzfJIAR/view) |
| Rufus fails to format USB sticks | Formatting fails with EPP installed | Test formatting after uninstalling EPP; check "Unknown Device" settings | Allow "Unknown Device" category in EPP settings | [Rufus Formatting Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BpeI2IAJ/view) |
| Mac screenshot and AWS CLI issues | Screenshots and AWS CLI fail on macOS | Confirm compatibility and check configurations | Update macOS and verify EPP settings | [Mac Screenshot Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BPpVdIAL/view) |
| Excess licensed computers | More computers licensed than expected | Investigate backend processes and inactive computers | Execute SQL commands to clean up licenses | [Excess Licensed Computers](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BU329IAD/view) |
| Logs missing for encrypted USB devices | File transfer logs not retrieved | Test with new client build; collect logs | Deploy updated client build | [Encrypted USB Logs Missing](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BvuOzIAJ/view) |
| External storage blocked after OTP approval | Drives not detected after OTP approval | Check MDM settings and disk access permissions | Disable MDM restrictions; enable full disk access | [External Storage Blocked](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BXa4pIAD/view) |
| Content Integrity Fail events | Frequent integrity fail logs | Verify permissions, certificates, and configurations | Ensure full disk access and proper configurations | [Content Integrity Fail](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C4mLiIAJ/view) |
| DPI blocks Android Studio and Maven | Applications fail with DPI enabled | Test with Stealthy DPI; disable MTP | Enable Stealthy DPI feature | [DPI Blocking Applications](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CclyIIAR/view) |
| Tamper mode bypassed | EPP service stops despite tamper mode | Collect logs and monitor affected endpoints | Update EPP agent and monitor endpoints | [Tamper Mode Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CFrGPIA1/view) |
| Content Aware Protection missing | Feature not visible on outdated OS | Verify OS compatibility | Upgrade operating system | [Content Aware Protection Missing](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CfWQ1IAN/view) |
| Workstation name conflict | Endpoint Protector console alternates between two workstation names | Enable logging and update policies | Enable the virtual desktop clone feature | [Workstation Name Conflict](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FwFNqIAN/view) |
| File uploads blocked despite whitelisting | Files fail to upload with "Web Upload*[JS_ENABLED_FLAG]" error | Review policy settings and file types | Deselect "Unidentified File type" in policy settings | [File Uploads Blocked](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FYkRBIA1/view) |
| Endpoint connectivity issues | Endpoints show "NO" status for Windows and macOS clients | Check network connectivity and firewall settings | Resolve network configuration issues | [Endpoint Connectivity Issues](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GDdokIAD/view) |
| Compatibility with macOS 15 | Uncertainty about client compatibility with macOS 15 Sequoia | Review documentation and confirm compatibility | Confirm compatibility with macOS 15 Sequoia | [macOS Compatibility Inquiry](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GcFXtIAN/view) |
| Linux client request | Customer requested Linux client builds | Verify availability of Linux builds | Provide requested Linux builds | [Linux Client Request](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Gdp1aIAB/view) |
| Screen blinking on macOS | Screen flickers on macOS endpoints | Remove EPP client and monitor behavior | Update EPP client to resolve compatibility issues | [Screen Blinking on macOS](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GuoCFIAZ/view) |
| Bluetooth devices disabled | Bluetooth peripherals stop working after server upgrade | Check Bluetooth driver status and logs | Update EPP client to latest version | [Bluetooth Devices Disabled](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HINE8IAP/view) |
| VPN profile installation error | VPN profile fails to install via Jamf | Remove conflicting VPN services | Remove existing VPN services and retry | [VPN Profile Installation Error](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JhbRDIAZ/view) |
| Excessive notifications | Frequent pop-ups after DLP policy changes | Refine Content Aware Protection settings | Remove unnecessary monitored URL categories | [Excessive Notifications](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Kgj5FIAR/view) |
| OTP functionality failure | OTP feature returns invalid error | Test OTP functionality and upgrade client | Upgrade to EPP client version 6.2.4.2000 | [OTP Functionality Failure](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ks8hsIAB/view) |

---

## Detailed Issues

### USB Keyboards Blocked on Windows 11
**Symptoms:** USB keyboards are blocked by EPP on new PCs running Windows 11.  
**Solution:** Enable the Minifilter option in EPP settings.  

---

### Rufus Fails to Format USB Sticks
**Symptoms:** Rufus fails to format USB sticks when EPP is installed.  
**Solution:** Set "Unknown Device" category to "Allow Access" in EPP settings.  

---

### Mac Screenshot and AWS CLI Issues
**Symptoms:** Screenshots fail and AWS CLI does not function properly on macOS.  
**Solution:** Update macOS and verify EPP settings.  

---

### Excess Licensed Computers
**Symptoms:** More computers are licensed than expected.  
**Solution:** Execute SQL commands to clean up licenses:  
```sql
DELETE FROM certificate;
UPDATE license SET assigned_to = NULL;
UPDATE clientmachine SET reregister = 1, trialversion = NULL WHERE deleted = 0;
```

---

### Logs Missing for Encrypted USB Devices
**Symptoms:** Logs for file transfers from encrypted USB devices are not retrieved.  
**Solution:** Deploy updated client build.  

---

### External Storage Blocked After OTP Approval
**Symptoms:** Drives not detected after OTP approval.  
**Solution:** Disable MDM restrictions and enable full disk access.  

---

### Content Integrity Fail Events
**Symptoms:** Frequent integrity fail logs.  
**Solution:** Ensure full disk access and proper configurations.  

---

### DPI Blocks Android Studio and Maven
**Symptoms:** Applications fail with DPI enabled.  
**Solution:** Enable Stealthy DPI feature.  

---

### Tamper Mode Bypassed
**Symptoms:** EPP service stops despite tamper mode.  
**Solution:** Update EPP agent and monitor endpoints.  

---

### Content Aware Protection Missing
**Symptoms:** Feature not visible on outdated OS.  
**Solution:** Upgrade operating system.  

---

## Best Practices
1. **Regular Updates:** Keep EPP clients and servers updated.  
2. **Policy Review:** Regularly review and refine DLP and Content Aware Protection policies.  
3. **Compatibility Checks:** Verify OS compatibility before deploying EPP clients.  
4. **Testing Environment:** Test changes in a controlled environment before production deployment.  

---

## Advanced Topics

### Debug Logging Management
- Use the `eppclient_append.log` file for persistent logs.  
- Disable debug mode and reboot to refresh logs.  

### DPI Configuration for VPN Compatibility
- Enable the "Stealthy DPI Driver" to resolve VPN conflicts.  

---

End of Article.