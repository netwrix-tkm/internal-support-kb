## Ticket Metadata
- **Ticket ID:** 500Qk00000EVPtKIAX
- **Case Number:** 418292
- **Status:** Closed - Resolved
- **Account/Company:** Bank of Mongolia
- **Contact Name:** Amgalan Kh
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** NONE

## Problem Description
The customer reported that the server disk was full. Although external storage was configured, it was found to be duplicated on the system disk. Additionally, the files were stuck and could not be deleted by users in File Maintenance.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Verified the disk usage on the server to confirm it was full.
2. Checked the configuration of external storage to identify duplication on the system disk.
3. Attempted to delete the duplicated files through File Maintenance, but the operation was unsuccessful.
4. Engaged in a remote session to further investigate and resolve the issue.

## Root Cause
The root cause of the issue was identified as the duplication of external storage on the system disk, which led to the server running out of disk space. The inability to delete files was likely due to permission issues or file locks within the File Maintenance system.

## Solution
The issue was resolved during a remote session where the support technician intervened to:
- Remove the duplicated files from the system disk.
- Ensure that the external storage was correctly configured and not duplicating data on the system disk.
- Confirmed that the server had sufficient disk space post-resolution.

## Notes
- It is important to regularly monitor disk usage and ensure that external storage configurations do not lead to duplication on the system disk.
- Future cases should consider checking for file locks or permission issues if files cannot be deleted in File Maintenance.