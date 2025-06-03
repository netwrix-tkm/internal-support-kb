# Netwrix Endpoint Protector: Client/OS Performance Knowledge Base

## Overview

Netwrix Endpoint Protector (EPP) is a robust Data Loss Prevention (DLP) solution designed to secure sensitive data across endpoints. The Client/OS Performance component ensures smooth operation of endpoint devices while enforcing security policies. However, certain issues may arise due to software updates, configuration conflicts, or environmental factors. This article provides a comprehensive guide to troubleshooting and resolving common Client/OS Performance issues.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Bluetooth devices greyed out after upgrade | Previously connected Bluetooth devices non-functional | Check Device Control settings and logs | Provide test build with fix | [Bluetooth Devices Greyed Out](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BOHBJIA5/view) |
| High memory usage on Windows agents | Excessive RAM usage (1-50GB) | Exclude drives from file tracing | Add drives to allowlist | [High Memory Usage](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C3YhRIAV/view) |
| File transfer speed throttling | Slow USB file transfers after daily limit alert | Analyze file transfer settings | Disable file transfer threshold | [File Transfer Throttling](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DXoMjIAL/view) |
| SSLSplit.exe crashes | Frequent crashes with Stealthy DPI enabled | Investigate thread safety in `libevent` | Update to fixed version | [SSLSplit Crashes](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EfJppIAF/view) |
| Unable to access specific tabs in Rancher Desktop | Tabs inaccessible with EPP enabled | Reset Rancher application settings | Perform factory reset | [Rancher Desktop Tabs](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GIpkPIAT/view) |
| Performance degradation with Visual Studio | Slow performance during POC | Add Visual Studio processes to exception list | Whitelist processes | [Visual Studio Performance](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GKyoPIAT/view) |
| Printing blocked in Outlook | DLP block pop-up during printing | Review CAP policies and logs | Upgrade EPP client and server | [Outlook Printing Blocked](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LAJ3kIAH/view) |
| AWS workspace instability after license import | Users unable to log in; temporary profiles created | Upgrade EPP server and client | Update to compatible versions | [AWS Workspace Instability](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O46fLIAR/view) |

---

## Detailed Issues

### Bluetooth Devices Greyed Out After Upgrade
**Symptoms:** Previously connected Bluetooth devices became greyed out and non-functional after upgrading to EPP version 3.0.2.1 on macOS. New devices worked correctly.

**Troubleshooting Steps:**
1. Verify if devices are disconnected or blocked in Device Control settings.
2. Request logs from the customer for analysis.
3. Provide a test build containing a fix for the issue.

**Root Cause:** A known bug in EPP version 3.0.2.1 caused previously connected Bluetooth devices to become non-functional.

**Solution:** Provide the test build `EPPMac3.0.3.0002.Notarized.zip` to resolve the issue. Monitor for the official fix in version 5.9.4.0.

**Source Ticket:** [Bluetooth Devices Greyed Out](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BOHBJIA5/view)

---

### High Memory Usage on Windows Agents
**Symptoms:** Windows EPP agents consumed 1-50GB of RAM due to excessive file tracing on drives hosting SCADA applications.

**Troubleshooting Steps:**
1. Create global file extension tracing exclusions.
2. Disable file tracing temporarily.
3. Add affected drives to the allowlist in EPP settings.

**Root Cause:** Excessive logging of file operations on heavily utilized drives treated as removable drives.

**Solution:** Add the D: and F: drives to the allowlist, reducing memory usage to under 40MB per host.

**Source Ticket:** [High Memory Usage](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C3YhRIAV/view)

---

### File Transfer Speed Throttling
**Symptoms:** File transfer speed to USB storage slowed significantly after hitting the daily file transfer limit.

**Troubleshooting Steps:**
1. Review file transfer threshold settings.
2. Analyze logs for throttling behavior.
3. Disable the file transfer threshold setting.

**Root Cause:** File transfer threshold settings inadvertently limited transfer speeds.

**Solution:** Disable the file transfer threshold to restore normal speeds.

**Source Ticket:** [File Transfer Throttling](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DXoMjIAL/view)

---

### SSLSplit.exe Crashes
**Symptoms:** SSLSplit.exe crashed weekly on 10% of machines with Stealthy DPI enabled.

**Troubleshooting Steps:**
1. Compare crash rates between EPP versions.
2. Investigate thread safety in the `libevent` library.
3. Test and deploy a fixed version.

**Root Cause:** A race condition in the `libevent` library caused by improper thread safety.

**Solution:** Update to EPP version 5941, which includes fixes for thread safety issues.

**Source Ticket:** [SSLSplit Crashes](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EfJppIAF/view)

---

### Unable to Access Specific Tabs in Rancher Desktop
**Symptoms:** Certain tabs in Rancher Desktop were inaccessible with EPP enabled.

**Troubleshooting Steps:**
1. Verify access with EPP disabled.
2. Collect logs during the issue.
3. Reset Rancher application settings.

**Root Cause:** Application-specific issue requiring a reset.

**Solution:** Perform a factory reset of Rancher Desktop settings.

**Source Ticket:** [Rancher Desktop Tabs](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GIpkPIAT/view)

---

### Performance Degradation with Visual Studio
**Symptoms:** Severe performance drops when using Visual Studio during POC testing.

**Troubleshooting Steps:**
1. Add Visual Studio processes to the exception list.
2. Test performance after adjustments.
3. Monitor for further issues.

**Root Cause:** EPP client interference with Visual Studio processes.

**Solution:** Whitelist Visual Studio processes in the EPP client settings.

**Source Ticket:** [Visual Studio Performance](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GKyoPIAT/view)

---

### Printing Blocked in Outlook
**Symptoms:** DLP block pop-up appeared when attempting to print emails from Outlook.

**Troubleshooting Steps:**
1. Review CAP policies and logs.
2. Add `outlook.exe` to Advanced Scanning Exceptions.
3. Upgrade to the latest EPP client and server versions.

**Root Cause:** Hidden CAP policy blocking print actions.

**Solution:** Upgrade to EPP client version 6.2.4.2 and server version 5.9.4.1.

**Source Ticket:** [Outlook Printing Blocked](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LAJ3kIAH/view)

---

### AWS Workspace Instability After License Import
**Symptoms:** Users unable to log in; temporary profiles created after license import.

**Troubleshooting Steps:**
1. Verify CAP policies and device settings.
2. Upgrade EPP server and client versions.
3. Restart affected machines.

**Root Cause:** Compatibility issues between EPP server and client versions.

**Solution:** Upgrade to EPP server version 5.9.4.1 and client version 6.2.4.2000.

**Source Ticket:** [AWS Workspace Instability](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O46fLIAR/view)

---

## Best Practices

1. **Regular Updates:** Always use the latest EPP client and server versions to ensure compatibility and access to bug fixes.
2. **Testing Before Deployment:** Test new versions or configurations on a single machine before rolling out to the entire environment.
3. **Monitor Logs:** Regularly review logs for anomalies or potential issues.
4. **Whitelist Critical Applications:** Add frequently used applications like Outlook or Visual Studio to exception lists to avoid disruptions.
5. **Backup Configurations:** Take snapshots of the EPP appliance before making significant changes.

---

## Advanced Topics

### Debugging DPI Issues on Linux
- Ensure the use of supported LTS versions of Ubuntu.
- Collect logs and verify CAP policy behavior with and without DPI enabled.
- Escalate unresolved issues to R&D for further analysis.

### Handling Stealthy DPI Crashes
- Monitor thread safety in libraries like `libevent`.
- Test new builds in controlled environments before deployment.

--- 

End of Article.