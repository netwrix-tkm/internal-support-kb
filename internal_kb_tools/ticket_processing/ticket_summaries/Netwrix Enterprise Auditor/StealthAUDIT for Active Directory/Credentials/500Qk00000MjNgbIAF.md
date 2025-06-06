## Ticket Metadata
- **Ticket ID:** 500Qk00000MjNgbIAF
- **Case Number:** 438176
- **Status:** Closed - Resolved
- **Account/Company:** Gleaner Life Insurance Society
- **Contact Name:** Mark Cruz
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Credentials
- **Version:** 11.6

## Problem Description
The customer reported a login error for the StealthBits service account, indicating that the wrong password was provided or there was a time mismatch between the Key Distribution Center (KDC) and the client.

## Environment Details
- **Event Category:** Authentication
- **Target Host:** HostDC01.GLEANERLIFE.COM
- **Target Host IP:** 10.100.1.185
- **Originating Host:** HostDC02.GLEANERLIFE.COM
- **Originating IP:** 10.100.1.186
- **Perpetrator Name:** GLEANERLIFEsvc_stealthbits

## Troubleshooting Steps
1. Confirmed the error message indicating a failed Kerberos login due to incorrect password or time mismatch.
2. Reviewed the service account password settings and confirmed that the password was updated in multiple locations.
3. Suggested the customer follow the article on updating service account passwords in Active Directory.
4. Conducted a meeting to navigate to Databases > Settings > Connection and applied the correct service profile for "GLEANERLIFEsvc_stealthbits".
5. Discussed potential configurations for SQL Server endpoints under Database > Settings > Host Lists Assignment.

## Root Cause
The issue was caused by the customer updating their password policy and changing the service account password in some locations but missing it in others, leading to authentication failures.

## Solution
The issue was resolved by ensuring that the correct service profile was applied in the Netwrix settings and confirming that all instances of the service account password were updated consistently across the environment. The customer was advised to carefully follow the provided documentation on updating service account passwords.

## Notes
- It is crucial to ensure that service account passwords are updated in all relevant locations to prevent authentication issues.
- Future changes to password policies should be communicated clearly to all relevant personnel to avoid similar issues.
- The customer was advised to review the configuration of SQL Server endpoints in the future, as it may impact the functionality of the Netwrix product.