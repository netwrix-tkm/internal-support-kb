## Ticket Metadata
- **Ticket ID:** 500Qk00000LoUJmIAN
- **Case Number:** 435669
- **Status:** Closed - Resolved
- **Account/Company:** Amount
- **Contact Name:** Don Stewart
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Deployment
- **Version:** Not specified

## Problem Description
The Amount team requested the EPP change script necessary for deploying the EPP.pkg from a Mobile Device Management (MDM) system. They were experiencing issues with endpoints not receiving the deployment, which was suspected to be related to license limits.

## Environment Details
- The customer was using an on-premises console for the Netwrix Endpoint Protector.
- The deployment was being managed through MDM tools, specifically JAMF and Intune.

## Troubleshooting Steps
1. Confirmed the license count was increased to accommodate additional devices.
2. Investigated whether the endpoints were correctly configured to communicate with the EPP server.
3. Provided documentation for JAMF and Intune MDM deployment tools.
4. Suggested enabling automatic license release for computers that had not communicated with the server for a specified time.
5. Scheduled a remote session to further investigate the issue with the customer.

## Root Cause
The primary issue was identified as a possible license limit being reached, which prevented some endpoints from receiving the deployment. After increasing the license count, additional troubleshooting was required to ensure proper communication between the endpoints and the EPP server.

## Solution
The issue was resolved by:
- Increasing the license count to allow for additional devices.
- Conducting a remote session where it was confirmed that the EPP clients were now online, licensed, and communicating with the server successfully.

## Notes
- Ensure that the license count is monitored regularly to prevent similar issues in the future.
- It is advisable to enable automatic license release to manage licenses effectively, especially in environments with fluctuating device counts.
- Always verify that the correct IP address is configured in the EPP Client settings for proper server communication.