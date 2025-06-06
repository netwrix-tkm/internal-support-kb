## Ticket Metadata
- **Ticket ID:** 500Qk00000CgyIeIAJ
- **Case Number:** 414155
- **Status:** Closed - Resolved
- **Account/Company:** SIBAN CORPORATE GROUP, S.L.U.
- **Contact Name:** Juan Vicente Muñoz
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Health
- **Version:** 5.0

## Problem Description
The customer, Juan Vicente Muñoz from ITB, reported an issue with the Netwrix Endpoint Protector server where, although the server started without any IP problems, he was unable to connect to a PC through the browser.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Location:** GRUPO PEOSA, Spain

## Troubleshooting Steps
1. Scheduled a remote session to investigate the issue further.
2. Attempted to connect to the main server to assess its functionality.
3. Reviewed server logs and configurations for any anomalies.
4. Discussed potential issues with the database integrity.

## Root Cause
The issue was identified as a corrupted database, which prevented successful connections to the PCs through the browser.

## Solution
To resolve the issue, a backup of the database was imported, restoring its integrity and allowing successful connections to the PCs through the browser.

## Notes
- Ensure regular backups of the database to prevent similar issues in the future.
- Monitor the health of the database and server to catch potential corruption early.
- Consider implementing alerts for database integrity checks to enhance proactive maintenance.