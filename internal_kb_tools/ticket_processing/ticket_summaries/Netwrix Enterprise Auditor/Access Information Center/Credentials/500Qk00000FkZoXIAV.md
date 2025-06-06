```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000FkZoXIAV
- **Case Number:** 421046
- **Status:** Closed - Resolved
- **Account/Company:** Apex Tool Group
- **Contact Name:** Michael Nanos
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Credentials
- **Version:** 11.6.0.23

## Problem Description
During a Proof of Concept (PoC) installation, the Access Information Center (AIC) was unable to connect to the database post-installation, despite successful installation and validation of database credentials.

## Environment Details
- Fresh installation of AIC version 11.6.0.23
- SQL authentication was used
- NEA was installed on the same machine with the same database and credentials without issues.

## Troubleshooting Steps
1. Verified the installation process and confirmed that the installer ran without issues.
2. Attempted to log in using 'admin/sb' credentials, which failed.
3. Checked the AIC logs, which indicated: 
   ```
   Format of the initialization string does not conform to specification starting at index 92.
   ```
4. Performed a complete wipe of AIC components and reinstalled using a new download to rule out file corruption.
5. Ensured that the downloaded installer was unblocked.
6. Consulted with the SWAT team regarding potential corruption in the configuration file.
7. Collected and reviewed logs from the installation for further analysis.

## Root Cause
The issue was traced back to how KeePass generated the password for the database connection. It was determined that entering a special character into the password manually before copying it over resolved the connection issue. There were no specific limitations identified regarding the use of special characters in passwords.

## Solution
The problem was resolved by manually entering a special character into the password before copying it from KeePass. This adjustment allowed the AIC to successfully connect to the database.

## Notes
- Future users should be aware that password generation tools like KeePass may not handle special characters correctly in some cases. Manual entry of passwords may be necessary to ensure proper formatting.
- No specific limitations around passwords with special characters were identified, but caution is advised when using password managers.
```