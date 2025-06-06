```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000DgmdSIAR
- **Case Number:** 416358
- **Status:** Closed - Resolved
- **Account/Company:** Tecplix Technologies Private Limited
- **Contact Name:** Himanshu Vaidya
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** Not specified

## Problem Description
The customer reported persistent issues with accessing the EPP Console, experiencing slow responsiveness and unresponsiveness, which hindered their daily tasks. Additionally, they raised concerns regarding mail alerts and requested information on data classification policies.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Multiple tickets were raised by the customer regarding the console access issue.
2. The ticket was escalated to a critical priority due to the ongoing nature of the problem.
3. The instance type was changed from `t3.small` (2 CPUs, 2 GB RAM) to `t3.large` (2 CPUs, 8 GB RAM) to improve performance.
4. Configuration optimization was performed on the server.
5. A remote session was scheduled to further investigate and resolve the issues.

## Root Cause
The root cause of the issue was identified as insufficient server resources, which led to slow performance and unresponsiveness of the EPP Console.

## Solution
The issue was resolved by increasing the server resources from `t3.small` to `t3.large`, which significantly improved the console's responsiveness. Following this change, the customer confirmed that the issue was resolved.

## Notes
- Ensure that server resources are adequately provisioned based on the expected load to prevent similar issues in the future.
- Regular monitoring of server performance can help identify resource constraints before they impact user experience.
- Consider scheduling regular check-ins with customers to address any ongoing concerns proactively.
```