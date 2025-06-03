```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000HDIrlIAH
- **Case Number:** 424426
- **Status:** Closed - Resolved
- **Account/Company:** Children's Medical Center of Dallas - Auditor
- **Contact Name:** William Lau
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** Not specified

## Problem Description
The customer reported a discrepancy between the devices displayed in the EPP client UI and those visible on the EPP server. Specifically, when filtering by computer name in Device Control -> Devices, the lists did not match, showing missing and extra devices in both displays.

## Environment Details
- The issue was observed on multiple endpoints using the Netwrix Endpoint Protector software.

## Troubleshooting Steps
1. Reviewed the logs provided by the customer to identify discrepancies.
2. Scheduled a remote session to apply troubleshooting steps from R&D.
3. Deleted all device_type_ids from the affected endpoints during the remote session.
4. Installed a test build of the EPP client on a few test computers to assess if it resolved the issue.
5. Monitored the endpoints for any duplicate device entries after the installation of the test build.

## Root Cause
The root cause of the issue was identified as a mismatch in device type IDs between the EPP client and server, leading to duplicate entries being displayed in the client UI.

## Solution
The issue was resolved by:
- Deleting all device_type_ids from the affected endpoints, which cleared the discrepancies.
- Installing a test build of the EPP client that included fixes for the device display issues.
- Monitoring the endpoints to ensure that no duplicate devices reappeared after the changes.

## Notes
- It is important to monitor the endpoints after making changes to device type IDs to ensure that duplicates do not reappear.
- Future installations of test builds should be conducted on a limited number of endpoints first to evaluate their impact before wider deployment.
- Ensure that logs are generated and reviewed during troubleshooting to provide insights into any further discrepancies.
```