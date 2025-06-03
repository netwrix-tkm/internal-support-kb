## Ticket Metadata
- **Ticket ID:** 500Qk00000OavtBIAR
- **Case Number:** 443570
- **Status:** Closed - Resolved
- **Account/Company:** Chevron Phillips Chemical
- **Contact Name:** Jeff Schemp
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** 6.2.4.2000

## Problem Description
The customer reported that after upgrading to client version 6.2.4.2000, disabled audio devices were automatically re-enabled and could not be disabled again. Stopping the Endpoint Protector service on the workstation temporarily resolved the issue.

## Environment Details
- The issue occurred on workstations running the latest EPP client version (6.2.4.2000) and server version.
- The customer had previously experienced issues with the tray icon for the 6.2.1.2004 agent.

## Troubleshooting Steps
1. Confirmed that the customer was running the latest EPP server and client versions.
2. Suggested upgrading to the latest EPP server and client versions as a potential resolution.
3. Proposed scheduling a remote session to investigate the issue further.
4. Discussed the possibility of reverting to an older client version (6.2.1.2004) to determine if the issue persisted.

## Root Cause
The issue was identified as a product defect related to the latest agent version (6.2.4.2000), which caused disabled audio devices to be re-enabled automatically.

## Solution
The problem was resolved by reverting to the older agent version (6.2.1.2004). This change allowed the customer to successfully disable audio devices without them being re-enabled.

## Notes
- It is important to monitor for any similar issues after deploying newer versions of the EPP client.
- Customers experiencing similar problems should consider reverting to a previous stable version until a fix is confirmed for the latest version.
- Ensure to gather logs from affected workstations for further analysis if issues arise again.