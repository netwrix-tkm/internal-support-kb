## Ticket Metadata
- **Ticket ID:** 500Qk00000LrCRzIAN
- **Case Number:** 435789
- **Status:** Closed - Resolved
- **Account/Company:** Polsinelli
- **Contact Name:** Brandon Artist
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Database
- **Version:** 11.6.0.12

## Problem Description
The customer reported that the Access Information Center (AIC) version 11.6.0.12 was not rendering Activity Details, which hindered their ability to view activity statistics.

## Environment Details
- **Operating System:** Not specified
- **Network Configuration:** Not specified
- **Logs:** Two sets of logs were attached for review.

## Troubleshooting Steps
1. Checked if Activity Statistics were displaying any data.
2. Reviewed logs for errors related to the Volume Shadow Copy Service (VSS).
3. Adjusted settings in NAM under Monitored Hosts to uncheck VSS operations.
4. Verified file output paths for the host DC2-P-FILE-02.
5. Checked account exclusions in NAM for NT AUTHORITY accounts.
6. Analyzed NEA jobs for timeouts and errors.
7. Reviewed Activity Details and Statistics for various date ranges.
8. Confirmed hostname reporting settings in NAM.
9. Ensured that the correct hostname format was being used in NEA.
10. Created a job to remove old applets and data from the remote server.
11. Monitored the success of the FSAA Bulk Import job.
12. Investigated errors related to the removal of old hosts from the database.
13. Drilled down into specific folders in AIC to check for data visibility.

## Root Cause
The issue was primarily caused by misconfigurations in the hostname reporting settings and the presence of an old applet on the server DC2-P-FILE-02, which prevented the AIC from rendering Activity Details correctly.

## Solution
The issue was resolved by:
- Unchecking unnecessary VSS operations in the NAM settings.
- Correcting the hostname reporting settings to ensure the NETBIOS name was used.
- Removing the old FSAA applet and associated data from the server using a custom job.
- Ensuring that the NEA jobs were configured correctly and that the old hosts were removed from the system.

After these adjustments, the AIC was able to display Activity Details correctly.

## Notes
- Ensure that hostname reporting is set correctly to avoid similar issues in the future.
- Regularly check for and remove any outdated applets or configurations that may interfere with system operations.
- Monitor NEA jobs for timeouts and errors to proactively address potential issues.