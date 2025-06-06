## Ticket Metadata
- **Ticket ID:** 500Qk00000ESaZyIAL
- **Case Number:** 418171
- **Status:** Closed - Resolved
- **Account/Company:** American Fidelity Assurance Company
- **Contact Name:** Calvin Minnick
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SharePoint
- **Feature:** Data Collection
- **Version:** Not specified

## Problem Description
The customer reported that SharePoint collections were locking the database, preventing access to the Network Enterprise Auditor (NEA) Console, particularly on Thursday mornings. The job "SP_StaleUsers" was identified as running for an excessive duration of 5 hours and 33 minutes, causing the database to be locked.

## Environment Details
- The issue occurred during scheduled SharePoint collection jobs.
- The customer experienced similar problems the previous week, necessitating a server restart to reset StealthAudit.

## Troubleshooting Steps
1. Identified that the NEA was encountering deadlocks and table blocks during SharePoint collection or report generation.
2. Reviewed logs to determine the cause of the console locking.
3. Disabled the "SP_StaleUsers" job to test if it resolved the locking issue.
4. Monitored the SharePoint group performance after disabling the job.
5. Re-enabled the job for a scheduled run to observe its impact on the console.

## Root Cause
The issue was caused by multiple SharePoint jobs running simultaneously, which attempted to access the same database table, leading to deadlocks and blocking.

## Solution
To resolve the issue, the runtimes of each job/group were assessed, and the start times of conflicting jobs were adjusted to avoid simultaneous execution. After disabling the "SP_StaleUsers" job, the SharePoint group was able to run successfully without locking the database. The job was then re-enabled for a later test run.

## Notes
- It is important to monitor job runtimes and adjust scheduling to prevent conflicts in the future.
- Consider implementing a review of job configurations and settings as part of regular maintenance to avoid similar issues.
- Ensure that application logs are collected for analysis if the console hangs again during job execution.