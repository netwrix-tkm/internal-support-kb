## Ticket Metadata
- **Ticket ID:** 500Qk00000MVZPuIAP
- **Case Number:** 437561
- **Status:** Closed - Resolved
- **Account/Company:** DataVisor
- **Contact Name:** Ismail Reyhanoglu
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Performance
- **Version:** Not specified

## Problem Description
The customer reported that after deploying the EPP agent through a Hexnode policy, the agent installed successfully, but the user's username did not appear on the server, which was an unexpected behavior.

## Environment Details
- Deployment method: Hexnode policy
- Product involved: Netwrix Endpoint Protector

## Troubleshooting Steps
1. Verified the deployment of the EPP agent through Hexnode.
2. Checked the server for the presence of the user's computer.
3. Investigated the licensing status of the deployed agents.
4. Reviewed the Device Control settings for any anomalies.

## Root Cause
The issue was identified as a licensing problem where one computer was registered multiple times, consuming all available licenses, which prevented the new deployment from functioning correctly.

## Solution
The resolution involved deleting the duplicate computer entries from Device Control, which freed up the licenses. Once the duplicates were removed, the newly deployed device began to function as expected, and the user's username appeared on the server.

## Notes
- Ensure that devices are not registered multiple times to avoid similar licensing issues in the future.
- Regularly monitor the licensing status to prevent depletion of available licenses, which can lead to unexpected behavior in agent deployments.