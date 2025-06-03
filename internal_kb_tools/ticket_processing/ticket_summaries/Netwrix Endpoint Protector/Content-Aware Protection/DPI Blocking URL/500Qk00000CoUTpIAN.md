## Ticket Metadata
- **Ticket ID:** 500Qk00000CoUTpIAN
- **Case Number:** 414387
- **Status:** Closed - Resolved
- **Account/Company:** Lyten Inc
- **Contact Name:** Canan Abumaali
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** DPI Blocking URL
- **Version:** Not specified

## Problem Description
The customer reported that users on Macs were experiencing certificate errors when attempting to connect to webpages after a URL restriction policy was applied to their machines. This issue was isolated to Mac devices.

## Environment Details
- The issue occurred specifically on Mac devices.
- The deployment of the agent was managed through Jamf, an MDM tool.

## Troubleshooting Steps
1. Initial inquiry to determine if the agent was installed manually or via MDM.
2. Requested confirmation on whether the certificate was added to the keychain and set to "allow all" trust.
3. Provided a guide for setting up the certificate through Jamf.
4. Followed up to ensure the customer had access to the necessary certificate and installation instructions.

## Root Cause
The root cause of the issue was identified as the absence of the required certificate in the Mac keychain, which was necessary for the URL restriction policy to function correctly without generating certificate errors.

## Solution
The issue was resolved by guiding the customer to:
- Locate the required certificate as detailed in the provided setup guide.
- Push the certificate to all Macs using the Jamf MDM tool, ensuring it was added to the keychain with the trust setting configured to "allow all."

## Notes
- Ensure that any future deployments of the Netwrix Endpoint Protector agent on Mac devices include the necessary certificate installation steps to prevent similar issues.
- Always verify the trust settings for certificates when applying URL restrictions or similar policies on Mac systems.