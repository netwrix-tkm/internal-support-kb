```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CpppcIAB
- **Case Number:** 414478
- **Status:** Closed - Resolved
- **Account/Company:** Allstate Insurance Company
- **Contact Name:** Stealth Audit
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Database
- **Version:** 11.5

## Problem Description
The customer reported an issue with the Access Information Center (AIC) where they received the error message: "No connection to DB in AIC" on the server A0775-APP2359-S.

## Environment Details
- The issue occurred in a production environment for Allstate Insurance Company.
- The AIC service was unable to connect to the database, which was critical for operations.

## Troubleshooting Steps
1. A live Zoom meeting was initiated to troubleshoot the issue, but the customer was unable to join.
2. Suggested checking if the MSSQL Server service was running and if port 1433 was open.
3. Recommended uninstalling and reinstalling the AIC service due to potential changes in service account credentials.
4. Investigated connectivity issues and confirmed that MSSQL ports 1433 and 1434 were not reachable.
5. Advised the customer to check with their firewall team to ensure that the necessary ports were open.

## Root Cause
The root cause of the issue was identified as either the MSSQL Server service being down or the firewall blocking the necessary ports (1433 and 1434) required for database communication.

## Solution
The issue was resolved by confirming that the MSSQL ports were blocked. The customer was instructed to work with their firewall team to open these ports. Once the ports were confirmed to be open, the AIC service was able to connect to the database successfully.

## Notes
- It is important to verify that the necessary database ports (1433 and 1434) are open in the firewall settings to avoid similar connectivity issues in the future.
- If the AIC service account credentials change, it may require uninstalling and reinstalling the AIC service, which does not affect the data in the database.
- Always ensure that leadership approval is obtained before making changes in a production environment, especially when it involves service account modifications.
```