## Ticket Metadata
- **Ticket ID:** 500Qk00000PCbBtIAL
- **Case Number:** 445265
- **Status:** Closed - Resolved
- **Account/Company:** AXAXL
- **Contact Name:** Neil Patterson
- **Product:** PingCastle
- **Component:** PC Standard
- **Feature:** PingCastle General
- **Version:** 3.3

## Problem Description
The customer inquired about connecting to Azure/Entra using App Registrations with PingCastle, following a previous ticket regarding the same issue. They requested documentation on the connection process and the necessary API permissions for the App Registration, as well as the roles required for manual user connections to fully scan Azure/Entra.

## Environment Details
- **Product Version:** 3.3.0.11
- **Platform:** PingCastle

## Troubleshooting Steps
1. Reviewed the customer's previous ticket regarding Azure connectivity.
2. Confirmed the update to the Graph API and its implications for App Registrations.
3. Provided information on the current limitations of scheduling scans using App Registrations.
4. Informed the customer about the ongoing migration to the Graph API scheduled for a future release.

## Root Cause
The inability to configure a scheduled scan of Azure using an App Registration was due to the current reliance on the old Azure Graph API (graph.windows.net). Although the necessary switches for configuration were present, the complete migration to the new Graph API had not yet been finalized.

## Solution
The customer was informed that while the configuration for scheduled scans using App Registrations is not possible at this time, it is expected to be feasible once the migration to the Graph API is completed in a future release. The customer was advised to monitor updates regarding this migration for future capabilities.

## Notes
- The customer should be aware that the current limitations are due to the ongoing transition to the Graph API.
- It is recommended to keep an eye on future releases for updates on the ability to schedule scans using App Registrations.
- Documentation regarding API permissions and roles for manual connections should be provided once the migration is complete.