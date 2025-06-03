```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000ChBfdIAF
- **Case Number:** 414151
- **Status:** Closed - Resolved
- **Account/Company:** Samsung - SRI Bangalore
- **Contact Name:** Mohammed Shafi
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client - Other
- **Feature:** EPP Client - Other
- **Version:** NONE

## Problem Description
The customer requested assistance in creating a department within the Netwrix Endpoint Protector system.

## Environment Details
- The issue was related to the configuration of departments for deployed computers, which are updated via a live database and server backend accessed through SSH.

## Troubleshooting Steps
1. Scheduled a remote session for Monday at 15:30 IST to assist the customer.
2. During the session, verified that both tools were operational.
3. Provided the following steps to change the department code:
   - Open the EPP tool and change the IP to a random one.
   - Change the department code.
   - Restart the machine.
   - After rebooting, revert the IP back to the original setup for the EPP server and reapply the same department code.
   - Update the policies and verify the changes.

## Root Cause
The initial issue was due to incorrect configuration steps being followed by the customer when attempting to change the department code.

## Solution
The issue was resolved by guiding the customer through the correct steps to change the department code, which involved temporarily changing the IP address and ensuring the policies were updated correctly. The departments for deployed computers were successfully updated via the live database.

## Notes
- Ensure that customers are aware of the need to follow the specific steps for changing configurations in the EPP tool.
- It may be beneficial to provide a checklist or a step-by-step guide for future reference to avoid similar issues.
```