## Ticket Metadata
- **Ticket ID:** 500Qk00000NoaawIAB
- **Case Number:** 441273
- **Status:** Closed - Resolved
- **Account/Company:** Avrioc Technologies
- **Contact Name:** Naveen Kumar
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** NONE

## Problem Description
The customer reported that the server was unreachable since the morning of April 8, 2025. This issue had occurred multiple times in the past, and the customer expected the server to become accessible shortly. They noted that even the failover link was not accessible.

## Environment Details
- Previous related ticket: "00438343 - Server is Unreachable"
- Initial instance type: c6i.xlarge (8 GB RAM)
- Recommended instance type: m6i.xlarge (16 GB RAM)

## Troubleshooting Steps
1. Acknowledged the issue and prioritized it for investigation.
2. Reviewed the previous ticket for context and identified the recommendation to increase the instance type due to RAM issues.
3. Awaited customer approval to proceed with the instance type modification.
4. Upon receiving confirmation from the customer, DevOps increased the instance type from c6i.xlarge to m6i.xlarge.
5. Restarted the appliance after the instance type modification.
6. Confirmed with the customer if they could access the server post-restart.

## Root Cause
The server became unreachable due to insufficient RAM, which caused continuous memory swapping. This issue was exacerbated by the server's current instance type (c6i.xlarge) being inadequate for the workload.

## Solution
The issue was resolved by:
- Increasing the instance type from c6i.xlarge (8 GB RAM) to m6i.xlarge (16 GB RAM).
- Restarting the appliance after the modification, which restored server accessibility.

## Notes
- It is recommended to monitor server performance and consider proactive instance type adjustments based on workload to prevent similar issues in the future.
- Implementing internal monitoring to alert when the server goes down could help in identifying and resolving issues more quickly.