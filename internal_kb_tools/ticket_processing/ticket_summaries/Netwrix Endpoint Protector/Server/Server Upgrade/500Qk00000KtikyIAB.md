## Ticket Metadata
- **Ticket ID:** 500Qk00000KtikyIAB
- **Case Number:** 433056
- **Status:** Closed - Resolved
- **Account/Company:** Capital Power Corporation
- **Contact Name:** Chaitanya Jariwala
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5941

## Problem Description
The customer reported that the appliance update was failing again this month, indicating a recurring issue with the update process.

## Environment Details
- The server version in MySQL matched the server version.
- The upgrade log was empty.
- Telnet to `upgrade.endpointprotector` was successful.

## Troubleshooting Steps
1. Verified that the server version in MySQL was the same as the server version.
2. Checked the upgrade log, which was found to be empty.
3. Successfully performed a telnet test to `upgrade.endpointprotector`.
4. Attempted to remove an erroneous patch, but the upgrade was still unsuccessful.
5. Noted that the progress bar did not disappear even after removing the `.json` file.
6. Collected upgrade logs from the server for further analysis.
7. Opened an escalation to R&D for additional assistance.
8. Scheduled a remote session to apply the offline patch.

## Root Cause
The root cause of the issue was identified as a failure in the live update process, which returned an error message indicating that the "Update Archive checksum does not match the received checksum from Live Update Server." This was likely due to network issues or firewall settings blocking the necessary traffic.

## Solution
The issue was resolved during a remote session by applying the offline patch for version 5941. This allowed the upgrade to complete successfully.

## Notes
- It is important to check firewall settings to ensure that HTTP (port 80) and HTTPS (port 443) traffic is not being blocked, as this can prevent successful live updates.
- The customer is considering migrating to a new instance, which may help avoid similar issues in the future.
- Ensure to monitor for any recurring issues with updates, as this was not the first occurrence for the customer.