## Ticket Metadata
- **Ticket ID:** 500Qk00000GivChIAJ
- **Case Number:** 423091
- **Status:** Closed - Resolved
- **Account/Company:** DEVCON GmbH
- **Contact Name:** Falko Groebel
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** Not specified

## Problem Description
The customer reported an issue with resetting the root password in the Netwrix Endpoint Protector (EPP). After a recent password change, the new password was not accepted during login, and the customer suspected that there might be "forbidden" characters that were not properly validated during the password creation process.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** EPP Other

## Troubleshooting Steps
1. Verified the password entered by the user to ensure it was copied correctly and did not contain any typing errors.
2. Checked for any documentation regarding forbidden characters in passwords for the EPP.
3. Attempted to reset the password through the standard password reset procedure.
4. Confirmed that the password creation tool used by the customer was functioning correctly.

## Root Cause
The root cause of the issue was identified as a failure in the password validation process, which did not adequately check for forbidden characters during the password creation. This led to the acceptance of a password that was ultimately deemed invalid by the system.

## Solution
The issue was resolved by performing a password reset for the user. The support team provided a new password that complied with the system's requirements, ensuring that it did not contain any forbidden characters. The customer was able to log in successfully with the new password.

## Notes
- It is important to communicate clearly to users about any restrictions on password characters to prevent similar issues in the future.
- Consider implementing additional validation checks in the password creation process to avoid acceptance of invalid passwords.
- Ensure that users are aware of the password reset procedure to expedite resolution in case of similar issues.