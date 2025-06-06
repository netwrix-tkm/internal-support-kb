## Ticket Metadata
- **Ticket ID:** 500Qk00000DEqotIAD
- **Case Number:** 415384
- **Status:** Closed - Resolved
- **Account/Company:** MUFG Bank, LTD.
- **Contact Name:** Michael Kong
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Configuration
- **Version:** 11.5

## Problem Description
The customer requested guidance on how to reset the AIC Builtin Administrator password, which had been changed. Due to Single Sign-On (SSO) being enabled, the customer was unable to log in with the admin account to make the necessary corrections.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Product Version:** 11.5
- **SSO Enabled:** Yes

## Troubleshooting Steps
1. Confirmed that the AIC Builtin Administrator password had been changed.
2. Identified that SSO was preventing access to the admin account.
3. Suggested using a private/incognito browser to bypass SSO and prompt for credentials.

## Root Cause
The issue was caused by the AIC Builtin Administrator password being changed without the ability to log in due to SSO restrictions.

## Solution
The customer successfully reset the password by:
1. Clearing the `AuthBuiltinAdminPassword` value in the `Web.config` file.
2. Using an incognito browser to bypass SSO, which prompted for the admin credentials.

## Notes
- When SSO is enabled, using a private/incognito browser can be an effective workaround to access admin accounts for password resets.
- Always ensure that the `Web.config` file is backed up before making changes to avoid potential misconfigurations.