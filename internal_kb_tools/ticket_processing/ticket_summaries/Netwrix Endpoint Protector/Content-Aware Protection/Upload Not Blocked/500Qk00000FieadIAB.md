## Ticket Metadata
- **Ticket ID:** 500Qk00000FieadIAB
- **Case Number:** 420952
- **Status:** Closed - Resolved
- **Account/Company:** CoreWin Distributor
- **Contact Name:** Danylo Didenko
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Upload Not Blocked
- **Version:** NONE

## Problem Description
PrivatBank reported an issue where the Content-Aware Protection (CAP) policy did not block file transfers to the browser on an Ubuntu 22 PC. The investigation revealed that the EPP DPI certificate was not active in the browser after the installation or update of the EPP client.

## Environment Details
- Operating System: Ubuntu 22
- EPP Client: Netwrix Endpoint Protector

## Troubleshooting Steps
1. Verified the absence of an active EPP DPI certificate in the browser.
2. Restarted the browser, which resulted in the valid certificate appearing and successfully blocking file transfers.
3. Discussed the necessity of rebooting the computer after EPP client installation or updates, noting that many users had not rebooted their PCs for an extended period.
4. Explored potential methods to force the upload of the DPI certificate to the browser without requiring a restart of the PC or browser.

## Root Cause
The primary issue was identified as the browser not recognizing the EPP DPI certificate due to it being loaded before the certificate was inserted into the browser's certificate store. The running browser did not reload the certificate store when modified by the EPP client, leading to unmonitored connections and bypassing the DPI.

## Solution
The resolution confirmed that in some cases, a browser restart is necessary for the EPP client to function properly. While no alternative method to force the certificate upload without a restart was identified, it was emphasized that regular reboots are recommended for system updates and optimal EPP performance.

## Notes
- It is crucial to inform users about the importance of rebooting their systems after EPP client updates to ensure proper functionality.
- There are currently no known console commands or methods to refresh the browser's certificate store without restarting the browser.
- Regular maintenance and updates, including system reboots, should be encouraged to prevent similar issues in the future.