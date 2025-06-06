## Ticket Metadata
- **Ticket ID:** 500Qk00000KdazTIAR
- **Case Number:** 432213
- **Status:** Closed - Resolved
- **Account/Company:** Allstate Insurance Company
- **Contact Name:** Stealth Audit
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Health Check Request
- **Version:** 11.6

## Problem Description
The customer reported that the transaction log for the database 'tempdb' was full due to 'ACTIVE_TRANSACTION', which was causing job failures. Additionally, there was a notification indicating that the F: drive was low on space.

## Environment Details
- **Database Recovery Model:** Simple Recovery Mode
- **Symptoms:** Jobs or reports could not be run on an overfilled database, leading to transaction log bloating.

## Troubleshooting Steps
1. Confirmed the error message related to the transaction log being full.
2. Noted that the F: drive was low on space.
3. Investigated the recovery model of the database, which was set to Simple Recovery Mode.
4. Analyzed the state of the transaction log and identified it was bloated due to uncommitted transactions.
5. Suggested running analytics queries to gather more information about the transactions.

## Root Cause
The root cause of the issue was identified as a bloated transaction log in the 'tempdb' database, primarily due to hundreds of millions of uncommitted transactions. This situation was exacerbated by low disk space on the F: drive.

## Solution
The resolution involved advising the customer to contact their DBA team to perform a manual cleanup of the transaction log and address the uncommitted transactions. After the cleanup, the customer confirmed that everything was functioning as intended.

## Notes
- It is important to monitor the transaction log size and the state of uncommitted transactions regularly to prevent similar issues in the future.
- Ensure that there is adequate disk space available on all drives, especially those hosting critical databases like 'tempdb'.
- Consider implementing alerts for low disk space and transaction log size thresholds to proactively manage these resources.