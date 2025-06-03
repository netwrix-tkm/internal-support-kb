## Ticket Metadata
- **Ticket ID:** 500Qk00000FJGrgIAH
- **Case Number:** 419969
- **Status:** Closed - Resolved
- **Account/Company:** CoreWin Distributor
- **Contact Name:** Danylo Didenko
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Upload Not Blocked
- **Version:** 5.9.4.1 (fix included in this version)

## Problem Description
PrivatBank reported instability with the file upload block feature in Web MS Teams. They observed that while some files were successfully blocked on a DLP-test website, they were not blocked in MS Teams, leading to inconsistent behavior of the Content-Aware Protection (CAP) policy.

## Environment Details
- **Customer:** PrivatBank
- **Testing Environment:** DLP-test website and Web MS Teams
- **CAP Policy:** Restrict Content Detection option was enabled during testing.

## Troubleshooting Steps
1. Customer reported the issue and provided logs, screenshots, and a video demonstrating the problem.
2. Initial tests were conducted to replicate the issue, focusing on the CAP policy settings.
3. The "Restrict Content Detection" option was toggled, revealing that disabling it improved file blocking behavior.
4. A test build was created and shared with the customer for further testing.

## Root Cause
The issue was linked to the "Restrict Content Detection" option within the CAP policy. When this option was enabled, it caused inconsistent blocking behavior for file uploads to MS Teams, while it worked correctly for other platforms.

## Solution
A test build was developed that addressed the instability issue. The fix was confirmed to be included in version 5.9.4.1 of the Netwrix Endpoint Protector. The customer was advised to install this version to resolve the issue.

## Notes
- Ensure that the "Restrict Content Detection" option is tested thoroughly in future cases, as it may lead to similar issues.
- Always verify the version of the software being used and recommend updates when issues arise.
- Document any customer feedback after implementing fixes to ensure the solution is effective.