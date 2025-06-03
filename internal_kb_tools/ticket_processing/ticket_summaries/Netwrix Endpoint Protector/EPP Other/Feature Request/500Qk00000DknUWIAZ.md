## Ticket Metadata
- **Ticket ID:** 500Qk00000DknUWIAZ
- **Case Number:** 416530
- **Status:** Closed - Resolved
- **Account/Company:** Fondo de Empelados para EPM - FEPEP
- **Contact Name:** Sistemas FEPEP
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Feature Request
- **Version:** Not specified

## Problem Description
The customer reported issues with generating a Content Aware report, where the tool would hang and fail to load data for a month or more. Additionally, the customer requested guidance on generating a report that only includes recipients of personal emails.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** EPP Other

## Troubleshooting Steps
1. Conducted a remote session with the customer using Google Translate for communication.
2. Explained how partitions work within the reporting tool.
3. Demonstrated how to filter logs from reports and analysis.
4. Discussed the issue of multiple partitions affecting log visibility for a specified timeframe.
5. Suggested an alternative method to export filtered logs and merge them into a single file for easier analysis.

## Root Cause
The issue stemmed from the way the reporting tool handled data across multiple partitions, which caused the logs not to display correctly for the selected timeframe. The customer was unaware of how partitions affected the reporting process.

## Solution
The issue was resolved by providing the customer with guidance on navigating partitions and exporting logs. The customer was instructed to merge the exported logs to create a comprehensive report. This approach allowed the customer to bypass the limitations of the reporting tool regarding partitioned data.

## Notes
- Customers should be made aware of the partitioning system in the reporting tool to avoid confusion when generating reports for specific timeframes.
- It is advisable to export and merge logs when dealing with multiple partitions to ensure complete data visibility.