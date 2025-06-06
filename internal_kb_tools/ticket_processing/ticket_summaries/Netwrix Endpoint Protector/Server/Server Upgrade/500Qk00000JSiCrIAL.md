## Ticket Metadata
- **Ticket ID:** 500Qk00000JSiCrIAL
- **Case Number:** 429805
- **Status:** Closed - Resolved
- **Account/Company:** Software GmbH
- **Contact Name:** Sonya Yoncheva
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** Not specified

## Problem Description
The customer reported an error message indicating that their EndPoint Protector appliance was running low on disk space after upgrading from an old operating system. The message stated that only 6.36 GB was free out of 19.52 GB (33%), which could severely affect server functionality and performance.

## Environment Details
- The EndPoint Protector is hosted.
- The operating system version prior to the upgrade was very old.

## Troubleshooting Steps
1. Reviewed the error message regarding low disk space.
2. Suggested using the Audit Log Backup feature to reduce logs stored in the database.
3. Recommended deleting older system and audit log backups.
4. Advised tuning policies to reduce the incoming log count.
5. Cleared space on the root partition (/) to free up additional disk space.

## Root Cause
The low disk space issue was primarily due to the accumulation of logs and backups from the previous operating system version, which had not been adequately managed during the upgrade process.

## Solution
The issue was resolved by clearing space on the root partition (/), which increased the available disk space from 6.36 GB to 47%. This action alleviated the low disk space warning and restored normal functionality to the EndPoint Protector server.

## Notes
- It is important to regularly monitor disk space and manage logs to prevent similar issues in the future.
- Consider implementing automated log management policies to ensure that disk space does not become a recurring problem after upgrades.