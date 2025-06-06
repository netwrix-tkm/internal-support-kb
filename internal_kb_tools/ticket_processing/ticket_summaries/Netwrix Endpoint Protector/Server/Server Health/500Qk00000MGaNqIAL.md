## Ticket Metadata
- **Ticket ID:** 500Qk00000MGaNqIAL
- **Case Number:** 436852
- **Status:** Closed - Resolved
- **Account/Company:** AV Squad
- **Contact Name:** Joshua Gomez-Santizo
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Health

## Problem Description
The customer reported an inability to connect to their CoSoSys hosted environment at the URL [5mydlwo.hosted.endpointprotector.com](https://5mydlwo.hosted.endpointprotector.com).

## Environment Details
- The issue was related to the hosted environment of Netwrix Endpoint Protector.
- The server did not pass health checks in AWS.

## Troubleshooting Steps
1. The support team checked the server health status in AWS.
2. It was identified that the server did not pass the necessary checks.
3. A reboot of the Endpoint Protector (EPP) server was performed.

## Root Cause
The root cause of the issue was that the EPP server failed to pass health checks in the AWS environment, which led to connectivity issues.

## Solution
The issue was resolved by rebooting the EPP server. After the reboot, the server passed all health checks, and the EPP user interface became accessible again.

## Notes
- Ensure regular monitoring of server health checks in AWS to prevent similar issues in the future.
- Consider implementing automated alerts for server health status to facilitate quicker response times.