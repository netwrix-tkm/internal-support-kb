## Ticket Metadata
- **Ticket ID:** 500Qk00000DSCegIAH
- **Case Number:** 415825
- **Status:** Closed - Resolved
- **Account/Company:** Albany International
- **Contact Name:** Justin Packard
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Performance
- **Version:** Not specified

## Problem Description
The customer reported slow response times when attempting to pull an Excel/CSV report of USB storage devices. The system would only export the number of items visible in the current view (e.g., 50/100/500), and selecting "Show All" resulted in the web browser indicating that the page was not responding.

## Environment Details
- The customer is using Azure for their deployment.
- The Azure admin confirmed that there were no resource issues on their end.
- The customer inquired about updates to the Azure deployment information, specifically regarding the Azure VM agent.

## Troubleshooting Steps
1. Confirmed the issue with the report generation process.
2. Verified that the system only exports the visible items in the report.
3. Checked for any resource issues on the Azure side, which were reported as normal.
4. Engaged with the customer to gather more details about their environment and any recent changes.
5. Provided the customer with a link to the deployment guide for Azure VM agent installation.

## Root Cause
The root cause of the issue was not explicitly identified in the case. However, it was suggested that the slow response and failure to export all items may be related to the system's handling of large datasets and potential limitations in the current deployment configuration.

## Solution
The issue was resolved by providing the customer with information on how to properly configure their Azure deployment, including the installation of the Azure VM agent. This allowed for better resource management and insight into the VM's performance, which may have alleviated the slow response times.

## Notes
- It is recommended to regularly check for updates to the Azure VM agent and ensure that the deployment is optimized for handling large datasets.
- Customers experiencing similar issues should be advised to monitor their resource usage and consider breaking down large reports into smaller segments if performance issues persist.