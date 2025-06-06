## Ticket Metadata
- **Ticket ID:** 500Qk00000ELIjTIAX
- **Case Number:** 417885
- **Status:** Closed - Resolved
- **Account/Company:** Westpac Banking Corporation
- **Contact Name:** Mark Chambers
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Resource Audit
- **Version:** 11.5

## Problem Description
The customer requested guidance on how to change the view in the Resource Audit feature to display the DomainSAMAccountName instead of the user name. This was necessary due to the presence of multiple accounts with the same user name in their organization, making the unique SAMAccountName more useful for identification.

## Environment Details
- **Product Version:** 11.5
- **Build Number:** 11.5.0.103

## Troubleshooting Steps
1. Reviewed the customer's request regarding the display of user names in the Resource Audit feature.
2. Confirmed the current functionality of the Activity Statistics and Activity Details views.
3. Provided guidance on how to modify the view settings to include the desired information.

## Root Cause
The issue stemmed from the default configuration of the Resource Audit feature, which displayed user names instead of the unique DomainSAMAccountName. This was not a technical fault but rather a limitation in the view settings.

## Solution
To resolve the issue, the customer was guided to add the `TrusteeAccount` column to the view in the Resource Audit feature. This adjustment allowed the display of the DomainSAMAccountName, meeting the customer's requirements for unique identification of accounts.

## Notes
- Ensure that users are aware of the ability to customize views in the Resource Audit feature to better suit their organizational needs.
- It may be beneficial to document similar requests for future reference, as organizations with large user bases may frequently encounter issues with duplicate user names.