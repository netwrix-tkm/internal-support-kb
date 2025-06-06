## Ticket Metadata
- **Ticket ID:** 500Qk00000CPnugIAD
- **Case Number:** 413370
- **Status:** Closed - Resolved
- **Account/Company:** OneSpan Canada, Inc.
- **Contact Name:** Anthony Nafarrete
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server LiveUpdate
- **Version:** NONE

## Problem Description
The customer reported that after installing the latest hotfix (HWA-EPP4-U8800) multiple times, the hotfix notification continued to appear in the application.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server
- **Age of the Issue:** 18.9 days

## Troubleshooting Steps
1. The customer was advised to refresh the browser page to check if the notification persisted.
2. The customer confirmed that the notification still appeared after refreshing the browser.
3. The customer attempted to install the hotfix three times without success.
4. A remote connection was offered to assist in resolving the issue.

## Root Cause
The issue was identified as a persistent notification bug that did not clear after the installation of the hotfix. The specific cause was not detailed, but it was related to the application not recognizing the successful installation of the hotfix.

## Solution
The issue was resolved by deploying a new hotfix (adv-2024-002) which addressed the notification problem. This deployment successfully cleared the persistent notification for the customer.

## Notes
- It is important to ensure that the application is fully updated after installing hotfixes.
- If notifications persist after multiple installations, consider deploying a subsequent hotfix or patch.
- Always verify the installation status of hotfixes and patches in the application settings to prevent confusion.