## Ticket Metadata
- **Ticket ID:** 500Qk00000EkkflIAB
- **Case Number:** 418773
- **Status:** Closed - Resolved
- **Account/Company:** ServiceNow
- **Contact Name:** Swaroop Tiyyagura
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** 6.2.2.2005

## Problem Description
The customer reported that the installation of the Netwrix Endpoint Protector client version 6.2.2.2005 caused corruption of several hard drives, rendering devices unusable. The issue was particularly severe, with some devices' C: drive filesystems changing to RAW format, and the Windows Recovery Environment becoming corrupted.

## Environment Details
- The issue occurred after a server update that pushed the new client update to the machines.
- The problem was not reproduced on most of the customer's Windows machines, which were up to date.

## Troubleshooting Steps
1. Investigated the installation process and found that if the previous installation media was not cached in the Windows installer directory, the uninstall of the previous version would fail.
2. Attempted to reproduce the issue on a test machine.
3. Discussed the possibility of using the ZAP tool to completely remove the old EPP Client before installing the new version.
4. Engaged in multiple communications with the customer to schedule remote sessions for testing.

## Root Cause
The root cause of the issue was identified as the failure to cache the previous installation media in the Windows installer directory. This failure led to the unsuccessful uninstallation of the previous version, which in turn caused the installation of the new client to corrupt the device.

## Solution
The issue was resolved by using an agent from a different version (5941) that successfully installed without causing corruption. It was recommended to ensure that the previous installation media is cached before attempting to uninstall the old client.

## Notes
- It is crucial to ensure that the previous installation media is cached in the Windows installer directory before uninstalling any previous versions of the client.
- The issue was only reported on one machine in the customer's environment, and testing on virtual machines did not replicate the problem.
- Future installations should consider using the ZAP tool to remove old clients completely to prevent similar issues.