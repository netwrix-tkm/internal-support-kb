```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000JdkstIAB
- **Case Number:** 430173
- **Status:** Closed - Resolved
- **Account/Company:** The Cloud Mail Store Inc / Cyberspace Networking Systems
- **Contact Name:** Pankaj Pandit
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** NONE

## Problem Description
The customer reported that while viewing the Content Aware Report, they were only able to see 200 entries and requested guidance on how to extend this limit for viewing and exporting the report.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Reviewed the current configuration settings for the Content Aware Report.
2. Checked for any limitations in the report generation settings that might restrict the number of entries displayed.
3. Inquired if external storage was necessary for retaining the report data for three months.

## Root Cause
The limitation of displaying only 200 entries in the Content Aware Report was due to default settings in the Netwrix Endpoint Protector configuration.

## Solution
To resolve the issue, the following steps were taken:
- Adjusted the configuration settings to increase the limit of entries displayed in the Content Aware Report beyond 200.
- Confirmed that no external storage was required for viewing/exporting the report data for three months, as the system could handle the data retention internally.

## Notes
- It is important to monitor the configuration settings for report generation to ensure that limits are set according to user needs.
- Future users should be aware that increasing the number of entries displayed may impact performance depending on the server's capacity and load.
```