## Ticket Metadata
- **Ticket ID:** 500Qk00000HihttIAB
- **Case Number:** 425671
- **Status:** Closed - Resolved
- **Account/Company:** NSM Magnettechnik
- **Contact Name:** Carsten Briesemann
- **Product:** Netwrix Endpoint Protector
- **Component:** System & Log Backups
- **Feature:** External Storage - FTP/Samba
- **Version:** NONE

## Problem Description
The customer, NSM Magnettechnik, reported an issue with configuring external storage settings to save "Audit Log Backups" and "System Backups" on a network share using the SMB protocol. They encountered an error message stating, "Could not connect to network share / Please check the credentials and server settings," despite using correct credentials.

## Environment Details
- **Protocol Used:** SMB
- **Backup Types:** Audit Log Backups, System Backups

## Troubleshooting Steps
1. Customer attempted to configure the external storage settings as per the operating instructions.
2. The customer verified that the credentials used for the network share were correct.
3. The customer requested assistance to check and test the settings made in the management console.
4. A TeamViewer session was scheduled to further investigate the issue.

## Root Cause
The root cause of the issue was not explicitly identified in the case documentation. However, it was implied that there may have been a misconfiguration in the external storage settings or network share settings that prevented a successful connection.

## Solution
During the scheduled TeamViewer session, the support engineer reviewed the external storage settings and identified the correct configuration parameters. The settings were adjusted accordingly, allowing the customer to successfully connect to the network share and save the backups as intended.

## Notes
- Ensure that all credentials and network share settings are double-checked before attempting to connect.
- If similar issues arise, consider scheduling a remote session to review configurations directly with the customer.
- Document any specific settings or configurations that resolved the issue for future reference.