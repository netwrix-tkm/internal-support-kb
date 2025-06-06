## Ticket Metadata
- **Ticket ID:** 500Qk00000EPazWIAT
- **Case Number:** 418066
- **Status:** Closed - Resolved
- **Account/Company:** USAA
- **Contact Name:** Justin Snyder
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.5

## Problem Description
The customer inquired whether a scan of a file system, when executed with the "import partial results" option checked, would resume from where it left off if the scan was either partially completed or cancelled, without executing the bulk import job.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT General
- **Product Version:** 11.5

## Troubleshooting Steps
1. Reviewed the customer's configuration settings for the file system scan.
2. Confirmed the functionality of the "import partial results" option.
3. Provided guidance on the "Restart incomplete scans" option in the scan settings.

## Root Cause
The issue stemmed from a lack of clarity regarding the functionality of the scanning options in the Netwrix Enterprise Auditor, specifically how the system handles incomplete or cancelled scans.

## Solution
The issue was resolved by confirming to the customer that the scan would indeed resume from where it stopped, provided that the "Restart incomplete scans" option was checked in the File System scan settings. This ensures that any partial or cancelled scans can be continued in subsequent scan jobs.

## Notes
- It is important for users to check the "Restart incomplete scans" option to ensure that scans can resume properly.
- Both FSAA and SEEK can be configured to resume a scan if cancelled, as detailed in the Netwrix help center documentation.