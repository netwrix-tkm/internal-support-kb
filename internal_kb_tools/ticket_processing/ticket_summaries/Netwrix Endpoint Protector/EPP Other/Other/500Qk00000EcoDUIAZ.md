## Ticket Metadata
- **Ticket ID:** 500Qk00000EcoDUIAZ
- **Case Number:** 418457
- **Status:** Closed - Resolved
- **Account/Company:** Liverpool University Hospitals NHS Foundation Trust
- **Contact Name:** Ray Soong
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** 5940

## Problem Description
The customer, Liverpool University Hospitals NHS Foundation Trust, reported low disk space on their EPP appliance and requested assistance to increase the available disk space.

## Environment Details
- **Server ID:** S55FZ1HL
- **Number of Device Control licenses:** 11,000
- **Deployment:** On-premise (virtual appliance)

## Troubleshooting Steps
1. Scheduled a remote session with the customer.
2. Cleared the `php-fpm` logs to free up disk space.
3. Cleared the journal logs to further reduce disk usage.

## Root Cause
The low disk space issue was primarily caused by the accumulation of `php-fpm` and journal logs, which were not being managed effectively, leading to excessive disk usage.

## Solution
The issue was resolved during a remote session by clearing the `php-fpm` logs and the journal logs, which successfully increased the available disk space on the EPP appliance.

## Notes
- It is recommended to implement regular log management practices to prevent similar issues in the future.
- Monitor disk space usage periodically to ensure that log files do not accumulate excessively.