## Ticket Metadata
- **Ticket ID:** 500Qk00000DWxlSIAT
- **Case Number:** 416061
- **Status:** Closed - Resolved
- **Account/Company:** Neue ZWL Zahnradwerk Leipzig GmbH
- **Contact Name:** Thomas Neue ZWL Zahnradwerk Leipzig GmbH
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server LiveUpdate
- **Version:** 7.0

## Problem Description
The customer reported that updates were not being installed on the Netwrix Endpoint Protector. When the "Updates ausführen" button was clicked, the system indicated that updates were being installed, but upon refreshing the web browser, the updates reappeared as available.

## Environment Details
- **Update Types Affected:** 
  - Security Update – EPP Server Hotfix #1.1
  - Backend Security Updates

## Troubleshooting Steps
1. Verified the update process by clicking the "Updates ausführen" button.
2. Monitored the system for any error messages during the update installation.
3. Checked the web browser for any caching issues that might affect the display of update status.
4. Reviewed server logs for any indications of failed update attempts.
5. Consulted internal documentation (Procedure 60) for potential solutions.

## Root Cause
The root cause of the issue was identified as a failure in the update installation process, which was not properly completing despite the system indicating success. This could have been due to a misconfiguration or a temporary glitch in the update mechanism.

## Solution
The issue was resolved by following the steps outlined in Procedure 60, which involved:
- Ensuring that the server had the necessary permissions to install updates.
- Restarting the update service to reset any stalled processes.
- Manually triggering the update installation again, which successfully completed the installation of the pending updates.

## Notes
- It is recommended to monitor the update installation process closely after applying updates to ensure they are successfully completed.
- If similar issues arise in the future, consider checking server permissions and restarting the update service as initial troubleshooting steps.