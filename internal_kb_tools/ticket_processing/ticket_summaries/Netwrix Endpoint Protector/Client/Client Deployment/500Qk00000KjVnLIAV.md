## Ticket Metadata
- **Ticket ID:** 500Qk00000KjVnLIAV
- **Case Number:** 432570
- **Status:** Closed - Resolved
- **Account/Company:** University of Texas Health Science Center in Houston
- **Contact Name:** Joseph Valle
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Deployment
- **Version:** Not specified

## Problem Description
The customer reported that the EPPSetServer utility was not successfully changing the department code to a newly created code (SOD). Instead of redeploying the client, they preferred to use the utility for this change, but it failed to update the department code, leaving the client on the previous department.

## Environment Details
- **Utility Used:** EPPSetServer
- **Previous Department Code:** Not specified
- **New Department Code:** SOD

## Troubleshooting Steps
1. Confirmed the customer’s intention to use the EPPSetServer utility instead of redeploying the client.
2. Verified that the IP set utility was indeed not changing the department code.
3. Sent an older version of the EPPSetServer utility to the customer for testing.
4. Awaited feedback from the customer regarding the effectiveness of the older version.

## Root Cause
The root cause of the issue was not explicitly identified during the troubleshooting process. However, it was confirmed that the EPPSetServer utility was not functioning as expected in changing the department code.

## Solution
The issue was resolved by redeploying the agents, which successfully updated the department code to the new value (SOD). This approach was taken after the EPPSetServer utility failed to perform the desired change.

## Notes
- It is recommended to verify the functionality of the EPPSetServer utility before relying on it for critical changes.
- In cases where the utility fails, redeployment of the client agents may be necessary to ensure the correct configuration is applied.
- Future users should ensure they are using the latest version of the utility to avoid similar issues.