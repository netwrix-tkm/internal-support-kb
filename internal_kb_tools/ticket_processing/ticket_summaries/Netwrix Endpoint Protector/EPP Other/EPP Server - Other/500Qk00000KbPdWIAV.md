```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000KbPdWIAV
- **Case Number:** 432060
- **Status:** Closed - Resolved
- **Account/Company:** Nixon Peabody LLP
- **Contact Name:** Danielle Rochford
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** EPP Server - Other
- **Version:** Server version: 5940, Client version: Windows 10 - 6231

## Problem Description
The customer reported that logs were not capturing the actual websites used during file uploads. Instead, the logs indicated generic Amazon sites (e.g., `s3.amazonaws.com`) rather than the specific websites (e.g., `Smartsheets.com`, `WeTransfer`) being utilized.

## Environment Details
- **All or only few endpoints:** All endpoints
- **All browsers or only certain ones:** Edge
- **Browser used for testing:** Edge
- **Reporting V2:** Enabled
- **DPI:** Enabled

## Troubleshooting Steps
1. Collected logs from the customer for analysis.
2. Conducted remote testing using the Edge browser with the following websites:
   - `app.smartsheet.com`
   - `wetransfer`
3. Verified that the issue persisted regardless of the file uploaded.
4. Escalated the issue to R&D for further investigation.
5. Provided a test build to the customer to address the logging issue.

## Root Cause
The issue was identified as a limitation in the logging mechanism where the destination details for file uploads were not accurately reflecting the actual websites used, particularly for sites that redirect uploads to Amazon S3.

## Solution
A test build was created and provided to the customer, which included modifications to the logging mechanism. This build successfully resolved the issue by ensuring that the logs captured the correct website information, including the origin of the uploads.

## Notes
- The customer reported a follow-up issue regarding content remediation logs, indicating that while the initial problem was resolved, further investigation may be needed for related issues.
- It is important to ensure that any future test builds are thoroughly vetted for similar logging issues to prevent recurrence.
```