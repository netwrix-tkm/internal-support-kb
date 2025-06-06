## Ticket Metadata
- **Ticket ID:** 500Qk00000LVJjsIAH
- **Case Number:** 434749
- **Status:** Closed - Resolved
- **Account/Company:** AXAXL
- **Contact Name:** Neil Patterson
- **Product:** PingCastle
- **Component:** PC Professional
- **Feature:** PingCastle General
- **Version:** 3.3

## Problem Description
The customer reported an issue where running PingCastle against their Azure tenant resulted in a blank authentication dialog in interactive mode, leading to a failure in authentication.

## Environment Details
- The application utilizes the proxy settings configured in the Internet Settings within the Control Panel.

## Troubleshooting Steps
1. Attempted to authenticate in interactive mode, which resulted in a blank authentication dialog that eventually failed.
2. Tried using command-line mode with the TenantID specified, but this still triggered the interactive mode, leading to the same blank authentication dialog.
3. The command used for troubleshooting was `--azureid --askcredentials`.

## Root Cause
The issue was identified as an incorrect configuration related to the proxy settings used by the application, which were inherited from the Internet Settings in the Control Panel.

## Solution
The resolution involved confirming and editing the proxy settings in the Internet Settings of the Control Panel to ensure proper authentication could occur. Once the settings were adjusted, the authentication process functioned correctly without displaying a blank dialog.

## Notes
- Ensure that proxy settings are correctly configured in the Internet Settings for applications that rely on them for authentication.
- Future users experiencing similar issues should verify their proxy configurations as a first step in troubleshooting authentication problems with PingCastle.