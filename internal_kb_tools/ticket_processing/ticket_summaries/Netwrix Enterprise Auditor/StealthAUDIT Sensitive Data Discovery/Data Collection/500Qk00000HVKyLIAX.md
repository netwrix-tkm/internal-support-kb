## Ticket Metadata
- **Ticket ID:** 500Qk00000HVKyLIAX
- **Case Number:** 425174
- **Status:** Closed - Resolved
- **Account/Company:** Eisai, Inc.
- **Contact Name:** William Lavary
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT Sensitive Data Discovery
- **Feature:** Data Collection
- **Version:** 11.6

## Problem Description
The customer reported that password-protected Office files (e.g., Excel) were being skipped during Sensitive Data Discovery (SDD) scans without any warning messages. The customer expected to see notifications for skipped files, similar to previous versions (11.0 or 11.5), where such warnings were provided.

## Environment Details
- The issue was observed in version 11.6 of the Netwrix Enterprise Auditor.
- The scans were conducted using the StealthAUDIT Sensitive Data Discovery component.

## Troubleshooting Steps
1. Reviewed the debug logs to identify any messages related to skipped files but found no relevant entries.
2. Escalated the issue due to the lack of error/warning messages in the job log.
3. Applied a hotfix released by development, which improved logging for locked files but still reported the SDD Temp folder path instead of the original file path.
4. Engaged in internal discussions to address customer frustration and determine next steps.
5. Identified additional scenarios where warnings were not generated, particularly for password-protected files within non-password-protected ZIP files.

## Root Cause
The root cause was identified as a defect in the product where the logging mechanism did not properly report skipped files, particularly password-protected files. The interaction between the FSAA and Tika libraries was also contributing to the issue, especially for files within ZIP archives.

## Solution
- A hotfix was released and applied, which improved the logging of skipped files. However, it initially reported the SDD Temp folder path instead of the original file path.
- Development fast-tracked a second hotfix to ensure that all skipped files would be logged with appropriate warnings, including the original file paths.
- The customer was kept informed throughout the process, and a follow-up was conducted to ensure all scenarios were addressed.

## Notes
- It is important to ensure that all skipped files are logged with clear warnings in future updates to avoid customer frustration.
- The customer expressed disappointment that the issue was not caught during QA, highlighting the need for thorough testing of logging functionalities.
- Future cases involving password-protected files, especially within ZIP archives, should be monitored closely to ensure proper logging and notifications are in place.