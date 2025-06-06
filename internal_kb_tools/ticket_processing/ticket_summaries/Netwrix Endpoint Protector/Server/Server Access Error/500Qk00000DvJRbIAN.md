## Ticket Metadata
- **Ticket ID:** 500Qk00000DvJRbIAN
- **Case Number:** 416935
- **Status:** Closed - Resolved
- **Account/Company:** Banca Comerciala Romana (BCR) Chisinau
- **Contact Name:** Iulian Stan
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** 5930

## Problem Description
The customer reported that the BCR Moldova client console for the Cocosys On-premises server failed to start. Initially, the issue was due to exhausted storage space, which prevented the console from launching. After deleting a snapshot, the disks did not consolidate, and the virtual machine (VM) would not start at all. Although the VM was eventually restarted, the Cocosys console still failed to launch, indicating that some components or services might be missing or not running.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Build Number:** 5930
- **Age of Issue:** 16.7 days

## Troubleshooting Steps
1. Verified the storage space on the server.
2. Deleted a snapshot to free up space.
3. Attempted to restart the virtual machine (VM).
4. Checked for missing services or components related to the Cocosys console.

## Root Cause
The root cause of the issue was the failure to consolidate disks after a snapshot was deleted, which left the VM in a non-operational state. This led to the inability of the Cocosys console to start due to missing components or services.

## Solution
The issue was resolved by performing a clean start of an Endpoint Protection Platform (EPP) image. This action restored the necessary components and allowed the Cocosys console to function correctly.

## Notes
- Ensure that disk consolidation is performed after deleting snapshots to prevent similar issues in the future.
- Regularly monitor storage space to avoid operational disruptions.
- Consider setting up alerts for low storage conditions to proactively manage resources.