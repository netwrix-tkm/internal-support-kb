## Ticket Metadata
- **Ticket ID:** 500Qk00000GuyWXIAZ
- **Case Number:** 423658
- **Status:** Closed - Resolved
- **Account/Company:** rotho Kunststoff AG
- **Contact Name:** Dennis Gerlach
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** NONE

## Problem Description
The customer reported that the synchronization between the Netwrix Endpoint Protector (EPP) and Active Directory (AD) was not functioning correctly. Although the system indicated that the synchronization was successful, new employees were not being synchronized. Additionally, attempts to manually create a new user resulted in persistent password errors, regardless of the password entered.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** EPP Other
- **Age:** 5.8

## Troubleshooting Steps
1. Verified the synchronization process with Active Directory to ensure no error messages were displayed.
2. Attempted to manually create a new user in the system with various passwords to identify if the issue was related to password validation.
3. Checked the configuration settings for the synchronization process to ensure they were correctly set up.

## Root Cause
The root cause of the issue was identified as a problem with the administrative account used for synchronization. The account may have had configuration issues or permissions that prevented successful synchronization and user creation.

## Solution
The issue was resolved by removing the problematic administrative account and then re-running the synchronization process. This action allowed the synchronization to complete successfully, and new users were created without any password errors.

## Notes
- Ensure that administrative accounts used for synchronization have the correct permissions and configurations to avoid similar issues in the future.
- Regularly review synchronization logs for any hidden errors that may not be immediately apparent during the process.