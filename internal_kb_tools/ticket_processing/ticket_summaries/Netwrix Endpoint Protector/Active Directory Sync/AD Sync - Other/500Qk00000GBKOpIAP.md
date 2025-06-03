## Ticket Metadata
- **Ticket ID:** 500Qk00000GBKOpIAP
- **Case Number:** 421927
- **Status:** Closed - Resolved
- **Account/Company:** ING companies
- **Contact Name:** Drake Scott
- **Product:** Netwrix Endpoint Protector
- **Component:** Active Directory Sync
- **Feature:** AD Sync - Other
- **Version:** NONE

## Problem Description
The customer reported that the Active Directory (AD) Administrators Group Sync was not functioning as expected, despite successfully enabling AD authentication. They inquired if a specific format was required for defining the group.

## Environment Details
- The group in question was named `GSADF1P_0000iqa_CoSoSysEPP-NPASuperAdmins_P`.
- The issue occurred within the Netwrix Endpoint Protector platform.

## Troubleshooting Steps
1. Verified that AD authentication was enabled and functioning correctly.
2. Checked the configuration settings for the AD Administrators Group.
3. Confirmed that the group was correctly defined in the system.
4. Attempted to sync the AD Administrators Group multiple times.
5. Reviewed the logs for any error messages related to the sync process.
6. Conducted tests on a test domain server to replicate the issue, including:
   - Creating a similar security group and user.
   - Modifying user logon names and testing connection and sync outcomes.
   - Introducing intentional errors in the configuration to observe system responses.

## Root Cause
The issue was identified as a configuration mistake in the AD settings. Specifically, the correct group was not being recognized due to improper configuration parameters.

## Solution
The configuration was corrected, ensuring that all settings were accurately defined. After making the necessary adjustments, the sync process was successfully executed, allowing the AD Administrators Group to sync properly.

## Notes
- Always ensure that changes made in the UI are saved before attempting to sync AD groups. Failure to do so may result in the system using outdated data.
- If encountering similar issues, verify the group name and configuration settings for any typos or incorrect formats.
- Regularly test the connection and sync functionality after any configuration changes to ensure proper operation.