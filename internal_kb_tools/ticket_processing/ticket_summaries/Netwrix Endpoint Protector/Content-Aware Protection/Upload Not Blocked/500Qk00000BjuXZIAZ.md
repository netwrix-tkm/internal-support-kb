```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BjuXZIAZ
- **Case Number:** 411684
- **Status:** Closed - Resolved
- **Account/Company:** Deloitte Services LP
- **Contact Name:** Zion R
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Upload Not Blocked
- **Version:** Not specified

## Problem Description
The customer reported that uploads were going through without being blocked by the configured policy, despite the presence of block pop-ups indicating that the policy was active.

## Environment Details
- The issue was reported while using the Netwrix Endpoint Protector, specifically the Content-Aware Protection feature.
- The customer had implemented a policy to block files containing a specific passcode.

## Troubleshooting Steps
1. Initial communication with the customer to gather more details about the issue, including the exit point being blocked and the types of files affected.
2. Scheduled a remote session to further investigate the issue.
3. During the remote session, the support team replicated the issue, generated log files, and recorded the behavior.
4. The issue was escalated to the development team for further analysis.

## Root Cause
The behavior reported was identified as a known limitation for the New Outlook application. The Endpoint Protector client on macOS was able to report confidential content but not block it due to the use of Microsoft Sync Technology.

## Solution
The support team confirmed the limitation and communicated this to the customer. They advised that the issue was under review by the development team, but no estimated time for a fix was provided.

## Notes
- Customers using New Outlook on macOS should be aware that the Endpoint Protector client may not block confidential content due to this known limitation.
- It is recommended to monitor updates from the development team regarding potential fixes for this issue.
```