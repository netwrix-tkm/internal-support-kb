# Knowledge Base Reference Guide: Troubleshooting CAP Network Share Issues in Netwrix Endpoint Protector

## Overview
This guide provides a comprehensive reference for troubleshooting issues related to the Content-Aware Protection (CAP) Network Share feature in Netwrix Endpoint Protector. CAP Network Share is a critical component for managing data security, enabling organizations to monitor and control file transfers to and from network shares. Understanding and resolving issues in this category is essential for maintaining data loss prevention (DLP) policies and ensuring compliance with organizational security standards.

---

## Technical Background
### Key Concepts
- **Content-Aware Protection (CAP):** A feature in Netwrix Endpoint Protector that monitors and controls data transfers based on content and context.
- **Network Share:** A shared folder or drive accessible over a network, often used for collaborative file storage and transfer.
- **Allow List/Deny List:** Configuration settings that permit or block specific IPs, file locations, or actions.
- **Exit Points:** Defined destinations or methods through which data can leave a system, such as network shares, email, or external devices.

### System Context
- CAP policies are applied to monitor and control file transfers based on predefined rules.
- Network Share functionality relies on proper configuration of allow/deny lists and CAP policies to enforce security measures.
- The effectiveness of CAP policies depends on accurate alignment with organizational requirements and proper client installation on endpoints.

---

## Issue Recognition & Triage
### Symptoms
- Files being blocked despite being added to the allow list.
- Inability to block specific file transfer directions (e.g., outgoing only).
- Network share functionality not operational without the DLP system.
- File transfers not being logged or monitored as expected.
- Requests to configure specific IPs or URLs for allow/block actions.

### Priority Assessment
- **High Priority:** Issues involving data leakage risks, such as inability to block unauthorized file transfers.
- **Medium Priority:** Configuration challenges that do not immediately compromise security.
- **Low Priority:** General inquiries or requests for feature clarification.

---

## Diagnostic Methodology
### Systematic Approach
1. **Verify Configuration:**
   - Check CAP policy settings for misconfigurations or conflicts.
   - Review allow/deny lists for accuracy.
2. **Reproduce the Issue:**
   - Attempt to replicate the reported behavior in a controlled environment.
3. **Analyze Logs:**
   - Collect and review logs from the Endpoint Protector server and client machines.
4. **Test Adjustments:**
   - Modify configurations incrementally and test the impact of each change.
5. **Confirm Resolution:**
   - Validate that the issue is resolved and document the changes made.

---

## Information Collection
### Key Questions for Customers
- What specific behavior or issue are you experiencing?
- What CAP policies and allow/deny lists are currently configured?
- Are all relevant endpoints running the latest EPP client version?
- Can you provide logs or screenshots demonstrating the issue?

### Logs and Data to Collect
- CAP policy configuration files.
- Network share allow/deny list settings.
- Endpoint Protector server logs.
- Client logs from affected machines.

---

## Common Scenarios & Solutions
### Scenario 1: Files Blocked Despite Being on Allow List
- **Root Cause:** Misconfiguration in CAP policy overriding the allow list.
- **Solution:** Adjust CAP policy settings to honor the allow list. Test with different file types to confirm resolution.  
  [Example Case: 500Qk00000BNgRlIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BNgRlIAL/view)

### Scenario 2: Unable to Block Outgoing Transfers Only
- **Root Cause:** Limitation in CAP feature; Network Share exit point applies to both upload and download actions.
- **Solution:** Use the File Location Denylist for blocking transfers or configure network shares with 'Read Only' access via Device Control.  
  [Example Case: 500Qk00000BnJJKIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BnJJKIA3/view)

### Scenario 3: Network Share Not Operational Without DLP
- **Root Cause:** EPP client not installed on the machine accessing the network share.
- **Solution:** Install the EPP client on all relevant machines and update the server to the latest version.  
  [Example Case: 500Qk00000GXLXbIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GXLXbIAP/view)

### Scenario 4: Allowing Specific IPs for SFTP
- **Root Cause:** Missing IP in the allow list for SFTP configuration.
- **Solution:** Add the specific IP to the allow list and test the connection to ensure functionality.  
  [Example Case: 500Qk00000DuNH1IAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DuNH1IAN/view)

### Scenario 5: Blocking File Transfers to External Destinations
- **Root Cause:** Incomplete configuration for blocking/reporting file transfers.
- **Solution:** Provide detailed configuration steps for CAP policies to block and report file transfers.  
  [Example Case: 500Qk00000KlbNJIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KlbNJIAZ/view)

---

## Detailed Case Studies
### Case 1: Files Blocked Despite Allow List ([500Qk00000BNgRlIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BNgRlIAL/view))
- **Symptoms:** Files blocked even after adding IP to allow list.
- **Diagnostic Steps:** Verified allow list, reviewed CAP policy, tested with different file types.
- **Resolution:** Adjusted CAP policy to honor the allow list.
- **Key Takeaways:** Always check for policy conflicts when allow lists are not functioning as expected.

### Case 2: Blocking Outgoing Transfers Only ([500Qk00000BnJJKIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BnJJKIA3/view))
- **Symptoms:** Unable to block outgoing transfers while allowing uploads.
- **Diagnostic Steps:** Reviewed CAP feature limitations and tested File Location Denylist.
- **Resolution:** Suggested 'Read Only' access via Device Control for granular control.
- **Key Takeaways:** Understand CAP feature limitations and explore alternative configurations.

### Case 3: Network Share Not Operational ([500Qk00000GXLXbIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GXLXbIAP/view))
- **Symptoms:** Network share functionality unavailable without DLP.
- **Diagnostic Steps:** Checked client installation and server version.
- **Resolution:** Installed EPP client and updated server to latest version.
- **Key Takeaways:** Ensure client installation on all endpoints for full functionality.

---

## Best Practices & Tips
- Regularly audit CAP policies and allow/deny lists to ensure alignment with security requirements.
- Always verify client installation and server version compatibility during troubleshooting.
- Document all configuration changes to maintain a clear audit trail.
- Educate customers on CAP feature limitations to set realistic expectations.
- Use controlled environments to replicate and test reported issues.

---

## Escalation Guidelines
### Criteria for Escalation
- Issues involving potential data breaches or critical security risks.
- Persistent issues that cannot be resolved after following diagnostic steps.
- Feature limitations requiring product team input for potential enhancements.

### Escalation Process
1. Document all troubleshooting steps and findings.
2. Collect relevant logs and configuration details.
3. Submit a detailed escalation request to the appropriate internal team.
4. Communicate escalation status and expected timelines to the customer.

--- 

This guide serves as a definitive reference for handling CAP Network Share issues, enabling support engineers to resolve cases efficiently and consistently.