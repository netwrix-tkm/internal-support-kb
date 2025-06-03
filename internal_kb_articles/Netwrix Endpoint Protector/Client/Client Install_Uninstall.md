# Netwrix Endpoint Protector: Client Install/Uninstall Knowledge Base

## Overview
The Netwrix Endpoint Protector (EPP) client is a critical component for managing endpoint security, including data loss prevention (DLP), device control, and compliance monitoring. This guide consolidates common issues, troubleshooting steps, and solutions related to the installation, uninstallation, and configuration of the EPP client across various operating systems and deployment methods. It also includes best practices and advanced topics to help support engineers resolve issues efficiently.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| DLP License Not Reflecting on Server | License installed on client but not visible on server | Reinstall client and verify connectivity | Reinstall client to restore license recognition | [DLP License Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bdhl8IAB/view) |
| Ubuntu 24.04 Compatibility | No compatible client available for Ubuntu 24.04 | Confirm compatibility with development team | Upgrade server to 5.9.4.1 and install compatible agent | [Ubuntu Compatibility](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000N5puHIAR/view) |
| MSI File Missing for Uninstallation | Unable to uninstall without MSI file | Provide zap tool or alternative uninstall methods | Use zap tool for uninstallation | [MSI File Missing](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BNgReIAL/view) |
| macOS Intune Deployment Script Missing | Deployment failed due to missing shell script | Provide required shell script | Share shell script for deployment | [macOS Intune Deployment](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C1cCPIAZ/view) |
| Windows Firewall Disabled During Installation | Installation failed with firewall off | Enable firewall temporarily during installation | Enable firewall, complete installation, then reconfigure | [Firewall Disabled](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GlYoFIAV/view) |
| Transparent Proxy Not Installed on macOS 15 | Proxy pop-up missing after upgrade | Perform clean macOS installation | Reinstall macOS 15 and retry | [Transparent Proxy Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GlvuTIAR/view) |
| SentinelOne Blocking Installation | SentinelOne flagged installation as suspicious | Disable SentinelOne and use zap tool | Use zap tool to clean remnants, then reinstall | [SentinelOne Blocking](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FpiCzIAJ/view) |
| Service Name Mismatch in Systemctl | Incorrect service name used in commands | Verify correct service name | Use `epp-client-daemon` instead of `epp-client-daemon-d` | [Service Name Mismatch](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FrGKYIA3/view) |
| Fedora Installer Request | Missing installer for Fedora 41 | Confirm availability, create product board request | Provide Fedora 40 and 41 installers | [Fedora Installer Request](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Hr2xxIAB/view) |
| Missing Uninstall Password | Unable to uninstall client without password | Provide zap tool for removal | Use zap tool to uninstall client | [Missing Uninstall Password](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OPxS5IAL/view) |
| macOS Notifications Missing | No notifications for policy violations | Verify notifier functionality and reinstall client | Update client to version 3.0.4.3 | [macOS Notification Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ntpe9IAB/view) |

---

## Detailed Issues and Solutions

### DLP License Not Reflecting on Server
**Symptoms:**  
- DLP license installed on the client but not visible on the server.  
- Clients unable to connect to the server despite updated policies.

**Troubleshooting Steps:**  
1. Verify that the license is installed on the client.  
2. Check server logs for connectivity issues.  
3. Attempt to uninstall and reinstall the client.  
4. Confirm that the uninstall password is valid.  

**Solution:**  
Reinstall the Endpoint Protector client on affected machines and verify that the license is recognized on the server after reinstallation.  

---

### Ubuntu 24.04 Compatibility
**Symptoms:**  
- No compatible EPP client available for Ubuntu 24.04.  

**Troubleshooting Steps:**  
1. Verify the EPP server version (ensure it is 5.9.4.1 or later).  
2. Inform the customer that the compatible client is available only for the latest server version.  
3. Provide download links for the compatible agent.  

**Solution:**  
Upgrade the server to version 5.9.4.1 and install the compatible agent.  

---

### MSI File Missing for Uninstallation
**Symptoms:**  
- Standard uninstallation command fails due to missing MSI file.  

