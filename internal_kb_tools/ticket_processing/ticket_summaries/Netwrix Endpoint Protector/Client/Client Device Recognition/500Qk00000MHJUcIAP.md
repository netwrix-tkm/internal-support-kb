## Ticket Metadata
- **Ticket ID:** 500Qk00000MHJUcIAP
- **Case Number:** 436897
- **Status:** Closed - Resolved
- **Account/Company:** Taurus Advisory GmbH
- **Contact Name:** Dirk Findeisen
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Device Recognition
- **Version:** NONE

## Problem Description
The client computer was completely blocked by the Endpoint Protector (EPP) client software, which restricted all external access methods, including LAN, WLAN, USB, and Internet access. The removal of the EPP client software was not possible due to blocked communication methods, and an Offline Temporary Password generated at the server did not resolve the issue.

## Environment Details
- The EPP client disabled the Wi-Fi adapter and Ethernet LAN access via a docking station.
- USB storage devices were also blocked.
- The EPP client was greyed out in Control Panel and Settings, preventing uninstallation.

## Troubleshooting Steps
1. Confirmed that the EPP client was blocking all external access methods.
2. Attempted to uninstall the EPP client through Control Panel and Settings, but it was greyed out.
3. Generated an Offline Temporary Password at the server, which was accepted by the EPP client but did not lift the restrictions.
4. Identified a mismatch between the user name and user ID/email in the EPP client.

## Root Cause
The issue was caused by the EPP client software enforcing strict access controls that were not lifted even after the acceptance of the Offline Temporary Password. Additionally, a mismatch in user credentials contributed to the inability to manage the EPP client effectively.

## Solution
A VB script file was provided to the customer, which needed to be executed via Command Line Interface (CLI) with administrator rights. This script successfully removed the EPP client software, restoring normal functionality to the computer.

## Notes
- Ensure that any future installations of the EPP client are properly configured to avoid access issues.
- Be aware of potential user credential mismatches that may complicate troubleshooting and resolution.
- Always have a backup method for client removal in cases where standard uninstallation methods fail.