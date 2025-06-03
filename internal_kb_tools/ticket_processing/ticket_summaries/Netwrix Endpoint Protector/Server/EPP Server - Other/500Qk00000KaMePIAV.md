## Ticket Metadata
- **Ticket ID:** 500Qk00000KaMePIAV
- **Case Number:** 431979
- **Status:** Closed - Resolved
- **Account/Company:** Klarna
- **Contact Name:** Deepti Singh
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 5940

## Problem Description
The customer, Deepti Singh, reported an inability to access the EPP (Endpoint Protector) portal, requesting assistance to investigate the issue.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Build Number:** 5940

## Troubleshooting Steps
1. Reviewed the configuration files related to the EPP portal.
2. Checked for any missing or incorrect settings that could affect SSL connectivity.
3. Identified that a specific configuration file was missing critical lines pertaining to SSL settings.

## Root Cause
The issue was caused by a missing configuration in the SSL settings within the relevant config file, which prevented access to the EPP portal.

## Solution
The missing lines regarding SSL were added back into the configuration file. After making these adjustments, access to the EPP portal was successfully restored.

## Notes
- Ensure that all configuration files are regularly backed up to prevent similar issues in the future.
- It is advisable to review SSL settings after any updates or changes to the system to avoid access issues.