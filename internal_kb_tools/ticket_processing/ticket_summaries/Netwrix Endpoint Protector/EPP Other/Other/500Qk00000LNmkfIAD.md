## Ticket Metadata
- **Ticket ID:** 500Qk00000LNmkfIAD
- **Case Number:** 434381
- **Status:** Closed - Resolved
- **Account/Company:** Mordor Intelligence Pvt. Ltd.
- **Contact Name:** mohammad.azam Azam
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** NONE

## Problem Description
The customer reported that after successfully installing the Mac Client 3.0.4.1 software, they were unable to open any websites in Google Chrome after launching the Safari browser.

## Environment Details
- **Operating System:** macOS (implied by the mention of Mac Client)
- **Browser:** Safari and Google Chrome

## Troubleshooting Steps
1. Verified the installation of the Mac Client 3.0.4.1 software.
2. Attempted to open websites in Google Chrome after launching Safari.
3. Identified that the DPI certificate had not been applied to the computer.

## Root Cause
The issue was caused by the absence of the DPI certificate on the customer's computer, which is necessary for the proper functioning of the Netwrix Endpoint Protector software.

## Solution
The issue was resolved by applying the DPI certificate to the computer. This action allowed Google Chrome to function correctly and access websites as intended.

## Notes
- Ensure that the DPI certificate is applied during the installation process of the Netwrix Endpoint Protector to prevent similar issues in the future.
- It may be beneficial to include instructions for applying the DPI certificate in the installation documentation for users.