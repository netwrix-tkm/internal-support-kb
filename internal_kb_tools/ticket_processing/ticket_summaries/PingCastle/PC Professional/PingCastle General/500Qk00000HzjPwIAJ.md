## Ticket Metadata
- **Ticket ID:** 500Qk00000HzjPwIAJ
- **Case Number:** 426337
- **Status:** Closed - Resolved
- **Account/Company:** DLA Piper
- **Contact Name:** Mark Cameron
- **Product:** PingCastle
- **Component:** PC Professional
- **Feature:** PingCastle General
- **Version:** 3.2.0.1

## Problem Description
The customer reported issues with upgrading their version of PingCastle to support .NET 8 after removing .NET 6. They encountered errors indicating that the .NET version was incorrect, and they were under pressure to resolve this before .NET 6 reached its end of support on November 12, 2024.

## Environment Details
- **Current .NET Version:** .NET 6 (to be removed)
- **Desired .NET Version:** .NET 8
- **PingCastle Version:** 3.2.0.1

## Troubleshooting Steps
1. Customer attempted to install .NET 8 and remove .NET 6.
2. Customer reported errors in the web console regarding the .NET version.
3. Support representative confirmed that a higher version of .NET was not supported at the time.
4. The case was escalated to R&D for further investigation.

## Root Cause
The issue stemmed from the fact that the current version of PingCastle did not support .NET 8, and the removal of .NET 6 led to compatibility issues with the application.

## Solution
The resolution involved informing the customer that they could upgrade to the new version of PingCastle that supports the .NET 8 Hosting Bundle. The customer was advised to install this new version to resolve the compatibility issues.

## Notes
- It is crucial for customers to verify compatibility with .NET versions before upgrading or removing existing installations.
- As of the date of this case, PingCastle was in the process of updating to support .NET 8, and customers should stay informed about future updates to avoid similar issues.
- Customers should plan upgrades well in advance of end-of-support dates to ensure continued security and functionality.