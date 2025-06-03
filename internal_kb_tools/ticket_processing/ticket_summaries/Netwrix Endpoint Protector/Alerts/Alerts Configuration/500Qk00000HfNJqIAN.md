## Ticket Metadata
- **Ticket ID:** 500Qk00000HfNJqIAN
- **Case Number:** 425511
- **Status:** Closed - Resolved
- **Account/Company:** Halodata International Pte Ltd
- **Contact Name:** Denni Prima Putra Roli
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts Configuration
- **Version:** Not specified

## Problem Description
The customer reported that they had not received the email alert that was previously configured. Additionally, there was a delay in confirming the timing for a remote support call.

## Environment Details
- The issue was related to the configuration of email alerts within the Netwrix Endpoint Protector platform.

## Troubleshooting Steps
1. Followed up on the previous ticket (#424032) regarding the email alert configuration.
2. Scheduled multiple remote sessions with the customer to investigate the issue.
3. Collected necessary logs during the remote sessions for further analysis.
4. Engaged the Engineering team for additional troubleshooting steps.
5. Dropped two tables that contained old configurations during the final remote session.

## Root Cause
The issue was caused by old configurations stored in two tables within the system, which interfered with the proper functioning of the email alert system.

## Solution
The problem was resolved by dropping the two outdated tables that contained the old configurations. This action allowed the email alert system to function correctly, and the customer was advised to monitor the situation for any further issues.

## Notes
- Ensure that configurations are regularly reviewed and cleaned up to prevent similar issues in the future.
- It is advisable to document any changes made during troubleshooting for future reference.
- Always confirm with the customer after making changes to ensure that the issue has been fully resolved.