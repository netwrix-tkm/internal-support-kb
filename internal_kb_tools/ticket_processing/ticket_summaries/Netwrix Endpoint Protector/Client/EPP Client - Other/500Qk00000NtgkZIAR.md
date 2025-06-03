## Ticket Metadata
- **Ticket ID:** 500Qk00000NtgkZIAR
- **Case Number:** 441540
- **Status:** Closed - Resolved
- **Account/Company:** The Stars Group Interactive Services / Flutter International
- **Contact Name:** Denis Pasca
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client - Other
- **Feature:** CAP Policy
- **Version:** Mac OS 15.4

## Problem Description
Users reported issues with building apps using Xcode after upgrading to Mac OS 15.4. The problem was identified as being related to `rsync`, which was causing build failures due to the Endpoint Protector (EPP) Client blocking file transfers.

## Environment Details
- Users were working on Mac OS 15.4.
- The issue was confirmed to be linked to the EPP Client's scanning policies, specifically regarding `rsync`.

## Troubleshooting Steps
1. Collected logs from affected users.
2. Verified if `rsync` was selected as an exit point in the CAP policy assigned to the affected endpoints.
3. Added users to an exemption group to test if the issue persisted.
4. Uninstalled EPP from a test user’s machine to confirm that EPP was the cause of the issue.
5. Analyzed logs which showed a high volume of threat scans related to `rsync`.

## Root Cause
The EPP Client was configured to scan files accessed by `rsync`. When users attempted to build applications, `rsync` was used to copy files, triggering the EPP Client to scan these files. If any files contained confidential content, the EPP Client would block them, causing the build process to fail. This behavior was exacerbated by the recent Mac OS update, which may have altered how `rsync` operates.

## Solution
The resolution involved removing `rsync` from the CAP policy assigned to developers. This change allowed users to build applications without interference from the EPP Client, effectively resolving the issue.

## Notes
- It is recommended to monitor any changes in the behavior of `rsync` after OS updates, as similar issues may arise in the future.
- Consider creating a special policy for developers that excludes `rsync` to mitigate security risks while allowing necessary functionality.
- Ensure that any changes to policies are communicated clearly to all affected users to prevent confusion and downtime.