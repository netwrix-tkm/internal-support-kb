## Ticket Metadata
- **Ticket ID:** 500Qk00000JUBSwIAP
- **Case Number:** 429876
- **Status:** Closed - Resolved
- **Account/Company:** Comerica Bank
- **Contact Name:** Edward Portillo
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 5.9.4.1

## Problem Description
After upgrading to version 5.9.4.1, Comerica's QA environment experienced a login loop when attempting to authenticate via Azure Single Sign-On (SSO). The process eventually resulted in an HTTP 502 error, forcing the team to use a failover login user as a temporary workaround.

## Environment Details
- **Error Log:** 
  ```
  2024/12/13 13:18:51 [alert] 23718#23718: *363094 open socket #7 left in connection 226
  2024/12/13 13:18:51 [alert] 23718#23718: aborting
  ```

## Troubleshooting Steps
1. Verified the upgrade process to ensure it completed without errors.
2. Reviewed Nginx error logs for any indications of connection issues.
3. Attempted to replicate the issue in a controlled environment.
4. Checked Azure SSO configuration settings for any discrepancies post-upgrade.
5. Engaged with the development team to investigate potential bugs in the new version.

## Root Cause
The issue was identified as a bug introduced in the new server version (5.9.4.1) that affected the Azure SSO authentication process, leading to the login loop and subsequent HTTP 502 errors.

## Solution
The problem was resolved by deploying a corrected version of the server software that addressed the identified bug. Users were able to authenticate successfully via Azure SSO after the update.

## Notes
- It is recommended to monitor the Azure SSO functionality closely after any future upgrades to ensure similar issues do not arise.
- Always ensure that backup authentication methods (like failover login users) are available during upgrades to mitigate downtime.