## Ticket Metadata
- **Ticket ID:** 500Qk00000MsdKgIAJ
- **Case Number:** 438657
- **Status:** Closed - Resolved
- **Account/Company:** Qast Systems Solutions Inc.
- **Contact Name:** Jessica Zhang
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** Server Version: 5.9.3.0, Client Version: 2.5.0.8

## Problem Description
Users were able to manually enable WiFi on Mac devices despite a policy set in Device Control that was supposed to disable WiFi and Bluetooth access at the computer level. This behavior was urgent and required immediate resolution.

## Environment Details
- **Client OS:** Mac Sonoma 14.7.4 (iMAC), Mac Sonoma 14.74 (Mac mini)
- **Server Version:** 5.9.3.0
- **Client Version:** 2.5.0.8

## Troubleshooting Steps
1. Verified the policy settings in Device Control to ensure they were correctly configured to deny access to WiFi and Bluetooth.
2. Conducted in-house testing with the latest client version (3.0.4.1006) to replicate the issue.
3. Observed that the issue did not reproduce with the latest client; WiFi was automatically deactivated after attempting to enable it.
4. Suggested to the customer to upgrade to the latest client version and provided a download link for testing.

## Root Cause
The issue was identified as being related to the outdated client version (2.5.0.8) being used by the customer. The latest client version resolved the issue, indicating that the older version had a bug that allowed users to bypass the policy settings.

## Solution
The problem was resolved by advising the customer to upgrade to the latest client version (3.0.4.1006). After testing with this version, the issue of users being able to manually enable WiFi was no longer present.

## Notes
- It is important to keep client software updated to the latest version to avoid similar issues in the future.
- Always verify policy settings and conduct in-house testing with the latest versions when troubleshooting unexpected behaviors.