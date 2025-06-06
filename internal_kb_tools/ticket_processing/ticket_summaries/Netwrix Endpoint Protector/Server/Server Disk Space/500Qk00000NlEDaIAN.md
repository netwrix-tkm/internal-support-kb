## Ticket Metadata
- **Ticket ID:** 500Qk00000NlEDaIAN
- **Case Number:** 441086
- **Status:** Closed - Resolved
- **Account/Company:** Securetech
- **Contact Name:** Subramani Vivek
- **Product:** Netwrix Endpoint Protector
- **Component:** Server Disk Space
- **Feature:** Server Disk Space
- **Version:** 5.8.1.0

## Problem Description
The customer reported that their appliance was running out of disk space, displaying an error message indicating critical low disk space with only 8.78 GB free from a total of 257.22 GB (3%). This situation was affecting the functionality and performance of the EPP server.

## Environment Details
- The server was operating in a closed environment, preventing remote access for troubleshooting.
- The current version of the software was 5.8.1.0.

## Troubleshooting Steps
1. **Initial Assessment**: The support team requested access to the server's UI to check disk space.
2. **Command Execution**: The customer was instructed to run commands via SSH to check disk usage:
   - `df -h` to check overall disk usage.
   - `du -sh /var.eppfiles/* | grep G` to identify large directories.
3. **Error Encountered**: The customer encountered a "500 Internal Server Error" when accessing the server information via the UI.
4. **Disk Space Increase**: The internal storage team increased the disk space, but the specific mount point size remained unchanged.
5. **Service Management**: Instructions were provided to stop services and unmount partitions for resizing.
6. **Disk Resizing**: Commands were executed to resize the disk partitions and check for errors.

## Root Cause
The root cause of the issue was identified as insufficient disk space due to large log files and backups stored on the server, particularly in the `/var/eppfiles/quicklogs` directory.

## Solution
1. The customer successfully executed the commands to resize the disk partitions.
2. After resizing, the disk space was confirmed to be increased to 2.2 TB, with the EPP server now showing 193 GB used out of 2.2 TB.
3. The customer was advised to apply offline patches to update the server from version 5.8.1.0 to 5.9.0.0, ensuring that each patch was applied sequentially.

## Notes
- It is crucial to create a VM snapshot before making any changes to disk sizes to allow for recovery in case of issues.
- The customer was informed that they could directly update from 5.8.1.0 to 5.9.0.0 without needing intermediate updates, but they must apply each patch one at a time and wait for confirmation of installation before proceeding to the next.