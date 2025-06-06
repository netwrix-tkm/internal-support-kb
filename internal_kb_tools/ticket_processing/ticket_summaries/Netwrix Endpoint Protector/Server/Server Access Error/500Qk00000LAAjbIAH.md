## Ticket Metadata
- **Ticket ID:** 500Qk00000LAAjbIAH
- **Case Number:** 433830
- **Status:** Closed - Resolved
- **Account/Company:** ELTRADE Ltd
- **Contact Name:** Hristo Marinov
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** 5.9.4.1 (HWA-EPP4-U0066)

## Problem Description
The client, ELTRADE Ltd, reported that after adding a new license key, the system became unresponsive following a failed update attempt for Netwrix Endpoint Protector. The update process halted at 62.5% with a hash mismatch error, and subsequent attempts to access the web interface were unsuccessful.

## Environment Details
- **Server ID:** SIN1LC73
- **Previous Version:** 5.9.0.0
- **Attempted Update Version:** 5.9.4.1

## Troubleshooting Steps
1. Attempted to install the update for Netwrix Endpoint Protector 5.9.4.1.
2. Encountered an error: "Hash does not match" at 62.5% during the update.
3. Restarted the system multiple times to regain access to the web interface.
4. Reverted to a previous snapshot, restoring functionality but leaving the update error unresolved.
5. Upgraded the server from version 5.9.0.0 to 5.9.4.0.
6. Attempted an online update to version 5.9.4.1, which failed again.

## Root Cause
The root cause of the issue was identified as a failure in the update process due to a hash mismatch, which prevented the installation of the update. This was compounded by the system becoming unresponsive after the failed update attempts.

## Solution
The issue was resolved by reverting the server to a previous snapshot, which restored functionality. The update error was temporarily removed, and the server was successfully upgraded from version 5.9.0.0 to 5.9.4.0. However, the client is still awaiting the release of an offline patch to address the persistent update error.

## Notes
- It is important to monitor the update process closely for hash mismatch errors, as they can lead to system unresponsiveness.
- Clients should be advised to maintain regular backups or snapshots before attempting significant updates to facilitate recovery from failed installations.
- Ensure that offline patches are communicated promptly to clients experiencing similar issues.