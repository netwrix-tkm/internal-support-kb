## Ticket Metadata
- **Ticket ID:** 500Qk00000HiZxzIAF
- **Case Number:** 425667
- **Status:** Closed - Resolved
- **Account/Company:** Kerry Group Services International Limited
- **Contact Name:** Cameron Bowlds
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.6

## Problem Description
The customer reported an issue with the Netwrix Access Information Center (NAIC) where they received an error message stating, "Unable to use to the SQL Server Database provided" when attempting to log in to the GUI.

## Environment Details
- The connection to the SQL database was established using Windows authentication.
- The issue began after an upgrade to the Netwrix Enterprise Auditor (NEA) on October 22, 2024.

## Troubleshooting Steps
1. Confirmed the connection method to the SQL database (Windows authentication).
2. Verified that the password for the SQL account had not changed.
3. Attempted to uninstall and reinstall the Access Information Center (AIC) but encountered an error: "Windows is unable to stop the service for the Access Information Center."
4. Tried disabling the server and rebooting it, but these actions did not resolve the issue.
5. Reviewed logs for additional information.

## Root Cause
The issue was identified as being related to the inability to stop the AIC service, which prevented the uninstallation and reinstallation process necessary to resolve the database connection error.

## Solution
The customer successfully stopped the AIC service and was able to uninstall and reinstall the NAIC. After the reinstallation, the application functioned correctly, allowing access to the SQL Server database without errors.

## Notes
- It is important to ensure that all services related to the application are stopped before attempting uninstallation to avoid similar issues in the future.
- If the service cannot be stopped, consider checking for any dependencies or processes that may be using the service, and ensure that they are terminated before proceeding with uninstallation.