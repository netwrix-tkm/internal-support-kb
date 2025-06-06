## Ticket Metadata
- **Ticket ID:** 500Qk00000JMsBjIAL
- **Case Number:** 429535
- **Status:** Closed - Resolved
- **Account/Company:** Euroclear SA/NV
- **Contact Name:** Thomas Bozzini
- **Product:** PingCastle
- **Component:** PC Enterprise
- **Feature:** PingCastle General
- **Version:** 3.3

## Problem Description
The customer, Thomas Bozzini, reported an error encountered during the installation of PingCastle Enterprise. The error message indicated that the installer had encountered an unexpected error, with the specific error code being 26201.

## Environment Details
- **Product Version:** 3.3
- **Platform:** PingCastle

## Troubleshooting Steps
1. Reviewed the error message and code (26201) for potential causes.
2. Checked user permissions related to the database engine used for the installation.
3. Confirmed that the installation package was not corrupted or incomplete.
4. Attempted to run the installer with elevated privileges.

## Root Cause
The issue was identified as a lack of sufficient rights for the user account that was used to perform the installation on the database engine.

## Solution
The problem was resolved by ensuring that the user account had the necessary permissions to install the software on the database engine. Once the permissions were granted, the installation proceeded successfully without any further errors.

## Notes
- Ensure that users performing installations have the appropriate rights and permissions to avoid similar issues in the future.
- It may be beneficial to document the required permissions for installation in the product documentation for future reference.