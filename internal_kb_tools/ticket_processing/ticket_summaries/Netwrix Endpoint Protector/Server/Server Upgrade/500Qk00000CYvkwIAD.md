## Ticket Metadata
- **Ticket ID:** 500Qk00000CYvkwIAD
- **Case Number:** 413726
- **Status:** Closed - Resolved
- **Account/Company:** CPAS Namur
- **Contact Name:** Nicolas Dupuis
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** Not specified

## Problem Description
The customer reported an issue where the installation of the update "EPP Server Hotfix #1 - Important Security Updates for EPP Server (HWA-EPP4-U8800)" appeared to complete successfully, but the update still showed as available when revisiting the update page.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. The support engineer requested the customer to check under the Live Update menu for the "View applied updates" button to confirm if the hotfix was listed there.
2. The customer confirmed that the hotfix appeared multiple times (seven instances).

## Root Cause
The issue was identified as a display anomaly in the update interface. The update did not disappear from the update page immediately after installation, which led to confusion regarding the successful application of the hotfix.

## Solution
The support engineer explained that the hotfix would not disappear from the update page until the next major server update to version 5.9.4.0 was applied. The customer was informed that the hotfix had been successfully applied, as confirmed by its presence in the "View applied updates" section.

## Notes
- Customers should be aware that certain updates may remain visible in the update interface until subsequent major updates are installed.
- It is recommended to check the "View applied updates" section to confirm successful installations of updates or hotfixes.