## Ticket Metadata
- **Ticket ID:** 500Qk00000FYeyTIAT
- **Case Number:** 420509
- **Status:** Closed - Resolved
- **Account/Company:** BMTS Technology GmbH & Co. KG
- **Contact Name:** Novak Vucetic
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server LiveUpdate
- **Version:** 5.9.4.0

## Problem Description
The customer requested a link to download an offline patch update for version 5.9.4.0, as their server in China encountered an error during installation stating, "An error occurred. Hash does not match."

## Environment Details
- **Location:** China
- **Server Type:** Netwrix Endpoint Protector

## Troubleshooting Steps
1. Verified the version of the software installed on the server.
2. Attempted to download the offline patch update from the provided link.
3. Checked the integrity of the downloaded patch file to ensure it was not corrupted.
4. Conducted a remote session to further investigate the installation error.

## Root Cause
The issue was identified as a mismatch in the hash value of the downloaded patch file, which indicated that the file may have been corrupted during the download process or was not the correct version.

## Solution
The issue was resolved during a remote session by:
- Providing the correct link for the offline patch update.
- Ensuring the customer downloaded the patch file again, verifying its integrity before installation.
- Guiding the customer through the installation process to confirm successful application of the patch.

## Notes
- Ensure that customers in regions with unstable internet connections are advised to use offline patch updates to avoid similar issues.
- Recommend verifying the hash of downloaded files when installation errors occur to prevent future complications.