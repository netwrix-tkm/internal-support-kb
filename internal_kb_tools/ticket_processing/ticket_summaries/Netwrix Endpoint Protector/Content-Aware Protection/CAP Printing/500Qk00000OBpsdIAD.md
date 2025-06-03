## Ticket Metadata
- **Ticket ID:** 500Qk00000OBpsdIAD
- **Case Number:** 442513
- **Status:** Closed - Resolved
- **Account/Company:** Raiffeisen Bank Kosovo J.S.C.
- **Contact Name:** Fuad Shaqiri
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Printing
- **Version:** 5.2

## Problem Description
The customer reported an issue with the Device Control module where they were unable to see events for printed files. The file tracing feature did not yield any results, and they requested guidance on how to resolve this issue.

## Environment Details
- The issue was related to the MTP Advanced Scanning and Printing feature within the Global Settings of the Netwrix Endpoint Protector.

## Troubleshooting Steps
1. Advised the customer to check if the MTP Advanced Scanning and Printing feature was enabled under Global Settings.
2. Instructed the customer to activate the feature if it was not enabled, save the changes, and restart the PC to apply the changes.

## Root Cause
The root cause of the issue was that the MTP Advanced Scanning and Printing feature was not enabled in the Global Settings, which is necessary for the file tracing functionality to work properly.

## Solution
The issue was resolved after the customer enabled the MTP Advanced Scanning and Printing feature under Global Settings. Following this, they restarted the target computer, which allowed the file tracing events to appear as expected.

## Notes
- It is important to ensure that the MTP Advanced Scanning and Printing feature is enabled for the file tracing functionality to work.
- Always advise customers to restart the target computer after making changes to the Global Settings to ensure that the changes take effect.
- For future reference, if customers inquire about exporting data to third-party tools, inform them about the SIEM integration section available in the UI for sending Syslog type logs to external services.