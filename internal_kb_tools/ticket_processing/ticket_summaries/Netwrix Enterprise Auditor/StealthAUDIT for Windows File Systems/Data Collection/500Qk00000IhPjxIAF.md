## Ticket Metadata
- **Ticket ID:** 500Qk00000IhPjxIAF
- **Case Number:** 427963
- **Status:** Closed - Resolved
- **Account/Company:** K2 Integrity (formerly K2 Intelligence)
- **Contact Name:** Jack Shashaty
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Data Collection
- **Version:** 11.6.0.138

## Problem Description
The customer reported an issue with the FSAC (File System Activity Collection) scan via Local or Applet mode, which resulted in a "Retry timeout exceeded" error. The setup involved a domain controller in the UK and a configuration with StealthBits pointing to a main Domain Controller in a US data center. The customer suspected that the current remote scanning setup was outdated and requested documentation for improved scanning methods.

## Environment Details
- Two-node Windows File Server cluster (Active-Passive)
- Netwrix Enterprise Auditor (NEA) version 11.6.0.138
- No agent installed on the UK domain controller
- Remote scanning configuration in place

## Troubleshooting Steps
1. Reviewed logs indicating "GetSessions failed with code 0x80004005" and "Error scanning server: Retry timeout exceeded."
2. Confirmed connection status as "ACCESS GRANTED."
3. Executed `Test-NetConnection` commands on both cluster nodes for ports 8766 and 8767, which failed.
4. Conducted a review of the Windows Task Scheduler to check for disabled tasks related to FSAC scans.
5. Identified a non-removed StealthAUDIT FSAA Proxy Scanner Service that was not visible in Add/Remove Programs.
6. Ensured that ports 8766 and 8767 were added to the host firewall settings.
7. Cleaned up older certificates from the nodes as advised by a professional services engineer.
8. Scheduled follow-up meetings to discuss findings and next steps.

## Root Cause
The root cause of the issue was identified as a misconfiguration in the Windows Defender Firewall, which was not in sync with the current IP of the Netwrix Access Analyzer (NAA). Additionally, the presence of a lingering StealthAUDIT FSAA Proxy Scanner Service and disabled scheduled tasks contributed to the failure of the scans.

## Solution
The issue was resolved by:
- Updating the Windows Defender Firewall settings to include the correct IP and ports (8766 and 8767).
- Removing the outdated StealthAUDIT FSAA Proxy Scanner Service using the command `sc delete StealthAUDITFSAA`.
- Ensuring that the FSAA and FSAC jobs were correctly scheduled and enabled in the Windows Task Scheduler.
- Conducting a successful ad hoc FSAC scan after making the necessary adjustments.

## Notes
- It is crucial to ensure that all firewall settings are correctly configured and that any lingering services from previous installations are removed to avoid conflicts.
- Regularly check the Windows Task Scheduler to ensure that necessary tasks are enabled and scheduled correctly.
- For future reference, documentation on configuring remote scanning setups should be reviewed to ensure best practices are followed.