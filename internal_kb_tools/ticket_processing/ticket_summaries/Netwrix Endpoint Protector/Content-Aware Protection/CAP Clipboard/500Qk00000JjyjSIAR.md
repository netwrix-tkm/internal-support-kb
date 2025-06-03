## Ticket Metadata
- **Ticket ID:** 500Qk00000JjyjSIAR
- **Case Number:** 430429
- **Status:** Closed - Resolved
- **Account/Company:** PeopleStrong
- **Contact Name:** Rohit Nawani
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Clipboard
- **Version:** Not specified

## Problem Description
The customer reported that a policy created to restrict copy-pasting of source code on specific websites (such as online code comparison tools, code compilers, and Gmail) was not functioning as intended. This policy was designed to align with their Data Loss Prevention (DLP) settings.

## Environment Details
- The policy involved blocking MS Office file types via Anydesk as an exit point.
- The policy was applied to a specific user within the Content-Aware Protection (CAP) settings.

## Troubleshooting Steps
1. Reviewed the policy settings to ensure correct configuration.
2. Confirmed that the denylist included the appropriate MS Office file types and source codes.
3. Verified that the policy was applied to the correct user in the CAP policy.
4. Selected the computer in the CAP policy to test the functionality.

## Root Cause
The initial issue stemmed from the policy not being applied correctly to the intended user and computer. The policy only worked after explicitly selecting the computer in the CAP policy.

## Solution
The issue was resolved by ensuring that the specific computer was selected in the CAP policy. Once this was done, the policy functioned as intended, successfully blocking the copy-pasting of MS Office files via Anydesk. The customer confirmed that the policy was now working correctly and agreed to close the ticket.

## Notes
- Ensure that when creating similar policies, the correct user and computer are selected in the CAP settings to avoid functionality issues.
- It is important to verify all settings in the policy configuration to ensure they align with the intended DLP objectives.