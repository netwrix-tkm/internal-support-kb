## Ticket Metadata
- **Ticket ID:** 500Qk00000KjZyzIAF
- **Case Number:** 432572
- **Status:** Closed - Resolved
- **Account/Company:** MUFG Bank, LTD.
- **Contact Name:** Michael Kong
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Upgrade
- **Version:** 11.5.0.214

## Problem Description
The customer requested guidance on upgrading from version 11.5 to 11.6 of the Netwrix Enterprise Auditor, specifically asking for steps to perform the upgrade and any known issues associated with it.

## Environment Details
- **Current Version:** 11.5.0.214
- **Target Version:** 11.6.0.131
- **Components Upgraded:** NEA, AIC, all proxy servers, and SDD.

## Troubleshooting Steps
1. Conducted a pre-flight check to ensure readiness for the upgrade.
2. Provided the customer with the necessary steps for the upgrade process.
3. Executed the upgrade to version 11.6.
4. Verified the functionality of the AIC and reporting portal post-upgrade.
5. Ran file system schema jobs and active directory inventory to confirm operational integrity.

## Root Cause
The issue was a routine upgrade from an older version (11.5) to a newer version (11.6) of the Netwrix Enterprise Auditor, which required careful execution to ensure all components functioned correctly post-upgrade.

## Solution
The upgrade was successfully completed, transitioning from version 11.5.0.214 to 11.6.0.131. Post-upgrade, the NEA was tested to confirm that all jobs were operational, and the AIC was verified to be starting and providing accurate information. The customer was satisfied with the results and requested a follow-up meeting to ensure Single Sign-On (SSO) functionality.

## Notes
- Ensure that pre-flight checks are always performed before an upgrade to identify any potential issues.
- It is advisable to schedule a follow-up meeting post-upgrade to confirm that all functionalities, including SSO, are working as expected.
- Document any specific issues encountered during the upgrade process for future reference.