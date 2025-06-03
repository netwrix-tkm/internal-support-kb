```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000NGYdDIAX
- **Case Number:** 439771
- **Status:** Closed - Resolved
- **Account/Company:** BMW Group AG
- **Contact Name:** Christian Spies
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** Not specified

## Problem Description
The customer reported that a Bluetooth device connected to a computer was not being blocked by the Endpoint Protector (EPP) despite the global rights setting for "Bluetooth other" device type being set to "Deny Access."

## Environment Details
- The affected device was not whitelisted.
- Logs and screenshots were provided for analysis.

## Troubleshooting Steps
1. Reviewed the global rights settings on the Unify console.
2. Checked the settings on the affected node to identify discrepancies.
3. Modified the node settings to align with the global rights configuration.
4. Conducted tests to verify if the Bluetooth device was being blocked as expected.

## Root Cause
The issue was caused by an inconsistency between the global rights set on the Unify console and the device-level settings on the affected node. While the global rights were correctly configured to "Deny Access," the settings on the affected node permitted access, leading to the unintended behavior.

## Solution
The support team realigned the node settings with the Unify console to ensure consistent application of the Bluetooth device blocking policies. After the modification, the customer confirmed that the Bluetooth devices were blocked as expected.

## Notes
- It is recommended to periodically validate global rights settings to ensure they are effectively propagated across all nodes and devices.
- In case of future discrepancies, toggling the settings off and on or removing and re-adding specific devices may help re-establish intended configurations.
- Monitoring processes should be enhanced to detect and prevent similar inconsistencies in the future.
```