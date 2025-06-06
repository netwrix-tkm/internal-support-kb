## Ticket Metadata
- **Ticket ID:** 500Qk00000HPsufIAD
- **Case Number:** 424906
- **Status:** Closed - Resolved
- **Account/Company:** Gameskraft
- **Contact Name:** Vikash Singh
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** NONE

## Problem Description
The customer reported a "disk full" issue, which prevented them from logging into the DLP server for more than three minutes. They had allocated 600 GB of space to the server, but the console displayed only 250 GB available.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Verified the disk space allocation on the DLP server.
2. Checked the console for discrepancies in reported disk space.
3. Attempted to log into the server to assess performance and access issues.

## Root Cause
The root cause of the issue was identified as insufficient disk space being allocated or recognized by the server, leading to performance degradation and login issues.

## Solution
The issue was resolved by:
- **Extending the disk space** allocated to the DLP server to ensure sufficient storage.
- **Optimizing the server** to improve performance and ensure that the disk space was correctly recognized by the system.

## Notes
- It is important to regularly monitor disk space usage on servers to prevent similar issues in the future.
- Consider implementing alerts for low disk space to proactively address potential problems before they impact server performance.