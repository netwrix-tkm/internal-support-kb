## Ticket Metadata
- **Ticket ID:** 500Qk00000NAljZIAT
- **Case Number:** 439583
- **Status:** Closed - Resolved
- **Account/Company:** EMSLAND-STÄRKE GMBH
- **Contact Name:** Eike Arends
- **Product:** Netwrix Endpoint Protector
- **Component:** Offline Temporary Password (OTP)
- **Feature:** Offline Temporary Password (OTP)
- **Version:** Server Version 5.9.4.1, Client Version 6.2.4.1006

## Problem Description
The customer reported that since the last update, the Offline Temporary Password (OTP) function was not working properly. Although OTPs could be created, they often returned an error stating that the OTP was incorrect when attempting to redeem them. This issue was intermittent, with some OTPs working while most did not.

## Environment Details
- **Server Version:** 5.9.4.1
- **Client Version:** 6.2.4.1006
- The OTP was generated for devices, and the correct device was selected in the EPP Client on the endpoint.

## Troubleshooting Steps
1. Confirmed the server and client versions being used.
2. Verified that the OTP was generated for the correct device and that the device was selected in the EPP Client.
3. Suggested updating the client to version 6.2.4.2 and importing an offline patch.
4. Advised checking the server time settings to ensure they were correct.

## Root Cause
The issue was identified as a compatibility problem between the server and client versions, which was affecting the proper application of OTPs in the EPP client.

## Solution
The issue was resolved by:
1. Importing the offline patch provided by Netwrix.
2. Updating the EPP client to version 6.2.4.2.
3. Confirming that the server time settings were correct.

After these steps, the OTP functionality was restored, and the customer confirmed that the issue was resolved.

## Notes
- Ensure that both the server and client versions are compatible to avoid similar issues in the future.
- Always verify that the correct device is selected in the EPP client when generating OTPs.
- Monitor for any further updates or patches that may affect OTP functionality.