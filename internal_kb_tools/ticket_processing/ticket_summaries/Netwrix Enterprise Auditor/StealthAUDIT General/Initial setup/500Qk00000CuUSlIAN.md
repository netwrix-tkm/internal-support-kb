```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CuUSlIAN
- **Case Number:** 414694
- **Status:** Closed - Resolved
- **Account/Company:** Franklin Templeton Companies, LLC
- **Contact Name:** Sean Steinberg
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.6

## Problem Description
The customer reported encountering two error messages after remoting into their session following a timeout of their RDP session. The first error appeared upon reconnecting, and the second error occurred when attempting to perform actions within the SA console.

## Environment Details
- The issue occurred in a Netwrix Enterprise Auditor environment.
- The customer was using a PAM account to access the SA console.

## Troubleshooting Steps
1. The customer was instructed to completely close the NEA console.
2. The customer was advised to end the `StealthAudit.exe` processes within the Task Manager.
3. The customer was asked to attempt reopening the SA console after performing the above steps.
4. A recommendation was made to switch the SQL host PageFile from a capped 12GB to a system-managed setting on the C: Drive.
5. A reboot of the server was suggested to finalize the changes.

## Root Cause
The errors were likely caused by a memory leak due to the NEA application being left open for an extended period, compounded by the timeout of the RDP session. This led to resource contention when attempting to reconnect and access the console.

## Solution
The issue was resolved by:
- Closing the NEA console and terminating the `StealthAudit.exe` processes.
- Switching the SQL host PageFile settings to system-managed, which increased the allocated space to 24GB.
- A reboot of the server was performed to apply the changes.

## Notes
- It is important to monitor the NEA application for memory usage, especially if it has been running for an extended period.
- If similar errors occur in the future, consider checking for multiple active sessions or resource contention issues.
- Ensure that the SQL server connection is stable and that the NEA console is not left open unnecessarily to prevent similar issues.
```