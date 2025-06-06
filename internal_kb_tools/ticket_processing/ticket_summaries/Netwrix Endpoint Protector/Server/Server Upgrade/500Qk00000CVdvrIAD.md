## Ticket Metadata
- **Ticket ID:** 500Qk00000CVdvrIAD
- **Case Number:** 413554
- **Status:** Closed - Resolved
- **Account/Company:** PEWO Energietechnik GmbH
- **Contact Name:** Veit Grauert
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.9.4.0

## Problem Description
The customer reported that the installation of the EPP Server Hotfix #1 (HWA-EPP4-U8800_5930) appeared to fail, with the update status incorrectly indicating that it was applied. Despite this, the update continued to be offered for installation, leading to uncertainty about whether the update was actually applied.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server
- **Age of the issue:** 71.1 days

## Troubleshooting Steps
1. Acknowledged the issue and confirmed that the hotfix update was still appearing in the list of "Available EPP Software Updates" even after being applied.
2. Investigated the behavior of the update status post-server reboot.
3. Communicated with the customer to gather additional details and confirm the symptoms.

## Root Cause
The root cause of the issue was identified as a bug in the update management system of the Netwrix Endpoint Protector, which caused the hotfix to incorrectly display as available for installation even after it had been successfully applied.

## Solution
The issue was resolved by deploying Hotfix adv-2024-002, which corrected the update management behavior and ensured that the status of applied updates was accurately reflected in the system.

## Notes
- It is important to monitor the status of updates after installation and reboot to ensure that they are correctly recognized by the system.
- Customers experiencing similar issues should be advised to check for any available hotfixes or updates that address known bugs in the update management system.