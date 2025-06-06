## Ticket Metadata
- **Ticket ID:** 500Qk00000CgsmgIAB
- **Case Number:** 414125
- **Status:** Closed - Resolved
- **Account/Company:** 9amHealth
- **Contact Name:** Bernhard Schandl
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** HWA-EPP4-U8800

## Problem Description
The customer reported an issue while attempting to apply the current security upgrade (HWA-EPP4-U8800) for the Netwrix Endpoint Protector. The upgrade process failed with the error message: "An error occurred. Hash does not match."

## Environment Details
- Platform: Netwrix Endpoint Protector
- Collector Code: Server

## Troubleshooting Steps
1. Scheduled a remote session to investigate the issue further.
2. Attempted to delete the erroneous patch that was causing the upgrade failure.
3. Suggested applying the upgrade using an offline patch instead.
4. Instructed the customer to reboot the server from the Appliance -> Server Maintenance menu.
5. Requested screenshots of the installation progress bar after rebooting for further analysis.
6. Escalated the issue to the DevOps team for additional support.

## Root Cause
The root cause of the issue was identified as a failed patch that was not properly removed from the system, which led to a mismatch in the hash during the upgrade process.

## Solution
The issue was resolved by:
- Removing the failed progress bar from the backend of the system.
- Confirming with the DevOps team that the server was successfully patched.
- The customer was asked to verify that the progress bar had disappeared after the backend changes were made.

## Notes
- Ensure that any failed patches are completely removed before attempting to apply new upgrades to avoid hash mismatch errors.
- It is advisable to use offline patches when encountering issues with online upgrades to mitigate similar problems in the future.