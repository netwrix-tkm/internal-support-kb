## Ticket Metadata
- **Ticket ID:** 500Qk00000MoBZxIAN
- **Case Number:** 438449
- **Status:** Closed - Resolved
- **Account/Company:** International Motors, LLC
- **Contact Name:** William Dammeier
- **Product:** Netwrix Enterprise Auditor
- **Component:** Activity Monitor
- **Feature:** Credentials
- **Version:** 11.6

## Problem Description
The customer reported receiving failed login alerts for their account in the SIEM from the server hosting Netwrix Enterprise Auditor. The failed logins began occurring after the customer made changes to a reporting feature in the application. The logins were showing as the customer's user ID, while jobs in NEA should be running under a service account.

## Environment Details
- The server is exclusively running Netwrix Enterprise Auditor.
- The customer typically accesses the server using their own account.

## Troubleshooting Steps
1. The customer was asked if any changes were made to the connection profile or if they were using the correct account to launch the application.
2. The customer confirmed that they reverted any changes made to the reporting feature and that they were using their account to access the application.
3. The customer was instructed to run a PowerShell command to check the installed software on the server.
4. The customer reported that the NEA application successfully launched without issues.
5. The support technician suggested checking for mistyped passwords that could be causing the failed login alerts.
6. The customer rebooted the server, but the failed logins continued immediately after the server came online.

## Root Cause
The root cause of the issue was identified as the password for the user's account not being updated in the Activity Monitor, which led to repeated failed login attempts.

## Solution
The support technician updated the password for the user's account in the Activity Monitor. The customer was advised to monitor their SIEM for any further failed login attempts after the password update.

## Notes
- The customer confirmed that no further authentication failures were observed after the password was updated.
- It is important to ensure that all service accounts and user accounts have their passwords updated in the relevant applications to prevent similar issues in the future.