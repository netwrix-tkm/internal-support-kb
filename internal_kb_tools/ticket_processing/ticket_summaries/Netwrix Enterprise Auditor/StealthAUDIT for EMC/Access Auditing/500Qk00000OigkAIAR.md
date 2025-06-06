## Ticket Metadata
- **Ticket ID:** 500Qk00000OigkAIAR
- **Case Number:** 443938
- **Status:** Closed - Resolved
- **Account/Company:** County of Travis
- **Contact Name:** Jesse Ohrmund
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for EMC
- **Feature:** Access Auditing
- **Version:** 11.6.0.137

## Problem Description
The customer reported an "access denied" error when attempting to configure a Dell Isilon share for an FSAA scan. Despite following the documentation, they were unable to bypass NTFS permissions, which was a requirement for their scanning process.

## Environment Details
- **Versions:** NEA 11.6.0.137
- **Target Share:** admin$ (located a few levels deep from the root)

## Troubleshooting Steps
1. Reviewed the configuration settings according to the provided documentation.
2. Engaged with Dell support for assistance regarding NTFS permissions.
3. Clarified the requirements for access to Isilon storage with the customer.
4. Updated the customer on the need for appropriate permissions as indicated by Dell support.

## Root Cause
The issue was primarily due to incorrect NTFS permissions set on the Isilon share, which prevented the scan account from accessing the required share.

## Solution
Dell support recommended adjusting the NTFS permissions for the scan account to allow access directly to the share. This change resolved the "access denied" error, enabling the FSAA scan to proceed successfully.

## Notes
- It is crucial to ensure that NTFS permissions are correctly configured for any accounts used in scanning processes.
- Future configurations should consider the hierarchy of permissions, especially when dealing with shares that are nested within deeper directory structures.