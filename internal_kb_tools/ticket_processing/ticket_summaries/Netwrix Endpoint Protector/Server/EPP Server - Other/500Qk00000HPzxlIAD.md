## Ticket Metadata
- **Ticket ID:** 500Qk00000HPzxlIAD
- **Case Number:** 424911
- **Status:** Closed - Resolved
- **Account/Company:** Satcom Infotech
- **Contact Name:** Rajesh Kumar
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server - Other
- **Feature:** Endpoint Protector Agent
- **Version:** Not specified

## Problem Description
The customer reported that after installing the Endpoint Protector agent via the JAMF tool on a Mac device, the server was not communicating with the agent.

## Environment Details
- **Deployment Tool:** JAMF
- **Device Type:** Mac
- **Additional MDM Solution:** ScaleFusion for Windows devices

## Troubleshooting Steps
1. The customer initially installed the agent using the JAMF tool but faced communication issues with the server.
2. A meeting was held with the customer to discuss the issue.
3. The deployment script was updated and tested on several laptops, which resolved the communication issue for those devices.
4. The customer attempted to deploy the agent through ScaleFusion for Windows devices but encountered similar communication issues.
5. The support team provided documentation for deploying the Windows agent via MDM.

## Root Cause
The initial communication issue was due to the configuration of the agent deployment script used with JAMF. After updating the script, the agent was able to communicate with the server successfully.

## Solution
The issue was resolved when the customer received trial extension licenses. They disabled and then re-enabled the Data Protection Integration (DPI) for Slack, which allowed the agent to function correctly. The customer confirmed that the agent was now communicating with the server, and the ticket was closed.

## Notes
- Ensure that the correct deployment scripts are used for both JAMF and ScaleFusion to avoid similar issues in the future.
- If users experience slow performance or communication issues with applications like Slack after agent installation, check the Content Aware policy settings and consider unchecking specific applications as a temporary workaround.
- Always verify that trial licenses are active before troubleshooting to avoid delays in support.