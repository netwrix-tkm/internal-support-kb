# Netwrix Endpoint Protector: Content-Aware Protection (CAP) Network Share Knowledge Base

## Overview
The Content-Aware Protection (CAP) Network Share feature in Netwrix Endpoint Protector allows organizations to monitor and control file transfers to and from network shares. This feature is critical for enforcing data loss prevention (DLP) policies and ensuring sensitive data is handled securely. However, misconfigurations or feature limitations can lead to issues such as blocked file transfers, incomplete policy enforcement, or unexpected behavior.

This article provides a comprehensive guide to common issues, troubleshooting steps, root causes, and tested solutions for CAP Network Share. It also includes best practices to prevent recurring problems.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Allow list not honored | Files blocked despite IP being added to allow list | Verify allow list and CAP policy settings | Adjust CAP policy to honor allow list | [Network Share Allow List Misconfiguration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BNgRlIAL/view) |
| Unable to block outgoing transfers only | Users can download files despite denylist | Test File Location Denylist and CAP policy | Use Device Control for read-only access | [Outgoing Transfers Not Blocked](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BnJJKIA3/view) |
| SFTP allow/block configuration | Unable to allow specific IP while blocking others | Modify SFTP allow list and test | Update allow list with specific IP | [SFTP Allow List Configuration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DuNH1IAN/view) |
| Network share functionality without DLP | Network share not operational without DLP | Verify EPP client installation | Install EPP client on all machines | [Network Share Requires EPP Client](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GXLXbIAP/view) |
| Blocking file transfers to external destinations | File transfers via web Outlook not blocked | Configure CAP for web-based transfers | Adjust CAP settings for internal-to-external transfers | [Blocking File Transfers to External Destinations](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KlbNJIAZ/view) |

---

## Detailed Issues

### 1. Network Share Allow List Misconfiguration
**Symptoms:**  
Files are blocked even though the IP address is added to the network share allow list.

**Troubleshooting Steps:**  
1. Verify that the IP address is correctly added to the allow list.  
2. Review the CAP policy settings to ensure they are not overriding the allow list.  
3. Check for conflicting policies that might block files from the specified IP.  
4. Test file transfers with different file types and access attempts.

**Root Cause:**  
A misconfiguration in the CAP policy settings was overriding the allow list, causing files to be blocked.

**Solution:**  
1. Adjust the CAP policy to ensure it honors the network share allow list.  
2. Test file transfers to confirm the issue is resolved.  
3. Document the changes to prevent future misconfigurations.

**Warnings:**  
- Ensure all policy changes are reviewed and documented.  
- Regularly audit CAP policies and allow lists for alignment.

**Source Ticket:** [Network Share Allow List Misconfiguration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BNgRlIAL/view)

---

### 2. Outgoing Transfers Not Blocked
**Symptoms:**  
Users can download files from a network share despite it being added to the File Location Denylist.

**Troubleshooting Steps:**  
1. Add the network share folder to the File Location Denylist.  
2. Test file transfers to confirm the denylist behavior.  
3. Review CAP policy settings for additional restrictions.  
4. Explore alternative configurations for granular control.

**Root Cause:**  
The CAP feature does not support blocking only outgoing transfers while allowing uploads. The File Location Denylist applies to both directions.

**Solution:**  
1. Use the Device Control module to configure network shares with 'Read Only' access.  
2. Inform the customer about the limitations of the CAP feature.  

**Warnings:**  
- The File Location Denylist cannot differentiate between upload and download actions.  
- Plan security policies with CAP feature limitations in mind.

**Source Ticket:** [Outgoing Transfers Not Blocked](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BnJJKIA3/view)

---

### 3. SFTP Allow List Configuration
**Symptoms:**  
The customer cannot allow a specific URL's IP through SFTP while blocking all other URLs.

**Troubleshooting Steps:**  
1. Review the current SFTP configuration and allow/block lists.  
2. Verify the IP address of the specific URL to be allowed.  
3. Modify the allow list to include the specified IP.  
4. Test the SFTP connection to ensure functionality.

**Root Cause:**  
The specified URL's IP address was not included in the SFTP allow list.

**Solution:**  
1. Update the SFTP configuration to include the specific IP in the allow list.  
2. Test the connection to confirm the changes are effective.  
3. Ensure other URLs remain blocked as intended.

**Warnings:**  
- Document all allow/block list changes for future reference.  
- Regularly review allow/block lists to maintain security.

**Source Ticket:** [SFTP Allow List Configuration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DuNH1IAN/view)

---

### 4. Network Share Requires EPP Client
**Symptoms:**  
The network share functionality is not operational without the DLP system in place.

**Troubleshooting Steps:**  
1. Verify if the EPP client is installed on the machine accessing the network share.  
2. Check the server version and plan for updates if necessary.  
3. Test the network share functionality with the latest client version.

**Root Cause:**  
The EPP client was not installed on the machine, preventing proper logging and functionality.

**Solution:**  
1. Install the EPP client on all relevant machines.  
2. Update the EPP server to the latest version (e.g., 5.9.4.1).  
3. Test the network share functionality post-update.

**Warnings:**  
- Ensure the EPP client is installed on all machines involved in file transfers.  
- Verify client installation status before troubleshooting network share issues.

**Source Ticket:** [Network Share Requires EPP Client](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GXLXbIAP/view)

---

### 5. Blocking File Transfers to External Destinations
**Symptoms:**  
File transfers from internal sources to external destinations (e.g., via web Outlook) are not blocked.

**Troubleshooting Steps:**  
1. Identify the method used for file transfers (e.g., web Outlook).  
2. Configure CAP settings to block file transfers to external destinations.  
3. Test the configuration to ensure it is effective.

**Root Cause:**  
The CAP settings were not properly configured to block file transfers from internal to external locations.

**Solution:**  
1. Adjust CAP settings to enable blocking and reporting of file transfers to external destinations.  
2. Monitor the effectiveness of the configuration post-implementation.

**Warnings:**  
- Regularly review CAP settings to adapt to changes in user behavior or organizational policies.  
- Monitor the blocking/reporting mechanism to ensure compliance.

**Source Ticket:** [Blocking File Transfers to External Destinations](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KlbNJIAZ/view)

---

## Best Practices
1. **Regular Audits:** Periodically review CAP policies, allow/block lists, and configurations to ensure alignment with organizational security policies.  
2. **Documentation:** Maintain detailed records of all policy changes and configurations to facilitate troubleshooting and prevent misconfigurations.  
3. **Client Installation:** Ensure the EPP client is installed on all machines involved in file transfers to enable proper logging and functionality.  
4. **Feature Limitations:** Be aware of CAP feature limitations and plan security policies accordingly.  
5. **Testing:** Test all configurations in a controlled environment before deploying them to production.

---

## Advanced Topics
### Handling Complex Scenarios
For advanced use cases, such as differentiating between upload and download actions or implementing granular SFTP controls, consider integrating additional modules like Device Control or consulting with Netwrix support for custom solutions.