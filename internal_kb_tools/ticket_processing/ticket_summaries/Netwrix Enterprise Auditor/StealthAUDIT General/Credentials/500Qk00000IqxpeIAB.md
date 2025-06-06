## Ticket Metadata
- **Ticket ID:** 500Qk00000IqxpeIAB
- **Case Number:** 428316
- **Status:** Closed - Resolved
- **Account/Company:** Fair Isaac Corporation (FICO)
- **Contact Name:** Chandan Trikha
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Credentials
- **Version:** 11.6

## Problem Description
The customer reported an issue while scanning a host using the Netwrix Stealth Audit tool, where the system displayed an "invalid credentials" error.

## Environment Details
- The issue occurred when attempting to scan a host on the "FICOCLOUDDEV.COM" domain.
- The user account in question was "svcStealthAudit".

## Troubleshooting Steps
1. The customer attempted to reset the password for the "svcStealthAudit" account.
2. The customer confirmed they could successfully log in via Remote Desktop with the new password.
3. The support team requested additional information regarding the issue, including screenshots and details about any changes in the environment.
4. The support team identified that the user account was disabled and needed to be enabled by the internal IT support.
5. The account was unlocked by the internal IT team, but the issue persisted initially.
6. A Zoom meeting was scheduled to further investigate the issue.

## Root Cause
The root cause of the issue was identified as the "svcStealthAudit" account being disabled, which led to the invalid credentials error during the scanning process. The account was locked due to multiple failed login attempts.

## Solution
The issue was resolved after the internal IT team enabled the "svcStealthAudit" account. The customer confirmed that after waiting for the account to unlock and ensuring no other changes were made to the product, the scanning process was successful.

## Notes
- Ensure that the "svcStealthAudit" account is enabled and not locked before attempting to run scans.
- It is advisable to monitor account lockout policies to prevent similar issues in the future.
- Always confirm successful login via Remote Desktop before running any jobs that require credentials.