## Ticket Metadata
- **Ticket ID:** 500Qk00000MXlmiIAD
- **Case Number:** 437673
- **Status:** Closed - Resolved
- **Account/Company:** Kerry Group Services International Limited
- **Contact Name:** Lorcan O'Sullivan
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Settings
- **Version:** Not specified

## Problem Description
The customer reported receiving an error message within the admin console indicating low disk space, which was affecting the performance of the portal. They also mentioned difficulties in deleting stored data and unneeded backups.

## Environment Details
- The appliance had 6.61 GB free out of 19.52 GB total disk space (approximately 34% free).
- The error message suggested that EPP Server functionality and performance may be severely affected.

## Troubleshooting Steps
1. Customer attempted to delete stored data and unneeded backups but faced issues with some items not deleting.
2. Customer reviewed the error message recommendations, which included:
   - Using Audit Log Backup to reduce logs stored in the database.
   - Deleting older system and audit log backups.
   - Tuning policies to reduce incoming log count.
3. Support technician reviewed the nginx configuration file.

## Root Cause
The root cause of the issue was identified as a misconfiguration in the nginx config file. The location for the debug log was incorrectly set to "off" instead of "/dev/null," resulting in the creation of an "off.log" file that stored nginx logs, consuming disk space.

## Solution
The solution involved updating the nginx configuration file to correctly set the debug log location to "/dev/null." Additionally, the technician removed the "off.log" file that had been created, which helped free up disk space and improved performance.

## Notes
- Ensure that the nginx configuration is correctly set to avoid similar issues in the future.
- Regularly monitor disk space and log file sizes to prevent performance degradation.
- Consider implementing automated log management practices to manage disk space effectively.