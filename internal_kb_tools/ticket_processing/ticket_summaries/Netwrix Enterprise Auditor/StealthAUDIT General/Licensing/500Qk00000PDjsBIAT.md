## Ticket Metadata
- **Ticket ID:** 500Qk00000PDjsBIAT
- **Case Number:** 445327
- **Status:** Closed - Resolved
- **Account/Company:** Point32Health Services, Inc.
- **Contact Name:** Peter Sterianos
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Licensing
- **Version:** 11.6

## Problem Description
The customer reported that the AIC (Activity Information Center) was displaying Security Identifiers (SIDs) instead of user names for Activity Events. This change in display behavior was unexpected and caused confusion for the user.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Product Version:** 11.6

## Troubleshooting Steps
1. The customer logged into the AIC.
2. Navigated to Resource Audit.
3. Expanded the SharePoint section.
4. Checked the Activity Details for user information.
5. The support technician explained that an Azure license is required to retrieve detailed user login information.

## Root Cause
The issue was identified as a licensing problem. The customer did not possess an Azure license, which is necessary for the application to collect and display detailed user information from the Azure domain.

## Solution
The resolution involved informing the customer that they needed to obtain an Azure license to access the required user details. Once the customer understood this requirement, the case was marked as resolved.

## Notes
- It is important for users to have the appropriate licenses for Azure to ensure full functionality of the AIC in displaying user information.
- Future support cases should verify licensing status when similar issues arise regarding user identification in the AIC.