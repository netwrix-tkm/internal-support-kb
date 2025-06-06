## Ticket Metadata
- **Ticket ID:** 500Qk00000GYQRuIAP
- **Case Number:** 422741
- **Status:** Closed - Resolved
- **Account/Company:** Shield Force
- **Contact Name:** Arturo Armando Flores Mejia
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported issues with disk space on their server, indicating that they had only 2.57GB of free space remaining. Despite debugging consulting records, problems persisted in the console.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Engaged with the DevOps team to investigate the disk space issue.
2. Reviewed consulting records for any potential errors or misconfigurations.
3. Attempted to clear unnecessary files and logs to free up disk space.

## Root Cause
The root cause of the issue was related to insufficient disk space, compounded by issues with SSM (System State Management) and NTP (Network Time Protocol) configurations that were affecting system performance.

## Solution
The issue was resolved by clearing disk space after collaborating with the DevOps team. They addressed the SSM and NTP issues, which contributed to the overall performance and stability of the server.

## Notes
- Ensure regular monitoring of disk space to prevent similar issues in the future.
- Consider implementing automated alerts for low disk space to facilitate timely intervention.
- Review SSM and NTP configurations periodically to maintain optimal server performance.