```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000JIxxzIAD
- **Case Number:** 429354
- **Status:** Closed - Resolved
- **Account/Company:** Giift
- **Contact Name:** Thanushree
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** None

## Problem Description
The customer reported a mismatch between the user count and the installed computer count in the Netwrix Endpoint Protector (EPP) dashboard. Specifically, they had 179 installed computers but 194 users were counted.

## Environment Details
- EPP client installed on Windows and macOS machines.
- EPP client versions attempted: 3.0.3.1009 and 3.0.4.1006.

## Troubleshooting Steps
1. Confirmed that the Client Registration Certificate and Server Certificate Stack were off.
2. Reinstalled the EPP client (version 3.0.3.1009) and restarted the computer; the computer was not visible in the UI.
3. Installed EPP client version 3.0.4.1006 and restarted; the computer was still not visible in the UI.
4. Deleted the old client certificate, downloaded a new certificate after a server upgrade, imported it, and set it as always trusted.
5. Verified client logs for both versions showed HTTP 200, indicating successful communication with the server.
6. Performed the client re-registration procedure multiple times.
7. Noted that several Mac computers had the same name, which could cause visibility issues.
8. Changed the name of a test computer and restarted; it was still not visible in the UI.

## Root Cause
The root cause of the issue was identified as multiple Mac computers having the same name, which likely led to conflicts in the EPP dashboard. Additionally, the client registration and server certificate issues contributed to the visibility problems.

## Solution
The customer was advised that the issue was related to naming conflicts among the Mac computers. They were informed that changing the names of the computers would resolve the visibility issue in the EPP dashboard. The customer acknowledged this information and requested to close the ticket.

## Notes
- Ensure that all computers have unique names to avoid visibility issues in the EPP dashboard.
- Monitor the client registration and server certificate settings after upgrades to prevent similar issues in the future.
```