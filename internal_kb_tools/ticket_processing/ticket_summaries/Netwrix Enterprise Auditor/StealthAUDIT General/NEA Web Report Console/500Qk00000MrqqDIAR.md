## Ticket Metadata
- **Ticket ID:** 500Qk00000MrqqDIAR
- **Case Number:** 438625
- **Status:** Closed - Resolved
- **Account/Company:** Eaton Vance Corp
- **Contact Name:** Jeffrey Schenkman
- **Product:** Netwrix Enterprise Auditor
- **Component:** NEA Web Report Console
- **Feature:** NEA Published Reports
- **Version:** 11.5

## Problem Description
The customer requested assistance with setting up correct access to the web interface for NEA Published Reports.

## Environment Details
- The issue involved the configuration of the web interface for Netwrix Enterprise Auditor (NEA) version 11.5.
- Active Directory (AD) accounts were being used for access control.

## Troubleshooting Steps
1. Clarified with the customer whether they were referring to the web interface for StealthAUDIT or NEA Published Reports.
2. Reviewed the settings in NEA > Settings > Access to ensure proper roles were assigned.
3. Added an AD account with a Report Viewer Role in SA/NEA > Settings > Access.
4. Attempted to save the changes to confirm the new user could access the reports.
5. Provided guidance on updating the URL in the "Publish Reports" desktop icon to point to the correct Published Reports link.

## Root Cause
The initial issue stemmed from incorrect access permissions for the user accounts and an outdated URL in the "Publish Reports" desktop icon.

## Solution
1. Assigned the Report Viewer Role to the appropriate AD account, which allowed the user to view reports after saving the changes.
2. Instructed the customer to update the URL in the "Publish Reports" desktop icon to the correct link found in NEA > Settings > Reporting > Website URL configuration. This was referenced in the Netwrix Help Center documentation.

## Notes
- Ensure that the URL in the "Publish Reports" desktop icon is always updated to reflect the correct Published Reports link to avoid access issues in the future.
- For future cases, verify user roles and permissions in the NEA settings to ensure users have the necessary access to reports.