## Ticket Metadata
- **Ticket ID:** 500Qk00000FfQfTIAV
- **Case Number:** 420813
- **Status:** Closed - Resolved
- **Account/Company:** Hydro Group Norway
- **Contact Name:** Fenilkumar S
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for NetApp
- **Feature:** Activity Auditing
- **Version:** 11.5

## Problem Description
The customer reported that the activity bulk import was failing for multiple NetApp systems during a transition from one proxy server to a new proxy server.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Product Version:** 11.5
- **Build Number:** 11.5.1342.975

## Troubleshooting Steps
1. Verified the transition process from the old proxy server to the new proxy server.
2. Checked permissions assigned to the proxy server against the documentation.
3. Reviewed the configuration settings for the NetApp systems.
4. Consulted relevant documentation for proxy server permissions and NetApp activity auditing.

## Root Cause
The issue was identified as incorrect configuration related to permissions for the new proxy server, which were not aligned with the requirements specified in the documentation.

## Solution
The problem was resolved by verifying and assigning the correct permissions for the new proxy server as per the documentation provided in the following links:
- [Proxy Server Permissions Documentation](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Requirements/Solutions/FileSystem/ProxyModeServicePermissions.htm)
- [NetApp Activity Monitoring Documentation](https://helpcenter.netwrix.com/bundle/ActivityMonitor_7.1/page/Content/ActivityMonitor/Admin/MonitoredHosts/Add/NetApp.htm)
- [NetApp Configuration Documentation](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/Config/NetAppCMode/Activity.htm)

## Notes
- Ensure that permissions are thoroughly checked and configured according to the documentation when transitioning proxy servers to avoid similar issues in the future.
- The ticket was initially opened under the wrong platform "Auditor" instead of "Enterprise Auditor," which may lead to confusion in case categorization.