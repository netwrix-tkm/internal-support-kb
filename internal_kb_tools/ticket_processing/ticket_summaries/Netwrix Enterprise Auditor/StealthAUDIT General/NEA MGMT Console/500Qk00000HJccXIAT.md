## Ticket Metadata
- **Ticket ID:** 500Qk00000HJccXIAT
- **Case Number:** 424605
- **Status:** Closed - Resolved
- **Account/Company:** TSMC
- **Contact Name:** Support Sphinxtec
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** NEA MGMT Console
- **Version:** 11.0

## Problem Description
The customer, TSMC, reported that a scheduled job executed by the Netwrix Enterprise Auditor (NEA) took longer to complete than the same job run in interactive mode. They requested clarification and assistance regarding this discrepancy.

## Environment Details
- **Product Version:** 11.0
- **Build Number:** 11.0.0.231

## Troubleshooting Steps
1. The customer was asked to share logs for the scheduled job to facilitate analysis.
2. The customer modified the scheduling priority for the task to ensure it was completed first.

## Root Cause
The issue was identified as being related to incorrect configuration regarding the scheduling priority of the job. The scheduled job was not prioritized appropriately, leading to longer execution times compared to the interactive mode.

## Solution
The customer resolved the issue by modifying the scheduling priority for the task, allowing it to be completed first. This adjustment ensured that the scheduled job executed more efficiently, aligning its performance closer to that of the interactive job.

## Notes
- It is important to ensure that scheduling priorities are configured correctly to avoid performance discrepancies between scheduled and interactive job executions in the future.
- Customers should be encouraged to share logs for analysis when performance issues arise, as this can help identify configuration-related problems quickly.