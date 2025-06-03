## Ticket Metadata
- **Ticket ID:** 500Qk00000NBgwTIAT
- **Case Number:** 439655
- **Status:** Closed - Resolved
- **Account/Company:** Black Sesame Technologies
- **Contact Name:** Tai Ting Tseng
- **Product:** Netwrix Endpoint Protector
- **Component:** Reports & Analysis / Logs
- **Feature:** Server Upgrade
- **Version:** Not specified

## Problem Description
The customer reported that the Netwrix Endpoint Protector (EPP) incorrectly logs browser downloads as potential uploads. Specifically, the logs show two sets of entries: one for the temporary download file (with a `.crdownload` extension) and another for the completed file, both indicating Chrome as the destination. This behavior creates unnecessary noise in their security monitoring.

## Environment Details
- The issue was observed on Mac and Linux operating systems.
- The customer uses Chrome as the web browser for downloads.

## Troubleshooting Steps
1. The support team requested detailed logs from the customer to understand the scenario better.
2. A remote session was scheduled to review the issue and collect logs if necessary.
3. The customer was provided with steps to generate logs on Mac and Linux systems.
4. The customer attempted to replicate the issue but was unable to do so.
5. The support team suggested enabling the "Use Stealthy DPI Driver" option to improve log accuracy.
6. The customer was informed that the "Use Stealthy DPI Driver" option is only available for Windows systems.

## Root Cause
The root cause of the issue was not definitively identified, but it was suggested that the EPP may log temporary files created during the download process as uploads due to the way the browser interacts with the EPP. The logs may also reflect actions taken by the browser that involve sending file hashes or other information to a server for validation.

## Solution
The issue resolved itself as the customer reported that the incorrect logging behavior did not occur in the days following the support interactions. The support team advised the customer to keep the ticket open until the end of the week to monitor for any recurrence of the issue. If the issue did not reappear, the ticket would be closed.

## Notes
- The customer was advised to collect logs if the issue reoccurred and to provide screenshots of the logs for further investigation.
- The "Use Stealthy DPI Driver" option is not applicable for Mac and Linux environments, which may limit the effectiveness of certain troubleshooting steps.
- The customer was encouraged to reach out for further assistance if the issue reappeared in the future.