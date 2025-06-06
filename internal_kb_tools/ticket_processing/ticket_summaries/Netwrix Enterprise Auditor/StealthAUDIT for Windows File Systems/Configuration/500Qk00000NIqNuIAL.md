## Ticket Metadata
- **Ticket ID:** 500Qk00000NIqNuIAL
- **Case Number:** 439897
- **Status:** Closed - Resolved
- **Account/Company:** Allstate Insurance Company
- **Contact Name:** Stealth Audit
- **Product:** Netwrix Enterprise Auditor
- **Component:** Configuration
- **Feature:** DropFSHostData Job
- **Version:** 11.6

## Problem Description
The customer reported that the "DropFSHostData" job failed with the error message "Job connection profile is not available." This job is intended to remove data for decommissioned hosts from the Enterprise Auditor database.

## Environment Details
- The job was configured following the instructions from the Netwrix knowledge base article.
- The customer has over 13,000 hosts listed in their system.

## Troubleshooting Steps
1. Scheduled a remote support session to review the job configuration.
2. Identified that the "DropFSHostData" job had an empty connection profile (no connection profile was selected).
3. Configured the job with an existing connection profile and restarted it.
4. Monitored the job execution, which took over 5 hours to complete for 2 hosts.
5. Analyzed logs to determine the cause of the long execution time, focusing on the "FSAA_Hosts" analysis task.
6. Suggested disabling the "FSAA_Hosts" analysis task to improve performance.

## Root Cause
The root cause of the initial failure was the absence of a selected connection profile for the "DropFSHostData" job. Although the job was designed to remove data rather than scan it, a connection profile is still required for execution.

## Solution
The issue was resolved by:
- Selecting an appropriate connection profile for the "DropFSHostData" job.
- Restarting the job, which then executed successfully.
- To address performance concerns, the "FSAA_Hosts" analysis task was disabled, which significantly reduced the job completion time.

## Notes
- The job took an excessive amount of time (over 5 hours) to complete for only 2 hosts due to the analysis task processing a large number of hosts (over 13,000).
- It is advisable to disable unnecessary analysis tasks for jobs that do not require them to improve performance.
- Future users should ensure that a valid connection profile is selected before executing jobs to avoid similar issues.