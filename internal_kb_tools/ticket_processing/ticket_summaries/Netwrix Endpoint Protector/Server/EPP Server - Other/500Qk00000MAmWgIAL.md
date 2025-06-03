## Ticket Metadata
- **Ticket ID:** 500Qk00000MAmWgIAL
- **Case Number:** 436670
- **Status:** Closed - Resolved
- **Account/Company:** Level One Robotics and Controls, Inc.
- **Contact Name:** Gurpal Nagra
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 5.9.3.0

## Problem Description
The customer reported an issue where they were unable to access the user interface of the Netwrix Endpoint Protector, receiving a "this site can't be reached" error. This problem was intermittent, affecting some computers on the same network while others could access the dashboard without issues.

## Environment Details
- The current version of the Endpoint Protector was 5.9.3.0.
- The issue was reported across multiple computers within the same network.

## Troubleshooting Steps
1. Confirmed the error message encountered by the user.
2. Suggested the user ping the EPP server from the affected computers to check connectivity.
3. Recommended updating the EPP server to version 5.9.4.0.
4. Advised creating a VM snapshot before performing the update to ensure a rollback point in case of issues.
5. Monitored the situation as the issue was intermittent, with reports of it working on some days and not on others.

## Root Cause
The root cause of the issue was not explicitly identified, but it was suggested that the intermittent connectivity issues could be related to network configurations or server load, as the EPP server was accessible from some computers but not others.

## Solution
The issue was resolved by updating the EPP server from version 5.9.3.0 to 5.9.4.0. This update likely addressed underlying bugs or performance issues that were causing the intermittent access problems.

## Notes
- It is important to ensure that the EPP server is regularly updated to the latest version to avoid similar issues in the future.
- If the issue recurs, it may be beneficial to check for any conflicting services on the same IP address or network configuration issues.
- Always create a VM snapshot before performing updates to safeguard against potential issues during the update process.