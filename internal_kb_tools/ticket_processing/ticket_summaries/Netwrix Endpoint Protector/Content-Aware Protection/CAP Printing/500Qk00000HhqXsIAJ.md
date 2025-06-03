## Ticket Metadata
- **Ticket ID:** 500Qk00000HhqXsIAJ
- **Case Number:** 425626
- **Status:** Closed - Resolved
- **Account/Company:** CoreWin Distributor
- **Contact Name:** Danylo Didenko
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Printing
- **Version:** 7.0

## Problem Description
The customer, PrivatBank, reported an issue with the Content-Aware Protection (CAP) policy where printing of confidential files was successfully blocked when accessed directly from the C: drive. However, when the same files were opened in a web browser (e.g., Google Docs), the print job was not blocked, leading to potential data leakage.

## Environment Details
- The issue was specifically related to the CAP feature for blocking print jobs from browsers.
- The customer was testing the print blocking capabilities of the Endpoint Protector.

## Troubleshooting Steps
1. Confirmed the settings for blocking print from browsers were enabled in the Device Control menu under Global Settings.
2. Advised the customer to enable the Advanced printers option and restart the endpoint.
3. Provided documentation on the CAP browser extension for Chrome and Edge.
4. Clarified that the CAP feature is currently only available for Windows and does not support Linux or MacOS.

## Root Cause
The root cause of the issue was identified as a limitation in the CAP feature, which only supports blocking print jobs from browsers on Windows systems using the dedicated browser extension for Chrome and Edge. Other browsers and operating systems (Linux and MacOS) do not have this capability.

## Solution
The issue was resolved by confirming that the customer needed to install the CAP browser extension for Chrome or Edge to enable print blocking from those browsers. Once the extension was installed and configured correctly, the print jobs from the browser were successfully blocked.

## Notes
- The print blocking feature is currently limited to Windows environments and does not extend to Linux or MacOS. 
- A feature request can be submitted for future support of print blocking in other operating systems.
- Ensure that users are aware of the need to install the browser extension for the CAP feature to function as intended.