## Ticket Metadata
- **Ticket ID:** 500Qk00000KshkSIAR
- **Case Number:** 432985
- **Status:** Closed - Resolved
- **Account/Company:** BMTS Technology GmbH & Co. KG
- **Contact Name:** Novak Vucetic
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server LiveUpdate
- **Version:** 5.9.4.1

## Problem Description
The customer reported an issue with the Live Update feature on their server located in China. They encountered a known error message: "An error occurred. Hash does not match." The customer requested an offline patch for version 5.9.4.1 to resolve this issue.

## Environment Details
- **Server Location:** China
- **Affected Version:** 5.9.4.1
- **Error Message:** "An error occurred. Hash does not match."

## Troubleshooting Steps
1. Customer attempted to upgrade the server via Live Update, which resulted in the error.
2. Customer requested an offline patch to bypass the Live Update issue.
3. Support team investigated the backend for potential fixes related to the error.

## Root Cause
The root cause of the issue was identified as a mismatch in the hash during the Live Update process, which is a known problem with the version 5.9.4.1.

## Solution
The support team resolved the issue by removing the error from the backend, allowing the server to function correctly without the need for the Live Update.

## Notes
- It is important to note that this issue is known to occur with version 5.9.4.1, and customers may need to request offline patches if they encounter similar hash mismatch errors during Live Updates.
- Future users experiencing similar issues should consider checking for backend fixes or patches before attempting standard upgrade procedures.