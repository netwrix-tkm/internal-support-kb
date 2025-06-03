## Ticket Metadata
- **Ticket ID:** 500Qk00000OqbTvIAJ
- **Case Number:** 444220
- **Status:** Closed - Resolved
- **Account/Company:** CoreWin Distributor
- **Contact Name:** CoreWin Tech
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** Not specified

## Problem Description
The PrivatBank customer reported that after enabling debug logging, the `eppclient.log` file was found to be empty upon download. Attempts to recreate the issue were unsuccessful.

## Environment Details
- The issue occurred on a system running Netwrix Endpoint Protector.
- The customer had enabled debug logging for troubleshooting purposes.

## Troubleshooting Steps
1. Requested additional details and a screenshot from the customer.
2. Investigated the scenario internally.
3. Involved Tier 2 support for further analysis.
4. Analyzed the contents of the C drive and identified the presence of `eppclient_append.log`, which retains logs across service restarts.
5. Recommended disabling debug mode and removing any `epp.log` files from the C drive.
6. Suggested rebooting the system and re-enabling debug mode to check if `eppclient.log` would populate.

## Root Cause
The `eppclient.log` file was empty because it is designed to clear its contents upon service restart. The `eppclient_append.log` file, which retains logs, was present but not utilized by the customer.

## Solution
The issue was resolved by following these steps:
1. Disable debug mode.
2. Remove any existing `epp.log` files from the C drive.
3. Reboot the system.
4. Re-enable debug mode.
5. Verify if the `eppclient.log` file populates with logs after these changes.

## Notes
- If logs are needed during troubleshooting, the `eppclient_append.log` file can be used as it retains log data.
- It is advisable to ensure that debug logging is managed properly to avoid confusion with log file contents in the future.