## Ticket Metadata
- **Ticket ID:** 500Qk00000EjEtBIAV
- **Case Number:** 418695
- **Status:** Closed - Resolved
- **Account/Company:** CVC Capital Partners Ltd
- **Contact Name:** Denver Diedericks
- **Product:** Netwrix Endpoint Protector
- **Component:** Active Directory Sync
- **Feature:** AD Sync - Other
- **Version:** NONE

## Problem Description
The customer reported that the Azure AD sync, which had been functioning correctly for the past two years, was no longer granting access to the EPP platform for members of a specific Security Group.

## Environment Details
- The issue occurred in the context of Azure Active Directory synchronization with the Netwrix Endpoint Protector platform.

## Troubleshooting Steps
1. Confirmed that the Azure AD sync was previously operational.
2. Investigated the configuration of the Security Group and its members.
3. Checked for any recent updates or changes that might have affected the AD sync settings.
4. Noted that the AD authentication settings were missing after a recent update.

## Root Cause
The root cause of the issue was identified as the MTP (Multi-Tenant Platform) option being turned off, which led to the loss of necessary AD authentication settings.

## Solution
The issue was resolved by re-enabling the MTP option, which restored the missing AD authentication settings. The customer was advised to set up the configuration again to ensure proper functionality.

## Notes
- It is important to monitor the MTP settings after updates to prevent similar issues in the future.
- Customers should be informed about the potential impact of updates on existing configurations, particularly regarding authentication settings.