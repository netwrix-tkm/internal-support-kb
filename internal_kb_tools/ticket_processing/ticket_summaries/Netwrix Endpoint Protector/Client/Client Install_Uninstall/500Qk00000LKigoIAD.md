## Ticket Metadata
- **Ticket ID:** 500Qk00000LKigoIAD
- **Case Number:** 434353
- **Status:** Closed - Resolved
- **Account/Company:** Blue Halo
- **Contact Name:** Justin Yackoski
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** Not specified

## Problem Description
The customer reported an issue with installing Netwrix Endpoint Protector on macOS. Although the installation was successful, the configuration could not be applied, and the system failed to connect to the server.

## Environment Details
- The customer used a different installation script than the recommended JAMF scripts for deploying the agents.

## Troubleshooting Steps
1. Customer followed all documentation for installing Endpoint Protector on macOS.
2. A troubleshooting call was requested to resolve the connection issue.
3. It was identified that the customer used an incorrect script for installation.
4. Correct installation scripts were provided to the customer.
5. The customer was advised to mass re-deploy the agents to check if they could connect to the EPP server.

## Root Cause
The issue was caused by the use of an incorrect installation script that did not align with the JAMF scripts recommended for deploying the agents.

## Solution
The problem was resolved after the customer re-deployed the agents using the correct installation scripts provided by support. The customer confirmed that the deployment was successful, and the agents were able to connect to the EPP server.

## Notes
- Ensure that customers are using the correct installation scripts, especially when deploying agents via JAMF or similar tools.
- It may be beneficial to verify the installation process and scripts before proceeding with troubleshooting to avoid unnecessary delays.