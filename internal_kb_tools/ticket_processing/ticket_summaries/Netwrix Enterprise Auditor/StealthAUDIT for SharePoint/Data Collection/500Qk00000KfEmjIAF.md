```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000KfEmjIAF
- **Case Number:** 432331
- **Status:** Closed - Resolved
- **Account/Company:** Liberty Bank
- **Contact Name:** Philip Richards
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SharePoint
- **Feature:** Data Collection
- **Version:** 11.6

## Problem Description
The customer reported that the agent-less SPSEEK scanning on their on-premises SharePoint resulted in 0 files and 0 folders being scanned, despite having confirmed the existence of sites within the web app and appropriate permissions.

## Environment Details
- SharePoint Web App URL: https://banknotes.liberty-bank.com/
- SQL Server: LH2PRDSPSQL01
- Service Account: LIBBANKnwxad
- Central Admin App Server: LH2PRDSPAPP01

## Troubleshooting Steps
1. Verified permissions for the LIBBANKnwxad service account on the SharePoint web app and associated content databases.
2. Checked the configuration of the Site Collection Auditor policy to ensure it granted Open Items permissions.
3. Confirmed that the service account was added to the Backup Operators and WSS_WPG local groups on the SharePoint central admin app server.
4. Tested network ports to ensure connectivity between servers.
5. Reviewed debug job logs for errors related to scanning personal sites and other resources.
6. Conducted an Access Report test, which indicated issues accessing the config and content databases.
7. Examined SQL Server Configuration Manager for the correct alias configuration pointing to the SQL Server.

## Root Cause
The issue was identified as a typo or incorrect entry of the SQL Server alias in the configuration, which led to the scanning job failing to access the necessary databases.

## Solution
To resolve the issue, the SQL Server alias was corrected to ensure it pointed to the correct server (LH2PRDSPSQL01). This adjustment allowed the data collection query to function properly, enabling the scanning job to access the required files and folders.

## Notes
- Ensure that all SQL Server aliases are accurately configured and consistent across the environment to prevent similar issues in the future.
- Regularly verify permissions and configurations after any changes to the SharePoint environment to maintain scanning functionality.
```