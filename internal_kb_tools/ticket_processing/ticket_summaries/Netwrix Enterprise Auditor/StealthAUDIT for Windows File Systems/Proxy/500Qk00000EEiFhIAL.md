## Ticket Metadata
- **Ticket ID:** 500Qk00000EEiFhIAL
- **Case Number:** 417711
- **Status:** Closed - Resolved
- **Account/Company:** Hawaii Pacific Health
- **Contact Name:** Steven Schiesl
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Proxy
- **Version:** 11.6

## Problem Description
The customer reported numerous errors from the Data Loss Prevention (DLP) job due to the inability to read filenames containing special characters, particularly those from the Japanese and Hawaiian languages. The DLP scan was unable to recognize certain characters, replacing them with a "?" symbol, which resulted in over 1,000 errors during the latest scan.

## Environment Details
- The issue was observed in a Windows environment using Netwrix Enterprise Auditor with StealthAUDIT for Windows File Systems.
- The filenames included special characters, such as apostrophes and characters from the Hawaiian and Japanese languages.

## Troubleshooting Steps
1. Ran a SEEK Scan job targeting the host displaying the special character errors.
2. Updated the proxy binaries to the latest version (11.6.0.89).
   - Result: The issue persisted.
3. Upgraded proxies to the latest version (11.6).
   - Result: A full scan was successful with 0 errors.

## Root Cause
The issue was caused by outdated proxy versions that did not support the recognition of special characters in filenames.

## Solution
The resolution involved upgrading the proxies to the latest version (11.6) where the issue with special characters in filenames was addressed in a bug fix. After the upgrade, a full scan was conducted successfully without any errors.

## Notes
- Ensure that proxies are kept up to date to avoid similar issues with special character recognition in filenames.
- Future cases involving special characters in filenames should consider checking for proxy version updates as a first troubleshooting step.