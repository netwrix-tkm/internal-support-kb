## Ticket Metadata
- **Ticket ID:** 500Qk00000HTOMyIAP
- **Case Number:** 425083
- **Status:** Closed - Resolved
- **Account/Company:** Howard County, MD
- **Contact Name:** Frank Salah
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Data Collection
- **Version:** 11.5

## Problem Description
The customer reported an error during the 2-FSAC Bulk Import step of the File System Scan job, which was triggered after expanding the server drive due to limited space. The error message indicated a mapping issue with the ResourceMap.

## Environment Details
- The issue occurred in a Netwrix Enterprise Auditor environment, specifically using the StealthAUDIT for Windows File Systems collector.
- The version in use was 11.5.

## Troubleshooting Steps
1. The customer expanded the server drive to address limited space.
2. The customer attempted to run the 1-FSAC System Scans, which produced a warning: "Cannot scan, Activity Scan needs bulk import."
3. The customer ran the 2-FSAC Bulk Import step, which failed with the error: 
   ```
   Stealthbits.StealthAUDIT.DataCollectors.FSAA.FSAAException: ID 32368372 mapping not found in ResourceMap
   ```
4. The customer used the "Reset Hosts" option to reset the Access GUID column value in the SA_FSAA_Hosts table.
5. A Repair job was executed, which completed successfully.
6. The customer queried the database directly to confirm that activity data existed but was not displayed in the web interface.

## Root Cause
The root cause of the issue was identified as a GUID mismatch in the database, likely due to interrupted scans or multiple scans running simultaneously. This mismatch prevented the bulk import from processing correctly.

## Solution
The issue was resolved by performing the following steps:
1. The "Reset Hosts" option was used to reset the GUIDs, allowing for a clean bulk import.
2. After resetting, the customer successfully ran the 1-FSAC System Scans followed by the 2-FSAC Bulk Import, which completed without errors.
3. The customer was advised to run the FSAC scan and import again to ensure all data was processed correctly.

## Notes
- Using "Reset Hosts" should not cause data loss or duplication and will not affect other hosts (e.g., NetApp).
- Future issues may arise from interrupted scans, multiple concurrent scans, or network issues affecting data imports.
- It is recommended to monitor the data processing in the AIC (Access Intelligence Center) for any delays in data display.