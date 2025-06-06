## Ticket Metadata
- **Ticket ID:** 500Qk00000NNvgHIAT
- **Case Number:** 440144
- **Status:** Closed - Resolved
- **Account/Company:** BD Software Distribution Pvt Ltd
- **Contact Name:** Pravin B.
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server - Other
- **Feature:** Webmail Protection
- **Version:** NONE

## Problem Description
The customer requested assistance with two main issues regarding the Netwrix Endpoint Protector:
1. Blocking the Brave browser on endpoints.
2. Configuring email alerts for unauthorized data transfers to domains outside of an authorized list.

## Environment Details
- The customer is using Gmail and has enabled Webmail Protection within the Netwrix Endpoint Protector.

## Troubleshooting Steps
1. Provided instructions to create an application denylist to block the Brave browser:
   - Navigate to Denylists -> Applications.
   - Click on "Add" and enter the name and description.
   - In the Application & CLI Command field, input `brave.exe*`.
   - Add the content and generate the denylist.
   - Update the CAP policy to include the newly created denylist.
2. For email alerts, confirmed the need to validate Email Server Settings and establish communication between the EPP server and the mail server.
3. Advised the customer to create a Content Aware Policy (CAP) with an allowlist for authorized domains.
4. Instructed on how to set up alerts for unauthorized data transfers:
   - Go to Alerts -> Content Aware Alerts -> Create.
   - Select the event type, policy, and specify the admins to receive alerts.

## Root Cause
The customer needed guidance on how to utilize the Netwrix Endpoint Protector features effectively to block specific applications and set up alerts for unauthorized data transfers.

## Solution
The issue was resolved by providing detailed instructions for both requests:
- For blocking the Brave browser, the customer was guided through the process of creating a denylist and updating the CAP policy.
- For email alerts, the customer was instructed on configuring the Email Server Settings, creating an allowlist for authorized domains, and setting up alerts for unauthorized data transfers.

## Notes
- Ensure that the Email Server Settings are correctly configured to establish communication with the mail server.
- When creating allowlists and denylists, always test the policies on a few endpoints before rolling them out organization-wide to avoid unintended disruptions.
- Future inquiries regarding similar configurations should reference the steps provided for both application blocking and email alert setups.