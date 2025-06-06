## Ticket Metadata
- **Ticket ID:** 500Qk00000KpuJBIAZ
- **Case Number:** 432821
- **Status:** Closed - Resolved
- **Account/Company:** Great Eastern Life Assurance (Malaysia) Berhad
- **Contact Name:** MOHD HASBUL HAFIZ MAT HASSAN
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** NEA Web Report Console
- **Version:** 11.0

## Problem Description
A member of the GE ID Management team was unable to manage user accounts due to a lack of permissions to access the StealthAUDIT web console. The user PCDAAIDMR01 could log in but could not view any reports.

## Environment Details
- **Active Directory (AD) Integration:** User PCDAAIDMR01 was onboarded to the AD servers for user AD group access.
- **Web Console Version:** 11.0.1221.1018

## Troubleshooting Steps
1. Verified that the user PCDAAIDMR01 could log in to the StealthAUDIT Reporting web module.
2. Confirmed that the user was not assigned any web-related roles in the User Access settings.
3. Discussed the issue in a meeting with the customer to clarify the permissions required.
4. Reviewed user access settings in both StealthAUDIT and StealthDEFEND.
5. Identified that the Reporting module does not allow for user management functions (adding/removing users) and that these actions must be performed via the StealthAUDIT desktop application.

## Root Cause
The issue was caused by the user PCDAAIDMR01 not being added to the correct role in the StealthAUDIT User Access settings, which restricted access to the necessary features in the web console.

## Solution
To resolve the issue, the support team added the user PCDAAIDMR01 to the appropriate role within the User Access settings. After this adjustment, the user was able to access and view reports in the StealthAUDIT Reporting web module.

## Notes
- The Reporting module does not provide administrative functionalities for user management; these must be handled through the StealthAUDIT desktop application.
- Ensure that all users are assigned the correct roles in the User Access settings to prevent similar issues in the future.