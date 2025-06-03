## Ticket Metadata
- **Ticket ID:** 500Qk00000HwyurIAB
- **Case Number:** 426184
- **Status:** Closed - Resolved
- **Account/Company:** Esds
- **Contact Name:** ManagedSecurity ManagedSecurity
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** NONE

## Problem Description
The customer reported an issue with the Data Loss Prevention (DLP) agent installed on a laptop. After installation, the laptop was unable to connect to the network because the USB ports were disabled, and the laptop relied on a USB to Ethernet converter. Additionally, attempts to uninstall the DLP agent from the console were unsuccessful as the system appeared offline.

## Environment Details
- The affected device was a laptop using a USB to Ethernet converter for network connectivity.
- The DLP agent was installed but caused USB ports to be disabled.

## Troubleshooting Steps
1. The customer attempted to uninstall the DLP agent from the console but encountered an "offline" status for the system.
2. The customer tried to enforce policy changes through the console, which did not resolve the issue.
3. A remote session was scheduled to assist with the uninstallation process.

## Root Cause
The root cause of the issue was identified as the DLP agent disabling USB ports, which prevented the laptop from using the USB to Ethernet converter for network connectivity. The system's offline status in the console was likely due to the DLP agent's restrictions.

## Solution
The issue was resolved by conducting a remote session where the technical support engineer assisted the customer in uninstalling the DLP agent. This allowed the USB ports to be re-enabled, restoring network connectivity through the USB to Ethernet converter.

## Notes
- Ensure that the DLP agent settings are reviewed before installation to prevent disabling critical hardware interfaces like USB ports.
- For future cases involving uninstallation issues, consider scheduling a remote session early in the troubleshooting process to expedite resolution.
- Always verify the online status of systems in the console before attempting policy enforcement or uninstallation.