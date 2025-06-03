## Ticket Metadata
- **Ticket ID:** 500Qk00000CYomfIAD
- **Case Number:** 413714
- **Status:** Closed - Resolved
- **Account/Company:** REIF Bauunternehmung GmbH & Co. KG
- **Contact Name:** Jonas Stöpfel
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device not recognized
- **Version:** Not specified

## Problem Description
The customer reported that after an update on June 28, 2024, the update notification continued to appear as available, and no data logging was occurring. This was critical as they receive a large volume of data daily, including from USB devices, which were not being logged despite the client being online.

## Environment Details
- The issue occurred on the Netwrix Endpoint Protector platform.
- The customer was using a client that was confirmed to be online and available in the Endpoint Protector (EPP).

## Troubleshooting Steps
1. Acknowledged the issue and confirmed that the update would still appear as available even after being applied.
2. Investigated the data logging issue with the engineering team.
3. Scheduled a Zoom session to perform backend procedures on the server.
4. Requested the customer to have PuTTY installed for SSH access to the server.
5. Conducted a remote session to implement the necessary backend procedures.

## Root Cause
The root cause of the issue was identified as a backend configuration problem that arose after the update was applied. This misconfiguration prevented the system from recognizing devices and logging data correctly.

## Solution
The issue was resolved by performing a backend procedure on the server, which involved:
- Accessing the server via SSH using PuTTY.
- Correcting the configuration settings that were preventing data logging.
- After the adjustments were made, the customer was advised to monitor the data logs for a few days to ensure the issue was fully resolved.

## Notes
- The customer confirmed that data logging resumed successfully after the backend adjustments.
- It is recommended to monitor system performance and ensure that the server meets the minimum requirements for RAM and CPU to prevent similar issues in the future. The minimum specifications provided were 4 CPUs and 6 GB of RAM.