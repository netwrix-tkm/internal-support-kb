## Ticket Metadata
- **Ticket ID:** 500Qk00000OqWsVIAV
- **Case Number:** 444228
- **Status:** Closed - Resolved
- **Account/Company:** Bank of America Corporation
- **Contact Name:** Greg Dieter
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.5

## Problem Description
The customer requested verification of the recommended method for updating the `getExchLocation` function to support new countries and to update hosts with the PADC (default site) in `ExchLocation` to ensure they re-process correctly in the `getExchLocation` function.

## Environment Details
- The issue pertains to a heavily customized environment where the `getExchLocation` function is part of the HOST MANAGEMENT job (MergeSORHosts child job).
- The default FSAA scanning site is PADC.
- The jobs reside on the REPORTING servers.

## Troubleshooting Steps
1. Reviewed the current implementation of the `getExchLocation` function.
2. Identified that the function assigns `ExchLocation` for hosts with blank `ExchLocations`.
3. Noted that hosts with no COUNTRY or STATE in the SA_SORHosts table are assigned to the `ExchLocation` PADC.
4. Investigated the possibility of modifying the existing analysis task to include scanning new locations and cleaning up old locations.
5. Consulted with Professional Services for guidance on modifying the custom analysis task.

## Root Cause
The issue stemmed from the need to update the `getExchLocation` function to accommodate new countries and to clean up old `ExchLocation` assignments for hosts that were no longer valid. The existing function was not designed to automatically reprocess hosts assigned to PADC when they received valid COUNTRY or STATE data.

## Solution
The resolution involved referring the case to Professional Services to assess the feasibility of modifying the custom analysis task. They determined that it was possible to update the `getExchLocation` function to:
- Reprocess PADC hosts weekly when the HOST MANAGEMENT job runs to update the `ExchLocation` to the appropriate site.
- Create an analysis task to manually reset the `ExchLocation` for hosts that needed to move out of PADC.

## Notes
- It is important to ensure that any modifications to the `getExchLocation` function are thoroughly tested in a non-production environment before applying them to production.
- Future updates to the function should consider the implications of changes on existing hosts and ensure that the cleanup process is efficient to avoid unnecessary resource usage.