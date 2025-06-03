## Ticket Metadata
- **Ticket ID:** 500Qk00000DkTvcIAF
- **Case Number:** 416499
- **Status:** Closed - Resolved
- **Account/Company:** Airpak
- **Contact Name:** Stefania Oltean
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** 6.1

## Problem Description
The user reported that the User remediation pop-up notification does not appear as expected. The notification only shows when the Netwrix Endpoint Protector (NEP) client is opened in the Content-Aware Protection (CAP) section, preventing users from seeing the pop-up for self-remediation actions.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Feature in Use:** CAP Policies

## Troubleshooting Steps
1. Verified the configuration settings for user notifications within the NEP client.
2. Checked user permissions and rights associated with the remediation actions.
3. Reviewed logs for any errors or warnings related to the notification system.
4. Confirmed that the NEP client was updated to the latest version (6.1).

## Root Cause
The issue was identified as a misconfiguration of user rights, specifically that the rights were not set with priority for the user, which prevented the pop-up notification from displaying.

## Solution
The problem was resolved by adjusting the user rights settings to ensure that they were prioritized correctly. This allowed the User remediation pop-up notification to display as intended when users attempted self-remediation actions.

## Notes
- Ensure that user rights are properly configured and prioritized in future cases to avoid similar issues.
- Regularly review and update user permissions as part of routine maintenance to ensure all features function correctly.