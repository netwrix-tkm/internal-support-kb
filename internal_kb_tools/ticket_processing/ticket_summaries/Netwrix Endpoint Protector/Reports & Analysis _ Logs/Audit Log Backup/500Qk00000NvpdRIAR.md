## Ticket Metadata
- **Ticket ID:** 500Qk00000NvpdRIAR
- **Case Number:** 441689
- **Status:** Closed - Resolved
- **Account/Company:** Callzilla
- **Contact Name:** Daniel Florez
- **Product:** Netwrix Endpoint Protector
- **Component:** Reports & Analysis / Logs
- **Feature:** Audit Log Backup
- **Version:** Not specified

## Problem Description
The customer inquired about how to check the duration for which logs are retained on the server and whether it is possible to customize the types of logs that the Netwrix Endpoint Protector (EPP) saves, specifically expressing a desire to stop collecting device logs.

## Environment Details
- The customer is using Netwrix Endpoint Protector.
- The inquiry was related to log retention and management.

## Troubleshooting Steps
1. Advised the customer to access the Reports and Analysis section to view the logs stored on the server.
2. Explained how to enable the Audit Log Backup feature to manage log retention.
3. Clarified that customization of log types to be saved is not possible.
4. Provided detailed steps to configure the Audit Log Backup for retaining logs for one year.

## Root Cause
The issue stemmed from a lack of clarity regarding the log retention policies and the capabilities of the Netwrix Endpoint Protector regarding log management.

## Solution
The issue was resolved by guiding the customer through the process of enabling the Audit Log Backup feature. The steps included:
- Navigating to **System Maintenance** -> **Audit Log Backup**.
- Configuring the backup settings to retain logs for one year.
- Ensuring that the option to keep backed-up logs was not selected to allow for the removal of older logs from the database.

## Notes
- It is important to inform customers that while they can configure log retention, they cannot selectively save specific types of logs.
- For compliance purposes (e.g., PCI), customers should be advised to regularly review their log retention settings to ensure they meet their organizational requirements.