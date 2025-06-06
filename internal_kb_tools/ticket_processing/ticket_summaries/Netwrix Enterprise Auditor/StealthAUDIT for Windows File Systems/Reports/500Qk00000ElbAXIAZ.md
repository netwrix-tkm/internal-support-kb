## Ticket Metadata
- **Ticket ID:** 500Qk00000ElbAXIAZ
- **Case Number:** 418799
- **Status:** Closed - Resolved
- **Account/Company:** Medpace, Inc
- **Contact Name:** Brittany Lac
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Reports
- **Version:** 11.6

## Problem Description
The customer reported that the Open Shares report in Netwrix Enterprise Auditor indicated there were no open shares, despite evidence of at least one open share folder existing.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for Windows File Systems
- **Build Number:** 46

## Troubleshooting Steps
1. Confirmed that the Open Access job had been successful.
2. Added the security identifier S-1-5-32-545 to the Open Access job.
3. Verified that the only detected share was a "Phantom Share" labeled as V.
4. Checked that the FSAA group completed successfully, including the Scan, Import, and Exceptions.
5. Reviewed the FS_OpenAccess_RemediationStatus, which indicated that the share was remediated on 4/16/24.
6. Attempted to reproduce the issue in a lab environment but was unable to do so.
7. Pulled new jobs from Instant Solutions and analyzed the FSAA Exceptions - Open Resources task.

## Root Cause
The issue was related to a failure in the detection of known open shares by the Open Access report, despite the FSAA group running successfully. The specific cause was not definitively identified, but it was noted that the FSAA Exceptions did not show the open share.

## Solution
The issue was resolved by rerunning the FSAA workflow, including the FSAA Exceptions, and then executing the job again. This action allowed the Open Shares report to correctly reflect the existing open shares.

## Notes
- The customer expressed a desire to understand why the issue occurred, indicating a need for further investigation into the underlying cause.
- It is important to ensure that the FSAA group runs successfully and that any exceptions are monitored closely to prevent similar issues in the future.
- Consider documenting any changes made during troubleshooting for future reference, especially if the issue arises again.