## Ticket Metadata
- **Ticket ID:** 500Qk00000DpJsMIAV
- **Case Number:** 416705
- **Status:** Closed - Resolved
- **Account/Company:** Chubb INA Holdings Inc.
- **Contact Name:** Karoline Robb
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.5

## Problem Description
The customer requested assistance in setting up SSL and HTTPS for the AIC (Audit Intelligence Center) and reporting index.

## Environment Details
- The issue involved the Netwrix Enterprise Auditor version 11.5.
- The customer was using Windows authentication for database access.

## Troubleshooting Steps
1. Assigned a new SSL certificate to the Publish Report on port 443 and the AIC on port 481.
2. Attempted to access the login page, which indicated that the page was not secure.
3. Advised the customer to consult their certificate team or use a different certificate.
4. Cleared the password from the configuration file to reactivate the default admin account for AIC.
5. Logged in to the AIC, which redirected to the Database configuration page with an error: "Unable to connect to the database, please review the settings below."
6. Noted that the database was locked to a CLQ account "StealthID," for which the customer did not know the password.
7. Attempted to switch the AIC database to Windows authentication, which did not resolve the connection issue.

## Root Cause
The primary issue stemmed from the database being locked to an account ("StealthID") for which the customer did not have the password, preventing successful database connections. Additionally, the SSL certificate setup was initially incomplete, leading to security warnings.

## Solution
The issue was resolved by:
- Successfully assigning the new SSL certificate to the appropriate services (Publish Report on port 443 and AIC on port 481).
- Ensuring that the default admin account was reactivated by clearing the password in the configuration file.
- The customer was advised to work with their database team to regain access to the locked database account.

## Notes
- It is crucial for customers to have access to the database credentials, especially when using accounts that may be locked or protected.
- Future cases involving SSL setup should ensure that the certificate is correctly assigned and that the customer is aware of any potential security warnings that may arise during the initial setup.
- Always verify the authentication method being used for database connections to avoid similar issues.