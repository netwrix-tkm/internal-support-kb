```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CVWzDIAX
- **Case Number:** 413541
- **Status:** Closed - Resolved
- **Account/Company:** Tech Elecon Pvt. Ltd. (Elecon Engineering Group)
- **Contact Name:** Mohit Shastri
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server
- **Feature:** EPP Server - Other
- **Version:** NONE

## Problem Description
The customer reported that no logs were being captured on the EPP server after backing up the logs on the server.

## Environment Details
- The server space increased from 162 GB to 164 GB after the backup, indicating that logs were being generated but not captured by the EPP server.

## Troubleshooting Steps
1. The support team requested additional details from the customer, including screenshots and a description of the logs that were not being captured.
2. A meeting was scheduled to further investigate the issue.
3. During the meeting, the issue was reproduced by attempting to share a file outside the organization, which should have generated logs.
4. The support team confirmed that the hotfix (adv-2024-002) was applied to the server.
5. The customer was advised to restart the server to ensure the hotfix took effect.

## Root Cause
The issue was identified as a failure to capture logs due to the server not being restarted after the application of the hotfix. This prevented the changes from taking effect.

## Solution
The issue was resolved after confirming with the customer that the hotfix was applied successfully. The customer was advised to restart the server, which allowed the logs to be captured correctly.

## Notes
- It is important to restart the server after applying hotfixes to ensure that all changes take effect.
- The customer requested missing logs from July 1 to July 4, which were confirmed to be safe in the backup archive.
- Future cases should ensure that customers are reminded to restart their servers after applying updates or hotfixes.
```