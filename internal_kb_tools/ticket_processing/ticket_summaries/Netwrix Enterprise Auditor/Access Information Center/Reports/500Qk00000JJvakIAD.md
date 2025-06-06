## Ticket Metadata
- **Ticket ID:** 500Qk00000JJvakIAD
- **Case Number:** 429410
- **Status:** Closed - Resolved
- **Account/Company:** ConocoPhillips Company
- **Contact Name:** Israel Cordero
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Reports
- **Version:** 11.5

## Problem Description
The customer reported an issue with the Access Information Center (AIC) application, specifically regarding the inability to include the "Target Path" column in their reports.

## Environment Details
- **Application:** Access Information Center (not Stealth-Audit)
- **Product Version:** 11.5

## Troubleshooting Steps
1. In AIC, navigate to "Resource Audit."
2. Drill down to the specific resource: "shared6" > "G&A_Model" > "2024."
3. Attempt to right-click on the column header for "Path" to check for the option to add "Target Path."

## Root Cause
The issue was due to the lack of visibility for the "Target Path" column in the report settings, which was not initially enabled for export.

## Solution
To resolve the issue, the following steps were provided to the customer:
1. In AIC, navigate to "Resource Audit" and drill down to "shared6" > "G&A_Model" > "2024."
2. Right-click on the column header for "Path."
3. Scroll down and check the box to add "Target Path."
4. The "Target Path" column will now be available for export into spreadsheets.

The customer was asked to confirm that this solution met their requirements.

## Notes
- Ensure that users are aware of the steps to enable additional columns in reports to avoid similar issues in the future.
- It is important to clarify the distinction between the Access Information Center and Stealth-Audit to prevent confusion in support requests.