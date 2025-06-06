## Ticket Metadata
- **Ticket ID:** 500Qk00000DqElpIAF
- **Case Number:** 416742
- **Status:** Closed - Resolved
- **Account/Company:** Hawaii Pacific Health
- **Contact Name:** Amy Caliboso
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Custom Reports
- **Version:** 11.6

## Problem Description
The customer reported that their file system should have permissions for BUILTINAdministrators by default for all shares, folders, and files. They were seeking guidance on how to identify where these permissions were missing, as they believed that an out-of-the-box report did not provide this information.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Product Version:** 11.6

## Troubleshooting Steps
1. Discussed the customer's requirements for identifying missing BUILTINAdministrators permissions.
2. Explored the possibility of creating a report or running a SQL query to gather the necessary information.
3. Suggested using the NAM console for a more immediate response to permission changes.
4. Determined that multiple reports would need to be created to target different types of permission changes for email automation.

## Root Cause
The issue stemmed from the absence of BUILTINAdministrators permissions on certain shares, folders, and files within the customer's file system, which was not being tracked effectively by existing reports.

## Solution
The resolution involved providing guidance on optimal methods to track permission changes and monitor when these changes occurred. The customer was advised to create multiple reports tailored to different change types and utilize the NAM console for real-time monitoring of permission changes.

## Notes
- It is important for future reference to ensure that permissions for BUILTINAdministrators are consistently applied across all shares, folders, and files.
- Customers should be encouraged to utilize the NAM console for immediate insights into permission changes, as it can enhance their monitoring capabilities.