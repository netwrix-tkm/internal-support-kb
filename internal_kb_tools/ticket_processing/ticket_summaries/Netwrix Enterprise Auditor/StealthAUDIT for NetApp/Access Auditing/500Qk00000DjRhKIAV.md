## Ticket Metadata
- **Ticket ID:** 500Qk00000DjRhKIAV
- **Case Number:** 416449
- **Status:** Closed - Resolved
- **Account/Company:** City National Bank (CNB)
- **Contact Name:** Kim Holmes
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for NetApp
- **Feature:** Access Auditing
- **Version:** 11.5

## Problem Description
The customer reported that file system scans have errored out for five consecutive weeks, with error messages occurring on different folders each week. The customer requested assistance in resolving these errors.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Feature:** Access Auditing
- **Collector Code:** StealthAUDIT for NetApp
- **Product Version:** 11.5

## Troubleshooting Steps
1. Reviewed the error messages attached by the customer from the previous scans.
2. Analyzed the configuration settings related to timeout minutes for the scans.
3. Investigated the folder names to identify any potential issues with length or characters.
4. Communicated with the customer to gather additional context regarding recent changes in folder naming conventions.

## Root Cause
The errors were primarily caused by:
- **RPC Timeout:** The timeout settings for the scans were not configured appropriately, leading to timeouts during the scanning process.
- **Folder Name Length:** A new contractor included a hash in the folder names, which resulted in excessively long folder names that exceeded system limits.

## Solution
To resolve the issue, the following actions were taken:
1. Adjusted the timeout settings for the file system scans to allow for longer processing times.
2. Instructed the customer to rename the affected folders to remove the hash and reduce the overall length of the folder names, ensuring they comply with system limitations.

## Notes
- It is important to monitor folder naming conventions and ensure they do not exceed character limits to prevent similar issues in the future.
- Regularly review and adjust timeout settings based on the size and complexity of the file system being scanned to avoid RPC timeouts.