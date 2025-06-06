## Ticket Metadata
- **Ticket ID:** 500Qk00000OyRAnIAN
- **Case Number:** 444639
- **Status:** Closed - Resolved
- **Account/Company:** Techsol Infosec
- **Contact Name:** Umesh Shetty
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** NONE

## Problem Description
The user reset their Multi-Factor Authentication (MFA) apps and was unable to log in to the Netwrix portal. They requested assistance to reset their password.

## Environment Details
- The EPP Server is hosted locally on premises.
- The issue involved accessing the backend of the EPP Server via SSH.

## Troubleshooting Steps
1. Conducted a remote session with the customer to gather information.
2. Confirmed that the customer could not retrieve MFA codes for login.
3. Requested SSH access to the EPP Server but was unable to connect, likely due to:
   - A firewall blocking port 22.
   - SSH being turned off on the EPP Appliance.
4. Requested console access, but the customer needed to involve their IT administration team for necessary access.
5. Scheduled a follow-up session for the following week when the IT team would be available.

## Root Cause
The root cause of the issue was the user's inability to access their MFA codes after resetting the MFA apps, which prevented them from logging into the Netwrix portal.

## Solution
The issue was resolved during a remote session by removing the MFA configuration via the backend of the EPP Server Appliance. The customer was then able to log in successfully.

## Notes
- Ensure that users are aware of the implications of resetting MFA apps and have a backup method for retrieving codes.
- Future cases may require coordination with the customer's IT team to gain necessary access for troubleshooting.
- Always verify firewall settings and SSH configurations when encountering access issues with local servers.