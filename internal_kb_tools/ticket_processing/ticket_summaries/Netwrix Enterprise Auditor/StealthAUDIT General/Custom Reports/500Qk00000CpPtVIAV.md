```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CpPtVIAV
- **Case Number:** 414449
- **Status:** Closed - Resolved
- **Account/Company:** AIG Global Operations, Inc.
- **Contact Name:** Tushar Dagaduvetal
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Custom Reports
- **Version:** 11.6

## Problem Description
The customer reported that distribution lists (DLs) were not being updated after the completion of a scheduled task.

## Environment Details
- The issue was related to a custom job created approximately 10 years ago for AIG through Stealthbits (now Netwrix).
- The job was running on a SQL server and was expected to update Exchange distribution lists.

## Troubleshooting Steps
1. Initial contact was made with the customer to gather more information about the issue.
2. A separate ticket regarding the DL_Feeds job health check was identified.
3. A meeting was scheduled to discuss the issue in detail.
4. The customer provided screenshots and logs showing discrepancies in the AD_Contact listing job.
5. The support team reviewed the custom job's functionality and its data collection process.
6. A follow-up meeting was held to discuss findings and next steps.

## Root Cause
The custom job was found to be running and collecting the correct data; however, it was not successfully joining the data needed to update the distribution lists in Exchange. The customer was unfamiliar with the job's intended function, complicating troubleshooting efforts.

## Solution
The issue was escalated to the Professional Services team for further investigation and resolution. It was determined that the custom job required modifications to function correctly and meet the current requirements. The account manager was also involved to facilitate this engagement.

## Notes
- The customer emphasized the urgency of the issue as it affected corporate communication distribution lists.
- It is important for future cases to gather detailed information about custom jobs and their intended functions to expedite troubleshooting.
- Any documentation or examples related to the custom job's expected behavior would be beneficial for the support team.
```