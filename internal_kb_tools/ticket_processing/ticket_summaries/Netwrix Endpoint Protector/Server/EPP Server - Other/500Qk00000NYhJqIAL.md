## Ticket Metadata
- **Ticket ID:** 500Qk00000NYhJqIAL
- **Case Number:** 440587
- **Status:** Closed - Resolved
- **Account/Company:** Oyster Bay Systems
- **Contact Name:** Andrew Temple
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 2.0

## Problem Description
The customer reported that they were unable to install available backend updates on their virtual appliance despite multiple attempts. They confirmed that the machine had sufficient space and internet access.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Type:** Virtual Appliance

## Troubleshooting Steps
1. Customer verified sufficient disk space on the virtual appliance.
2. Customer confirmed internet access was functional.
3. Support inquired about logs to diagnose the update installation failure.
4. Support identified that backend updates could not be applied from the user interface (UI).
5. A remote session was scheduled to apply the updates directly from the server's backend.

## Root Cause
The inability to install backend updates was due to a limitation in the user interface, which does not support applying these updates directly.

## Solution
During the scheduled remote session, the support technician accessed the server's backend and successfully applied all pending backend updates.

## Notes
- Future users should be aware that backend updates cannot be applied through the UI and will require backend access for installation.
- It is advisable to check for sufficient resources and connectivity before attempting updates, as these factors can affect installation success.