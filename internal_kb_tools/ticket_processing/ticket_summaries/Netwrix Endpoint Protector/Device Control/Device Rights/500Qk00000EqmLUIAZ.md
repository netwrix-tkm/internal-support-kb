## Ticket Metadata
- **Ticket ID:** 500Qk00000EqmLUIAZ
- **Case Number:** 418994
- **Status:** Closed - Resolved
- **Account/Company:** ProPress Verlagsgesellschaft mbH
- **Contact Name:** Dennis Schäfer
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** NONE

## Problem Description
The customer reported that a program used to sync files to the cloud (Tresorit) was generating a network drive that became blocked after upgrading to client version 6.2.3.1. The previous version, 5.8.2.5, worked without issues.

## Environment Details
- **Affected Software:** Tresorit (cloud sync program)
- **Previous Version:** 5.8.2.5
- **Current Version:** 6.2.3.1
- **Security Software:** Netwrix Endpoint Protector

## Troubleshooting Steps
1. Verified the functionality of the Tresorit program with the older version (5.8.2.5) to confirm the issue was version-specific.
2. Investigated the configuration settings of the Netwrix Endpoint Protector to identify any restrictions related to network drives.
3. Analyzed the behavior of the minifilter driver in relation to network share locations.
4. Discussed potential configuration changes with the customer to resolve the issue.

## Root Cause
The minifilter driver in the new version of the client changed how the network share location was perceived, leading to the Endpoint Protector blocking access to the network drive.

## Solution
The issue was resolved by disabling the minifilter driver, which allowed the network drive to function correctly with the new version of the Tresorit program. The customer agreed to this change.

## Notes
- Disabling the minifilter driver may have implications for security and monitoring; ensure that the customer is aware of potential risks.
- Future updates to the Endpoint Protector or Tresorit may require re-evaluation of this configuration to maintain functionality.