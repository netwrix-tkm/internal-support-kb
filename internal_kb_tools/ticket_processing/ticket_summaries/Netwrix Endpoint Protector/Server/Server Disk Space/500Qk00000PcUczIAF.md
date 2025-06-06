## Ticket Metadata
- **Ticket ID:** 500Qk00000PcUczIAF
- **Case Number:** 446290
- **Status:** Closed - Resolved
- **Account/Company:** EMSLAND-STÄRKE GMBH
- **Contact Name:** Eike Arends
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported that their appliance was running low on disk space and prompted to back up Audit Log Files. Despite configuring the backup, there was no change in disk space usage. The customer inquired about the possibility of expanding the disk at the hypervisor level.

## Environment Details
- The appliance was running on a customer-managed system.
- The root partition was reported to be at 86% usage with only 7GB available.

## Troubleshooting Steps
1. Verified the disk space usage on the appliance, confirming it was at 86% with only 7GB available.
2. Investigated disk usage with the command:
   ```bash
   du -sh /*
   ```
3. Identified that the PHP log was consuming 27GB of space:
   ```bash
   du -sh /usr/local/logs/*
   ```
4. Cleared the PHP log file and vacuumed the system journal, which was using 4GB of space, using the command:
   ```bash
   journalctl --vacuum-size=500M
   ```
5. After cleanup, confirmed that the disk usage dropped to 20% with 38GB available.

## Root Cause
The issue was caused by excessive growth of log files, specifically the PHP logs and system journal, which consumed a significant amount of disk space.

## Solution
The issue was resolved by manually clearing the large log files (PHP logs and system journal) on the appliance. This action significantly reduced disk usage, allowing the appliance to operate without the low disk space warning.

## Notes
- Backing up Audit Log Files does not automatically remove or archive the original log files from the appliance, which can lead to continued high disk usage.
- It is advisable to implement log rotation or regular cleanup procedures to prevent excessive log file growth in the future.
- If considering disk expansion at the hypervisor level, ensure that it is supported and follow the appropriate procedures for resizing the disk.