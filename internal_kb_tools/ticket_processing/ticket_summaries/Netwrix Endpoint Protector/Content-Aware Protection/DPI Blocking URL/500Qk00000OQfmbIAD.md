## Ticket Metadata
- **Ticket ID:** 500Qk00000OQfmbIAD
- **Case Number:** 443159
- **Status:** Closed - Resolved
- **Account/Company:** Black Sesame Technologies
- **Contact Name:** Tai Ting Tseng
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** DPI Blocking URL

## Problem Description
The customer inquired about the possibility of using DPI Blocking URL to selectively block Microsoft Teams activities for personal accounts while allowing uploads to company accounts, similar to their existing configuration for Microsoft OneDrive.

## Environment Details
- **Date of Initial Inquiry:** April 24, 2025
- **Date of Case Closure:** May 21, 2025

## Troubleshooting Steps
1. Customer requested clarification on blocking uploads to personal Microsoft Teams accounts.
2. Technical support explored the possibility of differentiating between personal and business accounts for uploads.
3. A test was conducted to determine if DPI URL blocking could prevent OneDrive attachments from being uploaded through Teams.
4. Follow-up communications were sent to the customer to confirm findings and clarify limitations.

## Root Cause
It was determined that there is currently no method to selectively apply DPI blocking URL to differentiate between personal and business Microsoft Teams accounts. The system does not support this level of granularity in blocking.

## Solution
The issue was resolved by confirming to the customer that it is not possible to block uploads selectively to personal Microsoft Teams accounts while allowing uploads from business accounts. The testing confirmed that applying DPI URL blocking to OneDrive would block all attachments in Teams, including those from OneDrive.

## Notes
- **Limitations:** The DPI Blocking URL feature does not allow for selective blocking based on account type (personal vs. business) for Microsoft Teams.
- **Future Considerations:** Customers should be informed that any attempts to block uploads selectively may result in broader restrictions than intended, affecting all users regardless of account type.