## Ticket Metadata
- **Ticket ID:** 500Qk00000DRJByIAP
- **Case Number:** 415776
- **Status:** Closed - Resolved
- **Account/Company:** USAA
- **Contact Name:** Justin Snyder
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for NetApp
- **Feature:** Data Collection
- **Version:** 11.5

## Problem Description
The customer reported that a newly added NetApp SVM scan target had been running for 6 days without completion, and several other SVM targets were encountering scan errors.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Build Number:** 177
- **Age:** 20.1

## Troubleshooting Steps
1. Validated the fpolicy against a single SVM and planned to apply it to all SVMs.
2. Reviewed the most recent StealthAUDIT (SA) 11.5 scan, identifying 46 issues related to non-existent Share locations.
3. Selected the "Import incomplete scan data" option for the NetApp FSAA Job group.
4. Adjusted the schedule to prevent overlapping FSAA bulk-imports and reporting from locking the database.
5. Stopped the current FSAA scan and initiated the import of incomplete scan data.
6. Configured the FSAA bulk import settings.
7. Kicked off the related NetApp bulk-import and planned to run the reports schedule task afterward.
8. Set the schedule to run only the Root Job Group Folder for FileSystem.
9. Confirmed the external engine configuration for the empty fpolicy.

## Root Cause
The issue was primarily due to an incorrect configuration of the fpolicy for the NetApp SVM targets, which led to prolonged scan times and errors.

## Solution
The issue was resolved by validating and updating the fpolicy for the SVMs. The following command was used to create the external engine for the empty fpolicy:
```bash
vserver fpolicy policy external-engine create -vserver [SVM_NAME] -engine-name StealthAUDITEngine -primary-servers [IP_ADDRESS,…] -port 9999 -extern-engine-type asynchronous -ssl-option no-auth
```
After applying the correct fpolicy settings, the scans were able to complete successfully.

## Notes
- Ensure that the fpolicy is correctly configured for all SVM targets to avoid similar issues in the future.
- Monitor the scan durations and errors closely after making configuration changes to quickly identify any further issues.