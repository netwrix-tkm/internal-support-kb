```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000FpHPeIAN
- **Case Number:** 421137
- **Status:** Closed - Resolved
- **Account/Company:** Bank AlJazira
- **Contact Name:** Mark Richmond
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Data Collection
- **Version:** 11.6

## Problem Description
The FSAA Scan was failing to complete due to an internal error related to SSL/TLS certificate validation. The error message indicated that the remote certificate was invalid according to the validation procedure.

## Environment Details
- **Server:** NEA server
- **Error Message:** 
  ```
  System.Net.WebException: The underlying connection was closed: Could not establish trust relationship for the SSL/TLS secure channel. ---> System.Security.Authentication.AuthenticationException: The remote certificate is invalid according to the validation procedure.
  ```

## Troubleshooting Steps
1. Reviewed the error logs to identify the specific error related to SSL/TLS.
2. Attempted to establish a secure connection to the remote server to verify certificate validity.
3. Checked the configuration of the SSL/TLS settings on the NEA server.
4. Upgraded the software to the latest version available.
5. Restarted the NEA server to apply changes and refresh the connection.

## Root Cause
The root cause of the issue was not definitively identified. However, it was related to SSL/TLS certificate validation failures, which may have been resolved through the upgrade and server restart.

## Solution
The issue was resolved by upgrading to the latest version of the software and restarting the NEA server. This action cleared the previous connection issues and allowed the FSAA Scan to complete successfully.

## Notes
- Ensure that SSL/TLS certificates are valid and properly configured to avoid similar issues in the future.
- Regularly update the software to the latest version to benefit from bug fixes and improvements.
- Monitor the server logs for any recurring SSL/TLS errors after upgrades or configuration changes.
```