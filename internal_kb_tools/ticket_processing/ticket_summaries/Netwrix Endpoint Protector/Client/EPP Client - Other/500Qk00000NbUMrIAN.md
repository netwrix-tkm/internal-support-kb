## Ticket Metadata
- **Ticket ID:** 500Qk00000NbUMrIAN
- **Case Number:** 440710
- **Status:** Closed - Resolved
- **Account/Company:** WTEX Fintech Private Limited (KreditPe)
- **Contact Name:** Sujith Nair
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** Not specified

## Problem Description
Users were experiencing frequent certificate errors on macOS when attempting to connect to the server named jetbrains.com. The error indicated that the certificate was not trusted, despite it being signed by CoSoSys.

## Environment Details
- **Operating System:** macOS
- **Server Name:** jetbrains.com
- **Certificate Authority:** CoSoSys

## Troubleshooting Steps
1. Identified the certificate error reported by users.
2. Confirmed that the certificate was signed by CoSoSys but was not recognized as trusted on macOS devices.
3. Suggested regenerating the certificate and importing it again on the affected devices to ensure they received the latest version.
4. Provided instructions for the regeneration and import process.

## Root Cause
The root cause of the issue was identified as the certificate not being recognized as trusted on macOS devices. This was likely due to an outdated or improperly configured certificate on the client devices.

## Solution
The issue was resolved by regenerating the certificate and importing it again on the affected devices. This ensured that all devices had the latest certificate and that it was set to trusted, eliminating the certificate error.

## Notes
- Ensure that certificates are regularly updated and properly configured on all client devices to prevent similar issues in the future.
- It is advisable to verify the trust settings for certificates on macOS devices after any updates or changes to the certificate.