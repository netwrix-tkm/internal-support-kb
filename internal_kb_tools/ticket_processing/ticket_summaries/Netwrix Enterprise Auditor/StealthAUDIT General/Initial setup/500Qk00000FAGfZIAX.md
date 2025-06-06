## Ticket Metadata
- **Ticket ID:** 500Qk00000FAGfZIAX
- **Case Number:** 419694
- **Status:** Closed - Resolved
- **Account/Company:** Daimler Trucks North America LLC
- **Contact Name:** John Anunsen
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.5

## Problem Description
The customer reported that the activity change report for permission changes was not updating as expected.

## Environment Details
- The customer is located in the US (Oregon).
- The issue involved changes made at the Active Directory (AD) level that were not reflected in the file share access reports.

## Troubleshooting Steps
1. Verified that the permission change to the AD group was recorded in the ADI scan and visible under the GroupsMemberView.
2. Confirmed that the account added to the group was recorded by the ADI scan.
3. Checked the FSAA system scan and bulk import jobs to ensure the host where the file share exists was successfully accessed and scanned.
4. Noted that permission changes were recorded for other shares on the same host, but not for the specific AccessReview share.
5. Suggested a test by adding the user associated with the group directly to the file share to monitor if that change would be recorded in the FSAA system scan.

## Root Cause
No specific root cause was identified; however, it was determined that the behavior observed was expected. Changes made at the top level in AD were reported in the ADI scan but not in the FSAA system scan.

## Solution
To resolve the issue, it was clarified that changes need to be made at the file share level to report on file permission changes. The expected functionality was confirmed, indicating that the FSAA system does not automatically reflect changes made at the AD level unless they are also made at the file share level.

## Notes
- Future changes to permissions should be made directly at the file share level to ensure they are reported correctly in the FSAA system.
- It is important to verify the designated timeframe in which changes are made, as this can affect visibility in the reports.