## Ticket Metadata
- **Ticket ID:** 500Qk00000MXJQbIAP
- **Case Number:** 437626
- **Status:** Closed - Resolved
- **Account/Company:** Biologische Heilmittel Heel GmbH
- **Contact Name:** Dominik Ernst
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Device Recognition
- **Version:** NONE

## Problem Description
Certain computers with the Endpoint Protector Client installed were not appearing in the server appliance's computer list, despite being operational for over a week. These computers were unable to receive updates to protection policies and could not connect to the server.

## Environment Details
- The affected computers had the Endpoint Protector Client installed.
- The issue persisted even after manually triggering policy updates on the client machines.

## Troubleshooting Steps
1. Reviewed new logs for any issues; no problems were found.
2. Analyzed old logs, which indicated that a specific file from the Endpoint Protector Client was missing.
3. Determined that the missing file was likely replaced upon reinstalling the Endpoint Protector Client.

## Root Cause
The root cause of the issue was identified as a missing file from the Endpoint Protector Client installation, which prevented the affected computers from communicating with the server and receiving updates.

## Solution
The issue was resolved by instructing the customer to reinstall the Endpoint Protector Client on the affected computers. This action replaced the missing file, allowing the clients to connect to the server and receive the necessary updates.

## Notes
- Ensure that all necessary files are present in the Endpoint Protector Client installation to avoid similar connectivity issues in the future.
- Regularly check logs for missing files or errors that could indicate underlying issues with client-server communication.