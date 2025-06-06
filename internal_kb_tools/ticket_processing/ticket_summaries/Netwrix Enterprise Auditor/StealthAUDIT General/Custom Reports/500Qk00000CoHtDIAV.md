```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CoHtDIAV
- **Case Number:** 414384
- **Status:** Closed - Resolved
- **Account/Company:** Cedars-Sinai Medical Center
- **Contact Name:** Andrew Kim
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Custom Reports
- **Version:** 11.5

## Problem Description
The customer reported encountering various permission scanning errors with the FSAA System Scans, including deadlock issues and unexpected behavior where certain directories were not excluded from scans despite attempts to do so.

## Environment Details
- The issue was related to permission scanning on a network share, specifically involving a NetApp server.
- The FSAA proxies were initially installed in an incorrect directory, leading to storage issues.

## Troubleshooting Steps
1. Reviewed error logs and identified deadlock messages related to the FSAA system scans.
2. Attempted to exclude problematic directories from the scans, but they continued to be scanned.
3. Investigated the installation directory of the FSAA proxies and confirmed they were incorrectly placed.
4. Uninstalled and reinstalled the FSAA proxies in the designated directory with adequate storage.
5. Made adjustments to the FSAA scan query properties to prevent restarts and allow continuation from where scans left off.
6. Monitored the scans after implementing changes to ensure they progressed without hanging.

## Root Cause
The primary cause of the issue was identified as a combination of:
- Access denied errors for certain shares/subfolders on the NetApp server, which caused the scans to hang.
- FSAA proxies being installed in a directory with insufficient storage, leading to performance issues during the scanning process.

## Solution
The issue was resolved by:
- Correctly installing the FSAA proxies in a designated directory with sufficient space.
- Implementing folder and share exclusions for the problematic shares that were causing access denied errors.
- Adjusting the FSAA scan settings to allow continuation of scans rather than restarting them, which helped in avoiding timeouts and deadlocks.

## Notes
- It is recommended to monitor the FSAA scans closely after making configuration changes.
- If similar issues arise in the future, generating a process dump on the FSAA proxy host may provide additional insights for troubleshooting.
- Ensure that all relevant logs (process dumps, msinfo32 exports, proxy logs) are collected and reviewed during troubleshooting.
```