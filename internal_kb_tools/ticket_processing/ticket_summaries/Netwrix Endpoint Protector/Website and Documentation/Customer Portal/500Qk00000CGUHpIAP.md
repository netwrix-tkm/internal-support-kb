```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CGUHpIAP
- **Case Number:** 412924
- **Status:** Closed - Resolved
- **Account/Company:** Chevron Phillips Chemical
- **Contact Name:** Jeff Schemp
- **Product:** Netwrix Endpoint Protector
- **Component:** Website and Documentation
- **Feature:** Customer Portal
- **Version:** Not specified

## Problem Description
The customer reported that their web server was unresponsive and very slow, displaying out of memory messages and process kill messages. Restart attempts resulted in messages indicating that SQL was attempting to stop but never completed. The only way to restore functionality was through a forced power reset, which did not resolve the underlying memory issues.

## Environment Details
- Server ID: FGEFMN4J
- Current server resources: 6 CPU cores, 24 GB of RAM
- Approximately 6500 endpoints connected to the EPP server.

## Troubleshooting Steps
1. Verified the server's resource allocation and performance metrics.
2. Attempted to restart the server multiple times, noting the failure to stop SQL processes.
3. Conducted a remote session to analyze the server's performance and resource usage.
4. Suggested increasing server resources to address performance issues.

## Root Cause
The root cause of the issue was identified as insufficient server resources (CPU and RAM) to handle the load from approximately 6500 connected endpoints, leading to memory exhaustion and unresponsiveness.

## Solution
- The support team re-optimized the server resources after the customer increased the server's capacity to 12 CPU cores and 32 GB of RAM.
- Post-optimization, the server performance improved significantly, resolving the unresponsiveness issue.

## Notes
- It is recommended that the customer monitor server performance closely and consider increasing resources proactively if they notice performance drops in the future.
- Suggested future resource allocations include increasing CPU from 6 to 12 or 16 cores and RAM from 24 GB to 32 GB.
```