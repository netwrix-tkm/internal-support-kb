## Ticket Metadata
- **Ticket ID:** 500Qk00000JplLVIAZ
- **Case Number:** 430599
- **Status:** Closed - Resolved
- **Account/Company:** WellSpan Health
- **Contact Name:** John Masgalas
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Access Auditing
- **Version:** 11.6

## Problem Description
The customer reported that a newly created job group was crashing during the Permissions job execution. The Activity and SDD jobs were functioning correctly. The issue arose after the server team changed the IP address of the host during the initial run of the Activity job, leading to potential remnants being left behind.

## Environment Details
- The issue occurred in a Windows Server environment.
- The job was configured to point to a host group with one host.

## Troubleshooting Steps
1. Reviewed the error message: `System.IndexOutOfRangeException: There is no row at position 0.`
2. Investigated the impact of the IP address change during the job execution.
3. Assessed the state of the T2 folders on the proxy server for potential corruption.
4. Renamed the old T2 folder associated with the problematic server.
5. Dropped the relevant data from the database.
6. Conducted a shallow test scan to verify if the issue was resolved.
7. Performed a full scan after confirming the shallow test was successful.

## Root Cause
The root cause of the issue was identified as corrupted T2 files on the proxy server, likely resulting from the IP address change during the execution of the Activity job.

## Solution
The issue was resolved by:
- Renaming the old T2 folder for the affected server, effectively deleting the corrupted files.
- Dropping the associated data from the database to clear any remnants.
- Running a shallow test scan to confirm the resolution, followed by a full scan which completed successfully.

## Notes
- It is important to ensure that any changes to server IP addresses are communicated and managed properly to avoid similar issues in the future.
- Regular maintenance of T2 folders on proxy servers may help prevent corruption and related job failures.