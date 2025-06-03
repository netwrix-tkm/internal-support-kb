## Ticket Metadata
- **Ticket ID:** 500Qk00000KZmCjIAL
- **Case Number:** 431950
- **Status:** Closed - Resolved
- **Account/Company:** CoSoSys Korea
- **Contact Name:** daehee kim
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** EPP Server: 5.9.4.0, EPP Client: 3.0.3.1

## Problem Description
The customer reported an issue with the Content Aware Protection (CAP) policy where compressed files sent via email or ADB were neither being blocked nor logged when the 'Archive Files' option was unchecked. Specifically, formats such as ace, xz, bz2, and xar were not being processed correctly.

## Environment Details
- **Operating System:** macOS (Sequoia 15.1.1)
- **EPP Server Version:** 5.9.4.0
- **EPP Client Version:** 3.0.3.1
- **Policy Configurations:** Various configurations were tested, including different file types and archive formats.

## Troubleshooting Steps
1. Verified the policy configurations related to Content Aware Protection.
2. Tested sending compressed files in various formats (zip, 7z, ace, rar, tar, bz2, gz, xz, xar) containing different file types (png, bmp, gif, ppt, docx).
3. Collected logs from the EPP client on macOS to analyze the behavior of the CAP policy.
4. Engaged with the engineering team to analyze the logs and provide insights on the issue.

## Root Cause
The root cause was identified as a limitation in the EPP client regarding unsupported archive formats. Specifically, formats such as ace, bz2, xz, and xar are not scanned by contents, which means that while the policy can recognize these file types, it cannot block or log them effectively. Supported formats like .zip and .gz can be scanned by contents, allowing for proper logging and blocking.

## Solution
The issue was resolved by clarifying the limitations of the EPP client to the customer. It was explained that:
- Some archive formats (like .zip and .gz) are scanned by contents and can be blocked/logged.
- Unsupported formats (like ace, bz2, xz, xar) are recognized by their MIME type but cannot be scanned for contents, hence they cannot be blocked or logged.
- The customer was advised to adjust their policies accordingly and to use supported formats for effective logging and blocking.

## Notes
- It is important to inform customers about the limitations of the EPP client regarding unsupported archive formats to set proper expectations.
- Ensure that the MIME types are correctly configured in the CAP policy to avoid confusion regarding which file types can be blocked or logged.
- Future testing should focus on supported formats to ensure that the CAP policies function as intended.