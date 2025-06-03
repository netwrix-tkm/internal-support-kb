# Netwrix Endpoint Protector Knowledge Base  
## Device Control: Device Rights  

### Overview  
The **Device Rights** feature in **Netwrix Endpoint Protector (EPP)** enables administrators to control access to devices such as USB drives, scanners, audio devices, and other peripherals. This functionality is critical for ensuring data security, compliance, and operational efficiency.  

This article consolidates troubleshooting guidance, solutions to common issues, best practices, and advanced topics related to Device Rights. It is designed to help administrators resolve issues effectively and optimize the use of the Device Control feature.  

---

### Common Issues and Solutions  

#### Issue Summary Table  

| Issue | Symptoms | Troubleshooting Steps | Solution | Case Reference |
|-------|----------|------------------------|----------|----------------|
| Ubuntu client availability | EPP client for Ubuntu 24.04 requested | Confirm release schedule and communicate with development team | Inform customer of upcoming release | [Ubuntu Client Availability](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BNgRiIAL/view) |
| Kodak scanner blocked | Scanner inaccessible due to DLP settings | Check device rights and disable MTP | Disable MTP feature | [Kodak Scanner Blocked](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BPtKlIAL/view) |
| CD/DVD drive visibility | CD/DVD content intermittently visible | Verify Minifilter driver settings | Adjust Minifilter driver configuration | [CD/DVD Drive Visibility](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C769rIAB/view) |
| Effective Rights report bug | Permissions displayed incorrectly | Confirm bug and escalate to development | Inform customer of upcoming fix | [Effective Rights Report Bug](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CcCKcIAN/view) |
| USB tokens blocked | USB authentication tokens not recognized | Set exceptions for affected device types | Allow access exceptions for tokens | [USB Tokens Blocked](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CCjVWIA1/view) |
| Logs Report loading issue | Logs page continuously loading | Backup logs and reduce retention period | Adjust log retention settings | [Logs Report Loading Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CDTEzIAP/view) |
| USB blocking rules misconfigured | USB devices not blocked as expected | Verify device control rules and schedule remote session | Correct rule configuration | [USB Blocking Rules Misconfigured](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CfI0TIAV/view) |
| NOX device write issue | Unable to write to NOX USB device | Check for software conflicts | Uninstall conflicting software | [NOX Device Write Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CGAhHIAX/view) |
| Whitelisting functionality broken | Whitelisted devices blocked after update | Delete duplicates and clear cache | Rebuild PHP and clear cached rights | [Whitelisting Functionality Broken](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000COIeRIAX/view) |
| Selective removable media policy | Need to disable removable media for specific devices | Create device-specific groups | Configure group-specific rights | [Selective Removable Media Policy](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CpiwCIAR/view) |
| Missing script for macOS deployment | Script unavailable for macOS deployment via Intune | Confirm script request and send via email | Provide script via email | [Missing Script for macOS Deployment](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NmBdSIAV/view) |
| Disabled audio devices re-enabled after upgrade | Disabled audio devices automatically re-enabled | Confirm client/server versions and revert to older version | Revert to stable client version | [Disabled Audio Devices Re-enabled](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OavtBIAR/view) |
| Computers not enforcing USB restrictions | Computers not visible in EPP console | Verify server IP/port configuration and redeploy agent | Redeploy EPP agent with correct settings | [Computers Not Enforcing USB Restrictions](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OQXAdIAP/view) |

---

### Detailed Issues  

#### Ubuntu Client Availability  
**Description:**  
The EPP client for Ubuntu 24.04 was requested by a customer but was still undergoing testing.  

**Symptoms:**  
- Inquiry about the status of the Ubuntu client.  
- Customer unable to deploy EPP on Ubuntu 24.04.  

**Solution:**  
Inform the customer that the EPP client compatible with Ubuntu 24.04 will be included in the upcoming 5.9.4.0 release.  

---

#### Kodak Scanner Blocked  
**Description:**  
A Kodak scanner was inaccessible due to interference from the MTP feature in DLP settings.  

**Symptoms:**  
- Scanner blocked when DLP software is installed.  

**Solution:**  
Disable the MTP feature on the affected computer.  

---

#### CD/DVD Drive Visibility  
**Description:**  
CD/DVD drives intermittently displayed content in Windows Explorer due to Minifilter driver settings.  

**Symptoms:**  
- Drives recognized but content occasionally invisible.  

**Solution:**  
Adjust Minifilter driver settings to ensure proper visibility of CD/DVD drive content.  

---

#### Effective Rights Report Bug  
**Description:**  
Effective Rights report displayed incorrect permissions for users.  

**Symptoms:**  
- Users shown as having access when they do not.  

**Solution:**  
Inform the customer that the issue will be resolved in the upcoming 5.9.4.0 release.  

---

#### Disabled Audio Devices Re-enabled After Upgrade  
**Description:**  
Disabled audio devices were automatically re-enabled after upgrading to client version 6.2.4.2000.  

**Symptoms:**  
- Audio devices re-enabled after upgrade.  

**Solution:**  
Revert to the older client version (6.2.1.2004), which resolved the issue.  

---

#### Computers Not Enforcing USB Restrictions  
**Description:**  
Several computers with EPP installed were not visible in the USB bypass policy or the EPP console due to incorrect server IP and port configuration.  

**Symptoms:**  
- USB restrictions not enforced.  

**Solution:**  
Redeploy the EPP agent with the correct server IP and port settings.  

---

### Best Practices  

1. **Regular Updates:**  
   Ensure both the Endpoint Protector server and client software are updated to the latest versions to benefit from bug fixes and feature enhancements.  

2. **Policy Validation:**  
   Periodically review and validate device control policies to ensure they align with organizational requirements and are correctly applied across all nodes.  

3. **Log Monitoring:**  
   Monitor logs regularly to identify discrepancies or errors early. Implement log retention policies to prevent performance degradation.  

4. **Testing Before Deployment:**  
   Conduct thorough testing in a controlled environment before deploying new configurations or updates to production systems.  

5. **Clear Communication:**  
   Maintain clear communication with customers regarding known limitations, upcoming fixes, and best practices for using Endpoint Protector effectively.  

---

### Advanced Topics  

#### Handling Device Control Conflicts  
**Scenario:**  
Conflicts between Endpoint Protector and third-party software (e.g., Samsung Magician) can cause device access issues.  

**Resolution:**  
Uninstall conflicting software and reconfigure Endpoint Protector settings to restore functionality.  

---

#### Offline Mode for IoT Devices  
**Scenario:**  
IoT devices without network connectivity require offline management of device rights.  

**Resolution:**  
Use encrypted registry files to manage allowed/denied devices. Ensure proper formatting and encryption for seamless offline operation.  

---

#### Network Configuration for EPP  
- Ensure that the EPP server is reachable from all endpoints over port 443.  
- Use tools like `ping` and `tracert` to verify connectivity.  
- Document server IP and port settings during deployment to avoid misconfigurations.  

---

### Conclusion  
The Device Rights feature in Netwrix Endpoint Protector is a powerful tool for managing device access and ensuring data security. By following the troubleshooting steps, solutions, and best practices outlined in this article, administrators can resolve issues efficiently and optimize their use of the Device Control feature.  

For further assistance, contact Netwrix Support or refer to the case references provided.