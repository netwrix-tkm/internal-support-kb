## Ticket Metadata
- **Ticket ID:** 500Qk00000HGErfIAH
- **Case Number:** 424469
- **Status:** Closed - Resolved
- **Account/Company:** FNB - First National Bank
- **Contact Name:** Clint Swartz
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** NONE

## Problem Description
The customer reported that a backup v1 task initiated on the evening of October 19, 2024, was stuck at 99% completion. Additionally, a daily reporting task entered a loop from approximately 11 PM on the same day until 12 PM the following day, which the customer suspected might be related to the stuck backup task.

## Environment Details
- **Build Number:** 5940
- **Platform:** Netwrix Endpoint Protector

## Troubleshooting Steps
1. Verified the status of the backup v1 task to confirm it was indeed stuck at 99%.
2. Checked system logs for any errors or warnings related to the backup process.
3. Investigated the daily reporting task to determine if it was impacted by the backup task.
4. Attempted to manually terminate the stuck backup task to see if it would allow the reporting task to complete.

## Root Cause
The root cause of the issue was identified as a failure in the backup v1 task that caused it to hang at 99% completion. This failure subsequently affected the execution of the daily reporting task, causing it to enter a loop.

## Solution
The issue was resolved by removing the status for the System Backup V1 task, which allowed the system to clear the stuck process. The customer confirmed that the resolution was effective and requested the ticket to be closed.

## Notes
- It is important to monitor backup tasks closely, especially when they approach completion, to prevent similar issues in the future.
- If a backup task becomes unresponsive, consider checking for system resource constraints or conflicts with other scheduled tasks.
- Regularly review system logs for early detection of potential issues with backup processes.