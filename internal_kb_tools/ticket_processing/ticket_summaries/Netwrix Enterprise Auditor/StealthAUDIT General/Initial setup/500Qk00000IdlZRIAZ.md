## Ticket Metadata
- **Ticket ID:** 500Qk00000IdlZRIAZ
- **Case Number:** 427859
- **Status:** Closed - Resolved
- **Account/Company:** Eglin Federal Credit Union
- **Contact Name:** Glenda Coley
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.6

## Problem Description
The customer reported that the host management list in Netwrix Enterprise Auditor contained many outdated targets, including decommissioned hosts. Although host lists were being updated by discovery queries, old hosts were not being cleaned up, leading to potential confusion and issues in monitoring.

## Environment Details
- The issue was observed in the Netwrix Enterprise Auditor environment.
- A new server was set up for host discovery to improve the accuracy of the host list.

## Troubleshooting Steps
1. Discussed the possibility of manually cleaning up stale hosts but decided to retain them temporarily for comparison during troubleshooting.
2. Installed and configured NEA host discovery on the new server.
3. Verified that the discovery was running and functioning correctly.
4. Monitored the host lists for accuracy and updates after the new server setup.
5. Confirmed with the customer that the host list looked improved and included new hosts.

## Root Cause
The root cause of the issue was identified as the intentional retention of offline or decommissioned hosts in the host management view. This behavior was designed to prevent the removal of temporarily unresponsive servers, but it resulted in an accumulation of outdated entries.

## Solution
The issue was resolved by:
- Deploying a new NEA server with a clean host list.
- Configuring host discovery on the new server, which accurately detected and updated the host list.
- Verifying that the host list was functioning as expected, with the customer confirming the improvements.

## Notes
- It is important to monitor the host management view regularly to ensure it reflects the current environment accurately.
- Future cleanup of stale hosts may be necessary to maintain an optimal host management list.
- Consider documenting the process for manual cleanup of hosts for future reference if similar issues arise.