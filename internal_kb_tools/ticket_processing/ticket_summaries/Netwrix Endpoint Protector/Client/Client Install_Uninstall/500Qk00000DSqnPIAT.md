## Ticket Metadata
- **Ticket ID:** 500Qk00000DSqnPIAT
- **Case Number:** 415852
- **Status:** Closed - Resolved
- **Account/Company:** University of Mississippi Medical Center
- **Contact Name:** Jack S
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** 3.0.2.1007 (updated to 3.0.3.1 for resolution)

## Problem Description
The customer reported that after updating to EPP client version 3.0.2.1007, the Jamf script used to install the EPP client was not setting the server address on Macs. While the client installed successfully, the server address was not configured automatically, which was a change from previous installations.

## Environment Details
- **Script Used:** A Bash script designed to set the EPP server parameters.
- **EPP Server Address:** epp.umc.edu
- **EPP Server Port:** 443
- **EPP Department Code:** defdep

## Troubleshooting Steps
1. Reviewed the existing Jamf script for any discrepancies.
2. Verified that the EPP client was installed correctly on the Mac.
3. Attempted a manual installation of the EPP client version 3.0.2, which successfully set the server address.
4. Checked the script for errors or misconfigurations.
5. Consulted with the development team regarding Jamf configuration support.

## Root Cause
The issue was identified as a compatibility problem with the Jamf script and the EPP client version 3.0.2.1007. The script did not properly set the server address due to changes in the client installation process.

## Solution
The issue was resolved by providing the customer with the latest Jamf IP change script and updating the EPP client to version 3.0.3.1. This combination allowed the server address to be set correctly during the installation process.

## Notes
- It is important to ensure that the latest version of the Jamf script is used in conjunction with the latest EPP client version to avoid similar issues in the future.
- Customers should be advised to consult Jamf support for any configuration-related issues, as Netwrix does not provide direct support for third-party installation tools.