## Ticket Metadata
- **Ticket ID:** 500Qk00000OGTUrIAP
- **Case Number:** 442577
- **Status:** Closed - Resolved
- **Account/Company:** Renewbuy
- **Contact Name:** Anil Kumar
- **Product:** Netwrix Endpoint Protector
- **Component:** SIEM
- **Feature:** SIEM Sync
- **Version:** NONE

## Problem Description
The customer requested assistance in integrating their Endpoint Protector (EPP) Data Loss Prevention (DLP) solution with IBM QRadar SIEM. They needed guidance on how to transfer logs from the EPP server to the QRadar log collector server.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Build Number:** 5941

## Troubleshooting Steps
1. The support team provided instructions on how to configure the SIEM integration under the Appliance > SIEM menu.
2. A remote session was scheduled to demonstrate the log transfer process.
3. Clarified with the customer whether QRadar was performing a pull from the EPP server, which is not supported.
4. Discussed the configuration settings required for the SIEM integration, including server IP, protocol, and log types.

## Root Cause
The issue was not with the EPP server itself but rather with the configuration settings on the QRadar side. The EPP server was successfully sending logs, but the customer's QRadar configuration needed adjustments to properly receive and process those logs.

## Solution
During the remote session, it was demonstrated that the logs were being sent from the EPP server to QRadar. The customer was advised to reconfigure their QRadar settings to ensure proper log reception. The ticket was confirmed as resolved after the demonstration.

## Notes
- The customer was cautioned that a maximum of four SIEM server integrations can be configured.
- If logging is disabled, logs will be stored on the EPP server or the SIEM server, depending on the configuration.
- Future users should ensure that QRadar is set to receive logs via a push mechanism from the EPP server, as pull mechanisms are not supported.