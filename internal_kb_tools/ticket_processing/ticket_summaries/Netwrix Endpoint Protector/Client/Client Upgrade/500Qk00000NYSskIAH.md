## Ticket Metadata
- **Ticket ID:** 500Qk00000NYSskIAH
- **Case Number:** 440577
- **Status:** Closed - Resolved
- **Account/Company:** WIEGEL Verwaltung GmbH & Co KG
- **Contact Name:** Armin Nguyen
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** 7.1

## Problem Description
The customer requested assistance in changing the default communication port from 443 to another port for approximately 900 clients running the Netwrix Endpoint Protector agent. Previous attempts to change the port via registry modifications were unsuccessful.

## Environment Details
- The customer operates around 900 clients with the agent currently configured to communicate over port 443.
- The customer had successfully installed a new client using a different port but needed a solution for the existing clients.

## Troubleshooting Steps
1. Engaged in a remote session with the customer to perform the port separation procedure.
2. Provided the customer with the EPPSetServer tool to facilitate the port change on the client-side.
3. Instructed the customer to test the port change on 5-10 computers using the provided tool.

## Root Cause
The initial issue stemmed from the inability to change the default port through registry modifications, which did not affect the existing clients already configured to use port 443.

## Solution
During the remote session, the support engineer successfully performed the port separation procedure, allowing the clients to communicate over the new port 4433. The EPPSetServer tool was provided to the customer to change the port for the existing clients.

## Notes
- The customer was advised to test the port change on a small number of clients before proceeding with the full deployment.
- It is important to ensure that any changes to client configurations are thoroughly tested to avoid disruptions in service.
- Future requests for port changes should consider the use of the EPPSetServer tool as a standard procedure for client-side modifications.