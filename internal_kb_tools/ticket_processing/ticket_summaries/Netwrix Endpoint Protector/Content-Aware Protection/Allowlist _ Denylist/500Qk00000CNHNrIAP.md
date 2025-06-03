## Ticket Metadata
- **Ticket ID:** 500Qk00000CNHNrIAP
- **Case Number:** 413237
- **Status:** Closed - Resolved
- **Account/Company:** Laykon Distributor
- **Contact Name:** Yağız Özkütük
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Allowlist / Denylist
- **Version:** Not specified

## Problem Description
The client reported that .dwg files were being blocked despite adding the specific domain to the Allowlist. The logs indicated that the blockage was due to a "Blocked File" rule, but no such policy was found in the Content Aware Protection settings.

## Environment Details
- The issue occurred within the Netwrix Endpoint Protector platform, specifically under the Content-Aware Protection feature.

## Troubleshooting Steps
1. Verified that the domain was correctly added to the Allowlist.
2. Checked the logs to confirm the reason for the file blockage.
3. Searched for any existing policies related to "Blocked File" in the Content Aware Protection settings.
4. Scheduled a remote session with the client to further investigate the issue.

## Root Cause
The issue was caused by the .dwg file extension being included in the policy denylist, which prevented the file from being sent even though the domain was allowed.

## Solution
During the remote session, the support engineer added the .dwg file extension to the policy denylist and ensured that the specific email domain was included in the policy allowlist. This adjustment resolved the issue, allowing the client to send .dwg files to the specified domain without blockage.

## Notes
- Ensure that any file extensions that need to be sent via email are not included in the denylist.
- Regularly review both the Allowlist and Denylist to prevent similar issues in the future.
- If a file type is being blocked unexpectedly, check both lists and the logs for any conflicting rules.