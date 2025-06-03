```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CDTEzIAP
- **Case Number:** 412777
- **Status:** Closed - Resolved
- **Account/Company:** Profertil - Argentina
- **Contact Name:** Leonardo Perosio
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** Not specified

## Problem Description
The customer reported issues with the "Logs Report" and "File Tracing" options in the Netwrix Endpoint Protector. When these options were selected, the page would continuously load without displaying any information.

## Environment Details
- High number of logs on the server (over 20 million logs).
- Potential high resource usage due to client-server activity.
- Possible disk space issues affecting performance.

## Troubleshooting Steps
1. Initial assessment of the issue indicated multiple potential causes, including:
   - High number of logs on the server.
   - High resource usage from ongoing client-server activities.
   - Disk space limitations.
2. Suggested setting up an audit log to monitor log generation.
3. Recommended a remote session for deeper troubleshooting, requiring SSH access to the server.
4. Scheduled a remote session with the customer to investigate further.

## Root Cause
The issue was primarily caused by an excessive number of logs (over 20 million) stored on the server, which led to performance degradation and slow loading times for the "Logs Report" and "File Tracing" features.

## Solution
- An audit log backup was set up to manage the high volume of logs.
- The customer was advised to decrease the retention period for logs in the audit log settings.
- After implementing these changes, the loading issues were resolved, and the pages began to load correctly.

## Notes
- It is important to monitor log generation and implement regular maintenance to prevent similar issues in the future.
- Consider advising customers to set appropriate log retention policies based on their usage to avoid performance issues.
```