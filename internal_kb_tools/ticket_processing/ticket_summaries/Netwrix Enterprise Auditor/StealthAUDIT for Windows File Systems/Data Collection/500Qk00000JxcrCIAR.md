## Ticket Metadata
- **Ticket ID:** 500Qk00000JxcrCIAR
- **Case Number:** 430821
- **Status:** Closed - Resolved
- **Account/Company:** Government of Nova Scotia
- **Contact Name:** Gregory Osborne
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Data Collection
- **Version:** 11.6

## Problem Description
The customer reported that the Activity Scan was failing, indicating that a bulk import was needed. However, the Bulk Import process was repeatedly failing immediately upon startup with an error message related to ID mapping.

## Environment Details
- The issue occurred in a multi-agent setup using Host Mapping.
- The customer was using Netwrix Enterprise Auditor version 11.6.

## Troubleshooting Steps
1. Ran FSAC System Scan.
2. Attempted FSAC Bulk Import.
3. Encountered ID mapping error: 
   ```
   Stealthbits.StealthAUDIT.DataCollectors.FSAA.FSAAException: ID 484474776 mapping not found in ResourceMap
   ```
4. Disabled "Strong proxy affinity" setting to see if it affected the scan.
5. Upgraded from NEA version 11.6.0.112 to 11.6.0.134.

## Root Cause
The root cause of the issue was not definitively identified, but it was suspected that the "Strong proxy affinity" setting was affecting the scan process in the multi-agent setup.

## Solution
The issue was resolved by upgrading the Netwrix Enterprise Auditor from version 11.6.0.112 to version 11.6.0.134. After the upgrade, the jobs began running more consistently, and the bulk import process completed successfully.

## Notes
- It is recommended to monitor the "Strong proxy affinity" setting in multi-agent setups, as it may impact scan performance.
- Future upgrades should be considered if similar issues arise, as they may contain fixes for underlying problems.
- Ensure to run a repair on the bulk import job if similar ID mapping errors occur in the future.