## Ticket Metadata
- **Ticket ID:** 500Qk00000GIpkPIAT
- **Case Number:** 422236
- **Status:** Closed - Resolved
- **Account/Company:** ZS
- **Contact Name:** Harshvardhan Mithapelli
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client/OS Performance
- **Version:** Not specified

## Problem Description
The user reported an issue accessing certain tabs within the Rancher Desktop application on a Mac system. Despite enabling Intercept VPN, the user was unable to access these tabs. The issue was temporarily resolved when the Endpoint Protector (EPP) was disabled.

## Environment Details
- **Operating System:** Mac
- **Application:** Rancher Desktop
- **VPN:** Intercept VPN enabled

## Troubleshooting Steps
1. Verified the user's ability to access the Rancher application with EPP disabled.
2. Collected logs while recreating the issue for further analysis.
3. Suggested potential workarounds based on similar issues encountered with other users.

## Root Cause
The issue was identified as being related to the Rancher application itself rather than the Endpoint Protector (EPP). It was determined that the application required a reset to function correctly.

## Solution
The user resolved the issue by performing a factory reset of the Rancher application settings and restarting the application. This action restored access to the previously inaccessible tabs.

## Notes
- It is important to consider application-specific issues when troubleshooting connectivity problems, especially when security software is involved.
- Future users experiencing similar issues with the Rancher application should be advised to reset the application settings as a first troubleshooting step.