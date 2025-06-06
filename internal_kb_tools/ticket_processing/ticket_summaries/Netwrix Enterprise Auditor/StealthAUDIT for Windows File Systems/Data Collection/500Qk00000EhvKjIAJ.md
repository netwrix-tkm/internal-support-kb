## Ticket Metadata
- **Ticket ID:** 500Qk00000EhvKjIAJ
- **Case Number:** 418650
- **Status:** Closed - Resolved
- **Account/Company:** State of Delaware
- **Contact Name:** Kevin Graber
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Data Collection
- **Version:** NEA v11.6.0.98

## Problem Description
The customer reported that duplicate entries were displayed within the FSAA_Gates table, with matching Share, Folder, and Policy IDs on the same host.

## Environment Details
- The issue occurred within the Netwrix Enterprise Auditor environment, specifically using the StealthAUDIT for Windows File Systems component.

## Troubleshooting Steps
1. The support team coordinated with the customer to schedule an upgrade of the NEA and NAM applications.
2. The case was temporarily postponed until a suitable time for the upgrade could be arranged.
3. The customer was advised to upgrade to NEA version 11.6.0.98 or run the 0-CreateSchema job after the upgrade.

## Root Cause
The root cause of the duplicate entries in the FSAA_Gates table was not definitively identified during the investigation.

## Solution
The issue was resolved by upgrading the Netwrix Enterprise Auditor to version 11.6.0.98. Alternatively, running the 0-CreateSchema job after the upgrade also appeared to correct the duplicate gate entries.

## Notes
- It is recommended to monitor the FSAA_Gates table after upgrades to ensure that duplicate entries do not reoccur.
- Future cases involving similar symptoms should consider upgrading to the latest version of the Netwrix Enterprise Auditor as a potential solution.