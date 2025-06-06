## Ticket Metadata
- **Ticket ID:** 500Qk00000CVKpzIAH
- **Case Number:** 413533
- **Status:** Closed - Resolved
- **Account/Company:** RKW SE Zweigniederlassung Wasserburg
- **Contact Name:** Adam Rudnicki
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SharePoint
- **Feature:** Database
- **Version:** 11.6.0.82

## Problem Description
The customer reported issues with SharePoint on-prem agent-based DLP scans where the scans were running for an extended period (15 hours) but the DLP results were not being imported into the database. The customer had recently upgraded the NEA console and SharePoint agents to the latest build and wiped out all SharePoint data from the database, but the issue persisted.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Build Number:** 11.6.0.82
- **DLP Data:** Missing from SharePoint, but permissions were imported correctly.

## Troubleshooting Steps
1. Confirmed the version/build number of the software.
2. Reviewed logs for any error messages related to DLP scans.
3. Suggested disabling endpoint protection temporarily to check for interference.
4. Advised the customer to ensure no other processes were accessing the DLP files during scans.
5. Requested logs in debug mode to gather more detailed information.
6. Suggested adding exclusions to the endpoint protection software.
7. Recommended upgrading to the latest version/build and dropping SPAA tables for a rescan.

## Root Cause
The issue was primarily caused by file access conflicts where the DLP agent could not back up the necessary files because they were being used by another process. This was compounded by endpoint protection software potentially interfering with file access.

## Solution
The issue was resolved by:
- Adding exclusions to the endpoint protection software on the NEA app server, which eliminated the "file is used by another process" errors.
- Running a repair on the system, which indicated that T2 files were damaged.
- Ensuring that the DLP scans were able to complete without interference, allowing the results to be imported into the database successfully.

## Notes
- It is crucial to ensure that no other processes (like backup or antivirus software) are accessing the DLP files during scans.
- For future cases, disabling endpoint protection temporarily during troubleshooting can help identify if it is causing file access issues.
- Always keep the software updated to the latest version to avoid compatibility issues.