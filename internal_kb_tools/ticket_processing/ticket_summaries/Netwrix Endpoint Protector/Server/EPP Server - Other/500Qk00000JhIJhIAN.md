## Ticket Metadata
- **Ticket ID:** 500Qk00000JhIJhIAN
- **Case Number:** 430310
- **Status:** Closed - Resolved
- **Account/Company:** AeroDynamics
- **Contact Name:** Anahit Hayrapetyan
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** NONE

## Problem Description
The customer requested assistance in changing the server-client communication port from 443 to 5443 to free up port 443 for HTTPS traffic. Additionally, the customer reported being unable to SSH into the server, receiving an error indicating that the password was incorrect.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Reviewed the customer's request to change the server-client communication port.
2. Attempted to change the port configuration from 443 to 5443.
3. Investigated the SSH access issue, confirming the error message regarding the incorrect password.

## Root Cause
The root cause of the SSH access issue was not explicitly identified in the case. However, it is common for such issues to arise from incorrect password entry or account lockout due to multiple failed login attempts.

## Solution
The issue was resolved by applying port separation, which changed the client communication port to 8443 instead of the initially requested 5443. This allowed port 443 to be used for HTTPS as intended.

## Notes
- Ensure that any changes to port configurations are documented and communicated to all relevant stakeholders to avoid confusion.
- For SSH access issues, verify the credentials and check for account lockout policies that may affect login attempts.