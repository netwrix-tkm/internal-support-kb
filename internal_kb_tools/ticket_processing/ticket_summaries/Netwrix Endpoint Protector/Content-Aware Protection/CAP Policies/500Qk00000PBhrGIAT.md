## Ticket Metadata
- **Ticket ID:** 500Qk00000PBhrGIAT
- **Case Number:** 445191
- **Status:** Closed - Resolved
- **Account/Company:** Parkar Global Technologies Private Limited
- **Contact Name:** IT Support
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** 5.9.4.1

## Problem Description
The customer requested assistance to verify their Content-Aware Protection (CAP) policy and ensure that all functionalities were operating correctly.

## Environment Details
- Initial EPP server version: 5.4.0.5
- Updated EPP server version: 5.9.4.1

## Troubleshooting Steps
1. Scheduled a remote session on 15-05 to discuss the CAP policy.
2. Conducted a remote session on 16-05 to address customer questions and check for premium version updates.
3. On 19-05, confirmed the update process for the premium version and advised the customer to take a snapshot before proceeding with updates.
4. Scheduled another remote session on 21-05 to assist with the upgrade from version 5.4.0.5.
5. Successfully updated the EPP server to version 5.9.4.1 during the session on 23-05.
6. Cleared disk usage by removing SIEM logs and updated the EPP client for one endpoint on 27-05.
7. Analyzed logs regarding URLs not being blocked and scheduled a follow-up session to investigate email alerts.

## Root Cause
The issue stemmed from the outdated EPP server version (5.4.0.5), which likely contributed to the problems with the CAP policy and URL blocking functionality.

## Solution
The issue was resolved by upgrading the EPP server from version 5.4.0.5 to 5.9.4.1 through the live update option. This upgrade addressed the functionality issues with the CAP policy.

## Notes
- Always take a snapshot of the current configuration before performing updates to prevent data loss.
- After applying updates, refresh the page to verify that the version has changed successfully.
- Future sessions may be required to address any remaining issues, such as URL blocking and email alerts.