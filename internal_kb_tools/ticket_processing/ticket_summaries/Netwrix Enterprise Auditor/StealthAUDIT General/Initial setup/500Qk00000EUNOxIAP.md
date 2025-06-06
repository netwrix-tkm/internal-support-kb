```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000EUNOxIAP
- **Case Number:** 418267
- **Status:** Closed - Resolved
- **Account/Company:** Bank of America Corporation
- **Contact Name:** Gregory Meyer
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.5

## Problem Description
The customer reported that scheduled tasks were not executing as expected. Attempts to run the schedules from the user interface and the task scheduler were unsuccessful.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Product Version:** 11.5

## Troubleshooting Steps
1. Reviewed the settings and permissions for the scheduled tasks.
2. Attempted to run the schedules from both the UI and the task scheduler.
3. Checked the user account permissions related to the scheduled tasks.

## Root Cause
The issue was caused by the user account associated with the scheduled tasks not being included in the Local Security Policy under "Log on as a batch job." This permission is necessary for the account to execute scheduled tasks.

## Solution
The resolution involved adding the user account to the Local Security Policy under "Log on as a batch job." After making this change, the scheduled tasks were successfully executed when run from the schedule.

## Notes
- Ensure that any user accounts designated to run scheduled tasks are properly configured in the Local Security Policy to avoid similar issues in the future.
- Regularly review permissions and settings for scheduled tasks during initial setup to prevent execution failures.
```