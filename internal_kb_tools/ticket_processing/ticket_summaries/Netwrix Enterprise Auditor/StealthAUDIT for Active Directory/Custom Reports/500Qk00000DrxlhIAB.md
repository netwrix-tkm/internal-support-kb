## Ticket Metadata
- **Ticket ID:** 500Qk00000DrxlhIAB
- **Case Number:** 416837
- **Status:** Closed - Resolved
- **Account/Company:** Gastro Health
- **Contact Name:** Marcos Lopez
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Custom Reports
- **Version:** Not specified

## Problem Description
The customer reported a data analysis error when running a custom job, specifically stating that certain multi-part identifiers could not be bound.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for Active Directory

## Troubleshooting Steps
1. Reviewed the SQL script associated with the custom job.
2. Identified the error messages indicating that the multi-part identifiers "S.GHOutlookDept" and "S.Employee_Type_Code" could not be bound.
3. Checked for the presence of a table aliased as "S." in the SQL script.

## Root Cause
The root cause of the issue was identified as the absence of a table aliased as "S." in the SQL script. This led to the SQL engine being unable to resolve the specified identifiers.

## Solution
The solution involved removing the "S." alias from the identifiers in the SQL script. After making this adjustment, the custom job was able to run successfully without throwing any errors.

## Notes
- Ensure that all identifiers in SQL scripts are correctly aliased to existing tables to avoid similar binding issues in the future.
- It is advisable to validate SQL scripts for syntax and binding errors before execution, especially when custom modifications are made.