## Ticket Metadata
- **Ticket ID:** 500Qk00000KpwRUIAZ
- **Case Number:** 432846
- **Status:** Closed - Resolved
- **Account/Company:** Hydro Group Norway
- **Contact Name:** Saveetha Anesh
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.5

## Problem Description
The customer reported discrepancies in the results of a discovery run for Windows share servers conducted in November. They sought clarification on the report, specifically regarding which columns indicated new shares, source server names, and destination servers. Additionally, they wanted to understand how the discovery run identifies new Windows shares for monitoring.

## Environment Details
- The discovery run utilized a custom job named "GET SHARE WIN," which was not a built-in Netwrix Enterprise Auditor job but rather a custom analysis task likely created by Hydro Group Norway or the Netwrix Professional Services team.

## Troubleshooting Steps
1. Reviewed the custom job "GET SHARE WIN" and its configuration.
2. Engaged with the Professional Services team to clarify the functionality of the "GET SHARE WIN" job.
3. Inquired about the settings for the "1.GetHostList1" and "GetHostShares1" jobs.
4. Provided guidance on configuring the "GetHostShares1" job to ensure it only shows a single server in the "HOST" column.
5. Communicated with the customer to gather additional details regarding their current concerns.

## Root Cause
The discrepancies in the discovery run results were attributed to the configuration of the custom jobs. Specifically, the "GetHostShares1" job was not set up to filter results to a single server, leading to multiple entries in the "HOST" column.

## Solution
The issue was resolved by configuring the "GetHostShares1" job to include only the StealthAudit server (AZITSBITS01) in its host settings. This adjustment ensured that the resulting "HOST" column in the output table displayed only the specified server. Additionally, it was clarified that the final report does not differentiate between newly found shares and those identified in previous runs, as this functionality was not included in the current job setup.

## Notes
- The "Remark" column in the report contains comments added during the creation of Windows Shares.
- The "ShareType" column indicates the type of share identified, with values corresponding to Microsoft Windows share types (e.g., Admin, Default, Printer, Special).
- Future configurations of similar custom jobs should ensure that host lists are correctly set to avoid multiple entries in output tables.