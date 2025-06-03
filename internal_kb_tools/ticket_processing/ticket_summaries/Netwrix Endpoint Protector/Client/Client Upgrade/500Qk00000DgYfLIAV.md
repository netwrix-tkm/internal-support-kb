```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000DgYfLIAV
- **Case Number:** 416345
- **Status:** Closed - Resolved
- **Account/Company:** Halodata International Pte Ltd
- **Contact Name:** Denni Prima Putra Roli
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** Not specified

## Problem Description
The customer reported issues with uninstalling and upgrading the EPP client on endpoints with the EPP client installed. The uninstall and upgrade features were not functioning as expected.

## Environment Details
- The issue was observed on endpoints running the EPP client.
- The customer indicated that the user did not have sufficient rights to run the installation package, as noted in the event viewer logs.

## Troubleshooting Steps
1. Verified the customer's report regarding uninstall and upgrade issues.
2. Reviewed event viewer logs which indicated insufficient user rights.
3. Suggested the customer run the installation using an administrator account to check if the issue persisted.
4. Collected logs from the customer, including the epp-upgrade log file and MSIInstaller log.

## Root Cause
The root cause of the issue was identified as insufficient user rights to execute the installation package for the EPP client. The user attempting the installation did not have administrative privileges.

## Solution
The issue was resolved by instructing the customer to perform the installation using an administrator account. This change allowed the installation and upgrade processes to complete successfully.

## Notes
- Ensure that users have the necessary administrative rights when attempting to install or upgrade the EPP client.
- Future troubleshooting should include checking user permissions as a first step when encountering installation issues.
```