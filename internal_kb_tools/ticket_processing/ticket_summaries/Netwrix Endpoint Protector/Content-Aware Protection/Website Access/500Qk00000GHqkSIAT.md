## Ticket Metadata
- **Ticket ID:** 500Qk00000GHqkSIAT
- **Case Number:** 422194
- **Status:** Closed - Resolved
- **Account/Company:** Sound and Vision Studios
- **Contact Name:** Ayaz Ahmad Ansari
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Website Access
- **Version:** NONE

## Problem Description
The customer reported that after updating their server, access to Outlook was blocked, indicating a potential issue with website access permissions.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Build Number:** 5940
- **Age:** 3.7 days

## Troubleshooting Steps
1. Verified the server update logs to identify any changes that could affect website access.
2. Checked the configuration settings of the Netwrix Endpoint Protector for any restrictions on Outlook.
3. Reviewed the Content-Aware Protection settings to ensure that Outlook was not inadvertently blocked.
4. Conducted tests to replicate the issue by attempting to access Outlook from different user accounts.

## Root Cause
The issue was identified as a misconfiguration in the Content-Aware Protection settings following the server update, which inadvertently restricted access to Outlook.

## Solution
The issue was resolved by adjusting the Content-Aware Protection settings to allow access to Outlook. The customer confirmed that the website blocking issue was solved after these changes were implemented.

## Notes
- Ensure to review configuration settings after any server updates to prevent similar issues.
- It may be beneficial to document any changes made during server updates for future reference.