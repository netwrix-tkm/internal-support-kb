```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CqgaXIAR
- **Case Number:** 414526
- **Status:** Closed - Resolved
- **Account/Company:** Saab Defense and Security USA LLC
- **Contact Name:** Zachary Springman
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The EPP Clients stopped sending logs to the EPP Server after the installation of the latest hotfix on June 27th, 2024. The last logs received were on the same day as the update.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Confirmed that the latest hotfix was installed on June 27th.
2. Checked for any new hotfix releases that might address the logging issue.
3. Scheduled a remote session to apply the hotfix if it was not installed.
4. Communicated with the customer to determine their availability for troubleshooting.

## Root Cause
The issue was caused by the installation of the hotfix, which led to a failure in communication between the EPP Clients and the EPP Server, preventing log transmission.

## Solution
The issue was resolved by applying a new hotfix that was released after the initial installation. A remote session was scheduled to ensure the hotfix was correctly applied, which restored communication between the EPP Clients and the EPP Server.

## Notes
- Ensure that all hotfixes are installed as soon as they are released to avoid similar issues.
- Monitor the communication between EPP Clients and the EPP Server after applying updates to catch any issues early.
- Maintain clear communication with clients regarding their availability for troubleshooting sessions.
```