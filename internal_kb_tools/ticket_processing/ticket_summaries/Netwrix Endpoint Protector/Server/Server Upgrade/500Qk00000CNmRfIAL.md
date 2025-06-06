## Ticket Metadata
- **Ticket ID:** 500Qk00000CNmRfIAL
- **Case Number:** 413293
- **Status:** Closed - Resolved
- **Account/Company:** Capital Power Corporation
- **Contact Name:** Chaitanya Jariwala
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.9.2.0 to 5.9.3.0

## Problem Description
The customer reported an inability to upgrade their server appliance from version 5.9.2.0 to 5.9.3.0, receiving an error message indicating a checksum mismatch during the update process.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Current Version:** 5.9.2.0
- **Target Version:** 5.9.3.0

## Troubleshooting Steps
1. Customer attempted the upgrade and encountered the following error:
   ```
   ERROR: 6 - Applied update returned: "Update Archive checksum does not match the received checksum from Live Update Server"
   ```
2. A remote session was scheduled to investigate the issue further.
3. During the remote session, the following actions were taken:
   - Applied the 5.9.3.0 EPP server patch.
   - Applied a vulnerability patch.
   - Provided the new Windows agent for the vulnerability patch.
4. Verified the logs to ensure they were received correctly after applying the patches.

## Root Cause
The root cause of the issue was identified as a checksum mismatch between the update archive and the checksum received from the Live Update Server. This typically indicates that the update file may have been corrupted or altered during the download process.

## Solution
The issue was resolved by:
- Applying the 5.9.3.0 EPP server patch and the associated vulnerability patch during a remote session.
- Ensuring that the correct Windows agent was deployed for the vulnerability patch.
- Confirming that the logs were received correctly post-application of the patches.

## Notes
- It is important to ensure that the update files are downloaded correctly and that the checksums match before proceeding with an upgrade.
- Future upgrades should be monitored for checksum errors to prevent similar issues.
- The ticket was left open for a few days post-resolution to ensure that no further issues arose.