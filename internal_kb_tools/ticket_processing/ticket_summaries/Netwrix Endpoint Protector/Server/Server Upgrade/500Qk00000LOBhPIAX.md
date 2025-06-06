```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000LOBhPIAX
- **Case Number:** 434405
- **Status:** Closed - Resolved
- **Account/Company:** Grampian Housing Association
- **Contact Name:** Martin Laws
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** NONE

## Problem Description
The customer encountered an error during the upgrade process of the EPP Server from Ubuntu 14 to Ubuntu 22, specifically receiving "Error 2 - errors occurred during installation - contact support." After the migration, the EPP clients displayed an incorrect last seen time, consistently an hour ahead.

## Environment Details
- **Previous OS:** Ubuntu 14
- **New OS:** Ubuntu 22
- **EPP Server UI Path for Time Sync:** "Appliance" > "Server Maintenance"

## Troubleshooting Steps
1. Assisted the customer with the migration in a remote session using backup v2.
2. Verified the migration was successful.
3. Attempted to re-synchronize the time via the EPP Server UI.
4. Conducted a remote session to manually set the correct time via SSH to the EPP Server's backend.

## Root Cause
The issue with the last seen time being consistently an hour ahead was due to incorrect time settings on the EPP Server after the migration.

## Solution
The issue was resolved by manually setting the correct time on the EPP Server's backend using SSH during a remote session. After this adjustment, the last seen time displayed correctly.

## Notes
- Ensure that time synchronization is verified post-migration to prevent similar issues.
- Consider checking time zone settings on the server if discrepancies occur after upgrades.
```