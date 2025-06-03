```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000COIeRIAX
- **Case Number:** 413315
- **Status:** Closed - Resolved
- **Account/Company:** Optics 1
- **Contact Name:** Gregg Monagle
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** 5.9.3.0

## Problem Description
The customer reported that after applying console updates from a recent security advisory, their whitelisting functionality stopped working. Although the server displayed all whitelisted devices, these devices were blocked on the endpoints. The customer noted that re-adding each device to the Allowed group resolved the issue temporarily, but this was impractical due to the large number of devices.

## Environment Details
- The issue occurred after applying a hotfix (adv-2024-002) and upgrading the EPP server to version 5.9.3.0.
- The customer also reported that file tracing functionality stopped working after the update.

## Troubleshooting Steps
1. Conducted a remote session with the customer to investigate the issue.
2. Reviewed logs and confirmed that the hotfix was applied multiple times.
3. Identified duplicate devices in the system.
4. Deleted the mcache and rebuilt the PHP.
5. Cleared cached rights from the intermediate MySQL tables.

## Root Cause
The issue was caused by duplicate devices being present in the system, which interfered with the device rights functionality. The hotfix was applied correctly, but the presence of duplicates led to the blocking of whitelisted devices.

## Solution
The issue was resolved by:
- Marking duplicate devices as deleted.
- Deleting the mcache.
- Rebuilding the PHP and clearing cached rights from the MySQL tables.
After these steps, the device rights functionality was restored, and logs began to come in as expected.

## Notes
- The file tracing issue is a known problem and is currently being addressed. It is recommended to raise a separate support ticket for this specific issue.
- Ensure that the hotfix is applied only once to avoid confusion regarding its status in the system.
- Monitor the system for any recurrence of the issue for a few days after applying the fix.
```