```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000DgapCIAR
- **Case Number:** 416344
- **Status:** Closed - Resolved
- **Account/Company:** SHW AG
- **Contact Name:** Christian Kopf
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** N/A

## Problem Description
The customer reported that after successfully installing the Security Update – EPP Server Hotfix #1.1 three times, the update still appeared in the available EPP Software Updates list.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Verified the installation status of the EPP Server Hotfix #1.1.
2. Checked the update logs to confirm successful installations.
3. Restarted the EPP Server to refresh the update status.
4. Cleared the cache of the update manager to ensure it reflects the latest updates.
5. Re-attempted the installation of the hotfix multiple times.

## Root Cause
The issue was identified as a caching problem within the update manager, which continued to display the hotfix as available even after successful installations.

## Solution
The issue was resolved by clearing the cache of the update manager, which allowed it to recognize that the hotfix had already been installed. After clearing the cache, the hotfix no longer appeared in the available updates list.

## Notes
- Ensure to clear the update manager's cache after installing updates to prevent similar issues in the future.
- Regularly check for any pending updates after installations to confirm their status.
```