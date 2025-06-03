## Ticket Metadata
- **Ticket ID:** 500Qk00000EkctVIAR
- **Case Number:** 418766
- **Status:** Closed - Resolved
- **Account/Company:** MJB International / Al Masood Gas Turbine
- **Contact Name:** Ojie Dayoc
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** Not specified

## Problem Description
The customer reported an outage with the Netwrix Endpoint Protector (EPP) application, specifically stating that they were suddenly unable to allow permanent USB access to registered EPP clients.

## Environment Details
- The issue occurred after a recent branding change to Netwrix.
- The customer inquired if any settings needed to be updated or if a server rebuild was required.

## Troubleshooting Steps
1. Checked and deployed the latest firmware and updates.
2. Used the suggested installer for the application but encountered failures.
3. Inquired about potential changes required due to the new branding.

## Root Cause
The root cause of the issue was identified as the incorrect device not being allowlisted in the system, which prevented USB access for registered clients.

## Solution
The issue was resolved by adding the correct device to the allowlist, which restored the ability to manage USB access for users effectively.

## Notes
- Ensure that devices are correctly allowlisted to prevent similar issues in the future.
- Monitor for any changes or updates related to branding that may affect settings or configurations.