## Ticket Metadata
- **Ticket ID:** 500Qk00000OWcxJIAT
- **Case Number:** 443338
- **Status:** Closed - Resolved
- **Account/Company:** Aon Australia
- **Contact Name:** Yuri van Leeuwen
- **Product:** Netwrix Enterprise Auditor
- **Component:** Database Configuration/Capacity
- **Feature:** Initial setup
- **Version:** 12.0

## Problem Description
The customer was attempting to set up Netwrix for the first time but encountered authentication failures when trying to connect to a newly established SQL database.

## Environment Details
- The SQL database is hosted on Azure SQL Managed Instance.
- The service account used for authentication is an Active Directory account with the following roles:
  - Database owner (db_owner) database-level role
  - dbcreator server-level role
- The customer was unsure whether to use Windows or SQL authentication.

## Troubleshooting Steps
1. Confirmed the service account had the necessary permissions and roles.
2. Verified that the SQL database supports SQL logins.
3. Attempted both Windows and SQL authentication methods.
4. Ensured the domain/user name was from a trusted domain and that the username was enabled.
5. Suggested checking different address types (NetBIOS name, FQDN, or IP Address).
6. Recommended running the installer as a domain admin and checking for any antivirus or endpoint protection interference.

## Root Cause
The initial authentication failure was due to insufficient rights for the service account to run the installer. The SQL database was not the issue, as it was confirmed to be operational.

## Solution
The issue was resolved by ensuring that the service account had the necessary database owner (db_owner) permissions and switching to SQL authentication, which was the only method that worked with Azure SQL Managed Instance. Additionally, it was confirmed that the installation should be performed using a domain admin account to avoid permission issues.

## Notes
- It is important to ensure that any endpoint protection software (e.g., CrowdStrike Falcon) does not interfere with the installation process, as it is known to cause issues with Netwrix Enterprise Auditor.
- Future installations should be conducted with the appropriate permissions and under the right account to prevent similar issues.