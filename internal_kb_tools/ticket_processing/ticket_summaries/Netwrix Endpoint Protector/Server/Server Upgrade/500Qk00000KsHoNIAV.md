## Ticket Metadata
- **Ticket ID:** 500Qk00000KsHoNIAV
- **Case Number:** 432964
- **Status:** Closed - Resolved
- **Account/Company:** Governikus KG
- **Contact Name:** Felix Dahms
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.9.4.1

## Problem Description
The customer reported that backend updates were not installing on their system running version 5.9.4.1. When attempting to apply the updates, the system displayed a message indicating that the process may take a few minutes, but the updates were never completed.

## Environment Details
- The /boot partition had 72% used space, which may have contributed to the issue.

## Troubleshooting Steps
1. Attempted to apply backend updates multiple times without success.
2. Inquired about the availability of logs to check for error messages related to the update process.
3. Connected to the server backend to perform a manual installation of the updates.

## Root Cause
The root cause of the issue was not definitively identified; however, the high usage of the /boot partition may have impacted the update process.

## Solution
The issue was resolved by connecting to the backend server and performing a manual installation of the backend updates, which completed successfully.

## Notes
- It is advisable to monitor the usage of the /boot partition to prevent similar issues in the future.
- Ensure that sufficient space is available on critical partitions before attempting updates to avoid installation failures.