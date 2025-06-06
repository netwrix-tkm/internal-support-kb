## Ticket Metadata
- **Ticket ID:** 500Qk00000DhfelIAB
- **Case Number:** 416403
- **Status:** Closed - Resolved
- **Account/Company:** Republic Bancorp, Inc. (Republic Bank)
- **Contact Name:** Lauren Messex
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.6

## Problem Description
The customer reported that they were unable to open the AIC (Audit Information Center).

## Environment Details
- **Web Server Port:** 8082
- **URL Protocol:** HTTPS

## Troubleshooting Steps
1. Reviewed the configuration file for the AIC and the Publish Report.
2. Identified that the customer was using the incorrect URL to access the AIC.
3. Deleted the existing AIC shortcut.
4. Created a new AIC shortcut with the correct URL.
5. Ran the command `netsh http show urlacl` to check the URL Access Control List (urlacl).
6. Noted that `http://+:8082/` was not listed in the urlacl.
7. Manually added the URL `https://+:8082/` to the urlacl list.
8. Restarted the web server service.

## Root Cause
The issue was caused by the customer using an incorrect URL to access the AIC, which was not properly configured in the URL Access Control List (urlacl).

## Solution
The issue was resolved by:
- Deleting the incorrect AIC shortcut and creating a new one with the correct URL.
- Adding the correct URL `https://+:8082/` to the URL Access Control List (urlacl).
- Restarting the web server service to apply the changes.

## Notes
- When configuring access to the AIC, ensure that the correct URL is used and properly registered in the URL Access Control List.
- If a message appears stating "Unable to use the SQL Server Database provided," it may not prevent access but should be investigated separately.