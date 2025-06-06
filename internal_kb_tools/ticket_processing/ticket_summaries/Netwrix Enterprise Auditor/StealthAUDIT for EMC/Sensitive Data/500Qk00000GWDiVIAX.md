## Ticket Metadata
- **Ticket ID:** 500Qk00000GWDiVIAX
- **Case Number:** 422633
- **Status:** Closed - Resolved
- **Account/Company:** Hobby Lobby
- **Contact Name:** Kyle Baldwin
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for EMC
- **Feature:** Sensitive Data
- **Version:** 11.6

## Problem Description
The customer reported an error during a SEEK job processing on a single Isilon host using Local Mode scan. The error indicated that a specific assembly, `System.Data.SQLite`, could not be loaded due to a mismatch in the assembly's manifest definition.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Scan Mode:** Local Mode
- **Host Type:** Single Isilon host

## Troubleshooting Steps
1. Verified the error message: "Could not load file or assembly 'System.Data.SQLite, Version=1.0.117.0, Culture=neutral, PublicKeyToken=db937bc2d44ff139' or one of its dependencies."
2. Checked the installation directory `%SAInstallDir%FSAA` for the specified assembly.
3. Identified outdated versions of `System.Data.SQLite` in the directory.
4. Replaced any outdated versions of `System.Data.SQLite` with the correct version (1.0.117.0).

## Root Cause
The issue was caused by the presence of an outdated version of the `System.Data.SQLite` assembly in the installation directory, which did not match the version required by the application.

## Solution
The issue was resolved by locating the outdated `System.Data.SQLite` assembly in the `%SAInstallDir%FSAA` directory and replacing it with the correct version (1.0.117.0). This ensured that the application could successfully load the required assembly and proceed with the SEEK job processing.

## Notes
- Ensure that all assemblies in the installation directory are kept up to date to prevent similar issues in the future.
- Regularly verify the integrity of assembly versions to avoid mismatches that can lead to processing errors.