## Ticket Metadata
- **Ticket ID:** 500Qk00000DRXuvIAH
- **Case Number:** 415795
- **Status:** Closed - Resolved
- **Account/Company:** Healthcare Fraud Shield
- **Contact Name:** Karl Strobach
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Health
- **Version:** 8.0

## Problem Description
The customer reported that alerting functionality was not working as expected. Although successful blocks were noted for configured alerts, no alert emails were being received, and the alert history on the server was empty.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Confirmed that the SMTP configuration was set up and functioning properly.
2. Checked if the customer was receiving test emails.
3. Stopped the cron service using the command:
   ```bash
   service cron stop
   ```
4. Cleared the mailer folder:
   ```bash
   rm /var/eppfiles/mailer/*
   ```
5. Logged into MySQL and emptied the mailer table:
   ```sql
   DELETE FROM mailer;
   ```
6. Deleted existing alert caches:
   ```bash
   rm -rf /run/shm/mcache/cf_alerts/
   rm -rf /run/shm/mcache/dc_alerts/
   ```
7. Logged into MySQL and dropped the following tables:
   ```sql
   DROP TABLE old_alert;
   DROP TABLE old_cf_alert;
   ```
8. Ran the cron job to regenerate the alert cache:
   ```bash
   php /opt/eppworker/build_alerts_cache.php
   ```
9. Verified that the alerts cache was recreated:
   ```bash
   ls -la /run/shm/mcache/cf_alerts/
   ls -la /run/shm/mcache/dc_alerts/
   ```
10. Restarted the cron service:
    ```bash
    service cron start
    ```
11. Generated an event to check if the email alert was received.

## Root Cause
The issue was identified as a problem with the alerts cache, which had become corrupted or outdated, preventing the system from sending alert emails.

## Solution
The issue was resolved by regenerating the alerts cache. This involved stopping the cron service, clearing the mailer folder, emptying the mailer table in MySQL, deleting the existing alert caches, and running a script to rebuild the alert cache. After these steps, the alerting functionality was restored, and the customer began receiving alert emails.

## Notes
- Ensure that the SMTP configuration is always verified when alerting issues arise.
- Regular maintenance of the alerts cache may prevent similar issues in the future.
- Document any changes made to the configuration or system settings for future reference.