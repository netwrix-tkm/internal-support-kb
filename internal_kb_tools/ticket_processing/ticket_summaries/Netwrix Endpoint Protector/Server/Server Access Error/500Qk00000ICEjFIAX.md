## Ticket Metadata
- **Ticket ID:** 500Qk00000ICEjFIAX
- **Case Number:** 426764
- **Status:** Closed - Resolved
- **Account/Company:** Mibo komunikacije d.o.o.
- **Contact Name:** Esma Tandir
- **Product:** Netwrix Endpoint Protector
- **Component:** Server Access Error
- **Feature:** Server Access Error
- **Version:** Not specified

## Problem Description
The customer reported an issue accessing a Linux server using root credentials. Due to incorrect credentials, access to the server was blocked, and the customer requested assistance in resetting the credentials and unblocking access. They also needed to verify if ports 513 and 514 were allowed for integration with a SIEM application.

## Environment Details
- **Server Type:** Linux
- **Access Method:** Root credentials
- **Ports of Interest:** 513 and 514

## Troubleshooting Steps
1. The support team acknowledged the issue and reassigned the ticket to a technician in the customer's time zone.
2. A request was sent to the DevOps team to grant access to the hosted server.
3. A remote session was scheduled to further investigate the access issue.
4. During the session, the server was restarted.

## Root Cause
The root cause of the issue was the use of incorrect root credentials, which led to the account being locked out and access being denied.

## Solution
The issue was resolved by restarting the server, which allowed the logs to start entering the SIEM server as intended. This action restored access and functionality, enabling the customer to verify the necessary ports for their integration.

## Notes
- Ensure that correct credentials are used to avoid similar access issues in the future.
- It may be beneficial to implement a process for credential recovery or reset to prevent account lockouts.
- Always verify port configurations before attempting integrations with external applications like SIEM.