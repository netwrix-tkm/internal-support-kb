## Ticket Metadata
- **Ticket ID:** 500Qk00000CvVszIAF
- **Case Number:** 414719
- **Status:** Closed - Resolved
- **Account/Company:** Tech Elecon Pvt. Ltd. (Elecon Engineering Group)
- **Contact Name:** Mohit Shastri
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Upload Not Blocked
- **Version:** EPP server version: 5.9.3.0, EPP client version: 6.2.2.1

## Problem Description
The customer reported that files were not being blocked when uploaded to Microsoft Teams (both web and application versions), while uploads via WeTransfer were being blocked.

## Environment Details
- EPP server version: 5.9.3.0
- EPP client version: 6.2.2.1
- The issue occurred in a corporate environment using Microsoft Teams for file sharing.

## Troubleshooting Steps
1. Confirmed EPP server and client versions.
2. Checked the Deep Packet Inspection (DPI) settings under Content Aware Protection to ensure it was enabled for Microsoft Teams.
3. Updated policies and tested file uploads again.
4. Collected logs using the EPPSupportTool to analyze the issue further.
5. Suggested testing with different file types to identify if the issue was specific to certain formats.
6. Recommended reinstalling the EPP client to see if the issue persisted.
7. Conducted a remote session to further investigate the issue.

## Root Cause
The root cause was identified as a misconfiguration in the DPI settings for Microsoft Teams, which allowed certain file types to bypass the blocking mechanism. Additionally, the logs indicated that `LsPush.exe` was exempt from scanning, which contributed to the issue.

## Solution
To resolve the issue:
- A DPI allowlist was created, and exceptions were set for the files being sent through Microsoft Teams.
- The DPI settings were verified and adjusted to ensure proper scanning of uploads.
- The customer was advised to test the uploads again after the changes were made.

## Notes
- Ensure that the DPI settings are correctly configured for all applications where file uploads are expected to be monitored.
- Regularly review and update the allowlist to prevent unauthorized file transfers.
- Consider conducting periodic audits of the Endpoint Protector settings to ensure compliance with security policies.