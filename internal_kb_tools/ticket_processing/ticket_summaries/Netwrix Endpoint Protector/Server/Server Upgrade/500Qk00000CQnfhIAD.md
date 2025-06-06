```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CQnfhIAD
- **Case Number:** 413435
- **Status:** Closed - Resolved
- **Account/Company:** Titanium Metals
- **Contact Name:** Kyle Toth
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.9.3.0

## Problem Description
The customer requested offline update files for the Netwrix Endpoint Protector server to perform an upgrade.

## Environment Details
- The customer was using Netwrix Endpoint Protector version 5.9.3.0.
- The system is air-gapped, meaning it cannot connect to the internet for updates.

## Troubleshooting Steps
1. The support technician requested the current version of the EPP Server from the customer.
2. The customer confirmed they were running version 5.8.1.0.
3. The technician informed the customer that multiple offline patches would be needed to upgrade to the latest version.
4. The technician provided download links for the necessary offline patches:
   - EPP 5820 maintenance offline clients patch
   - EPP5900, EPP5910, EPP5920, EPP5930 offline patches
   - Vulnerability fix patch
5. The customer applied the patches and reported back that they were now on version 5.9.0.0.
6. The technician guided the customer on how to check if the vulnerability patch was applied correctly via the Dashboard.
7. The customer reported not seeing the option to view applied patches due to the air-gapped environment.

## Root Cause
The issue stemmed from the customer's air-gapped environment, which limited their ability to register the EPP Server and view applied patches.

## Solution
The technician provided the necessary offline update files and guided the customer through the patch application process. The customer successfully applied the patches and confirmed the upgrade to version 5.9.3.0.

## Notes
- The customer must ensure that all details are filled in the Dashboard -> Live Update to register the EPP Server for future updates.
- The inability to view applied patches is a limitation of operating in an air-gapped environment.
- It is safe to reapply patches if necessary, as it will not cause issues.
```