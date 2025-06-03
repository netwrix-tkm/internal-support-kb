## Ticket Metadata
- **Ticket ID:** 500Qk00000OOXRdIAP
- **Case Number:** 443007
- **Status:** Closed - Resolved
- **Account/Company:** Renewbuy
- **Contact Name:** Anil Kumar
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device not recognized
- **Version:** 2.4.4.1004

## Problem Description
The customer reported that three Linux servers running Ubuntu 22.04 with the installed EPP version 2.4.4.1004 were not appearing in the Computer list of the Endpoint Protector (EPP) for the past two days. The customer required these devices to be recognized in order to apply necessary policies.

## Environment Details
- **Operating System:** Ubuntu 22.04
- **EPP Version:** 2.4.4.1004

## Troubleshooting Steps
1. The customer was advised to check the `options.sh` configuration file, which is responsible for client-server communication.
2. Instructions were provided to ensure that the installation steps outlined in the README.txt file were followed, including:
   - Ensuring execution rights on `install.sh` (using `chmod`).
   - Confirming that the EPP client was not already installed before running `install.sh`.
   - Setting the correct server IP in the `options.sh` file.
   - Running the installation script as root.
3. The customer was asked to verify the configuration and report back.

## Root Cause
The issue was identified as a misconfiguration in the client-server communication settings, specifically within the `options.sh` file, which prevented the EPP clients from being recognized by the server.

## Solution
The customer successfully resolved the issue by following the provided instructions to correctly install the EPP client on the Linux servers. This included ensuring the correct configuration in the `options.sh` file and executing the installation script with the appropriate permissions.

## Notes
- It is crucial to ensure that the `options.sh` file is correctly configured with the appropriate server IP and that all necessary lines are uncommented as specified in the README.txt file.
- Future installations should strictly follow the installation guidelines to avoid similar issues with client recognition.