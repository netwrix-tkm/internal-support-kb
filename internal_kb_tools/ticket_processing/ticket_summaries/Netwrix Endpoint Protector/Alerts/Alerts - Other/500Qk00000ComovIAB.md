## Ticket Metadata
- **Ticket ID:** 500Qk00000ComovIAB
- **Case Number:** 414399
- **Status:** Closed - Resolved
- **Account/Company:** East Global (PT RGE Indonesia)
- **Contact Name:** Stephen Grace
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts - Other
- **Version:** NONE

## Problem Description
The customer reported that the disk space on their system was full, indicating that 100% of the disk space had been utilized.

## Environment Details
- The issue was related to the Netwrix Endpoint Protector platform.
- The disk space issue was primarily caused by the accumulation of shadow copies.

## Troubleshooting Steps
1. The support engineer, Andrei Pop, reviewed the disk space usage and identified that most of the space was occupied by shadow copies.
2. Andrei inquired whether the customer was using the shadow copies and if they could be deleted remotely.
3. The customer confirmed that they were not using the shadow copies.
4. A remote session was scheduled to clear the disk space.

## Root Cause
The root cause of the disk space issue was the accumulation of shadow copies, which are copies of files that the logs refer to. Since the customer was not utilizing these shadow copies, they contributed to the disk space being fully utilized.

## Solution
The issue was resolved by clearing the disk space, specifically by deleting the unnecessary shadow copies. This action was taken during a remote session, which allowed for immediate resolution of the disk space issue.

## Notes
- It is advisable to monitor the disk space regularly to prevent similar issues in the future.
- If shadow copies are not needed, consider disabling this feature to avoid unnecessary disk space consumption.
- Ensure that customers are aware of the function and implications of shadow copies to make informed decisions about their usage.