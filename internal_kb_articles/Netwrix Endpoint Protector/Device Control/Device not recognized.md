# Netwrix Endpoint Protector Knowledge Base: Device Control - Device Not Recognized

## Overview
Netwrix Endpoint Protector (EPP) is a robust platform designed to manage and secure devices across enterprise environments. The "Device Control" feature ensures that connected devices are recognized, managed, and controlled according to organizational policies. However, issues may arise where devices are not recognized or blocked unexpectedly. This article provides a comprehensive guide to troubleshooting, resolving, and preventing such issues.

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Zebra USB printer not recognized | Printer blocked unless USB printing support enabled globally | Verify printer recognition with USB printing support enabled | Update to Windows agents version 6.2.3.0037 or later | [Zebra USB Printer Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BOQr3IAH/view) |
| USB headset and camera not detected | Devices not recognized after enabling DLP | Collect logs, escalate to R&D, test build provided | Apply test build; fix included in version 5.9.5.0 | [DLP Device Recognition Conflict](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ByhrmIAB/view) |
| Domain migration reporting issue | Computers report old domain names in EPP console | Verify domain synchronization status | Synchronize new domain into EPP console | [Domain Migration Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000COD5FIAX/view) |
| Update notification persists | Update applied but notification remains; no data logging | Investigate backend configuration | Correct backend settings via SSH | [Update Notification Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CYomfIAD/view) |
| Devices offline after license renewal | Devices appear offline; last seen date not updated | Check `epp.nginx.conf` file configuration | Adjust `epp.nginx.conf` to normal configuration | [License Renewal Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DBsLnIAL/view) |
| Agent deployment visibility issue | Only 500 out of 1500 agents visible in WebUI | Verify SCCM deployment and communication | Known WebUI limitation; monitor updates | [Agent Deployment Visibility](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DkiBUIAZ/view) |
| Card printer blocked | Printer offline despite being connected | Adjust device settings in EPP client | Correct device permissions in EPP client | [Card Printer Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DnmDhIAJ/view) |
| Intel LTE card hidden in Device Manager | Device disabled by EPP client | Check device status with and without EPP client | Correct EPP settings; reinstall client | [Intel LTE Card Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EAGEkIAP/view) |
| AirDrop not detected | AirDrop functionality not recognized or blocked | Review device control settings | Adjust configuration to block AirDrop | [AirDrop Detection Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EAGEkIAP/view) |
| MediaTek WiFi adapter not recognized | Device not visible in EPP console | Update server and client versions | Update EPP server to version 5.9.4.1 | [MediaTek WiFi Adapter Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EIj9vIAD/view) |
| Canon scanner not recognized | Scanner not visible in server console | Check logs, whitelist using VID/PID | Whitelist device; monitor for patch updates | [Canon Scanner Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FfsqDIAR/view) |
| RFID reader marked as blocked | Device operational but marked as blocked | Verify device functionality | Issue resolved; no further action needed | [RFID Reader Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000H04GNIAZ/view) |
| SD Card Reader security gap | Inbuilt SD Card Reader not controlled by EPP | Investigate SD Card identification limitations | Control SD Card Reader hardware | [SD Card Reader Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LgnUsIAJ/view) |
| Licensing issues on EPP panel | Machines offline; licenses not applied | Use zap tool to remove and reinstall agent | Reinstall agent using zap tool | [Licensing Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MtbezIAB/view) |
| USB device missing from list | Deleted device not visible in device list | Reconnect device and update policies | Reconnect device; update policies | [USB Device Visibility Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MUSDWIA5/view) |
| Google Pixel device details missing | Device code/serial number not displayed | Reinstall EPP client; install DPI certificate | Correct client configuration; install DPI certificate | [Google Pixel Device Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NQit2IAD/view) |
| Docking stations blocked | Docking stations categorized as blocked | Adjust global rights settings | Allow USB and Unknown Devices in global rights | [Docking Station Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Od8KtIAJ/view) |
| Linux servers not recognized | Servers not appearing in EPP console | Verify `options.sh` configuration | Correct `options.sh` file; reinstall client | [Linux Server Recognition Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OOXRdIAP/view) |

---

## Detailed Issues

### Zebra USB Printer Not Recognized
**Symptoms:** Zebra USB printer blocked unless USB printing support enabled globally.  
**Troubleshooting Steps:**  
1. Verify printer recognition with USB printing support enabled.  
2. Discuss potential exceptions with engineering.  
3. Confirm resolution after enabling USB printing support.  

**Root Cause:** Default settings blocked recognition without USB printing support.  
**Solution:** Update to Windows agents version 6.2.3.0037 or later.  
**Source Ticket:** [Zebra USB Printer Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BOQr3IAH/view)

---

### USB Headset and Camera Not Detected
**Symptoms:** Devices not recognized after enabling DLP features.  
**Troubleshooting Steps:**  
1. Collect logs from affected devices.  
2. Escalate issue to R&D team.  
3. Provide test build for customer testing.  

**Root Cause:** Conflict between DLP settings and device recognition.  
**Solution:** Apply test build; fix included in version 5.9.5.0.  
**Source Ticket:** [DLP Device Recognition Conflict](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ByhrmIAB/view)

---

### Domain Migration Reporting Issue
**Symptoms:** Computers report old domain names in EPP console.  
**Troubleshooting Steps:**  
1. Verify domain synchronization status.  
2. Provide documentation for domain synchronization.  
3. Follow up with customer post-synchronization.  

**Root Cause:** Lack of synchronization between new domain and EPP console.  
**Solution:** Synchronize new domain into EPP console.  
**Source Ticket:** [Domain Migration Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000COD5FIAX/view)

---

### Update Notification Persists
**Symptoms:** Update applied but notification remains; no data logging.  
**Troubleshooting Steps:**  
1. Investigate backend configuration.  
2. Schedule SSH access session.  
3. Correct backend settings via remote session.  

**Root Cause:** Backend configuration issue post-update.  
**Solution:** Correct backend settings via SSH.  
**Source Ticket:** [Update Notification Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CYomfIAD/view)

---

## Best Practices
- **Regular Updates:** Ensure all EPP server and client versions are up-to-date to avoid compatibility issues.
- **Configuration Reviews:** Periodically review global rights and device control settings to prevent unexpected behavior.
- **Documentation:** Maintain detailed records of configuration changes for future reference.
- **Testing:** Test new configurations in controlled environments before deploying to production systems.
- **Communication:** Inform customers of known limitations and provide clear instructions for resolving issues.

---

## Advanced Topics
### Managing Inbuilt SD Card Readers
Due to identification limitations, SD Cards cannot be controlled directly. Focus on managing the SD Card Reader hardware to enforce security policies effectively.

### Using the Zap Tool
The zap tool is an internal utility for removing EPP agents in extraordinary situations. Ensure it is deleted after use and not shared externally.

---

End of Article.