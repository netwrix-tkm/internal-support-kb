```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000EcAXpIAN
- **Case Number:** 418430
- **Status:** Closed - Resolved
- **Account/Company:** Sheridan&Co
- **Contact Name:** Peter Longley
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** 5.9.4.0

## Problem Description
The client was unable to upgrade devices running older versions of the Netwrix Endpoint Protector client to the latest version (6.2.3.1010). All online devices were greyed out in the system when attempting to perform the update.

## Environment Details
- Current server version: 5.9.4.0
- Target client version for upgrade: 6.2.3.1010

## Troubleshooting Steps
1. Verified the server version and confirmed it was 5.9.4.0.
2. Attempted to initiate the client upgrade process for online devices.
3. Noted that all online devices running older versions were greyed out and unresponsive to upgrade commands.
4. Investigated previous upgrade jobs to identify any potential conflicts.

## Root Cause
The issue was caused by the devices being associated with previous upgrade jobs, which prevented them from being selected for the new upgrade process.

## Solution
The resolution involved removing the affected computers from the previous upgrade jobs. Once this was done, the devices became available for the upgrade to version 6.2.3.1010.

## Notes
- Ensure that devices are not tied to any previous upgrade jobs before attempting to upgrade to a new version.
- It may be beneficial to document any previous upgrade jobs associated with devices to avoid similar issues in the future.
```