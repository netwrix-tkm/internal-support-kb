## Ticket Metadata
- **Ticket ID:** 500Qk00000HKCUfIAP
- **Case Number:** 424636
- **Status:** Closed - Resolved
- **Account/Company:** ING companies
- **Contact Name:** Sudipa Bera
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** NONE

## Problem Description
Two users reported that their print attempts were being blocked by the Content-Aware Protection (CAP) policy without receiving any notifications regarding the block.

## Environment Details
- **Users Affected:** WPO1L5CG2193W4G and WPO1L5CG2193W4C
- **Platform:** Netwrix Endpoint Protector

## Troubleshooting Steps
1. Verified the CAP policy settings to ensure notifications were enabled.
2. Checked the logs for any entries related to the print attempts of the affected users.
3. Conducted a test print attempt under the same conditions to replicate the issue.
4. Reviewed user permissions and roles to ensure they were correctly configured.
5. Engaged in a short call with the users to gather more context about their print attempts.

## Root Cause
The issue was identified as a misconfiguration in the CAP policy settings, which inadvertently suppressed notifications for blocked print attempts.

## Solution
The CAP policy was reconfigured to ensure that notifications are sent to users when their print attempts are blocked. After making the necessary adjustments, the users were able to receive notifications as expected during subsequent print attempts.

## Notes
- Ensure that CAP policy settings are regularly reviewed to prevent similar issues in the future.
- It is advisable to communicate any changes in policy settings to users to keep them informed about potential impacts on their activities.