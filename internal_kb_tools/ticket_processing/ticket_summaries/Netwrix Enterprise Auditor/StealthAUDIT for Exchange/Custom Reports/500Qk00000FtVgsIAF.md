## Ticket Metadata
- **Ticket ID:** 500Qk00000FtVgsIAF
- **Case Number:** 421302
- **Status:** Closed - Resolved
- **Account/Company:** Federated Hermes
- **Contact Name:** Dennis Nicholson
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Exchange
- **Feature:** Custom Reports
- **Version:** 11.5

## Problem Description
The customer was unable to create a custom report as per the documented process provided by a Netwrix Technical Support Engineer (TSE). The issue persisted for over 40 days, with multiple missed meetings between the support technician and the client.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for Exchange
- **Product Version:** 11.5

## Troubleshooting Steps
1. Attempted to schedule multiple meetings with the client to discuss the issue.
2. Reviewed the documentation created with the previous TSE regarding the custom report creation process.
3. Identified that the client was trying to create two analysis tasks to generate a filtered table.
4. Noted that the second task could not query the table created by the first task because it had not been executed yet.
5. Conducted a meeting with the client to walk through the steps of creating the custom report.

## Root Cause
The client was missing a critical step in the report creation process: they needed to run the first analysis task before attempting to create the second task. As a result, the table that the second task needed to query did not exist, leading to the configuration issue.

## Solution
After running the first analysis task, the table was successfully created. The client was then able to configure the second task to pull from this newly created table. Both tasks were executed, and a report was generated that successfully emailed the results as intended. The client confirmed the accuracy of the information in the report.

## Notes
- Ensure that clients are aware of the necessity to execute tasks in the correct order when creating custom reports.
- Document any missed meetings and follow up promptly to avoid delays in issue resolution.
- Consider providing a checklist for clients to follow when creating complex reports to prevent similar issues in the future.