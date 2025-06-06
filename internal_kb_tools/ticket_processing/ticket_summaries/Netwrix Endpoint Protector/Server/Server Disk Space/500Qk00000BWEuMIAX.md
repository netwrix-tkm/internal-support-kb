```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BWEuMIAX
- **Case Number:** 411212
- **Status:** Closed - Resolved
- **Account/Company:** Updike, Kelly & Spellacy, P.C.
- **Contact Name:** Jamie Mastrio
- **Product:** Netwrix Endpoint Protector
- **Component:** Server Disk Space
- **Feature:** Server
- **Version:** Premium 5.8.1.0

## Problem Description
The customer reported difficulties in identifying the current version of the Netwrix Endpoint Protector server and requested assistance with cleaning up logs to reduce disk space usage.

## Environment Details
- The server is hosted by Netwrix.
- The current version in use was identified as Premium 5.8.1.0.

## Troubleshooting Steps
1. Instructed the customer on how to access the Audit Log Backup feature for log cleanup:
   - Navigate to **System Maintenance -> Audit Log Backup**.
   - Select the log type and choose logs to back up.
   - Start the backup process.
2. Provided guidance on scheduling automatic backups to clean up logs older than 6 months.
3. Informed the customer that the current EPP Server version can be found in the bottom right corner of the EPP UI.
4. Confirmed the latest server version available was 5.9.3.0 and advised on the update process.
5. Scheduled a remote session to address alerts stuck in the queue and investigate the slow server performance.

## Root Cause
The customer was using an outdated version of the EPP Server (5.8.1.0) and had not configured log cleanup settings, leading to excessive disk space usage and potential performance issues.

## Solution
- During a remote session, the support technician cleared the alerts from the queue, which resolved the issue of not receiving notifications.
- The customer was guided to update the EPP Server to the latest version (5.9.3.0) and was provided instructions for updating client software across their machines.

## Notes
- For Windows machines, the installer will fail if the new EPP Client is installed on top of the old version; the old client must be uninstalled first.
- For Mac machines, the new client can be installed over the old version without issues.
- The customer confirmed that the server was functioning better after the cleanup and updates, and they planned to deploy the new version company-wide.
```