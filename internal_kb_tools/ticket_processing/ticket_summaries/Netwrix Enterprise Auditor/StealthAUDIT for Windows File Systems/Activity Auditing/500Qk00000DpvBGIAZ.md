## Ticket Metadata
- **Ticket ID:** 500Qk00000DpvBGIAZ
- **Case Number:** 416732
- **Status:** Closed - Resolved
- **Account/Company:** Central Bank of Trinidad and Tobago
- **Contact Name:** Kevin Fraser
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Activity Auditing
- **Version:** 11.6

## Problem Description
The customer reported an issue where user permissions on certain file shares on their file server were removed and replaced by the "Everyone" user group. Additionally, the owner of the affected folders was also changed. The customer sought assistance in configuring StealthIntercept to monitor and alert on any further changes to these permissions.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for Windows File Systems
- **Product Version:** 11.6

## Troubleshooting Steps
1. Initial investigation revealed that the customer did not have the necessary credentials to access the StealthIntercept Console.
2. During a follow-up meeting, it was noted that file system monitoring in StealthIntercept was not enabled, which prevented capturing the permission change events.
3. The Activity Monitor agent was unable to connect, further hindering the monitoring capabilities.
4. Recommendations were made to schedule monthly reports to identify folders with the "Everyone" group added and to create alerts for changes in folder permissions.
5. A review of group policy settings was suggested to ensure best practices for auditing were being followed.

## Root Cause
The root cause of the issue was identified as a lack of proper monitoring configuration in StealthIntercept, which resulted in the inability to track changes to file permissions effectively. Additionally, the absence of necessary credentials limited access to the monitoring tools.

## Solution
1. The host was added to the Activity Monitor, and monitoring was configured to track changes.
2. A File System Activity Monitoring (FSAC) scan was set up for the host.
3. The customer was advised to utilize the generated reports to identify any future changes to permissions and to determine the responsible parties if the issue recurred.

## Notes
- Ensure that proper credentials are available for accessing monitoring tools to facilitate troubleshooting.
- Regularly review and update monitoring configurations to capture critical events effectively.
- Consider implementing alerts for immediate notification of permission changes to prevent unauthorized access.