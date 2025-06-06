## Ticket Metadata
- **Ticket ID:** 500Qk00000IabxyIAB
- **Case Number:** 427747
- **Status:** Closed - Resolved
- **Account/Company:** W. L. Gore & Associates, Inc.
- **Contact Name:** Connie Liang
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Credentials
- **Version:** 11.6

## Problem Description
The customer reported that after upgrading to version 11.6 of the Netwrix Access Information Center (AIC), users were required to specify their domain prefix (e.g., US.East) when logging in. Previously, in version 11.5, the USE domain was set as the default, allowing users to log in without the domain prefix. The customer sought a way to revert to the previous behavior.

## Environment Details
- Multiple domains configured in the environment.
- Previous version: Netwrix Access Information Center 11.5.
- Current version: Netwrix Access Information Center 11.6.0.25.

## Troubleshooting Steps
1. Confirmed the version of Netwrix Access Information Center and Enterprise Auditor installed.
2. Reviewed the Active Directory configuration settings to check for domain access permissions.
3. Explored the possibility of changing the Active Directory account settings to eliminate the need for the domain prefix.
4. Communicated with R&D to understand the changes in the new web server configuration compared to the previous IIS setup.

## Root Cause
The requirement for users to include their domain prefix during login was due to a change in the underlying web server technology from IIS to a new web server in version 11.6. This change removed the assumption of a default domain, which was previously handled by IIS.

## Solution
The issue was resolved by informing the customer that the new version requires the domain prefix for login. While this change may cause initial inconvenience for users accustomed to the previous behavior, it ultimately provides a more consistent login experience across all domains. The customer was advised to communicate this change to their users.

## Notes
- Users will need to adjust to the new login requirement by including their domain prefix.
- The change is intended to enhance security and uniformity across multiple domains.
- The ticket can be reopened within 30 days if any related issues arise.