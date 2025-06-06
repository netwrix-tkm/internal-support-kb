## Ticket Metadata
- **Ticket ID:** 500Qk00000OJjzkIAD
- **Case Number:** 442759
- **Status:** Closed - Resolved
- **Account/Company:** WellSpan Health
- **Contact Name:** John Masgalas
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Qumulo
- **Feature:** Credentials
- **Version:** 11.6

## Problem Description
The customer reported that a new scan for Qumulo NAS was failing, while scans for other systems (NAM) were functioning correctly.

## Environment Details
- **Product Version:** 11.6
- **Build Number:** 11.6.0.130

## Troubleshooting Steps
1. Reviewed the permissions required for the Access Analyzer scans on the Qumulo target.
2. Identified that the collection account lacked "Group membership in the Data-Administrators role."
3. Confirmed that the necessary permissions needed to be granted on both nodes of the Qumulo NAS.
4. After granting the required permissions, verified that the scan was now operational.

## Root Cause
The issue was caused by the collection account not having the necessary permissions, specifically the "Group membership in the Data-Administrators role," which is required for the Access Analyzer scans to function correctly.

## Solution
The issue was resolved by granting the "Group membership in the Data-Administrators role" permission to the collection account on both nodes of the Qumulo NAS. After this adjustment, the scan was successfully executed.

## Notes
- Ensure that the required permissions are granted on all nodes of the Qumulo NAS when setting up scans.
- Refer to the [Qumulo Target Requirements](https://helpcenter.netwrix.com/bundle/AccessAnalyzer_12.0/page/Content/Config/Qumulo/Overview.htm) for detailed permission requirements.
- These permissions are in addition to those needed for deploying applet scans or installing the File System Proxy Service for running scans in proxy mode.