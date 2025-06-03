## Ticket Metadata
- **Ticket ID:** 500Qk00000FfUsjIAF
- **Case Number:** 420815
- **Status:** Closed - Resolved
- **Account/Company:** CoreWin Distributor
- **Contact Name:** Danylo Didenko
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server - Other
- **Feature:** N/A
- **Version:** N/A

## Problem Description
PrivatBank reported that they had run out of licenses for the Netwrix Endpoint Protector (EPP) and had several questions regarding the implications of this situation, particularly concerning the behavior of unlicensed clients.

## Environment Details
- The customer has the Automatic License Release feature enabled.
- The EPP client on one computer was exhibiting unexpected behavior by switching from "Block and Remediate" to "Block only" actions.

## Troubleshooting Steps
1. Confirmed that the customer was experiencing a lack of available licenses.
2. Discussed the expected behavior of unlicensed computers, which should not be able to communicate with the EPP server.
3. Reviewed the implications of the Automatic License Release feature and its configuration.
4. Investigated the specific case of the EPP client that changed its policy action unexpectedly.

## Root Cause
The issue was identified as being related to the unlicensed status of the EPP client. When a computer is unlicensed, it cannot communicate with the EPP server, which leads to the cessation of policy application. The unexpected behavior of the EPP client switching to "Block only" was a direct result of the license being released.

## Solution
The issue was resolved by ensuring that the latest agents were deployed on the endpoints. This update restored proper functionality and allowed the EPP clients to operate as expected, including the correct application of policies.

## Notes
- It is crucial for customers to monitor their license usage to prevent unlicensed clients from affecting endpoint protection.
- The Automatic License Release feature should be regularly reviewed to ensure it is functioning as intended, especially in environments with fluctuating license needs.
- Future inquiries regarding unlicensed clients should consider the possibility of license release and its impact on policy enforcement.