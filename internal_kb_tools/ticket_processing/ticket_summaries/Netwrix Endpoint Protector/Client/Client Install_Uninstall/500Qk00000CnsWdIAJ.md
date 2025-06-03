## Ticket Metadata
- **Ticket ID:** 500Qk00000CnsWdIAJ
- **Case Number:** 414368
- **Status:** Closed - Resolved
- **Account/Company:** Lincoln Savings Bank
- **Contact Name:** Nick Suender
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** 5.8.4.1, 6.0.1.60000, 6.2.2.1006, 5.6.31, 5.8.25

## Problem Description
The customer reported difficulties in uninstalling Netwrix Endpoint Protector clients from their machines after their support contract ended. They were unable to successfully uninstall all clients using the console and sought a method to automate the uninstallation process via PowerShell, similar to their existing practices with other software using InTune.

## Environment Details
- The customer has multiple versions of the Endpoint Protector client installed:
  - 5.8.4.1
  - 6.0.1.60000
  - 6.2.2.1006
  - 5.6.31
  - 5.8.25

## Troubleshooting Steps
1. The customer attempted to use the console for uninstallation but faced inconsistent success.
2. The support engineer provided a silent uninstall script in the form of a .vbs file, which could be executed via command line or an MDM.
3. The customer was advised to enter an uninstall protection password if applicable and to reboot machines after executing the uninstall command.

## Root Cause
The issue stemmed from the customer's inability to use the provided uninstall script effectively, as they created their own script instead of utilizing the official one provided by support.

## Solution
The issue was resolved when the customer was guided to use the official silent uninstall script provided by the support engineer. The script was designed to be run via command line or through an MDM solution, which aligned with their existing deployment practices. The customer confirmed successful uninstallation after following the provided instructions.

## Notes
- It is crucial for customers to utilize the official uninstall scripts provided by support to avoid complications.
- If an uninstall protection password is in place, it must be correctly entered in the script before execution.
- Rebooting the machines after the uninstall command is recommended to ensure complete removal of the client software.