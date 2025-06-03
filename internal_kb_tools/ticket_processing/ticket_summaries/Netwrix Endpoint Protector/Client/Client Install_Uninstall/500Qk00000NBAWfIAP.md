## Ticket Metadata
- **Ticket ID:** 500Qk00000NBAWfIAP
- **Case Number:** 439613
- **Status:** Closed - Resolved
- **Account/Company:** RoundRobin Tech Services
- **Contact Name:** Nayan Rajore
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** NONE

## Problem Description
The customer attempted to deploy the EPP agent on Mac devices using a central deployment tool but encountered issues where the server IP was not visible in the EPP client. They were unable to uninstall the EPP client from the laptops due to an error message indicating that uninstallation was not permitted.

## Environment Details
- **Platform:** Mac Devices
- **Deployment Method:** Central deployment tool

## Troubleshooting Steps
1. Customer attempted to uninstall the EPP client directly from the laptop but received an error message.
2. Customer reached out for instructions on how to uninstall the EPP client.
3. Support provided the `remove-epp` file for uninstallation.
4. Customer inquired if the uninstaller would work without server communication.
5. Support confirmed that the uninstaller could be executed without server connection.
6. Customer asked for clarification on how to execute the `remove-epp` file (terminal vs. autorun).
7. Support clarified that the `remove-epp` file needed to be executed via the terminal.

## Root Cause
The issue arose from a failed deployment of the EPP agent, which resulted in the client being unable to communicate with the server. This communication failure prevented the standard uninstallation process from completing successfully.

## Solution
The issue was resolved by executing the `remove-epp` file through the terminal on the affected Mac devices. The customer successfully uninstalled the EPP client after following the provided instructions.

## Notes
- Ensure that the `remove-epp` file is available for customers who may need to uninstall the EPP client without server communication.
- Always confirm the method of execution (terminal vs. autorun) when providing instructions for uninstallation to avoid confusion.
- Document any similar issues and resolutions for future reference to streamline support processes.