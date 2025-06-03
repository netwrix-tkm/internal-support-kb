## Ticket Metadata
- **Ticket ID:** 500Qk00000PfKnaIAF
- **Case Number:** 446390
- **Status:** Closed - Resolved
- **Account/Company:** QBurst
- **Contact Name:** Sabeesh Thomas
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Allowlist / Denylist
- **Version:** 6.2

## Problem Description
The customer requested assistance in configuring their system to allow specific emails for upload while blocking others. Additionally, they wanted to create custom alerts for these actions.

## Environment Details
The customer was using Netwrix Endpoint Protector with a focus on Gmail for business accounts.

## Troubleshooting Steps
1. Connected remotely with the customer, Sabeesh, to discuss the requirements.
2. Advised on using the CAP (Content-Aware Protection) -> DPI (Deep Packet Inspection) settings to configure allowed business accounts.
3. Added the customer's business domain to the "Allowed business accounts" list.
4. Conducted tests on a machine to verify that access to non-business domains was blocked successfully.

## Root Cause
The issue stemmed from the lack of proper configuration in the Content-Aware Protection settings, which did not initially restrict access to non-business email domains.

## Solution
The issue was resolved by:
- Adding the customer's business domain to the CAP -> DPI -> Allowed business accounts settings.
- Testing the configuration confirmed that personal email domains (e.g., gmail.com) were blocked as intended.

## Notes
- Ensure that the allowed business accounts are regularly reviewed and updated to maintain compliance with company policies.
- Custom alerts can be configured in conjunction with the allowlist/denylist settings for better monitoring of email uploads.