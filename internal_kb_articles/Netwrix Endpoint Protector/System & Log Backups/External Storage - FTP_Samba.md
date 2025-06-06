# Knowledge Base Reference Guide: Troubleshooting External Storage Issues in Netwrix Endpoint Protector

## Overview

This guide provides a comprehensive reference for troubleshooting issues related to the **External Storage - FTP/Samba** feature in the **Netwrix Endpoint Protector (EPP)** platform. External storage is a critical component for system and log backups, enabling secure data transfer and storage on remote servers. Understanding and resolving issues in this category ensures data integrity, compliance, and operational continuity.

## Technical Background

### Key Concepts
- **External Storage**: Refers to the use of remote servers (via FTP, SFTP, or SMB protocols) for storing backups, audit logs, and shadow copies.
- **FTP/Samba Protocols**: Commonly used protocols for file transfer and network file sharing. FTP/SFTP is used for secure file transfers, while SMB facilitates network file sharing.
- **Authentication**: The process of verifying credentials (username and password) to establish a connection with the external storage server.
- **Shadow Copies**: Temporary or backup copies of files stored for redundancy or recovery purposes.
- **Ciphers and Encryption**: Protocols used to secure data transfer. Compatibility between client and server ciphers is critical for successful connections.

### System Context
- **Netwrix Endpoint Protector**: A data loss prevention (DLP) solution that integrates with external storage for backups and log management.
- **Backup Types**: Includes system backups, audit log backups, and shadow file backups.
- **Integration Points**: External storage configurations often interact with other systems, such as SIEM tools, which can introduce complexity.

## Issue Recognition & Triage

### Common Symptoms
- Authentication failures (e.g., "Incorrect credentials" errors).
- Inability to connect to external storage servers.
- Backups not being performed automatically.
- Disk space depletion due to unremoved shadow copies.
- Excessive authentication failure logs.

### Priority Assessment
- **High Priority**: Issues causing data loss, backup failures, or operational disruptions.
- **Medium Priority**: Errors with no immediate impact but potential for escalation (e.g., excessive logs).
- **Low Priority**: Cosmetic issues (e.g., display glitches) that do not affect functionality.

## Diagnostic Methodology

### Systematic Approach
1. **Verify Credentials**: Confirm the username, password, and permissions for the external storage server.
2. **Test Connectivity**: Use tools like telnet, ping, or external FTP/SFTP clients to test server accessibility.
3. **Review Configuration**: Check the EPP management console for correct settings (e.g., server address, protocol, paths).
4. **Analyze Logs**: Collect and review logs from both the EPP server and the external storage server.
5. **Isolate Variables**: Disable integrations (e.g., SIEM) or features (e.g., shadow copies) one at a time to identify the root cause.
6. **Engage Remote Sessions**: If necessary, schedule a session to directly review the customer’s environment.

## Information Collection

### Questions to Ask Customers
- What error messages are being displayed?
- Have there been any recent changes to credentials, server configurations, or network settings?
- Are backups working with other clients or tools?
- Can you provide screenshots of the configuration and error messages?
- What troubleshooting steps have already been attempted?

### Logs and Data to Collect
- EPP server logs (e.g., `/var/eppfiles/syslog`).
- External storage server logs (e.g., FTP/SFTP logs).
- Screenshots of the EPP configuration and error messages.
- Network connectivity test results (e.g., telnet, tcpdump).

## Common Scenarios & Solutions

### Scenario 1: Display Glitch Misreporting Incorrect Credentials
- **Symptoms**: "Incorrect credentials" error despite valid credentials.
- **Solution**: Address the display glitch in the EPP interface. No changes to credentials or server settings are required.
- **Reference Case**: [500Qk00000E9iWRIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000E9iWRIAZ/view)

---

### Scenario 2: Disk Space Depletion Due to Shadow Copies
- **Symptoms**: Disk storage running out of space; old data not being moved.
- **Solution**: Manually clear shadow copies older than 90 days. Set up automated tasks for regular cleanup.
- **Reference Case**: [500Qk00000GpAljIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GpAljIAF/view)

---

### Scenario 3: SMB Configuration Errors
- **Symptoms**: "Could not connect to network share" error when configuring SMB for backups.
- **Solution**: Review and adjust SMB configuration parameters during a remote session.
- **Reference Case**: [500Qk00000HihttIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HihttIAB/view)

---

### Scenario 4: Authentication Failures for Automatic Backups
- **Symptoms**: Backups not performed; authentication test unsuccessful.
- **Solution**: Verify and correct credentials and configuration settings for the FTP/Samba connection.
- **Reference Case**: [500Qk00000I9HwvIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000I9HwvIAF/view)

---

### Scenario 5: Outdated Ciphers Causing SFTP Errors
- **Symptoms**: "Incorrect credentials" error despite successful SFTP tests with other clients.
- **Solution**: Enable outdated ciphers on the EPP server to match the SFTP server’s requirements.
- **Reference Case**: [500Qk00000JMADtIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JMADtIAP/view)

---

### Scenario 6: Excessive Authentication Failure Logs
- **Symptoms**: Over 1200 daily authentication failure logs despite successful file transfers.
- **Solution**: Update configurations for File Shadow Repository, SIEM, and External Storage to resolve misconfigurations.
- **Reference Case**: [500Qk00000PcBdaIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PcBdaIAF/view)

## Detailed Case Studies

### Case Study: [500Qk00000JMADtIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JMADtIAP/view)
- **Symptoms**: SFTP connection failed with "incorrect credentials" error.
- **Diagnostic Steps**:
  1. Verified credentials and SFTP settings.
  2. Tested SFTP functionality with external clients.
  3. Investigated server logs and identified outdated cipher requirements.
- **Resolution**: Enabled outdated ciphers on the EPP server.
- **Key Takeaways**: Always verify cipher compatibility when troubleshooting SFTP issues.

---

### Case Study: [500Qk00000GpAljIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GpAljIAF/view)
- **Symptoms**: Disk space depletion due to unremoved shadow copies.
- **Diagnostic Steps**:
  1. Verified external storage connection.
  2. Reviewed shadow copy settings and logs.
  3. Manually cleared shadow copies older than 90 days.
- **Resolution**: Implemented manual cleanup and recommended automated tasks.
- **Key Takeaways**: Regular monitoring and automated cleanup are essential for shadow copy management.

## Best Practices & Tips

1. **Credential Management**: Regularly update and verify credentials for external storage connections.
2. **Configuration Validation**: Double-check all settings in the EPP management console before concluding an issue.
3. **Log Analysis**: Use server and EPP logs to pinpoint root causes efficiently.
4. **Remote Sessions**: Schedule remote sessions for complex issues to expedite resolution.
5. **Documentation**: Maintain detailed records of configurations and resolutions for future reference.
6. **Automation**: Set up automated tasks for shadow copy cleanup and backup verification.

## Escalation Guidelines

### Criteria for Escalation
- Persistent issues after following standard troubleshooting steps.
- Complex problems requiring development team input (e.g., cipher compatibility).
- High-priority cases with potential data loss or compliance risks.

### Escalation Process
1. Document all troubleshooting steps and findings.
2. Collect relevant logs and configuration details.
3. Submit a detailed escalation request to the appropriate team.
4. Follow up regularly to ensure timely resolution.