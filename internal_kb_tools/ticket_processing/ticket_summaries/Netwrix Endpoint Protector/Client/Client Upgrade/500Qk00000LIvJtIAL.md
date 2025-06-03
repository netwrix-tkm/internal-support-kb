## Ticket Metadata
- **Ticket ID:** 500Qk00000LIvJtIAL
- **Case Number:** 434235
- **Status:** Closed - Resolved
- **Account/Company:** Patrikios Pavlou
- **Contact Name:** Kostas Mousmoulis
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** NONE

## Problem Description
The customer reported an issue where the Agent software upgrade from the Endpoint Protector (EPP) failed on 10 out of 50 machines.

## Environment Details
- The EPP Server IP address was lost from the EPP client, which was not documented, and logs were not enabled for further investigation.

## Troubleshooting Steps
1. The customer attempted to perform the Agent software upgrade on 50 machines, but it failed on 10.
2. The EPPSetServer tool was utilized to address the issue.
3. The customer was advised to release the licenses from the machines that were unable to install the Agent update.

## Root Cause
The root cause of the issue was identified as the loss of the EPP Server IP address from the affected EPP clients. The exact reason for this loss was not determined due to the absence of logs.

## Solution
The issue was resolved by:
1. Releasing the licenses from the 10 machines that were not successfully upgrading.
2. Performing a bulk update, which successfully applied the Agent upgrade to those machines.
3. Re-importing the licenses back to the machines after the upgrade was completed.

## Notes
- Ensure that logs are enabled in future cases to facilitate better troubleshooting and root cause analysis.
- Monitor the EPP Server IP address configuration on clients to prevent similar issues from occurring in the future.