```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000DBHVvIAP
- **Case Number:** 415231
- **Status:** Closed - Resolved
- **Account/Company:** Diehl Metall
- **Contact Name:** Wolfgang Holst
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.8.1.0 (new appliance), 5.6.0.0 (old installation)

## Problem Description
The customer, Wolfgang Holst, requested download entitlements for upgrading their Netwrix Endpoint Protector appliance from version 5.6.0.0 to 5.8.1.0. They needed to import Backup v2 EPP files from the old installation but were unable to download the necessary files due to a migration of the portal to Netwrix.

## Environment Details
- Current installation licensed until 2025-09-06.
- Managing 150 devices.

## Troubleshooting Steps
1. Confirmed the customer had already performed initial migration steps.
2. Provided links to download the new EPP server image and user manual.
3. Suggested creating a snapshot of the current EPP server.
4. Instructed the customer to ensure both servers (old and new) were on the same version.
5. Provided a detailed update process for the old server to reach version 5.6.0.0:
   - Download and apply offline patches in the specified order:
     - EPP5650
     - EPP5700
     - EPP5710 maintenance
     - EPP5800
     - EPP5810
6. Advised on the backup and restore process for migrating settings and configurations.

## Root Cause
The issue arose from the mismatch in versions between the old and new appliances, which prevented the import of backup files. The customer needed to update the old server to match the new server's version before proceeding with the migration.

## Solution
The issue was resolved by providing the customer with the necessary download links for the offline patches and detailed instructions on how to apply them. Once the old server was updated to the same version as the new server, the customer was able to successfully import the backup files.

## Notes
- Ensure that the server versions match before attempting to import backup files.
- Always create a snapshot of the current server before performing updates.
- The System Backup v2 will only backup database and metadata without logs data, but it retains table structure.
```