## Ticket Metadata
- **Ticket ID:** 500Qk00000BkTrvIAF
- **Case Number:** 411724
- **Status:** Closed - Resolved
- **Account/Company:** Hobby Lobby
- **Contact Name:** Kyle Baldwin
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Access Auditing
- **Version:** 11.6 (recommended for upgrade)

## Problem Description
The customer reported that their FSAA (File System Access Auditing) scan was taking an excessive amount of time to complete, specifically 15 days. They sought recommendations to improve the performance of the scan.

## Environment Details
- The issue was related to the configuration of the FSAA scan settings within the Netwrix Enterprise Auditor platform.
- The scans were initially set to scan an unlimited number of probable owners.

## Troubleshooting Steps
1. Engaged with the customer to understand the current configuration and performance issues.
2. Suggested limiting the number of probable owners scanned from unlimited to a maximum of 4.
3. Discussed the potential benefits of upgrading to version 11.6 and implementing a proxy to further enhance performance.

## Root Cause
The prolonged scan duration was primarily due to the configuration setting that allowed for an unlimited number of probable owners to be scanned, which significantly increased the workload and processing time.

## Solution
- Adjusted the FSAA scan settings to limit the number of probable owners scanned from unlimited to 4, which provided a moderate improvement in scan performance.
- Recommended upgrading to version 11.6 of the Netwrix Enterprise Auditor and setting up a proxy to achieve a more substantial performance boost.

## Notes
- Future users experiencing similar performance issues should consider reviewing and adjusting the probable owners setting in their FSAA configurations.
- Upgrading to the latest version of the software and utilizing proxies can lead to significant improvements in scan performance.
- It is advisable to monitor scan performance after making configuration changes to ensure desired outcomes are achieved.