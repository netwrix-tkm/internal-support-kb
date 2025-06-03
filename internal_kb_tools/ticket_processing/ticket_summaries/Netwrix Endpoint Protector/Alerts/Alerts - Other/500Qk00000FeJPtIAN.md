## Ticket Metadata
- **Ticket ID:** 500Qk00000FeJPtIAN
- **Case Number:** 420752
- **Status:** Closed - Unable to Resolve
- **Account/Company:** Florida Lottery
- **Contact Name:** Anthony Davis
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts - Other
- **Version:** 5.9.4.0

## Problem Description
The customer inquired about the ability to set up an alert within the Netwrix Endpoint Protector Appliance for changes to file hashes on files located on internal hard drives. They noted that while various alerts could be created, there was no option for file hash modifications. Additionally, they observed that file hashes were only generated for files on removable storage devices, raising the question of whether hashes could also be generated for files on network shares and internal storage.

## Environment Details
- **Netwrix Endpoint Protector Appliance Version:** 5.9.4.0

## Troubleshooting Steps
1. The customer enabled the File Hashes option from the Global Settings.
2. Logs were generated to check for any file hash modifications.
3. Communication was established with the customer to clarify the findings.

## Root Cause
It was determined that there is no available method within the Netwrix Endpoint Protector Appliance to receive alerts when a file's hash is modified. The functionality for monitoring file hashes is limited to removable storage devices only.

## Solution
The issue was resolved by confirming to the customer that the current version of the Netwrix Endpoint Protector Appliance does not support alerts for file hash modifications on internal hard drives or network shares. The customer was informed that this limitation is inherent to the software's design.

## Notes
- Customers should be made aware that the current version does not support alerts for file hash modifications on internal storage or network shares.
- Future updates or versions of the software may include this functionality, so it is advisable to check for updates regularly.