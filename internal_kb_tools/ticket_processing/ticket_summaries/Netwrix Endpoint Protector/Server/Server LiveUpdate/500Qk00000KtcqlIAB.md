## Ticket Metadata
- **Ticket ID:** 500Qk00000KtcqlIAB
- **Case Number:** 433049
- **Status:** Closed - Resolved
- **Account/Company:** Alacriti Payments LLC
- **Contact Name:** Rahul Pandey
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server LiveUpdate
- **Version:** NONE

## Problem Description
The customer reported an error while attempting to update their server with the latest security patch (ADV-2025-001). The error message received was "An error occurred. Hash does not match."

## Environment Details
- The issue occurred on the Netwrix Endpoint Protector platform.
- The customer's environment included a firewall that was potentially affecting network traffic.

## Troubleshooting Steps
1. The customer attempted to run a live update for the security patch.
2. Support tested communication from the EPP Server's backend to identify any connectivity issues.
3. It was determined that the firewall was blocking traffic between the EPP Server and the live update server.

## Root Cause
The root cause of the issue was identified as the customer's firewall configuration, which was blocking necessary traffic for the live update process.

## Solution
The issue was resolved after the customer configured their firewall to allow the required traffic between the EPP Server and the live update server. This adjustment enabled successful communication and the completion of the update process.

## Notes
- Ensure that firewall settings are reviewed and configured to allow necessary traffic for updates in future cases.
- It may be beneficial to provide customers with guidelines on firewall configurations related to Netwrix products to prevent similar issues.