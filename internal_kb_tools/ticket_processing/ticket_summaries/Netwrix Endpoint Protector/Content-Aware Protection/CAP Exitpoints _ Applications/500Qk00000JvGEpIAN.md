## Ticket Metadata
- **Ticket ID:** 500Qk00000JvGEpIAN
- **Case Number:** 430756
- **Status:** Closed - Resolved
- **Account/Company:** Communication Links
- **Contact Name:** Anil Bisht
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Exitpoints / Applications
- **Version:** NONE

## Problem Description
The client, Powerweave, reported multiple issues with the Netwrix Endpoint Protector (EPP), including email blocking due to PNG signatures, file replacement prompts during file copying, and incomplete audit log backups.

## Environment Details
- **Server ID:** F025XQ84
- **Client Requirements:**
  - License allocation from auto to manual.
  - Automatic backup of logs to a local path with deletion from the server.
  - Filtering options for reports by department or policy.
  - Inquiry about allocated storage size for logs and shadow copies on the Cloud Server.

## Troubleshooting Steps
1. Attempted to add the PNG signature file to the "Allowed File" section under Allowlists.
2. Applied the "Allowed File" rule in the Content-Aware Protection (CAP) policy.
3. Investigated the file replacement prompt when copying files through the network drive.
4. Reviewed the audit log backup settings to identify missing Device Control logs.

## Root Cause
The email blocking issue was caused by the strict file format restrictions in the CAP policy, which did not recognize the newly added PNG signature in the allowed list. The file replacement prompt was likely due to a misconfiguration in the network drive settings, and the incomplete audit log backups were a result of the logging configuration focusing solely on Content Aware Protection.

## Solution
- Adjusted the CAP policy to ensure that the PNG signature was correctly recognized and allowed, resolving the email blocking issue.
- Corrected the network drive settings to prevent unnecessary file replacement prompts during file copying.
- Updated the audit log backup configuration to include Device Control logs alongside Content Aware Protection logs.

## Notes
- Ensure that any new file formats added to the allowed list are properly validated in the CAP policy to prevent similar email blocking issues.
- Regularly review logging configurations to ensure all necessary logs are captured and backed up.
- Consider documenting any changes made to policies or configurations for future reference and troubleshooting.