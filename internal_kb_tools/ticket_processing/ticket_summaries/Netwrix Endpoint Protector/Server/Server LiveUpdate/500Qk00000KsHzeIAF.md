## Ticket Metadata
- **Ticket ID:** 500Qk00000KsHzeIAF
- **Case Number:** 432936
- **Status:** Closed - Resolved
- **Account/Company:** The Office of Public Works
- **Contact Name:** Anthony Meehan
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server LiveUpdate
- **Version:** 5.9.4.1

## Problem Description
The customer reported that backend security updates were not being applied, and an EPP software update was scheduled but not installed. The update process indicated that it was applying the update, but no changes were actually made.

## Environment Details
- **Product Version:** Netwrix Endpoint Protector 5.9.4.1
- **Platform:** Server

## Troubleshooting Steps
1. Attempted to apply the backend update from the Dashboard using the Live Update feature.
2. Verified the connection to the Ubuntu keyserver to ensure it was reachable.
3. Reviewed logs for any error messages related to the update process.

## Root Cause
The EPP server was unable to reach the Ubuntu keyserver, which prevented the backend updates from being applied successfully.

## Solution
The issue was resolved by manually applying the key for the Ubuntu keyserver. After this, the update command was executed from the user interface, which successfully applied the updates.

## Notes
- Ensure that the EPP server has a stable connection to the Ubuntu keyserver to avoid similar issues in the future.
- Regularly check for connectivity issues that may affect update processes.
- Document any manual steps taken for future reference in case similar issues arise.