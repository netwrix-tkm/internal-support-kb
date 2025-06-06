## Ticket Metadata
- **Ticket ID:** 500Qk00000MrJvzIAF
- **Case Number:** 438610
- **Status:** Closed - Resolved
- **Account/Company:** Bowman Gilfillan
- **Contact Name:** Shaun Morris
- **Product:** Netwrix Endpoint Protector
- **Component:** Server Disk Space
- **Feature:** Server Disk Space
- **Version:** NONE

## Problem Description
The customer reported poor performance and low disk space messages in the UI of the Netwrix Endpoint Protector. Additionally, there was an issue with a login request from a previously disabled user, BOWTECH, originating from the server.

## Environment Details
- The server is hosted by CoSoSys with 8 GB of RAM allocated.
- The system is running Ubuntu.

## Troubleshooting Steps
1. **Performance Issue:**
   - Noted that memory was spilling over to swap, and after resuming to normal load, swap memory was still being utilized.
   - Advised the customer to restart their EPP server to clear swap memory.

2. **Low Disk Space Issue:**
   - Checked disk space utilization, which was at 65%.
   - Cleared Ubuntu log files using the following commands:
     ```bash
     echo "" > /usr/local/logs/php-fpm.log
     sudo journalctl --vacuum-size=1M
     ```
   - After executing the commands, the disk space utilization was reduced to 54%.

3. **User Login Issue:**
   - Discussed the login request from the disabled user and confirmed that there was no option in the UI to alter the user settings.

## Root Cause
- The poor performance was primarily due to the server's memory management, where RAM was spilling over to swap memory.
- The low disk space issue was caused by accumulated log files on the Ubuntu server.

## Solution
- Restarted the EPP server to clear the swap memory, which improved performance.
- Cleared unnecessary log files to free up disk space, resolving the low disk space message in the UI.

## Notes
- The customer confirmed that the low disk space message is no longer present and assumed that performance had improved after the server reboot.
- It is important to monitor server memory usage and log file accumulation regularly to prevent similar issues in the future.