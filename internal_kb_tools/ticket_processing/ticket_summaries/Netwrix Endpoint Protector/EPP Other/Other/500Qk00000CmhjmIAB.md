## Ticket Metadata
- **Ticket ID:** 500Qk00000CmhjmIAB
- **Case Number:** 414326
- **Status:** Closed - Resolved
- **Account/Company:** Ropes and Gray LLC
- **Contact Name:** Richard Michlik
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** Not specified

## Problem Description
The customer, Ropes and Gray LLC, reported confusion regarding a security advisory and whether they needed to apply an update. They had already performed an update on July 1, 2024, but their system still indicated that an update was available.

## Environment Details
- The issue occurred after an update was applied on July 1, 2024.
- The system showed that the same update was applied at 7:52 PM on July 1, which was after a prior advisory notice on June 27.

## Troubleshooting Steps
1. Confirmed that the update was applied on July 1, 2024.
2. Advised the customer to disregard the available patch as it was identified as a bug.
3. Suggested setting up a remote session to further investigate the issue.
4. Customer reported that after the update, detailed logs for clients were no longer visible, with only "Policies Received" entries being logged.
5. Identified that the lack of logs was due to a bug introduced by the update.
6. Informed the customer that a hotfix was available to resolve the logging issue.

## Root Cause
The root cause of the issue was a bug in the update applied on July 1, 2024, which caused the logging functionality to fail, resulting in the absence of detailed logs for clients.

## Solution
The issue was resolved by applying a hotfix that addressed the logging bug. The customer was advised to create a snapshot of the server before applying the hotfix. The hotfix was confirmed to not require a reboot, allowing it to be applied during business hours.

## Notes
- Customers experiencing similar issues should be informed to disregard any erroneous patches that appear after an update has been applied, as these may be bugs that are being addressed by the development team.
- Always recommend creating a snapshot of the server before applying hotfixes to ensure that a rollback option is available if needed.