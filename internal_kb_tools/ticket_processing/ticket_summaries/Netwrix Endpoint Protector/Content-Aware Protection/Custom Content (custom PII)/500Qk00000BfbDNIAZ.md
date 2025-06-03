## Ticket Metadata
- **Ticket ID:** 500Qk00000BfbDNIAZ
- **Case Number:** 411529
- **Status:** Closed - Resolved
- **Account/Company:** Outcomes Matter Innovations
- **Contact Name:** George Chiligiris
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Custom Content (custom PII)
- **Version:** 5.9.2 (server), 6.2.1.2 (client)

## Problem Description
A user was experiencing issues sending emails to two team members within the same domain (@omimanagement.com). Emails sent to one member were successful, while those sent to the other two were being blocked. The customer sought assistance to identify the cause of the blockage and to prevent it from recurring.

## Environment Details
- The organization uses Microsoft Exchange as their email server.
- The current version of the Endpoint Protector server was 5.9.2, and the client version was updated to 6.2.1.2.

## Troubleshooting Steps
1. Confirmed that the email domain (@omimanagement.com) was whitelisted in the Endpoint Protector settings.
2. Advised the customer to add "Exchange Administrative Group" to the email domain allowlist.
3. Ensured that the allowlist was included in a Content-Aware Policy (CAP) targeting the client machines.
4. Verified that the "Deep Packet Inspection" (DPI) setting was enabled from the Device Control > Global settings page.
5. Suggested refreshing the policies from the client machine side after making changes.
6. Scheduled a remote session to assist with configuration if issues persisted.

## Root Cause
The issue was caused by the Endpoint Protector's configuration, specifically the lack of proper whitelisting for the Exchange domain. The system required the entire Exchange Administrative Group to be whitelisted rather than individual email addresses.

## Solution
The issue was resolved by:
- Adding "Exchange Administrative Group" to the email domain allowlist in the Endpoint Protector settings.
- Ensuring that the allowlist was included in the relevant Content-Aware Policy.
- Confirming that the Deep Packet Inspection feature was enabled.

After these changes were made, the user was able to send emails to all team members within the organization without any blocks.

## Notes
- New Outlook is currently not supported by the Endpoint Protector, and users should be advised to use the older version of Outlook.
- Ensure that all licenses are valid and in use, as the customer had issues with licenses being fully utilized.
- Regularly check for updates to the Endpoint Protector server and client versions to mitigate vulnerabilities and improve functionality.