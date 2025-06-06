## Ticket Metadata
- **Ticket ID:** 500Qk00000EnQvnIAF
- **Case Number:** 418873
- **Status:** Closed - Resolved
- **Account/Company:** Phillips & Cohen Associates, Ltd
- **Contact Name:** Adam Ivill
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Sensitive Data
- **Version:** 11.6

## Problem Description
The customer reported an error during a bulk import operation for a sensitive data scan, specifically stating: "DLPEX database does not exist, there is no data to import." The customer was unable to find relevant information in the help articles or admin guides.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for Windows File Systems
- **Product Version:** 11.6

## Troubleshooting Steps
1. Reviewed help articles and admin guides for information regarding the error.
2. Investigated the database status and configuration.
3. Checked for any outdated or incompatible library files related to the operation.
4. Considered the possibility of needing to delete the t2 database and rescan the Sensitive Data group.

## Root Cause
The issue was caused by an outdated version of the `System.Data.SQLite.dll` library (version 1.0.112.0) located in the `C:\Program Files (x86)\STEALTHbits\StealthAUDIT\FSAA` folder, which was incompatible with the current version of the software following an upgrade.

## Solution
The resolution involved replacing the outdated `System.Data.SQLite.dll` library with the updated version (1.0.117.0) sourced from the Sensitive Data folder in the Netwrix Enterprise Auditor (NEA). After the replacement, the SEEK-System Scans job was initiated, and the scan completed successfully without further errors.

## Notes
- Ensure that all library files are updated to their latest versions after any software upgrade to prevent similar issues.
- Monitor the database status regularly to avoid disruptions in sensitive data scans.
- If similar errors occur, check for outdated libraries as a first troubleshooting step.