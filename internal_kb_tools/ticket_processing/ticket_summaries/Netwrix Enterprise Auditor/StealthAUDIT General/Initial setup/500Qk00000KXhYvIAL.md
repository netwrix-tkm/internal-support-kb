```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000KXhYvIAL
- **Case Number:** 431839
- **Status:** Closed - Resolved
- **Account/Company:** USAA
- **Contact Name:** Paul Pitas
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.6.0.138

## Problem Description
The customer reported that when scheduling a Host Discovery with the setting to run Host Inventory upon completion, the Host Inventory does not refresh automatically when the discovery is executed through the schedule. However, it refreshes correctly when the discovery is initiated manually.

## Environment Details
- The customer upgraded to NEA version 11.6.0.138 prior to reporting the issue.

## Troubleshooting Steps
1. Configured Host Discovery settings.
2. Scheduled Host Discovery.
3. Initiated Host Discovery from the schedule.
4. Observed that the Host Inventory did not refresh automatically.

## Root Cause
The issue was identified as a bug in the software that prevented the scheduled Host Inventory refresh from executing correctly. This bug was present in versions prior to NEA v11.6.0.132.

## Solution
The issue was resolved by upgrading the software to NEA version 11.6.0.138, which included a fix for the identified bug. After the upgrade, the scheduled Host Inventory refresh functioned as intended.

## Notes
- Ensure that future upgrades are monitored for similar bugs, especially when new features or scheduling functionalities are introduced.
- It may be beneficial to check the release notes of new versions for any known issues or fixes related to scheduled tasks.
```