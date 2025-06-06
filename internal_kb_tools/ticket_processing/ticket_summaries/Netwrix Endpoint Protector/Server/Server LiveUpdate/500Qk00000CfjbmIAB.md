## Ticket Metadata
- **Ticket ID:** 500Qk00000CfjbmIAB
- **Case Number:** 414095
- **Status:** Closed - Resolved
- **Account/Company:** Aviva Brasil
- **Contact Name:** Giovani Paganini
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server LiveUpdate
- **Version:** Not specified

## Problem Description
The customer reported that the hot fix HWA-EPP4-U8800 failed to apply during installation, resulting in an error message indicating that the installation failed at 65% due to a hash mismatch.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Customer contacted support after encountering the installation error.
2. Support technician Emil Podar scheduled a remote session to address the issue.
3. During the remote session, the erroneous patch was removed.
4. The patch was reapplied to resolve the installation failure.

## Root Cause
The installation failure was caused by a hash mismatch, which indicates that the downloaded patch file was corrupted or altered, preventing successful installation.

## Solution
The issue was resolved by:
- Removing the erroneous patch that failed to install.
- Reapplying the patch correctly during the remote session, which allowed for successful installation.

## Notes
- Ensure that the integrity of patch files is verified before installation to prevent hash mismatch errors.
- In cases of installation failure, consider scheduling a remote session to facilitate troubleshooting and resolution.