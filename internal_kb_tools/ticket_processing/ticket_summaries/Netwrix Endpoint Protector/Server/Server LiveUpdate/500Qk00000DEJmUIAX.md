## Ticket Metadata
- **Ticket ID:** 500Qk00000DEJmUIAX
- **Case Number:** 415346
- **Status:** Closed - Resolved
- **Account/Company:** Laykon Distributor
- **Contact Name:** Faruk Sarı
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server LiveUpdate
- **Version:** NONE

## Problem Description
The customer reported that after applying the "Security Update - Epp Server Hotfix #1.1," the update still appeared incomplete in the update screen. Despite the successful installation and server restart, the Live Update area continued to prompt for the same update.

## Environment Details
- **Customer:** Kamelya Hotel
- **Update Attempted:** Security Update - Epp Server Hotfix #1.1
- **Current Version:** Not specified, but the update prompt was for version 5.9.3.0.

## Troubleshooting Steps
1. Confirmed the installation of the update by checking the view update list in the Live Update.
2. Noted that the update prompt would remain available for version 5.9.3.0 until a future update to version 5.9.4.0 was installed.
3. Advised the customer that if the update was confirmed as installed, they could ignore the update prompt.

## Root Cause
The issue was identified as a normal behavior of the update system, where the prompt for the update remained visible due to the versioning system in place. The update was successfully installed, but the prompt persisted until a subsequent version was released.

## Solution
The issue was resolved by confirming that the update was indeed installed. The customer was informed that the update prompt could be ignored until the next version (5.9.4.0) was available, at which point the prompt would disappear.

## Notes
- Customers should be made aware that update prompts may persist even after successful installations due to versioning settings.
- Future updates to the software may change the visibility of such prompts, so monitoring for new versions is recommended.