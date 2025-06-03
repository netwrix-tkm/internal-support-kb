## Ticket Metadata
- **Ticket ID:** 500Qk00000NgOOtIAN
- **Case Number:** 440956
- **Status:** Closed - Resolved
- **Account/Company:** Allied Telesis K.K
- **Contact Name:** Junichi Katagiri
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts Configuration
- **Version:** NONE

## Problem Description
The customer, Junichi Katagiri, reported that they were unable to see the Alerts menu in their Netwrix Endpoint Protector application and requested assistance in making it available.

## Environment Details
- The customer was using Netwrix Endpoint Protector.
- The server was experiencing high CPU usage due to receiving a large number of logs from clients.

## Troubleshooting Steps
1. Confirmed the user's role under "System Configuration > System Administrators" to ensure they had Super Administrator privileges, which are required to access and edit alerts.
2. Suggested checking the SMTP settings in "System Configuration > System Settings" before setting up alerts.
3. Investigated the server's performance and resource allocation, particularly CPU and RAM usage.
4. Enhanced the CPU and RAM of the server to improve performance.

## Root Cause
The root cause of the issue was identified as insufficient hardware resources on the server, which was unable to handle the high volume of logs being received. This led to high CPU usage, preventing the user from maintaining a session and accessing the Alerts menu.

## Solution
The issue was resolved by enhancing the CPU and RAM of the Endpoint Protector server. After the hardware upgrade, the user was able to access the Alerts menu successfully with Super Administrator privileges.

## Notes
- It is important to monitor server performance and resource allocation, especially when dealing with high log volumes, to prevent similar issues in the future.
- Consider advising customers to regularly review their server configurations and resource usage to ensure optimal performance.