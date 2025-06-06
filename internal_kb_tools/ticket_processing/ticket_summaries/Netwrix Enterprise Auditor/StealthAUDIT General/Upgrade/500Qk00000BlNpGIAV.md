## Ticket Metadata
- **Ticket ID:** 500Qk00000BlNpGIAV
- **Case Number:** 411772
- **Status:** Closed - Resolved
- **Account/Company:** Dotnext South Africa
- **Contact Name:** Ziyaad Rasool
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Upgrade
- **Version:** 11.6

## Problem Description
The customer reported receiving multiple warnings and errors when attempting to run a job in the Netwrix Enterprise Auditor, specifically related to the absence of the `Reports.xml` file, which is necessary for report generation.

## Environment Details
- The issue occurred on a new installation of the software.
- The customer was using local admin credentials during the Proof of Concept (POC) and did not have Domain Admin credentials.

## Troubleshooting Steps
1. The customer provided logs indicating multiple warnings about missing libraries (`CPasswordSDK.dll` and `libeay32.dll`).
2. The support team requested the customer to check the `C:\Program Files (x86)\STEALTHbits\StealthAUDIT\Reports` directory for the `Reports.xml` file.
3. The customer confirmed that the directory existed but was empty.
4. The support team suggested reinstalling the application and ensuring the installer was unblocked.
5. The customer attempted reinstallation on two application servers but encountered the same issue.
6. The support team advised running the installation file using PowerShell as Domain Admin.
7. The customer reported that the steps provided by support to end NEA processes and restart the application successfully generated the `Reports.xml` file.

## Root Cause
The issue was caused by the improper generation of necessary files during the installation or upgrade of the Netwrix Enterprise Auditor. This was likely due to the installation being performed without adequate permissions (Domain Admin rights).

## Solution
The issue was resolved by following these steps:
1. The customer was instructed to open Task Manager and end all NEA instances/processes.
2. They then reopened the Netwrix Enterprise Auditor.
3. The `Reports.xml` file was successfully created in the specified directory.
4. The customer was able to publish the reports as intended.

## Notes
- It is crucial to perform installations or upgrades with Domain Admin credentials to ensure all necessary files are generated correctly.
- If encountering similar issues, restarting the application after ending processes can help regenerate missing files.