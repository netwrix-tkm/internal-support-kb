## Ticket Metadata
- **Ticket ID:** 500Qk00000MLpkRIAT
- **Case Number:** 437173
- **Status:** Closed - Resolved
- **Account/Company:** AconSeg
- **Contact Name:** Mariano Amigo
- **Product:** Netwrix Endpoint Protector
- **Component:** Active Directory Sync
- **Feature:** AD Sync Error
- **Version:** Not specified

## Problem Description
The customer reported issues with implementing a local network Microsoft Active Directory for administrative users, which was intended to enable single sign-on functionality. An error message was encountered during the setup process.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Feature Involved:** Active Directory Sync

## Troubleshooting Steps
1. Reviewed the error message provided by the customer (attached picture).
2. Made configuration changes to the Active Directory settings.
3. Attempted to reconnect and sync the Active Directory with the Netwrix Endpoint Protector.
4. Tested the login functionality for administrative users to verify successful integration.

## Root Cause
The specific root cause of the issue was not explicitly identified in the case details. However, it was implied that the initial configuration settings for the Active Directory were incorrect or incomplete, leading to the sync failure.

## Solution
The issue was resolved by making necessary changes to the Active Directory configuration. After these adjustments, the connection was successfully established, and the synchronization process was completed. Subsequent testing confirmed that administrative users were able to log in to the Endpoint Protector User Interface (EPP UI) without issues.

## Notes
- Ensure that all Active Directory settings are correctly configured before attempting to sync.
- It may be beneficial to document any specific changes made during troubleshooting for future reference.
- Regular testing of the single sign-on functionality is recommended after any configuration changes to avoid similar issues.