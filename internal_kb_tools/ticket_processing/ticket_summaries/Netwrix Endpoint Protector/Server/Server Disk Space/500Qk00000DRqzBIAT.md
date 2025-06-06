## Ticket Metadata
- **Ticket ID:** 500Qk00000DRqzBIAT
- **Case Number:** 415817
- **Status:** Closed - Resolved
- **Account/Company:** FAN Courier
- **Contact Name:** Danut Pirvu
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** NONE

## Problem Description
The customer reported an issue while attempting to apply the Security Update – EPP Server Hotfix #1.1. Although the update process indicated that the patch was applied successfully, the patch remained available in the Endpoint Protector Server menu under Live Update - Available EPP Software Updates. The customer suspected that insufficient disk space was the cause of the issue.

## Environment Details
- **Disk Space System:** 38 GB used (82% of 50 GB)
- **Disk Space EPP Server:** 582 GB used (32% of 2.0 TB)
- **Free Disk Space:** 8.65 GB out of 49.04 GB (18%)

## Troubleshooting Steps
1. Verified the disk space usage on the system and EPP server.
2. Confirmed that the update process completed with a "Patch applied successfully" status.
3. Identified that the system partition had limited free space, which could hinder the application of updates.
4. Noted that a PHP log file was excessively large, consuming 27 GB of space.

## Root Cause
The root cause of the issue was identified as insufficient disk space on the system partition, which prevented the successful application of the security update despite the update process indicating success.

## Solution
To resolve the issue, the following steps were taken:
1. The large PHP log file, which was 27 GB in size, was identified and deleted to free up disk space.
2. The customer was advised to map the 2 TB storage attached to the VM for other components/system logs to further increase the capacity of the 50 GB system partition.

After these actions, the customer was able to successfully apply the Security Update – EPP Server Hotfix #1.1.

## Notes
- It is important to monitor disk space regularly to prevent similar issues in the future.
- Consider implementing log rotation or cleanup policies to manage log file sizes effectively.
- Ensure that sufficient disk space is available before applying updates to avoid complications.