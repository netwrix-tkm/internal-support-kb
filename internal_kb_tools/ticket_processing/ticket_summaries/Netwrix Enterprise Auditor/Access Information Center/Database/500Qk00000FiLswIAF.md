## Ticket Metadata
- **Ticket ID:** 500Qk00000FiLswIAF
- **Case Number:** 420930
- **Status:** Closed - Resolved
- **Account/Company:** Schlumberger Technology Corporation (SLB)
- **Contact Name:** Sherry Lie
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Database
- **Version:** 11.5.0.174

## Problem Description
The customer reported that queries made on the Access Information Center (AIC) were extremely slow, indicating that the AIC was not functioning properly.

## Environment Details
- **Product Version:** 11.5
- **Build Number:** 11.5.0.174
- The AIC application server was installed separately from the SQL server.

## Troubleshooting Steps
1. Analyzed SQL server performance and identified SQL timeout errors.
2. Monitored CPU utilization on the SQL server, which was found to be at 100%.
3. Collaborated with the customer's DBA to investigate connection issues.
4. Noted that there were 120+ simultaneous connections from AIC to the SQL server.
5. Disabled all StealthAUDIT jobs and stopped AIC services to assess impact.
6. Rebooted the SQL server to observe changes in CPU usage and query performance.
7. Investigated the impact of Carbon Black AV on SQL server performance.

## Root Cause
The issue was primarily caused by an excessive number of connections (144) from the AIC application server to the SQL server, with many connections lacking a login name and others using the local "sa" account. This led to high CPU usage and slow response times from the AIC.

## Solution
The issue was resolved by allowing the excessive connections to die out or close. After the connections were reduced, the CPU utilization on the SQL server returned to normal levels, and the AIC performance improved significantly. 

## Notes
- It is recommended to monitor the number of connections from AIC to the SQL server to prevent similar issues in the future.
- Consider reviewing the configuration of the AIC application to optimize connection handling.
- Be aware of the potential impact of antivirus software on SQL server performance; testing with AV disabled may be necessary.