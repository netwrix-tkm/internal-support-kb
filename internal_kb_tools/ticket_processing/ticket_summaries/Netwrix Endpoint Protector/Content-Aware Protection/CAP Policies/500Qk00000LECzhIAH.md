## Ticket Metadata
- **Ticket ID:** 500Qk00000LECzhIAH
- **Case Number:** 434031
- **Status:** Closed - Resolved
- **Account/Company:** Jopari
- **Contact Name:** Lance Bouchard
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** 6.2.3.10

## Problem Description
The customer reported an issue where they were unable to find the option to enter a One-Time Password (OTP) for allowing file transfers under Content Aware Protection. Previously, there was a tab in the client for this feature, but it was missing in the current version.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Client Version:** 6.2.3.10

## Troubleshooting Steps
1. Confirmed the absence of the OTP entry option in the Content Aware Protection tab.
2. Investigated potential bugs related to the issue, specifically referencing bug 5941.
3. Determined that a client patch was necessary to resolve the issue.

## Root Cause
The issue was identified as being caused by a bug introduced in the software version related to bug 5941, which affected the functionality of the Content Aware Protection feature.

## Solution
An offline patch containing the fixed agents was sent to the customer. The patch addressed the missing OTP entry option, allowing the customer to utilize the Content Aware Protection feature as intended.

## Notes
- It is important to monitor for similar issues in future versions and ensure that patches are applied promptly to avoid disruptions in functionality.
- Customers should be informed about the existence of patches for known bugs and encouraged to apply them as necessary.