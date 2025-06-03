## Ticket Metadata
- **Ticket ID:** 500Qk00000McqFVIAZ
- **Case Number:** 437926
- **Status:** Closed - Resolved
- **Account/Company:** JSE Investor Services (Pty) Limited
- **Contact Name:** Tumelo Molefe
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts Configuration
- **Version:** NONE

## Problem Description
The customer requested clarification on the purpose of the configured IP address 111.33.33.111 and whether it needed to be whitelisted to allow SMTP settings access for sending emails to Mimecast.

## Environment Details
- The issue involved SMTP settings and connectivity to Mimecast and Office 365 hosts.
- The customer was using Netwrix Endpoint Protector.

## Troubleshooting Steps
1. Connected remotely with the customer (Tumelo) and another engineer (Adrian) to investigate the issue.
2. Conducted a ping test to both Mimecast and Office 365 hosts.
3. Tumelo explored the Exchange site and performed tests to establish connectivity through a relay.
4. Confirmed that the IP address 111.33.33.111 is used for internal routing and should not be blocked.

## Root Cause
The IP address 111.33.33.111 is utilized for internal routing within the Netwrix Endpoint Protector system. Blocking this IP could disrupt the functionality of the EPP server and does not impact SMTP settings.

## Solution
- Informed the customer that the IP address does not need to be whitelisted and should not be blocked.
- Provided guidance on configuring SMTP settings correctly, including the use of an app password for authentication.
- Scheduled a remote session to assist with further testing and configuration adjustments.

## Notes
- Ensure that the IP address 111.33.33.111 remains unblocked to maintain the functionality of the EPP server.
- When configuring SMTP settings, verify that the settings align with the requirements for using TLS and app passwords for authentication.
- Follow up with the customer after changes to confirm successful connectivity and functionality.