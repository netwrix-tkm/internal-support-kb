## Ticket Metadata
- **Ticket ID:** 500Qk00000NVrsRIAT
- **Case Number:** 440453
- **Status:** Closed - Resolved
- **Account/Company:** Kassenärztliche Vereinigung Rheinland Pfalz (RLP)
- **Contact Name:** Markus Grill
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 3.0

## Problem Description
The customer reported an update error indicating that database partitions were disabled, preventing further upgrades on their Endpoint Protector appliance.

## Environment Details
- The issue occurred on an older Endpoint Protector appliance.
- The customer had accumulated old patches that were consuming significant disk space.

## Troubleshooting Steps
1. Initiated a remote session with the customer to investigate the issue.
2. Requested the customer to prepare a snapshot of their Endpoint Protector appliance from the virtualization environment (VMWare, HyperV, AWS, Azure, GoogleCloud) as a safety measure.
3. Removed old patches from the appliance, freeing up approximately 20GB of disk space.
4. Installed a patch that activated the previously disabled database partitions.
5. Followed up with the customer to confirm if the updates were successful after the changes.

## Root Cause
The root cause of the issue was the presence of disabled database partitions on the older Endpoint Protector appliance, which prevented the installation of necessary updates.

## Solution
The issue was resolved by:
- Removing old patches that were taking up disk space.
- Installing a patch that enabled the database partitions, allowing the customer to proceed with the server upgrade.

## Notes
- It is crucial to ensure that sufficient disk space is available before attempting upgrades on the Endpoint Protector appliance.
- Always recommend customers to take a snapshot of their appliance prior to making significant changes to ensure a quick recovery if needed.
- Follow up with customers after resolving issues to confirm that the solution was effective and that no further problems have arisen.