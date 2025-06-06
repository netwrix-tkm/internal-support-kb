## Ticket Metadata
- **Ticket ID:** 500Qk00000HAeiOIAT
- **Case Number:** 424325
- **Status:** Closed - Resolved
- **Account/Company:** Hydro Group Norway
- **Contact Name:** Saveetha Anesh
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Configuration
- **Version:** 11.5

## Problem Description
The customer reported that the Stealthreport URL (https://stealthreport.nhy.hydro.com/) was down, and the newly renewed SSL certificate was not visible in the web portal. The issue was impacting production and required urgent attention.

## Environment Details
- The issue occurred on a server running Netwrix Enterprise Auditor version 11.5.
- The server was configured to use IIS for hosting the web application.

## Troubleshooting Steps
1. Verified the status of the SSL certificate in IIS and MMC.
2. Attempted to update the renewed certificate in both IIS and MMC.
3. Checked the web portal for the visibility of the updated certificate.
4. Reviewed the server configuration for any potential misconfigurations.
5. Confirmed the port settings used for the web application.

## Root Cause
The issue was caused by an incorrect port configuration. The application was set to use port 8082 instead of the standard HTTPS port 443.

## Solution
The resolution involved the following steps:
1. Rebound the application to the correct port (443).
2. Restarted the relevant services to apply the changes.
3. Confirmed that both the Access Information Center (AIC) and Reports were accessible after the changes were made.

## Notes
- Always verify the basic configurations before proceeding with more complex troubleshooting steps. 
- Do not rely solely on screenshots for diagnostics; ensure that all settings are checked directly in the server configuration.
- Future cases should include a thorough check of port settings when encountering similar issues with web accessibility.