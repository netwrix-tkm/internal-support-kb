## Ticket Metadata
- **Ticket ID:** 500Qk00000OmuTaIAJ
- **Case Number:** 444002
- **Status:** Closed - Resolved
- **Account/Company:** OPL Innovate
- **Contact Name:** Paresh Patel
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 5.9.4.2

## Problem Description
The customer was unable to access their Endpoint Protector (EPP) server instance via SSH using root credentials, which was necessary for checking SIEM integration issues.

## Environment Details
- The issue was related to the SSH access of the Endpoint Protector server.
- The customer was experiencing problems with SIEM integration, specifically that no logs were being received.

## Troubleshooting Steps
1. Initial remote connection with the customer to understand the issue.
2. Provided instructions from the Netwrix help center regarding SSH access.
3. Followed up with a second remote session to investigate the SIEM integration.
4. Checked the `siem_rsyslog_update` setting via SSH to confirm it was set to 1.
5. Attempted to reconnect the EPP server to the SIEM and monitored the syslog using `tail -f syslog`.

## Root Cause
The root cause of the issue was identified as an incorrect configuration related to the SIEM integration, which prevented logs from being received.

## Solution
The issue was resolved by:
- Verifying the `siem_rsyslog_update` setting was correctly configured.
- Successfully reconnecting the EPP server to the SIEM, which allowed logs to be received and confirmed that the system was functioning as expected.

## Notes
- Ensure that the root credentials are correctly set and accessible for future troubleshooting.
- For similar cases, verify SIEM integration settings and configurations as a first step.
- Always refer to the official Netwrix documentation for guidance on configuration and troubleshooting.