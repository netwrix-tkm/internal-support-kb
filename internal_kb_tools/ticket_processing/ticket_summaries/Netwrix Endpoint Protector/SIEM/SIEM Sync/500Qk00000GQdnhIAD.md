```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000GQdnhIAD
- **Case Number:** 422421
- **Status:** Closed - Resolved
- **Account/Company:** Tecplix Technologies Private Limited
- **Contact Name:** Himanshu Vaidya
- **Product:** Netwrix Endpoint Protector
- **Component:** SIEM
- **Feature:** SIEM Sync
- **Version:** NONE

## Problem Description
The customer reported that they were unable to ingest logs from the Netwrix Endpoint Protector to their internal SIEM log forwarder. Despite configuring the necessary settings, the logs were not being captured in the SIEM console.

## Environment Details
- The SIEM solution used by the customer is Google Chronicle.
- The logs were intended to be sent from an on-premises server.

## Troubleshooting Steps
1. Verified that the SIEM logs service was running on the EPP appliance and that logs were being generated.
2. Conducted a communication test using `tcpdump` to check for traffic on the specified port (1516) but found no response.
3. Suggested the customer delete and reconfigure the SIEM settings on the EPP server.
4. Confirmed that the UDP port used for communication was open.
5. Identified that there were two SIEM servers configured with the same destination FQDN, which could cause conflicts.

## Root Cause
The issue was caused by the configuration of two identical SIEM servers pointing to the same destination FQDN, leading to conflicts in log forwarding.

## Solution
The customer removed one of the duplicate SIEM configurations from the EPP server's UI. After this adjustment, the logs began to flow correctly to the SIEM console.

## Notes
- Ensure that only one SIEM configuration is active for a given destination to avoid conflicts.
- Always verify that the necessary ports are open and that the correct protocols (UDP in this case) are being used for communication.
- Regular checks on the configuration settings can prevent similar issues in the future.
```