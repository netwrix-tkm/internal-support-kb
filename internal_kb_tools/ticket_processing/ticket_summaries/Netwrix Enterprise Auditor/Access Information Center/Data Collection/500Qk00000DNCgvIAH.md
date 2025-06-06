## Ticket Metadata
- **Ticket ID:** 500Qk00000DNCgvIAH
- **Case Number:** 415604
- **Status:** Closed - Resolved
- **Account/Company:** M&G Investments
- **Contact Name:** Warren Stevens
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Data Collection
- **Version:** 11.5

## Problem Description
The customer reported that Effective Access reports were blank in the Access Information Center (AIC). Despite confirming that the folder had user permissions and that the Permissions Report was displaying group and user/group memberships, the Effective Access view was not showing any results.

## Environment Details
- The customer operates two hosts: 
  - Host 1: Main file system with an active query and part of an FSAA scan.
  - Host 2: Offline, used only for testing.
- The directory in question is "Stealthbits" located on Host 1.

## Troubleshooting Steps
1. Verified user permissions on the folder in question.
2. Checked the Permissions Report for group and user/group memberships.
3. Confirmed that Host 1 was part of an FSAA scan and had an active query.
4. Reviewed the health of FSAA scans and Bulk Import jobs.
5. Suggested checking the collected permissions on the shares.
6. Discussed the need for a meeting to investigate why `dbo.SA_FSAA_EffectiveAccessView` was not updating properly.

## Root Cause
The root cause of the issue was identified as incorrect configuration related to the target server software, specifically affecting the Effective Access view not updating as expected.

## Solution
The issue was resolved by deleting the records from the BD (presumably the database), which allowed the Effective Access reports to populate correctly in the AIC.

## Notes
- Ensure that the FSAA-System Scans and Bulk Import jobs are functioning correctly, as they are required to update the Effective Access view.
- Future investigations should include checking the health of the FSAA scans and verifying that the collected permissions are accurately reflected in the AIC.
- It may be beneficial to document any changes made to the configuration to prevent similar issues from arising in the future.