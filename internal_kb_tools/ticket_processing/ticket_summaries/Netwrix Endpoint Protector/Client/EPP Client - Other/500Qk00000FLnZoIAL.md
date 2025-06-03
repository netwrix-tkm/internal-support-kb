## Ticket Metadata
- **Ticket ID:** 500Qk00000FLnZoIAL
- **Case Number:** 420112
- **Status:** Closed - Resolved
- **Account/Company:** De Brauw Blackstone Westbroek
- **Contact Name:** Frans van Berkum
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** NONE

## Problem Description
The customer requested clarification on the functionality of the Netwrix Endpoint Protector client when used on two standalone laptops that would not have a network connection for an extended period (approximately six months). They needed to know if the client could operate effectively after initially connecting to the Endpoint Protector server to download policies.

## Environment Details
- Two standalone laptops
- No network connection during the project duration
- Initial connection to the Endpoint Protector server for policy retrieval

## Troubleshooting Steps
1. Reviewed the functionality of the Endpoint Protector client in offline scenarios.
2. Confirmed the client’s ability to retain and enforce policies after the initial connection.
3. Provided information regarding the expected behavior of the client when disconnected from the server.

## Root Cause
The issue stemmed from a misunderstanding of how the Endpoint Protector client operates in offline mode. The client is designed to retain and enforce the policies it downloads from the server, even when it cannot connect to the server for an extended period.

## Solution
The customer was informed that the Endpoint Protector client would function as expected even without a network connection for six months, provided it had successfully connected to the server initially to download the necessary policies. This information reassured the customer that their project could proceed without issues related to the Endpoint Protector client.

## Notes
- It is important to ensure that the Endpoint Protector client is fully configured and policies are downloaded before disconnecting from the network.
- Future users should be aware that while the client can operate offline, any updates or changes to policies will require a network connection to the Endpoint Protector server.