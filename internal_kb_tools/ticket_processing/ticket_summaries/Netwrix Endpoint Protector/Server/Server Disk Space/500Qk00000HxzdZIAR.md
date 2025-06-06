```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000HxzdZIAR
- **Case Number:** 426261
- **Status:** Closed - Resolved
- **Account/Company:** Velocity Global
- **Contact Name:** Nathan Cunningham
- **Product:** Netwrix Endpoint Protector
- **Component:** Server Disk Space
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported receiving an error message indicating "Full disk space" when attempting to log into the Netwrix Endpoint Protector appliance. They were unable to find help articles on how to free up disk space.

## Environment Details
- The issue occurred on the Netwrix Endpoint Protector server.
- The disk was filled primarily due to logs and File Shadows, which occupied approximately 123 GB of space.

## Troubleshooting Steps
1. Requested SSH access to the backend of the EPP server from the devops team.
2. Investigated the disk usage and identified that logs and File Shadows were consuming significant space.
3. Confirmed with the customer to delete the File Shadows and reboot the EPP server.
4. Deleted the identified File Shadows and unnecessary backups/patches, freeing up 31 GB of space.
5. Rebooted the EPP server to apply changes.

## Root Cause
The disk space issue was primarily caused by the accumulation of logs and File Shadows, which are copies of files uploaded/copied to the EPP server. The configuration allowed File Shadows to be set at a global level, leading to excessive storage use.

## Solution
- Cleared the File Shadows and unnecessary backups from the server, which resolved the disk space issue.
- Provided recommendations to the customer to prevent future occurrences:
  - Create Audit Log Backups to archive logs and clear space.
  - Set File Shadows at a Computer or Group level instead of globally for all computers.

## Notes
- It is crucial to monitor disk space regularly and manage log retention settings to avoid similar issues.
- Customers should be advised on the implications of enabling File Shadowing and encouraged to limit its use to necessary systems only.
```