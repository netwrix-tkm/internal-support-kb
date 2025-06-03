## Ticket Metadata
- **Ticket ID:** 500Qk00000CXBkCIAX
- **Case Number:** 413652
- **Status:** Closed - Resolved
- **Account/Company:** Vida Health
- **Contact Name:** Amir Elssibony
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client - Other
- **Feature:** EPP Client - Other
- **Version:** Not specified

## Problem Description
The customer reported uncertainty regarding the installation of a hotfix for endpoints related to the security vulnerability identified as CVE-2024-36072. They successfully installed the server patch but needed guidance on patching the endpoints.

## Environment Details
- The customer is using Netwrix Endpoint Protector.
- The inquiry involved endpoint protection clients for both macOS and Windows.

## Troubleshooting Steps
1. Confirmed the installation of the server patch/hotfix.
2. Informed the customer that an Offline Client Patch was being developed by the development team.
3. Provided alternative methods for deploying the EPP clients using Mobile Device Management (MDM) tools, specifically JAMF and Intune.
4. Shared links to deployment guides for JAMF and Intune.
5. Provided download links for the EPP clients containing the fix for both macOS and Windows.
6. Followed up with the customer regarding the availability of a new hotfix and confirmed that the initial clients provided were functioning correctly.

## Root Cause
The issue stemmed from the need for a hotfix for the EPP clients to address the vulnerability CVE-2024-36072. The initial server-side hotfix was resolved by applying a new Hotfix 1.1, which did not affect the functionality of the clients provided earlier.

## Solution
The issue was resolved by:
- Providing the customer with the necessary download links for the updated EPP clients that included the hotfix.
- Advising the customer to replace the current installation files in their MDM with the new client versions.
- Offering to assist with a remote session to apply the hotfix if needed.

## Notes
- Ensure that any future deployments of EPP clients include the latest hotfixes to mitigate vulnerabilities.
- It is advisable to monitor for updates from the development team regarding offline patches and hotfixes for endpoint clients.
- For MDM deployments, confirm that the installation files are updated to prevent distribution of outdated versions.