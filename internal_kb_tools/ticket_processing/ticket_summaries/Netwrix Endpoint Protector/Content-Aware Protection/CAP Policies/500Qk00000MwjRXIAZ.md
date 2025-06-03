```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000MwjRXIAZ
- **Case Number:** 438873
- **Status:** Closed - Resolved
- **Account/Company:** Atris Technology, LLC
- **Contact Name:** Mark Bernard
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** Not specified

## Problem Description
The customer was attempting to set up a content-aware policy for credit card information reporting. However, the policy was flagging an excessive number of files on the test computer, leading to confusion about the configuration.

## Environment Details
- The issue occurred on a test computer configured with Netwrix Endpoint Protector.
- The specific content-aware policy was designed to monitor for Personally Identifiable Information (PII), particularly credit card information.

## Troubleshooting Steps
1. The customer reported the issue via a support ticket.
2. Initial communication was established to schedule a remote session for further investigation.
3. During the remote session, the configuration of the content-aware policy was reviewed.
4. It was identified that both file types (Office and text) were selected in the policy settings.

## Root Cause
The root cause of the issue was that the content-aware policy was configured to include specific file types (Office and text) in addition to monitoring for PII. This configuration caused all files of those types to be reported or blocked, regardless of whether they contained PII.

## Solution
To resolve the issue, the following steps were taken:
- The customer was advised to remove the selection of file types from the policy settings.
- The policy was then configured to only monitor for PII information.
- This adjustment ensured that only files containing PII would be flagged, regardless of their file type.

## Notes
- It is important to configure content-aware policies carefully to avoid unnecessary logging and blocking of files that do not contain sensitive information.
- Future users should ensure that file type selections are appropriate for their monitoring needs to prevent similar issues.
```