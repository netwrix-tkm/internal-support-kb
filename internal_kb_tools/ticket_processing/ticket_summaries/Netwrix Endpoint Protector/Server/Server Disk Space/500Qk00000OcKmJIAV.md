```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000OcKmJIAV
- **Case Number:** 443632
- **Status:** Closed - Resolved
- **Account/Company:** AGS Health Inc.
- **Contact Name:** Palvannan Thangaiah
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** NONE

## Problem Description
The customer reported an inability to access the Endpoint Protector (EPP) server and console, requesting urgent assistance to resolve the issue.

## Environment Details
- The EPP Server Appliance was hosted on a hypervisor with a physical hard disk allocation of 320 GB.
- The total disk space usage reported was 500 GB, exceeding the allocated space.

## Troubleshooting Steps
1. Conducted a remote session to investigate the issue.
2. Checked disk space usage on the EPP Server Appliance.
3. Identified that 180 GB of disk space was consumed by 6 snapshots stored on the hypervisor.
4. Advised the customer to delete older snapshots to free up disk space.
5. After deletion of snapshots, rebooted the EPP Server Appliance to verify functionality.

## Root Cause
The root cause of the issue was the EPP Server Appliance running out of disk space due to excessive snapshot storage, which filled the allocated physical hard disk space on the hypervisor.

## Solution
The issue was resolved by:
- Deleting older snapshots that were consuming 180 GB of disk space.
- Rebooting the EPP Server Appliance, which allowed it to resume normal operations and restored access to the web UI.

## Notes
- It is recommended to monitor disk space usage regularly and manage snapshots effectively to prevent similar issues in the future.
- Customers should be advised to allocate sufficient disk space for their EPP Server Appliance, considering potential growth and snapshot usage.
```