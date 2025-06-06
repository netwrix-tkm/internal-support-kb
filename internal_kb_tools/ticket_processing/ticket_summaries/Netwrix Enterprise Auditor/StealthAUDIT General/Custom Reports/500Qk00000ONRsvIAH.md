## Ticket Metadata
- **Ticket ID:** 500Qk00000ONRsvIAH
- **Case Number:** 442966
- **Status:** Closed - Resolved
- **Account/Company:** W. L. Gore & Associates, Inc.
- **Contact Name:** Connie Liang
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Custom Reports
- **Version:** 11.6

## Problem Description
The customer reported that after upgrading from version 11.5 to 11.6 of StealthAUDIT, a previously created analysis for their Active Directory (AD) user summary, which was used for licensing, had disappeared from the GUI. The customer attempted to follow troubleshooting steps from a previous case but was unsuccessful in restoring the analysis.

## Environment Details
- The issue occurred during a full upgrade of the AD Solutions.
- The analysis file was located at: `C:\Program Files (x86)\STEALTHbits\StealthAUDIT\Jobs\GROUP_.Active Directory Inventory\JOB_1-AD_Scan\VIEW_SA_ADInventoryWLGORE_LicenseUsers.INI.xml`.

## Troubleshooting Steps
1. Closed all open instances of StealthAUDIT.
2. Attempted to copy the `JOB_1-AD_Scan` folder from the archived jobs folder in `%SAInstallDir%\Jobs` to `%SAInstallDir%\Jobs\GROUP_.Active Directory Inventory`.
3. Verified that the copied folder was not blocked and removed the "Read Only" attribute.
4. Went to Control Panel, selected "Change," and then performed a "Repair" on StealthAUDIT.
5. Checked if the analysis for "SA_ADInventoryWLGORE_LicenseUsers" was visible after the repair.

## Root Cause
The issue was likely caused by selecting the "Full Upgrade" option during the upgrade process instead of the "Upgrade in Place" option, which may have led to the loss of the custom analysis in the GUI.

## Solution
The issue was resolved by following these steps:
1. Close all instances of StealthAUDIT.
2. Copy the `JOB_1-AD_Scan` folder from the archived jobs folder in `%SAInstallDir%\Jobs` to `%SAInstallDir%\Jobs\GROUP_.Active Directory Inventory`.
3. Right-click on the copied folder, check for any blocks, and ensure the "Read Only" checkbox is unchecked.
4. Perform a repair on StealthAUDIT via Control Panel.
5. After the repair, the analysis for "SA_ADInventoryWLGORE_LicenseUsers" became visible again in the GUI.

## Notes
- It is recommended to use the "Upgrade in Place" option during future upgrades to avoid similar issues.
- Ensure that all necessary backups are taken before performing upgrades to prevent data loss.