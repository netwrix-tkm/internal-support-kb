# Netwrix Endpoint Protector Knowledge Base: Client Device Recognition

## Overview
Netwrix Endpoint Protector's Client Device Recognition feature ensures secure and accurate identification of devices connected to the network. Common issues include device registration failures, misconfigurations, compatibility problems, and communication disruptions between clients and servers. This article provides troubleshooting procedures, root cause analyses, and tested solutions for resolving these issues effectively.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Device not appearing in admin portal | Device remains unregistered after client installation | Confirm device name, reinstall client | Reinstall EPP client | [Device Registration Failure](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BSPI5IAP/view) |
| COM Port devices not recognized | COM Port devices fail to appear in system | Start logs, apply offline patches | Upgrade server using offline patches | [COM Port Recognition Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CFjifIAD/view) |
| Duplicate entries in EPP console | Multiple duplicate laptop entries in console | Review client recognition settings | Correct recognition settings, remove duplicates | [Duplicate Device Entries](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CswGEIAZ/view) |
| Server shows PC as offline | Agent reports connection, server shows offline | Check logs, reinstall client | Restore communication during remote session | [Offline Device Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Cvf5xIAB/view) |
| Audio devices not recognized | Audio devices fail to connect or display correctly | Deploy test build, apply patch | Apply patch to fix audio recognition bug | [Audio Device Recognition Bug](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FfR22IAF/view) |
| CentOS clients offline | CentOS clients show "expired=1" in config file | Upgrade client, check licenses | Upgrade client to latest version | [CentOS Client Offline](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FPrBqIAL/view) |
| USB permissions misconfigured | USB devices not blocked or permissions unclear | Review USB permission settings | Configure trusted devices with correct permissions | [USB Permissions Misconfiguration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GHBYwIAP/view) |
| Device not recognized after update | Device fails to appear after client update | Verify compatibility, restart server | Update client to compatible version | [Device Recognition Post-Update](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HMtVXIA1/view) |
| Hosted server migration issues | USB devices not blocked on migrated server | Re-register clients, reinstall client | Re-register clients in backend | [Hosted Server Migration Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IFQUUIA5/view) |
| Missing client details in portal | Portal shows device names but no usernames/IPs | Re-register clients, monitor updates | Re-register clients to restore communication | [Missing Client Details](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IyaBDIAZ/view) |
| Incorrect device type displayed | Windows machines shown as Mac in console | Verify recognition settings | Correct console configurations | [Incorrect Device Type](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Jh6tdIAB/view) |
| Hostname overwriting issue | Hostname overwritten post-installation | Check installation settings | Correct hostname assignment | [Hostname Overwriting Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Jp49xIAB/view) |
| USB device not detected | USB device connected to voting boxes not recognized | Review USBDeview logs, update client | Update client to latest version | [USB Device Detection Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JSdWZIA1/view) |
| Complete device block | EPP client blocks all external access | Generate offline password, execute VB script | Use VB script to remove EPP client | [Complete Device Block](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MHJUcIAP/view) |
| Missing devices in control list | No devices displayed in control list | Check certificates, verify digital signature | Install missing root certificates | [Missing Devices in Control List](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MLmL8IAL/view) |
| Missing computers in server list | Computers not listed in server appliance | Analyze logs, reinstall client | Reinstall client to replace missing file | [Missing Computers in Server List](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MXJQbIAP/view) |
| Ubuntu client download request | Request for Ubuntu 24.04 client | Verify server version, provide links | Provide download links for Ubuntu clients | [Ubuntu Client Download Request](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NlenxIAB/view) |
| Placeholder IP in deployment | Placeholder IP prevents client-server communication | Update deployment configuration | Replace placeholder IP with actual server IP | [Placeholder IP Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NmJZQIA3/view) |
| Virtual hard drives blocked | Virtual drives inaccessible on VM | Upgrade EPP server and client | Apply patches sequentially | [Virtual Hard Drives Blocked](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NQIdZIAX/view) |
| NAT configuration for OOO user | OOO user unable to connect to server | Configure NAT without SSL termination | Implement NAT for server communication | [NAT Configuration Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NyyYjIAJ/view) |
| Undetected endpoints | Endpoints not listed in Computers section | Perform clean client installation | Reinstall latest client version | [Undetected Endpoints](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OwpHOIAZ/view) |

---

## Detailed Issues

### Device Registration Failure
**Symptoms:** Device remains unregistered in the admin portal after client installation.  
**Troubleshooting Steps:**  
1. Confirm device name and EPP client version.  
2. Restart the PC and update policies.  
3. Reinstall the EPP client.  

**Root Cause:** Certificate issues within the EPP client prevented device registration.  
**Solution:** Reinstall the EPP client to resolve certificate-related problems.  
**Source Ticket:** [Device Registration Failure](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BSPI5IAP/view)

---

### COM Port Recognition Issue
**Symptoms:** COM Port devices fail to appear in the system.  
**Troubleshooting Steps:**  
1. Start logs on Mac using terminal commands.  
2. Apply offline patches to upgrade the EPP server.  
3. Ensure sufficient disk space before patching.  

**Root Cause:** Closed network environment prevented updates and patches.  
**Solution:** Upgrade the server using offline patches and OVF image for simplification.  
**Source Ticket:** [COM Port Recognition Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CFjifIAD/view)

---

### Duplicate Device Entries
**Symptoms:** Multiple duplicate laptop entries in the EPP console.  
**Troubleshooting Steps:**  
1. Review client device recognition settings.  
2. Remove duplicate entries manually.  

**Root Cause:** Misconfiguration in client device recognition settings.  
**Solution:** Correct recognition settings and remove duplicates.  
**Source Ticket:** [Duplicate Device Entries](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CswGEIAZ/view)

---

### Complete Device Block
**Symptoms:** EPP client blocks all external access methods, including LAN, WLAN, USB, and Internet.  
**Troubleshooting Steps:**  
1. Attempt to uninstall the EPP client via Control Panel.  
2. Generate an Offline Temporary Password.  
3. Execute VB script via CLI with administrator rights.  

**Root Cause:** Strict access controls enforced by the EPP client.  
**Solution:** Use VB script to remove the EPP client and restore access.  
**Source Ticket:** [Complete Device Block](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MHJUcIAP/view)

---

## Best Practices
- **Regular Updates:** Ensure all clients and servers are running the latest versions to avoid compatibility issues.  
- **Certificate Management:** Verify that root certificates are installed and trusted, especially in offline environments.  
- **Deployment Configuration:** Replace placeholder values with actual server details during deployment.  
- **Patch Application:** Apply patches sequentially and monitor logs for errors.  
- **Backup Procedures:** Create VM snapshots before upgrades to ensure rollback options.  

---

## Advanced Topics

### NAT Configuration for Remote Users
**Scenario:** Connecting out-of-office users to on-premises servers without FQDN.  
**Solution:** Configure NAT or port forwarding from a public IP to allow communication. Avoid SSL termination to maintain certificate integrity.  
**Source Ticket:** [NAT Configuration Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NyyYjIAJ/view)

---

End of Article.