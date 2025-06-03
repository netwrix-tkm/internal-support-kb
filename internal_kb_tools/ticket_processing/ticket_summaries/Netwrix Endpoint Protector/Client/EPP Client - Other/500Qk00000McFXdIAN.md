## Ticket Metadata
- **Ticket ID:** 500Qk00000McFXdIAN
- **Case Number:** 437882
- **Status:** Closed - Resolved
- **Account/Company:** VicCnS Co.,Ltd.
- **Contact Name:** Kwang-jae Shin
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** 5.8.2.5

## Problem Description
The customer reported that after installing the EPP client on their server, the Server IP and Port settings were displayed as “Not set,” preventing normal communication.

## Environment Details
- The customer operates in an airgapped environment, which restricts remote support capabilities.
- The server and client versions were updated to 5941 and 6241, respectively, but the issue persisted.

## Troubleshooting Steps
1. Customer provided debug logs and screenshots for analysis.
2. Technical support requested additional logs using the EPPSupportTool:
   - Download and unzip the support tool.
   - Execute log creation for both the client and DPI.
   - Update policies on the EPP client.
   - Export the generated log files for further investigation.
3. Customer attempted to collect the requested logs but was unable to do so.
4. After several attempts, the customer installed EPP client version 5.8.2.5.

## Root Cause
The root cause of the issue was not explicitly identified in the logs or communications. However, it was determined that the version of the EPP client initially installed may have had compatibility issues or bugs that were resolved in version 5.8.2.5.

## Solution
The issue was resolved by installing the EPP client version 5.8.2.5, which restored normal communication functionality. The customer confirmed that after the installation, the Server IP and Port settings were correctly configured.

## Notes
- Ensure that clients are updated to the latest stable version to avoid similar issues in the future.
- When dealing with airgapped environments, consider alternative methods for log collection and troubleshooting, as remote support may not be feasible.