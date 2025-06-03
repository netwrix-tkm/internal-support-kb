## Ticket Metadata
- **Ticket ID:** 500Qk00000MYakMIAT
- **Case Number:** 437713
- **Status:** Closed - Resolved
- **Account/Company:** DataVisor
- **Contact Name:** Ismail Reyhanoglu
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server - Other
- **Feature:** N/A
- **Version:** N/A

## Problem Description
The customer reported that a user account was duplicating on the Netwrix Endpoint Protector server. After previous support interactions, the customer had deleted multiple duplicate accounts, but the same user account multiplied again, reaching four instances overnight.

## Environment Details
- The issue was observed on the Netwrix Endpoint Protector server.
- The customer indicated that the problem was specific to a single end user.

## Troubleshooting Steps
1. The support team requested the customer to run specific terminal commands on the affected computer to generate log files for further investigation:
   ```bash
   sudo /bin/launchctl unload /Library/LaunchDaemons/com.cososys.eppclient.launchdaemon.plist
   sudo touch /private/var/log/eppclient_append.log
   sudo touch /private/var/log/eppsslsplit.log
   sudo /bin/launchctl load /Library/LaunchDaemons/com.cososys.eppclient.launchdaemon.plist
   ```
2. The customer was instructed to allow the issue to reproduce and then collect the logs using the following commands:
   ```bash
   cp /private/var/log/eppclient_append.log ~/Desktop
   cp /private/var/log/eppsslsplit.log ~/Desktop
   cp /etc/epp/reprovision.db ~/Desktop
   cp /etc/epp/rights.s3db ~/Desktop
   cp /etc/epp/netdlp/netdlp_settings.json ~/Desktop
   ```
3. The customer confirmed that the issue reproduced and provided the logs to the support team.
4. A remote session was scheduled to further investigate the issue.

## Root Cause
The root cause of the issue was identified as a potential bug in the Netwrix Endpoint Protector that caused the duplication of user accounts under specific conditions.

## Solution
The customer ran a script provided by the support team during a remote session, which resolved the issue of the computer name duplicating. The support team confirmed that the problem was addressed and the ticket was closed.

## Notes
- Ensure that the customer is aware of the need to monitor for any further duplications after applying the solution.
- It is recommended to keep the logs for future reference in case the issue reoccurs.
- If similar issues arise, consider checking for any updates or patches for the Netwrix Endpoint Protector that may address known bugs related to account duplication.