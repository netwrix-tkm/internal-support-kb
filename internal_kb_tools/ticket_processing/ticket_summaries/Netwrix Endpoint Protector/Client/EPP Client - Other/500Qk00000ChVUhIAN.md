## Ticket Metadata
- **Ticket ID:** 500Qk00000ChVUhIAN
- **Case Number:** 414178
- **Status:** Closed - Resolved
- **Account/Company:** BMW Group AG
- **Contact Name:** Anatoli Lorenz
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client - Other
- **Feature:** Minimum character setting
- **Version:** Not specified

## Problem Description
The customer reported that the minimum character setting for user remediation was configured to 10 characters on the server, but the system still required 20 characters.

## Environment Details
- The issue was observed on the Netwrix Endpoint Protector platform.
- Logs and screenshots were provided by the customer to illustrate the problem.

## Troubleshooting Steps
1. The support team acknowledged the issue and escalated it to the engineering team for further investigation.
2. The engineering team attempted to reproduce the issue in their environment but could not replicate the problem.
3. A remote session was scheduled with the customer to observe the issue directly.
4. During the session, the customer was guided to save the settings again, which had not been done previously.

## Root Cause
The issue was caused by the settings not being saved correctly after the minimum character requirement was adjusted. This led to the system still enforcing the previous requirement of 20 characters.

## Solution
The issue was resolved when the customer saved the justification settings again after the minimum character requirement was set to 10 characters. This action updated the system to reflect the correct minimum character requirement.

## Notes
- Ensure that settings are saved after making changes to configuration options to avoid similar issues in the future.
- If a customer reports discrepancies in settings, verify if the settings have been saved correctly before further troubleshooting.