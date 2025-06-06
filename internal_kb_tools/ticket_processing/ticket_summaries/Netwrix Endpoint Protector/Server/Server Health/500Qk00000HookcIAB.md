```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000HookcIAB
- **Case Number:** 425858
- **Status:** Closed - Resolved
- **Account/Company:** EMERGING MARKET TECHNOLOGIES TRADING FZCO (EMT UAE)
- **Contact Name:** Aiman Jadiba
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Health
- **Version:** None

## Problem Description
The customer reported significant slowness in the WEBUI of the Netwrix Endpoint Protector (EPP) when multiple administrators were connected to the system. They requested a health check to diagnose the issue.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Age of the system:** 9.1 years

## Troubleshooting Steps
1. Scheduled a remote session with the customer to assess the system.
2. Conducted a health check on the server during the remote session.
3. Identified and removed duplicate devices from the database.
4. Optimized server performance settings.

## Root Cause
The slowness was primarily caused by the presence of duplicate devices in the database, which led to increased load and performance degradation when multiple admins accessed the WEBUI simultaneously.

## Solution
The server was optimized, and duplicate devices were removed from the database. The customer was advised to monitor the server performance for a few days following the changes to ensure the issue was resolved.

## Notes
- The customer was advised to confirm the mount point used on their external storage and ensure that the user connected has the appropriate write permissions.
- A follow-up ticket was recommended for any ongoing issues related to external storage integration.
```