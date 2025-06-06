## Ticket Metadata
- **Ticket ID:** 500Qk00000MncqhIAB
- **Case Number:** 438395
- **Status:** Closed - Resolved
- **Account/Company:** American Express
- **Contact Name:** Alex Parsa
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Custom Reports
- **Version:** 11.5

## Problem Description
The customer, Alex Parsa from American Express, requested assistance in organizing a custom report that provides permission groups for their servers. He wanted to better understand the columns available for addition and to filter out users from the report.

## Environment Details
- The report utilizes the `SA_FSAA_PrermissionsView`.
- The report includes groups and users, and the customer expressed a preference for displaying share paths instead of folder paths.

## Troubleshooting Steps
1. Conducted a remote session to review the report configuration.
2. Modified the existing report filters to include only Domain Groups, excluding service principals and Domain Users.
3. Attempted to change the folder paths to associated Share paths but found that the necessary information was not available in the current table.
4. Suggested the customer explore SQL View Creation to join multiple tables for further customization.

## Root Cause
The inability to change folder paths to share paths was due to the limitations of the data structure in the report's underlying table, which did not contain the required information.

## Solution
The issue was resolved by modifying the report filters to meet the customer's needs for filtering out users. The customer was encouraged to continue experimenting with SQL View Creation for further customization of the report.

## Notes
- The customer was advised that further customization might require engaging with Professional Services (ProServ) if they needed more advanced report configurations.
- It is important to note that while basic filtering can be accomplished, complex report modifications may require additional technical support or services.