**Troubleshooting Steps:**  
1. Attempt uninstallation using the MSI file path.  
2. Provide alternative methods, such as the zap tool.  

**Solution:**  
Use the zap tool to forcibly remove the EPP client. Ensure the zap tool is executed with administrative privileges.  

---

### macOS Intune Deployment Script Missing
**Symptoms:**  
- Deployment via Intune fails due to missing shell script.  

**Troubleshooting Steps:**  
1. Confirm the requirement for a shell script in the deployment process.  
2. Provide the necessary shell script to the customer.  

**Solution:**  
Share the shell script with the customer and provide guidance on its use.  

---

### Windows Firewall Disabled During Installation
**Symptoms:**  
- Installation fails with an error when the Windows firewall is disabled.  

**Troubleshooting Steps:**  
1. Verify that the firewall is disabled on the client machine.  
2. Attempt installation with the firewall temporarily enabled.  

**Solution:**  
Enable the firewall temporarily during installation. Once complete, reconfigure the firewall as needed.  

---

### Transparent Proxy Not Installed on macOS 15
**Symptoms:**  
- Transparent proxy pop-up does not appear after upgrading to macOS 15.  

**Troubleshooting Steps:**  
1. Verify the installation of the EPP client and certificate.  
2. Restart the MacBook and attempt to trigger the proxy pop-up.  
3. Perform a clean installation of macOS 15.  

**Solution:**  
Perform a full wipe and reinstall macOS 15. Retry the installation process.  

---

### SentinelOne Blocking Installation
**Symptoms:**  
- SentinelOne flags the EPP installation as suspicious.  

**Troubleshooting Steps:**  
1. Disable SentinelOne temporarily.  
2. Use the zap tool to clean remnants of previous installations.  
3. Perform a fresh installation of the EPP client.  

**Solution:**  
Use the zap tool to remove remnants, then reinstall the EPP client.  

---

### Service Name Mismatch in Systemctl
**Symptoms:**  
- Error message: "Unit epp-client-daemon-d.service could not be found."  

**Troubleshooting Steps:**  
1. Verify the service name using `ps ax | grep epp-client`.  
2. Use the correct service name (`epp-client-daemon`) in commands.  

**Solution:**  
Use `epp-client-daemon` as the correct service name.  

---

### Fedora Installer Request
**Symptoms:**  
- Customer requested installers for Fedora 40 and Fedora 41.  

**Troubleshooting Steps:**  
1. Provide the installer link for Fedora 40.  
2. Confirm availability of Fedora 41 installer with engineering.  

**Solution:**  
Share the Fedora 40 and 41 installer links with the customer.  

---

### macOS Notifications Missing
**Symptoms:**  
- Notifications for policy violations were not displayed.  

**Troubleshooting Steps:**  
1. Verify notifier functionality and check logs for errors.  
2. Ensure full disk access and DPI certificate import.  
3. Provide patch for updated client version (3.0.4.3).  

**Solution:**  
Update the client to version 3.0.4.3 to resolve notifier functionality.  

---

## Best Practices

1. **Pre-Installation Checks:**  
   - Ensure all remnants of previous installations are removed using tools like the zap tool.  
   - Verify compatibility with the operating system and network configuration.

2. **Backup MSI Files:**  
   - Retain MSI files for future uninstallation needs.  

3. **Use Latest Versions:**  
   - Ensure the latest versions of the EPP client and server are installed to avoid compatibility issues.  

4. **Document Configurations:**  
   - Maintain detailed records of configurations, including uninstall passwords and server settings.  

5. **License Management:**  
   - Regularly monitor license allocation and ensure devices are within the license limit.  

---

## Advanced Topics

### Using the Zap Tool for Uninstallation
The zap tool is a powerful utility for forcibly removing the EPP client. Use it only as a last resort and ensure administrative privileges are available.  
**Steps:**  
1. Obtain written agreement from the customer.  
2. Provide the zap tool and instruct the customer to run it as an administrator.  
3. Ensure the tool is deleted from the machine after use.  

**Warnings:**  
- Do not share the zap tool with third parties.  
- Use the tool responsibly and only in extraordinary circumstances.  

---

End of Article.