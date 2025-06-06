```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000IVObaIAH
- **Case Number:** 427491
- **Status:** Closed - Resolved
- **Account/Company:** Great Eastern Life Assurance (Malaysia) Berhad
- **Contact Name:** Mohd Hasbul Hafiz Mat Hassan
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** NEA MGMT Console
- **Version:** 11.0

## Problem Description
The IDM Team was unable to log into the StealthAudit application using the username `PCDAAIDMR01` to reset user passwords. The issue arose because this username existed only in the Local Active Directory (AD) and was not recognized within the StealthAudit system.

## Environment Details
- Ongoing integration activities by the server team to connect child AD servers to new servers, which may have contributed to the issue.
- Multiple users reported being unable to log into StealthAudit and required password resets.

## Troubleshooting Steps
1. Confirmed that the username `PCDAAIDMR01` was created for password reset and maintenance of user access.
2. Investigated whether any team members could log into the Netwrix Enterprise Auditor (NEA) console.
3. Inquired if there was a custom job set up for resetting user accounts within NEA/SA, as password resets are not standard functionality.
4. Requested output from a PowerShell script to gather information about installed applications related to Netwrix/Stealth.

## Root Cause
The root cause of the issue was not definitively identified, but it was noted that the username `PCDAAIDMR01` was not recognized by the StealthAudit system due to its existence only in the Local AD. Additionally, ongoing server integration activities may have impacted the system's functionality.

## Solution
The issue was resolved by the customer's internal infrastructure team, who addressed the server connection issues. The team confirmed that the server connection issue was resolved, allowing access to the StealthAudit application.

## Notes
- It is important to ensure that usernames required for application access are properly synchronized between Local AD and the application system.
- Future activities involving server integration should be monitored closely to prevent similar access issues.
- A change freeze was initiated until December 2nd, with activities planned to resume on December 4th.
```