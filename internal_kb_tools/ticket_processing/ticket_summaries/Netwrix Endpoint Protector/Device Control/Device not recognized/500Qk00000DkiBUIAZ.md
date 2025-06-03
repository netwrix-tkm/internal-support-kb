## Ticket Metadata
- **Ticket ID:** 500Qk00000DkiBUIAZ
- **Case Number:** 416515
- **Status:** Closed - Resolved
- **Account/Company:** Dubai Police
- **Contact Name:** Aiman Jadiba
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device not recognized
- **Version:** 5930

## Problem Description
The customer, Dubai Police, reported multiple issues regarding their use of the Netwrix Endpoint Protector (EPP). They requested to be added to email notifications for application updates and faced challenges with agent deployments, where only 500 out of 1500 deployed agents were visible in the WebUI despite successful communication with the EPP server.

## Environment Details
- **Deployment Method:** SCCM (System Center Configuration Manager)
- **Communication Port:** 443 (HTTPS)

## Troubleshooting Steps
1. Confirmed the customer’s request to be added to email notifications for EPP updates.
2. Verified that the agents were successfully pushed to 1500 devices via SCCM.
3. Checked the communication status of several devices to ensure they could connect to the EPP server on port 443.
4. Investigated the WebUI to determine why only 500 devices were displayed in the inventory.

## Root Cause
The issue with the agent visibility in the WebUI was identified as a limitation in the EPP system's ability to display all connected devices simultaneously. This was not due to a failure in agent deployment or communication but rather a restriction in the inventory display functionality.

## Solution
The resolution involved confirming the successful deployment of agents and ensuring that the customer was added to the email notification list for updates. Additionally, it was communicated to the customer that the limitation in the WebUI was a known issue, and they were advised to monitor the situation for future updates that may address this limitation.

## Notes
- It is important to keep customers informed about known limitations in the product to manage expectations.
- Ensure that customers are added to notification lists promptly to maintain communication regarding updates and changes.
- Future updates to the EPP may improve the visibility of deployed agents in the WebUI, so ongoing monitoring of product releases is recommended.