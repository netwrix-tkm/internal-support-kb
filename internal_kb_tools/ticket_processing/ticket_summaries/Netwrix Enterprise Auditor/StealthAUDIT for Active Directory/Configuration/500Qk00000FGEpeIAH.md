## Ticket Metadata
- **Ticket ID:** 500Qk00000FGEpeIAH
- **Case Number:** 419858
- **Status:** Closed - Resolved
- **Account/Company:** Marsh & McLennan Companies
- **Contact Name:** Kay Groth
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Configuration
- **Version:** 11.5

## Problem Description
The customer reported a violation of the PRIMARY KEY constraint 'PK_SA_ADInventory_EffectiveGroupMembers', indicating that an attempt was made to insert a duplicate key into the database table 'dbo.SA_ADInventory_EffectiveGroupMembers'. The error message specified that the duplicate key value was (2290937, 3784170), and the SQL statement was terminated as a result.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Previous Version:** 11.5
- **Current Version:** 11.6 (after resolution)

## Troubleshooting Steps
1. Reviewed the error message to identify the specific PRIMARY KEY constraint violation.
2. Checked the database for existing entries that matched the duplicate key values.
3. Investigated the configuration settings in the Netwrix Enterprise Auditor to determine if there were any misconfigurations leading to the duplicate key insertion.
4. Consulted internal documentation for known issues related to PRIMARY KEY constraints in version 11.5.
5. Upgraded the software to version 11.6 to see if the issue was addressed in the latest release.

## Root Cause
The issue was identified as a product defect in version 11.5 of the Netwrix Enterprise Auditor, which allowed for the insertion of duplicate keys into the database, violating the PRIMARY KEY constraint.

## Solution
The issue was resolved by upgrading the Netwrix Enterprise Auditor from version 11.5 to version 11.6. This upgrade included fixes for the identified product defect, preventing the occurrence of duplicate key insertions.

## Notes
- It is recommended to always keep the Netwrix Enterprise Auditor updated to the latest version to avoid similar issues related to database constraints.
- Monitor the database for any anomalies after upgrades to ensure that no new issues arise from the changes made.