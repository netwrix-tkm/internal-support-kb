## Ticket Metadata
- **Ticket ID:** 500Qk00000DQADxIAP
- **Case Number:** 415704
- **Status:** Closed - Resolved
- **Account/Company:** The Stars Group Interactive Services / Flutter International
- **Contact Name:** Crecan Andrei
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** Not specified

## Problem Description
The customer reported that the Endpoint Protection Platform (EPP) was not applying Content-Aware Protection (CAP) policies on their machine after a restart, allowing the transfer of sensitive information despite the system being active and targeted with a block policy.

## Environment Details
- The system was confirmed to be active and connected to the server.
- The machine was configured with a block policy for sensitive information transfer.

## Troubleshooting Steps
1. The customer performed several system reboots.
2. Policy updates were attempted without success.
3. The issue was escalated to support for further investigation.

## Root Cause
The issue was identified as being related to the Intercept VPN Traffic setting, which was not enabled, preventing the CAP policies from being applied correctly.

## Solution
The issue was resolved during a remote support session by enabling the Intercept VPN Traffic setting. This allowed the CAP policies to be applied effectively, restoring the intended functionality of the EPP.

## Notes
- Ensure that the Intercept VPN Traffic setting is enabled in environments where CAP policies are expected to function.
- Regularly verify policy application after system updates or reboots to prevent similar issues.