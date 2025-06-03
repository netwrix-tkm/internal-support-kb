# Support Case Summary

## Ticket Metadata
- **Ticket ID:** 500Qk00000GElAlIAL
- **Case Number:** 422055
- **Status:** Closed - Resolved
- **Account/Company:** IGA Airport
- **Contact Name:** Yunus ICIN
- **Product:** Netwrix Endpoint Protector
- **Component:** Active Directory Sync
- **Feature:** AD Sync Error
- **Version:** Not specified

## Problem Description
The customer, IGA Airport, reported receiving a server access error when attempting to connect to Active Directory. The issue was also replicated in the technician's test environment.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Active Directory Sync

## Troubleshooting Steps
1. Reviewed the error message displayed in the attached screenshot.
2. Attempted to replicate the issue in a controlled test environment.
3. Conducted a remote session to diagnose the connection settings and configurations.
4. Verified network connectivity and permissions for the Active Directory service account.

## Root Cause
The root cause of the issue was identified as a misconfiguration in the Active Directory connection settings, which prevented successful authentication and access to the directory services.

## Solution
The issue was resolved during a remote session by:
- Correcting the Active Directory connection settings.
- Ensuring that the service account used for the connection had the necessary permissions.
- Testing the connection post-correction to confirm successful access to Active Directory.

## Notes
- Ensure that all Active Directory connection settings are thoroughly reviewed and validated during initial setup to prevent similar issues.
- Document any changes made to connection settings for future reference.
- Regularly verify permissions for service accounts used in Active Directory integrations to avoid access issues.