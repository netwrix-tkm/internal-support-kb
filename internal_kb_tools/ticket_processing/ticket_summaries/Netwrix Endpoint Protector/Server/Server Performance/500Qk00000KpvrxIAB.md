## Ticket Metadata
- **Ticket ID:** 500Qk00000KpvrxIAB
- **Case Number:** 432822
- **Status:** Closed - Resolved
- **Account/Company:** Dubai Police
- **Contact Name:** Fakhra Abdulla
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Performance
- **Version:** 9.3

## Problem Description
The customer reported that they were not receiving logs for large user files in the Netwrix Endpoint Protector. They required logging for all user files, but the system was failing to capture logs for files exceeding a certain size.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Identified the issue of missing logs for large user files.
2. Reviewed the shadow file size settings within the Netwrix Endpoint Protector.
3. Proposed increasing the shadow file size to accommodate larger files.
4. Planned to retest the logging functionality after adjusting the settings.

## Root Cause
The root cause of the issue was determined to be the insufficient size of the shadow file, which was unable to handle the logging of larger user files.

## Solution
The issue was resolved by increasing the shadow file size within the Netwrix Endpoint Protector settings. After making this adjustment, the customer was able to successfully receive logs for all user files, including those that were previously too large to log.

## Notes
- Ensure that shadow file size settings are appropriately configured to handle the expected file sizes in future implementations.
- Regularly monitor logging functionality after any configuration changes to confirm that all necessary data is being captured.