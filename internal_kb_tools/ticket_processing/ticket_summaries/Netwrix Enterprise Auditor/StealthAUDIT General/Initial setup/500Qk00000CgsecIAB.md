## Ticket Metadata
- **Ticket ID:** 500Qk00000CgsecIAB
- **Case Number:** 414130
- **Status:** Closed - Resolved
- **Account/Company:** ANZ
- **Contact Name:** Geethika Alakam
- **Product:** Netwrix Enterprise Auditor
- **Component:** File System Action Module
- **Feature:** Initial setup
- **Version:** 11.0

## Problem Description
The customer reported an issue with the File System Action Module where moving files containing Unicode characters (specifically Chinese characters) resulted in the characters being replaced with "?" in the output. This alteration rendered the file paths invalid for further processing in subsequent jobs.

## Environment Details
- **Current Version:** 11.0.0.250
- **Language Settings:** English (United States) with English (Australia) also added.

## Troubleshooting Steps
1. Initial inquiry about whether files were being moved to another server or within the same server.
2. Verification of whether the issue had occurred previously with Chinese characters.
3. Confirmation that the issue was reproducible in a lab environment by Professional Services.
4. Request for the build number of the StealthAUDIT version being used.
5. Execution of a PowerShell script to check the installed versions of relevant applications on the StealthAUDIT console server.

## Root Cause
The issue was identified as a bug in the version 11.0 of the StealthAUDIT software, which did not handle Unicode characters correctly during file operations.

## Solution
The problem was resolved in version 11.5.0.221 of the software. However, the customer indicated they were not ready to update to this version at the time of the resolution.

## Notes
- It is important to encourage customers to keep their software updated to benefit from bug fixes and enhancements.
- Future cases involving Unicode character handling should reference the resolution in version 11.5.0.221 and recommend an upgrade if similar issues arise.