## Ticket Metadata
- **Ticket ID:** 500Qk00000OJUCfIAP
- **Case Number:** 442728
- **Status:** Closed - Resolved
- **Account/Company:** Bright Life Care Limited
- **Contact Name:** Vikas Kataria
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Upload Not Blocked
- **Version:** NONE

## Problem Description
The customer reported that file uploads were not being blocked on the web, despite having a Content-Aware Protection (CAP) policy in place that should restrict such actions.

## Environment Details
- The customer had implemented a CAP policy to prevent files larger than 0.01 KB from being uploaded through web browsers.

## Troubleshooting Steps
1. Connected remotely with the client to investigate the issue.
2. Reviewed the configuration of the CAP policy.
3. Identified that the option "Apply Policy if File Size Threshold is Matched" was enabled.
4. Disabled the aforementioned option and tested the file upload functionality again.

## Root Cause
The issue was caused by an incorrect configuration of the CAP policy. The client had enabled the "Apply Policy if File Size Threshold is Matched" option, which required both the file size threshold and the CAP policy conditions to be met for the policy to take effect. This configuration prevented the policy from blocking all uploads as intended.

## Solution
The issue was resolved by disabling the "Apply Policy if File Size Threshold is Matched" option within the CAP policy. After making this change, the file upload restrictions worked as expected, effectively blocking uploads that exceeded the specified size limit.

## Notes
- Ensure that clients understand the implications of enabling the "Apply Policy if File Size Threshold is Matched" option, as it can lead to unexpected behavior if not configured correctly.
- Recommend reviewing all policy settings thoroughly during initial setup to avoid similar issues in the future.