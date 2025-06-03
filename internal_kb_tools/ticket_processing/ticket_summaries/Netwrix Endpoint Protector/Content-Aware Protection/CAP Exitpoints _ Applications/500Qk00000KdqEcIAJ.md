## Ticket Metadata
- **Ticket ID:** 500Qk00000KdqEcIAJ
- **Case Number:** 432222
- **Status:** Closed - Resolved
- **Account/Company:** Government (Malta)
- **Contact Name:** Glenn Bilocca
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Exitpoints / Applications
- **Version:** 6.2.4.1

## Problem Description
The customer reported significant slowness when attempting to open hyperlinks within Outlook. Additionally, there were instances where clicking a hyperlink resulted in a different link being opened, which caused confusion and operational issues.

## Environment Details
- The issue was reproducible every time with the latest Windows OS client version 6.2.4.1.
- The affected user was using Outlook to access hyperlinks.
- No third-party security applications were in use.
- The EPP Addin was enabled.

## Troubleshooting Steps
1. Gathered logs, including DPI extended logs and configuration screenshots.
2. Verified that the EPP Addin was enabled.
3. Checked system resources in Task Manager.
4. Attempted to reproduce the issue by accessing hyperlinks from Outlook with DPI enabled.
5. Disabled the policy "IT - report only" for exit points selected for Browsers and Email, and enabled another policy with "block and report" and no exit points selected.
6. Suggested excluding .ost and .pst archive files from scanning.

## Root Cause
The root cause of the slowness was not definitively identified, but it was linked to the scanning of Outlook archive files (.ost and .pst) by the Endpoint Protector, which caused delays in hyperlink access.

## Solution
The issue was resolved by disabling the existing policy that caused the slowness and enabling a new policy that blocked and reported without exit points selected. This change eliminated the performance issues when opening hyperlinks in Outlook.

## Notes
- It is recommended to exclude .ost and .pst files from scanning in future configurations to prevent similar performance issues.
- Monitor for any recurrence of the issue, especially after updates to the Endpoint Protector or Outlook.
- Ensure that the EPP Addin remains enabled for optimal functionality.