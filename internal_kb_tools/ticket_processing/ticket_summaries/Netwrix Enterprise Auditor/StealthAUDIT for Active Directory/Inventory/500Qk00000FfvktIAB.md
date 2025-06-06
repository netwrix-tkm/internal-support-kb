## Ticket Metadata
- **Ticket ID:** 500Qk00000FfvktIAB
- **Case Number:** 420836
- **Status:** Closed - Resolved
- **Account/Company:** MUFG Bank, LTD.
- **Contact Name:** Michael Kong
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Inventory
- **Version:** 11.5

## Problem Description
Active users in Active Directory (AD) are being incorrectly marked as deleted during each AD Inventory run, leading to issues where users appear to be removed from AD groups. This situation poses a risk of access issues for end users.

## Environment Details
- **Product Version:** 11.5
- **Build Number:** 11.5.0.214
- **Platform:** Netwrix Enterprise Auditor

## Troubleshooting Steps
1. Confirmed the issue with the customer regarding active users being marked as deleted.
2. Discussed potential automation processes that might be modifying user statuses.
3. Suggested running a full ADI scan as a temporary fix.
4. Proposed upgrading to the latest cumulative update (CU) version 11.5.0.277 or the latest version 11.6.
5. Recommended backing up the `ADInventory_UsersView` table, dropping the data, and running a full ADI scan post-upgrade.
6. Noted that if the above steps did not resolve the issue, escalation to R&D could be considered.

## Root Cause
The root cause was identified as a synchronization issue between ADI differential scans and the actual state of Active Directory, leading to discrepancies in user status reporting.

## Solution
The issue was temporarily resolved by consistently running a full ADI scan, which corrected the discrepancies in user status. The customer opted not to perform any upgrades at this time but acknowledged that the full ADI scan serves as a workaround. They will consider opening a new ticket for upgrades in the future.

## Notes
- It is crucial to always run full ADI scans to maintain accurate synchronization with Active Directory.
- The customer should be aware that without upgrading, the issue may recur, and they should monitor for any further discrepancies.
- If the problem persists after implementing the suggested solutions, further investigation or escalation to R&D may be necessary.