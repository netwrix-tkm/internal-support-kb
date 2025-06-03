# Netwrix Endpoint Protector: Content-Aware Protection - Third Party Conflict

## Overview
Netwrix Endpoint Protector's Content-Aware Protection feature is designed to safeguard sensitive data by monitoring and controlling endpoint activities. However, conflicts with third-party applications, particularly VPN clients and other software, can occasionally arise. This article provides a comprehensive guide to identifying, troubleshooting, and resolving these conflicts.

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Cisco AnyConnect DPI VPN Recurrence | VPN functionality issues | Review previous ticket history, assess third-party conflicts | No resolution implemented; issue deprioritized | [Cisco AnyConnect DPI VPN Recurrence](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000G1kAsIAJ/view) |
| Cisco VPN Connection Drops | VPN disconnects after 10-15 minutes; browser pages fail to load | Terminate EPP client, open ADO for investigation | Provided updated EPP client builds to resolve compatibility issues | [Cisco VPN Connection Drops](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KvRrEIAV/view) |
| MobileX Server Connection Failure | MobileX cannot connect to its server | Test DPI settings, enable "Stealth DPI driver" | Enabled "Stealth DPI driver" to resolve issue | [MobileX Server Connection Failure](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MsACEIA3/view) |
| CiscoVPN Disabling Intermittently | VPN disables every 10-30 minutes; intermittent internet access | Disable "Advanced Printer and MTP Scanning," add CiscoVPN to exception list | Disabled advanced scanning and added CiscoVPN process to exception list | [CiscoVPN Disabling Intermittently](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NeNtXIAV/view) |

---

## Detailed Issues

### Cisco AnyConnect DPI VPN Recurrence
**Symptoms:**  
PrivatBank reported recurring issues with the Cisco AnyConnect DPI VPN, previously addressed in an older ticket (#10855). The VPN functionality was disrupted, but the issue was deprioritized by the customer.

**Troubleshooting Steps:**  
1. Reviewed the history of the previous ticket (#10855) for insights into the issue.  
2. Engaged with the customer to gather detailed information about the symptoms and any changes in their environment since the last occurrence.  
3. Assessed potential conflicts with third-party applications affecting VPN functionality.  
4. Confirmed that the issue was not prioritized by the customer at this time.

**Root Cause:**  
The root cause was not explicitly identified but was likely linked to conflicts with third-party applications.

**Solution:**  
No specific resolution was implemented as the customer deprioritized the issue.

**Source Ticket:** [Cisco AnyConnect DPI VPN Recurrence](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000G1kAsIAJ/view)

---

### Cisco VPN Connection Drops
**Symptoms:**  
PrivatBank reported intermittent VPN connection drops with the Cisco Secure Client. After rebooting the PC, the VPN worked for 10-15 minutes before failing, causing browser pages to stop loading.  

**Troubleshooting Steps:**  
1. Verified the initial problem description with the customer.  
2. Observed the behavior of the Cisco Secure Client during the issue.  
3. Terminated the EPP client, which temporarily resolved the connectivity issue.  
4. Opened an Application Development Order (ADO) to investigate further.  
5. Awaited updates from R&D regarding the conflict.

**Root Cause:**  
A conflict between the Cisco VPN client and the EPP client caused the VPN connection to drop intermittently.

**Solution:**  
Provided the customer with updated EPP client builds that resolved compatibility issues with the Cisco VPN client.

**Source Ticket:** [Cisco VPN Connection Drops](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KvRrEIAV/view)

---

### MobileX Server Connection Failure
**Symptoms:**  
After installing the EPP client, the MobileX application failed to connect to its server. The issue was isolated to one client machine, while other machines with identical EPP settings functioned correctly.

**Troubleshooting Steps:**  
1. Confirmed the issue was specific to the MobileX client, not the EPP client itself.  
2. Suggested disabling the DPI option for the affected computer from "Device Control > Computers > Manage settings."  
3. Advised updating the EPP client policy and restarting the MobileX client software.  
4. Tested various DPI settings, including enabling/disabling "Advanced Printer and MTP Scanning."  
5. Explored enabling bypass options for TLS handshakes and HTTP errors.  
6. Suggested enabling the "Stealth DPI driver" as a potential solution.

**Root Cause:**  
A conflict between the EPP client’s DPI settings and the MobileX application prevented the application from connecting to its server.

**Solution:**  
Enabled the "Stealth DPI driver" option on the affected client machine, allowing the MobileX application to connect successfully.

**Source Ticket:** [MobileX Server Connection Failure](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MsACEIA3/view)

---

### CiscoVPN Disabling Intermittently
**Symptoms:**  
PrivatBank reported that the CiscoVPN (Cisco Secure Client) disabled every 10-30 minutes, causing intermittent internet access issues. The problem was isolated to a single Windows endpoint.

**Troubleshooting Steps:**  
1. Reviewed logs and identified errors related to the Cisco Secure Client:  
   - `ERROR wow64 helper returned error: 87 for pid: 3112`  
   - `ERROR hooking failed 0x00000057 - 3112`  
2. Suggested disabling the "Advanced Printer and MTP Scanning" option to test resolution.  
3. Confirmed with the customer if the issue persisted after disabling advanced scanning.  
4. Proposed adding the CiscoVPN process name to the scanning exception list if disabling advanced scanning resolved the issue.

**Root Cause:**  
A conflict between the EPP client’s advanced scanning features and the Cisco Secure Client caused intermittent VPN disabling.

**Solution:**  
- Disabled the "Advanced Printer and MTP Scanning" option in the EPP client.  
- Added the CiscoVPN (Cisco Secure Client) process name to the advanced scanning exception list.

**Source Ticket:** [CiscoVPN Disabling Intermittently](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NeNtXIAV/view)

---

## Best Practices
1. **Monitor Compatibility:** Regularly test compatibility between the EPP client and third-party applications, especially VPN clients.  
2. **Document Recurring Issues:** Maintain detailed records of recurring issues to identify patterns and streamline future troubleshooting.  
3. **Use Exceptions:** Add known conflicting processes (e.g., CiscoVPN) to the EPP client’s exception list to prevent disruptions.  
4. **Enable Stealth DPI Driver:** Consider enabling the "Stealth DPI driver" globally if conflicts with independent software vendors are common.  
5. **Communicate Changes:** Inform customers about potential conflicts and provide guidance on configuration changes to mitigate issues.

---

## Advanced Topics
### Using the Stealth DPI Driver
The "Stealth DPI driver" improves interoperability with third-party applications by minimizing interference with their operations. It is particularly useful for resolving conflicts with software that relies on specific network protocols or DPI-sensitive configurations.  

**Steps to Enable:**  
1. Navigate to "Device Control > Computers > Manage settings."  
2. Locate the DPI settings section.  
3. Enable the "Stealth DPI driver" option.  
4. Save changes and restart the affected application or endpoint.

**Considerations:**  
- Monitor performance after enabling the Stealth DPI driver to ensure stability.  
- If enabling globally, test thoroughly to avoid unintended side effects on other endpoints.

---  
End of Article.