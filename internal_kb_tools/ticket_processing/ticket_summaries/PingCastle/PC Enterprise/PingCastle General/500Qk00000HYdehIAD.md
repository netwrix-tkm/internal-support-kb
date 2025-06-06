## Ticket Metadata
- **Ticket ID:** 500Qk00000HYdehIAD
- **Case Number:** 425208
- **Status:** Closed - Resolved
- **Account/Company:** Suez SA
- **Contact Name:** Thibault Chatiron
- **Product:** PingCastle
- **Component:** PC Enterprise
- **Feature:** PingCastle General
- **Version:** 3.2.0.1

## Problem Description
The customer reported an error with the PingCastle API, specifically receiving a `(405) Method Not Allowed` error when attempting to delete a user via the API. The script had been functioning correctly for several months prior to this issue.

## Environment Details
- **API Endpoint:** `https://serverping.domain.local/api/Agent/Login`
- **Script Language:** PowerShell
- **Authentication Method:** API key

## Troubleshooting Steps
1. Reviewed the script provided by the customer to identify potential issues.
2. Confirmed that the API endpoint was correct and accessible.
3. Investigated the server logs for any related error messages.
4. Identified that the error occurred when trying to delete a user while an active session was present in the database.
5. Noted that the UI method for deleting users was functioning correctly, indicating the issue was isolated to the API.

## Root Cause
The root cause of the issue was identified as a bug in the API related to user deletion. Specifically, if any session was open (even after closing the browser), the session remained in the database for a period, preventing the deletion of the user and any associated permissions granted to Azure AD.

## Solution
The issue was resolved in the latest release of PingCastle (version 3.2.0.1). The development team implemented a hotfix to address the bug affecting the API's user deletion functionality. Customers were advised to use the UI for user deletions while awaiting the hotfix.

## Notes
- It is important to monitor for any similar issues in future API interactions, particularly concerning session management.
- Users should be informed that using the UI is a viable workaround until the API is fully functional.
- Ensure that customers are updated promptly about any hotfixes or patches that address critical bugs in the API.