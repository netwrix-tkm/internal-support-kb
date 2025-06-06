## Ticket Metadata
- **Ticket ID:** 500Qk00000FJaYcIAL
- **Case Number:** 419980
- **Status:** Closed - Resolved
- **Account/Company:** Allstate Insurance Company
- **Contact Name:** Stealth Audit
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SharePoint
- **Feature:** Sensitive Data
- **Version:** 11.5

## Problem Description
The customer reported that a scheduled SharePoint scan (SPPEEK Scan) appeared to have frozen on the server Y0185-APP0443-S.

## Environment Details
- **Scan Process ID (PID):** 7432
- **Server:** Y0185-APP0443-S
- **Product Version:** 11.5

## Troubleshooting Steps
1. Verified the status of the scheduled scan on the server.
2. Checked system resources (CPU, memory) to determine if the server was under heavy load.
3. Attempted to restart the scan process, but it remained unresponsive.
4. Consulted with the SA/NEA team for additional insights.

## Root Cause
The root cause of the issue was not identified during the troubleshooting process. It was noted as "Root Cause Unknown."

## Solution
The issue was resolved by restarting the scheduled scan, which allowed it to proceed without further issues.

## Notes
- It is advisable to monitor the performance of scheduled scans regularly to identify potential freezing issues early.
- Consider implementing alerts for scan failures or freezes to facilitate quicker responses in the future.