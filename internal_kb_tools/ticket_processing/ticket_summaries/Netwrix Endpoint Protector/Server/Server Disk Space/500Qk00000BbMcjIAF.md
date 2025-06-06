```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BbMcjIAF
- **Case Number:** 411427
- **Status:** Closed - Resolved
- **Account/Company:** Zee Entertainment and Enterprises ltd
- **Contact Name:** Jagadish Ashadapu
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** NONE

## Problem Description
The customer reported that the disk usage on the EPP server exceeded 82%, specifically reaching 83%, and requested assistance to free up space on the disk.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Current Disk Usage:** 83%

## Troubleshooting Steps
1. The customer initially reported the disk usage issue and requested an update.
2. Follow-up communications indicated the disk usage remained at 83%.
3. The support engineer, Andrei Pop, communicated with the customer to arrange a remote connection for further investigation.
4. The customer expressed difficulty in reading responses from the support team, which appeared garbled in their email client.
5. The support team clarified the situation and confirmed the steps taken to address the disk space issue.

## Root Cause
The root cause of the disk space issue was identified as the accumulation of shadow copies, which consumed significant disk space on the EPP server.

## Solution
The issue was resolved by clearing server space through the deletion of shadow copies, which effectively reduced the disk usage below the critical threshold.

## Notes
- It is important to monitor disk usage regularly to prevent it from exceeding critical limits.
- Consider implementing automated cleanup processes for shadow copies to manage disk space proactively.
- Ensure that all communications are clear and accessible to avoid misunderstandings regarding technical responses.
```