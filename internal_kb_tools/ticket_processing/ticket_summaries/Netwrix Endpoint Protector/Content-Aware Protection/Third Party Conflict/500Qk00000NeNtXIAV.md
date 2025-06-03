## Ticket Metadata
- **Ticket ID:** 500Qk00000NeNtXIAV
- **Case Number:** 440862
- **Status:** Closed - Resolved
- **Account/Company:** CoreWin Distributor
- **Contact Name:** CoreWin Tech
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Third Party Conflict
- **Version:** NONE

## Problem Description
PrivatBank reported that the CiscoVPN (Cisco Secure Client) was disabling every 10-30 minutes when the Endpoint Protection Platform (EPP) client was installed, leading to intermittent Internet access issues. The problem was isolated to a single Windows endpoint.

## Environment Details
- **Customer:** PrivatBank
- **Affected Software:** Cisco Secure Client
- **EPP Client:** Installed on the affected endpoint

## Troubleshooting Steps
1. Reviewed logs and identified errors related to the Cisco Secure Client:
   - `ERROR wow64 helper returned error: 87 for pid: 3112`
   - `ERROR hooking failed 0x00000057 - 3112`
2. Suggested disabling the "Advanced Printer and MTP Scanning" option to see if it resolved the issue.
3. Confirmed with the customer if the issue persisted after disabling the advanced scanning option.
4. Proposed adding the CiscoVPN process name to the scanning exception if disabling the advanced scanning resolved the issue.

## Root Cause
The issue was identified as a conflict between the EPP client’s advanced scanning features and the Cisco Secure Client, which caused the VPN to disable intermittently.

## Solution
The issue was resolved by:
- Disabling the "Advanced Scanning" option in the EPP client.
- Adding the CiscoVPN (Cisco Secure Client) process name to the advanced scanning exception list to prevent future conflicts.

## Notes
- It is recommended to monitor the performance of the Cisco Secure Client after making these changes to ensure stability.
- If the "Advanced Printer and MTP Scanning" option needs to be enabled in the future, ensure that the CiscoVPN process remains in the exception list to avoid similar issues.