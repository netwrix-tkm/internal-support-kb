## Ticket Metadata
- **Ticket ID:** 500Qk00000DkjdqIAB
- **Case Number:** 416526
- **Status:** Closed - Resolved
- **Account/Company:** Addleshaw Goddard LLP
- **Contact Name:** Sean Reilly
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Health
- **Version:** 5.9.4.0

## Problem Description
The customer reported experiencing high CPU spikes on their EPP product, which lasted for a few minutes, and noted that the EPP portal was nearly unusable between 9:00 and 10:00 AM daily. They requested a resource check to ensure adequate resources were allocated for optimal performance.

## Environment Details
- **Azure VM Resource:** D4s_v3
  - **vCPUs:** 4
  - **RAM:** 16 GiB
  - **Data Disks:** 8
- **Licenses:** 3150 (approximately 2500 in use at peak times)
- **Current Device Count:** 3281

## Troubleshooting Steps
1. Reviewed the current resource allocation for the EPP product.
2. Identified and freed up network duplicates, which amounted to approximately 800,000 entries.
3. Rebooted the MySQL service to refresh the database connections.
4. Monitored the `df -i` command output for inode usage on the `dev/shm/mcace` location.

## Root Cause
The high CPU usage and portal unavailability were primarily caused by excessive network duplicates, which overloaded the system resources during peak usage times.

## Solution
The issue was resolved by:
- Removing the excessive network duplicates, which significantly reduced the load on the system.
- Restarting the MySQL service to ensure that the database was functioning optimally after the cleanup.

## Notes
- It is recommended to implement a routine check for network duplicates to prevent similar issues in the future.
- Consider automating the deletion of inactive machines that have not connected for a specified number of days to reduce manual overhead and improve system performance.