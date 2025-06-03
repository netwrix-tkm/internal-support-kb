```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000EqBQjIAN
- **Case Number:** 418963
- **Status:** Closed - Resolved
- **Account/Company:** The Stars Group Interactive Services / Flutter International
- **Contact Name:** Denis Pasca
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Upload Not Blocked
- **Version:** 5.9.4.0

## Problem Description
The customer reported that Skype was not being blocked by the Netwrix Endpoint Protector (EPP) despite being included in their Content-Aware Protection (CAP) policies. Document uploads via the desktop version of Skype were not restricted, leading to unmonitored usage by multiple users.

## Environment Details
- **EPP Version:** 5.9.4.0
- **Operating System:** macOS 14.6
- **Testing Environment:** Desktop version of Skype

## Troubleshooting Steps
1. Confirmed that Skype was listed as an exit point in the CAP policies.
2. Verified the EPP version installed on the testing machine.
3. Collected logs from the affected Mac to analyze the issue.
4. Engaged with internal engineering teams to investigate the problem further.
5. Communicated with the customer regarding updates and potential fixes.

## Root Cause
The issue was identified as a missing process name for Skype in the monitored process names list on the server side. Specifically, the process name "com.skype.skype.Helper" was not included, preventing EPP from intercepting Skype traffic effectively.

## Solution
The issue was resolved by updating the server version to 5.9.4.1, which included the necessary process name for Skype. This update allowed EPP to correctly block document uploads via Skype as intended.

## Notes
- Ensure that any future updates to EPP include necessary process names for applications that are critical to monitoring.
- Regularly review and update CAP policies to reflect any changes in application versions or behaviors.
- Monitor user feedback after updates to confirm that issues are resolved and no new problems arise.
```