## Ticket Metadata
- **Ticket ID:** 500Qk00000JDdBvIAL
- **Case Number:** 429167
- **Status:** Closed - Resolved
- **Account/Company:** Kassenärztliche Vereinigung Nordrhein
- **Contact Name:** Gerrit Beyken
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** NONE

## Problem Description
The customer reported that their Hyper-V administrator was unable to deploy a new VHD image, as it appeared to be compatible only with Hyper-V 2022. They requested an image compatible with Hyper-V 2019.

## Environment Details
- Hyper-V 2019 Cluster
- The new VHD image was initially designed for Hyper-V 2022.

## Troubleshooting Steps
1. Confirmed the compatibility of the provided VHD image with Hyper-V 2019.
2. Engaged the Hyper-V administrator to verify the deployment error.
3. Attempted to provide a compatible VHD image for Hyper-V 2019.
4. Escalated the issue to the DevOps team for further investigation.
5. The Hyper-V administrator tested importing the image on a Hyper-V 2022 test system.

## Root Cause
The original VHD image was specifically designed for Hyper-V 2022, which led to compatibility issues when attempting to deploy it on Hyper-V 2019 systems.

## Solution
The issue was resolved by having the Hyper-V administrator export the VM from the Hyper-V 2022 test system after successfully importing the image there. This exported VM image was then used to set up the new EPP server VM on the Hyper-V 2019 cluster.

## Notes
- Ensure that any new VHD images are explicitly stated to be compatible with the intended Hyper-V version before deployment.
- Future requests for images should clarify the required Hyper-V version to avoid similar compatibility issues.