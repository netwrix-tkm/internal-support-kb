## Ticket Metadata
- **Ticket ID:** 500Qk00000DLccIIAT
- **Case Number:** 415570
- **Status:** Closed - Resolved
- **Account/Company:** Emtmeta
- **Contact Name:** Fawad Iaiq
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.9.3.0

## Problem Description
The customer reported an issue where they were unable to successfully apply hotfix #1.1 to their server running version 5.9.3.0. Although the update process indicated success with a 100% completion rate, the update reverted upon checking for updates again.

## Environment Details
- **Server Version:** 5.9.3.0
- **Hotfix Attempted:** #1.1

## Troubleshooting Steps
1. Verified the current server version and confirmed it was running 5.9.3.0.
2. Attempted to apply hotfix #1.1 multiple times, each time receiving a success message.
3. Checked for updates post-application of the hotfix, which indicated that the update was not retained.
4. Reviewed server logs for any errors or warnings during the update process.

## Root Cause
The root cause of the issue was identified as a deployment failure of the hotfix, which did not persist after the update process was completed. This was likely due to a misconfiguration or a compatibility issue with the existing server setup.

## Solution
The issue was resolved by deploying a different hotfix, specifically **adv-2024-002**, which successfully updated the server without reverting. This deployment was confirmed to be compatible with the existing server configuration.

## Notes
- Ensure that the server is compatible with any hotfixes before deployment.
- Always verify the success of an update by checking both the update logs and the server functionality post-update.
- Document any specific configurations or settings that may affect future updates to prevent similar issues.