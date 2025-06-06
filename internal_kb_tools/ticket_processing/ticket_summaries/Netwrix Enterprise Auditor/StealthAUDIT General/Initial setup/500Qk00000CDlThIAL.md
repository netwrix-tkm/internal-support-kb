```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CDlThIAL
- **Case Number:** 412805
- **Status:** Closed - Resolved
- **Account/Company:** Mastercard
- **Contact Name:** Naeemah Robert
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.6

## Problem Description
After upgrading to version 11.6, the customer reported that jobs in Stealth Audit were taking significantly longer to complete, with some jobs increasing from 20 minutes to over 2 hours.

## Environment Details
- **Servers Involved:** stl4amcaud10, bel4amcaud10

## Troubleshooting Steps
1. Conducted a meeting with the customer to review SQL jobs and their performance post-upgrade.
2. Noted the number of threats assigned to the jobs (initially 4).
3. Increased the number of threads from 4 to 8 to assess if this would improve job completion times.
4. Monitored job performance after the increase in threads.
5. Reviewed logs for any anomalies related to job execution times.

## Root Cause
The increase in job execution time was attributed to the insufficient number of threads assigned to the jobs. The initial configuration of 4 threads was inadequate for the workload, leading to longer processing times.

## Solution
The issue was resolved by increasing the number of threads from 4 to 8. Following this adjustment, the customer reported that jobs were running faster and more efficiently, aligning with the performance observed in their production environment.

## Notes
- It is important to monitor thread configurations after upgrades, as changes in software versions may impact performance.
- Ensure that the number of threads is appropriate for the workload to prevent similar issues in the future.
- The customer confirmed that the adjustments made were satisfactory, and they proceeded with upgrading their production servers.
```