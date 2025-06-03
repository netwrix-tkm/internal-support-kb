## Ticket Metadata
- **Ticket ID:** 500Qk00000FwFNqIAN
- **Case Number:** 421416
- **Status:** Closed - Resolved
- **Account/Company:** CTBC Bank Corp. (Canada)
- **Contact Name:** Tony Hsieh
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** Not specified

## Problem Description
A user reported confusion regarding their workstation name. The user primarily logged into a workstation named LT303, but the Endpoint Protector occasionally showed activity from a different workstation, LT302. Both workstations had the Endpoint Protector agent installed, but they could not appear simultaneously in the console.

## Environment Details
- Two workstations (LT302 and LT303) located in different subnets and geographic locations.
- Both workstations have the Endpoint Protector agent installed.

## Troubleshooting Steps
1. Verified that both LT302 and LT303 were listed under "Device Control" in the Endpoint Protector console.
2. Noted that when one workstation appeared, the other would disappear from the console and database.
3. Enabled logging on both workstations and updated policies to gather log files.
4. Suggested by R&D to enable the virtual desktop clone feature to monitor the situation.

## Root Cause
The issue was identified as a conflict in the Endpoint Protector's handling of virtual desktop sessions, which caused the system to incorrectly associate the user with one workstation while the other disappeared from the console.

## Solution
Enabling the virtual desktop clone feature in the Endpoint Protector settings resolved the issue. This adjustment allowed both workstations to be recognized simultaneously, eliminating the confusion regarding the user's active session.

## Notes
- Ensure that the virtual desktop clone feature is enabled for environments where users may log into multiple workstations to prevent similar issues in the future.
- Monitor the system after enabling this feature to confirm that the issue does not recur.