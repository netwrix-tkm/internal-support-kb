## Ticket Metadata
- **Ticket ID:** 500Qk00000IyaBDIAZ
- **Case Number:** 428522
- **Status:** Closed - Resolved
- **Account/Company:** Zepko Limited
- **Contact Name:** Kasia Gawda
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Device Recognition
- **Version:** 6.2.3.1

## Problem Description
The client reported that after installing the EPP agent version 6.2.3.1 on multiple computers, the portal displayed computer names but did not show associated usernames, IP addresses, or client version numbers.

## Environment Details
- EPP Agent Version: 6.2.3.1
- Client: Multiple computers within the client's network

## Troubleshooting Steps
1. Confirmed that the EPP clients were visible in the portal and had a recent "last seen" timestamp.
2. Tested policy changes (blocking USB storage) to verify if they reflected on the client.
3. Checked if the EPP client icon blinked upon policy updates.
4. Arranged a screen share session to further investigate the issue.

## Root Cause
The issue was identified as a communication problem between the EPP clients and the server, which prevented the proper display of usernames and other client details in the portal.

## Solution
The resolution involved re-registering the clients to restore proper client-server communication. After this step, the portal began to display the usernames and other relevant information correctly. It was advised to monitor the two remaining computers for a day to see if they updated automatically. If not, further logging and potential reinstallation of the client would be necessary.

## Notes
- If issues persist with clients not updating, consider starting logs on those specific machines to identify any recurring errors.
- Reinstallation of the EPP client may be required if communication issues continue after re-registration.
- Ensure that clients are regularly monitored for updates to avoid similar issues in the future.