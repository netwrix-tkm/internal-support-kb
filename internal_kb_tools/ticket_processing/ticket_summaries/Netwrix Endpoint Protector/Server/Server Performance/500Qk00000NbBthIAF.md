## Ticket Metadata
- **Ticket ID:** 500Qk00000NbBthIAF
- **Case Number:** 440695
- **Status:** Closed - Resolved
- **Account/Company:** NHS South, Central and West Commissioning Support Unit
- **Contact Name:** Pete Taylor
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Performance
- **Version:** Not specified

## Problem Description
Following a migration to a new server, one of the servers was experiencing approximately 70% CPU usage throughout the working day, significantly higher than other servers which maintained around 30% CPU usage. Additionally, the SIEM (Logpoint) was not receiving logs from any server after the migration.

## Environment Details
- The affected server was migrated from an older server that used `rsyslog` to a new server that uses `syslog-ng`.
- The SIEM integration details were confirmed to be correct, but logs were not being forwarded.

## Troubleshooting Steps
1. Confirmed the CPU usage issue and compared it with other servers.
2. Checked the SIEM settings to ensure they were correctly migrated.
3. Ran a `tcpdump` from the Logpoint SIEM to verify if logs were being sent from the affected server.
4. Scheduled a remote session to investigate the issue further.

## Root Cause
The issue was identified as being caused by `syslog-ng` not being enabled on the new servers. The previous server was using `rsyslog`, which was not configured on the new server.

## Solution
During the remote session, `syslog-ng` was enabled on the new servers. After this configuration change, logs began to be successfully sent to the SIEM.

## Notes
- Ensure that the logging service (either `rsyslog` or `syslog-ng`) is properly configured and enabled on new servers during migration to avoid similar issues.
- Monitor CPU usage after migrations to identify any discrepancies early on.