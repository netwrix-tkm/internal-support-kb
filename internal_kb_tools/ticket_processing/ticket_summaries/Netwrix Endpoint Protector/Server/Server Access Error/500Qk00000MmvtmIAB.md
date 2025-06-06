```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000MmvtmIAB
- **Case Number:** 438343
- **Status:** Closed - Resolved
- **Account/Company:** Avrioc Technologies
- **Contact Name:** Naveen Kumar
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** NONE

## Problem Description
The customer reported that the EPP Server was unreachable for approximately one hour, preventing access to the server's UI. They expressed concern over not being informed of any maintenance activities that might have caused the downtime.

## Environment Details
- The issue occurred on the EPP Server hosted by Netwrix.
- The server had previously experienced similar access issues on two other occasions.

## Troubleshooting Steps
1. The customer opened a P0 support ticket due to the server being down.
2. DevOps investigated and noted that the EPP Server had "stopped sending metrics."
3. The EPP Server was restarted by DevOps, which restored access to the UI.
4. The support team checked disk space and performed status reports on services, confirming everything appeared normal.
5. An escalation to R&D was initiated to investigate the root cause of the server's unresponsiveness.

## Root Cause
The root cause was identified as the server's RAM entering swap mode, which led to performance degradation and unresponsiveness. It was determined that increasing the instance type from `c6i.xlarge (8 GB RAM)` to `m6i.xlarge (16 GB RAM)` would help mitigate this issue.

## Solution
The instance type was successfully modified to `m6i.xlarge (16 GB RAM)` after obtaining customer approval. This change was implemented without incurring additional costs as a gesture of goodwill from Netwrix management. Following the modification, the server was confirmed to be accessible again.

## Notes
- The customer inquired about internal monitoring capabilities to alert them if the server goes down in the future. It was communicated that Netwrix is working on implementing a feature to send alerts and create Salesforce tickets for server issues, but this integration may take time.
- It is recommended to monitor server performance closely and consider proactive resource adjustments to prevent similar issues in the future.
```