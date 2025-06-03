## Ticket Metadata
- **Ticket ID:** 500Qk00000GKLezIAH
- **Case Number:** 422274
- **Status:** Closed - Resolved
- **Account/Company:** Shield Force
- **Contact Name:** Jose Luis Vera Garcia
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** 6.2.3.1

## Problem Description
The customer reported an issue while attempting to update the Netwrix Endpoint Protector agent from version 5.8.4.1 to version 6.2.3.1. During the creation of an update job, some online computers appeared in grey and could not be selected for the upgrade.

## Environment Details
- **Previous Version:** 5.8.4.1
- **Target Version:** 6.2.3.1

## Troubleshooting Steps
1. Verified the online status of the computers that appeared in grey.
2. Checked the configuration settings for the update job.
3. Attempted to refresh the agent status on the affected computers.
4. Reviewed existing upgrade jobs to identify any conflicts.

## Root Cause
The issue was caused by the presence of old upgrade jobs that were still active, which prevented the selection of certain computers for the new upgrade job.

## Solution
The problem was resolved by removing the old upgrade jobs that were conflicting with the new update process. Once these jobs were cleared, the affected computers became selectable for the upgrade.

## Notes
- Ensure to regularly clean up old upgrade jobs to prevent similar issues in future updates.
- It may be beneficial to document the status of upgrade jobs before initiating a new upgrade process to avoid conflicts.