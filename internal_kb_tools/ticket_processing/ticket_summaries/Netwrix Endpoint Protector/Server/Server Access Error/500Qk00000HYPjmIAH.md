```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000HYPjmIAH
- **Case Number:** 425219
- **Status:** Closed - Resolved
- **Account/Company:** Senedd
- **Contact Name:** Dezso Fater
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** NONE

## Problem Description
The customer reported that network packets from EPP clients to the EPP server were being dropped, particularly when the TCP traffic load was high. While clients could access other server resources, they faced issues connecting to the EPP server, which worked fine from on-premise servers.

## Environment Details
- The EPP clients send traffic to the EPP server via Zscaler servers, which aggregate connections from multiple clients, making them appear to originate from only two IP addresses.
- The customer operates under a zero trust security model, which may have contributed to the packet loss.

## Troubleshooting Steps
1. Collected logs from affected endpoint machines during the occurrence of the issue.
2. Analyzed the flow of TCP traffic between EPP clients and the EPP server.
3. Enabled debug logging on several endpoint machines to capture detailed logs during high traffic periods.
4. Reviewed Zscaler server logs for timeout errors and connection issues.
5. Conducted remote sessions to discuss the issue and gather additional insights.

## Root Cause
The issue was identified as being related to the Zscaler configuration, which was likely dropping packets due to high traffic loads and possibly due to DDoS protection settings that limited connections from the same IP addresses.

## Solution
The customer was advised to:
- Disable the firewall temporarily on the local server to confirm if it was causing the packet drops.
- If disabling the firewall resolved the issue, they were instructed to re-enable it and adjust the settings to allow for the necessary traffic without dropping packets.

## Notes
- The customer only has a Device Control license, which does not allow for Deep Packet Inspection with the "Stealthy DPI Driver."
- Future configurations should consider the impact of security settings on traffic flow, especially in environments using zero trust models.
- It is recommended to monitor the server's resource usage closely after re-enabling the firewall to ensure stability.
```