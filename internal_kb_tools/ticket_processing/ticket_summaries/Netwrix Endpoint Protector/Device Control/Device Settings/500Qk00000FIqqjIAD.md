```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000FIqqjIAD
- **Case Number:** 419931
- **Status:** Closed - Resolved
- **Account/Company:** DataCultr
- **Contact Name:** Ganga Singh
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Settings
- **Version:** Not specified

## Problem Description
The customer reported issues with file shadowing functionality within the Netwrix Endpoint Protector, indicating that shadows were not being generated as expected.

## Environment Details
- The issue was related to the configuration of file shadowing policies and the size thresholds set within the system.

## Troubleshooting Steps
1. Reviewed the file shadowing policy settings, including file size thresholds.
2. Conducted tests on the dlptest.endpointprotector.com to replicate the issue.
3. Analyzed logs to determine if files were being scanned or hashed correctly.
4. Confirmed that the policy had a file size threshold of 1 MB, while the default maximum file size for shadowing was set to 512 KB.
5. Investigated whether files were being skipped from scanning due to being downloaded.

## Root Cause
The root cause of the issue was identified as a mismatch between the file size threshold set in the policy (1 MB) and the default maximum file size for shadowing (512 KB). This discrepancy prevented shadows from being generated for files smaller than 1 MB. Additionally, files were not being hashed after the first send attempt, leading to them being skipped in subsequent attempts.

## Solution
The issue was resolved by adjusting the file shadowing policy to ensure that the file size threshold was compatible with the maximum file size for shadowing. This adjustment allowed the system to correctly generate shadows for files as intended.

## Notes
- Ensure that file size thresholds in policies are aligned with the maximum file size settings to avoid similar issues in the future.
- Monitor logs for any skipped files to identify potential scanning issues early on.
- Regularly review and test configurations after updates to the system to ensure continued functionality.
```