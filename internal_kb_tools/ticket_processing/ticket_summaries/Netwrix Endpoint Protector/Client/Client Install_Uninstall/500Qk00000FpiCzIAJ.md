```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000FpiCzIAJ
- **Case Number:** 421156
- **Status:** Closed - Resolved
- **Account/Company:** Bennett Jones Services Limited
- **Contact Name:** Karan Bhagat
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** 6.2.3

## Problem Description
The customer, Karan Bhagat, reported an issue while attempting to upgrade the existing Netwrix Endpoint Protector agent to version 6.2.3. The upgrade was blocked by SentinelOne, which flagged the installation as suspicious. After disabling SentinelOne, the customer encountered further issues when trying to upgrade or install the agent.

## Environment Details
- **Existing Agent Version:** Not specified
- **New Agent Version:** 6.2.3
- **Security Software:** SentinelOne

## Troubleshooting Steps
1. The customer attempted to upgrade the existing agent to version 6.2.3.
2. The upgrade was blocked by SentinelOne due to a security alert.
3. The customer disabled SentinelOne to proceed with the installation.
4. The customer attempted to upgrade/install the agent again but encountered errors.
5. The customer requested guidance on completely removing the existing software for a fresh installation.

## Root Cause
The issue was primarily caused by SentinelOne's security settings, which flagged the upgrade process as suspicious. This led to the installation being blocked initially. Subsequent errors during the installation attempt were likely due to remnants of the previous agent installation.

## Solution
The issue was resolved by utilizing the Zapp tool, which is designed to completely remove existing installations of the Netwrix Endpoint Protector agent. After using the Zapp tool, the customer was able to perform a fresh installation of the latest version (6.2.3) without further issues.

## Notes
- It is recommended to temporarily disable any security software like SentinelOne during the installation or upgrade of the Netwrix Endpoint Protector agent to prevent similar issues.
- Ensure that the Zapp tool is used to cleanly uninstall any previous versions before attempting a fresh installation to avoid conflicts.
```