## Ticket Metadata
- **Ticket ID:** 500Qk00000ETeutIAD
- **Case Number:** 418228
- **Status:** Closed - Resolved
- **Account/Company:** Sierra Nevada Corporation
- **Contact Name:** Kellen Carl
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Proxy
- **Version:** 11.6

## Problem Description
FSAA scans were failing without any error messages. The scans would run for about an hour and then disappear from the Running Instances list, showing that they ran for 0 seconds despite being observed running for the full duration.

## Environment Details
- **Product Version:** Netwrix Enterprise Auditor v11.6
- **Feature in Use:** File System Access Auditing (FSAA)
- **Proxy Configuration:** Multiple Proxy hosts for the same file servers

## Troubleshooting Steps
1. Reviewed logs and messages sections for error messages but found none.
2. Observed the scans running for an hour with no results produced.
3. Attempted to split the scan credentials into separate jobs.
4. Built out the schedule for one of the file servers.
5. Configured strong proxy affinity settings to ensure scans only run on the last proxy to scan the host.
6. Set the old domain to scan via MSTask Task Scheduler.
7. Ensured the applet was deployed to all targeted Windows servers and configured for local scanning on NAS devices.

## Root Cause
The issue was identified as an incorrect configuration related to the use of multiple Proxy hosts for the same file servers, which led to conflicts in the scanning process.

## Solution
The issue was resolved by splitting the scan credentials into separate jobs. Additionally, the configuration was adjusted to ensure strong proxy affinity, allowing scans to run only on the last proxy that scanned the host. This adjustment minimized conflicts and allowed the scans to complete successfully.

## Notes
- When using multiple Proxy hosts for the same file servers, it is crucial to configure strong proxy affinity to avoid conflicts.
- Refer to the following documentation for future configurations:
  - [File System Proxy as a Service Overview](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Install/FileSystemProxy/Upgrade.htm)
  - [FSAA: Applet Settings](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/DataCollector/FSAA/AppletSettings.htm)
  - [Scan Server Selection](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/DataCollector/FSAA/ScanServerSelection.htm)