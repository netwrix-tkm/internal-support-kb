## Ticket Metadata
- **Ticket ID:** 500Qk00000PcScnIAF
- **Case Number:** 446285
- **Status:** Closed - Resolved
- **Account/Company:** Halodata International Pte Ltd
- **Contact Name:** Halodata Support Tech
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Deployment
- **Version:** None

## Problem Description
The customer reported that after upgrading their RHEL operating system from version 8.7 to 8.10, the RHEL clients still displayed as version 8.7 in the Netwrix Endpoint Protector Device Manager. The customer was concerned whether this discrepancy was merely cosmetic or if it could lead to production impacts, such as modules not functioning correctly.

## Environment Details
- **Client OS Version:** RHEL 8.7 (originally deployed)
- **Client Agent Version:** 2.1.0.6
- **EPP Server Version:** 5.8.0.0 (as of December 2023)
- **Current Client OS Version:** RHEL 8.10 (recently upgraded)

## Troubleshooting Steps
1. Conducted a health check on the connected computers via the Device Manager.
2. Verified that the RHEL clients were online and licensed.
3. Confirmed that the OS version displayed in the Device Manager was still RHEL 8.7 despite the upgrade to RHEL 8.10.
4. Assessed whether the outdated client agent could cause any production impacts.

## Root Cause
The issue was identified as being caused by the outdated RHEL client agent (version 2.1.0.6) that was not updated following the upgrade of the operating system to RHEL 8.10. This resulted in the Device Manager displaying the incorrect OS version.

## Solution
The support team provided the customer with the latest available RHEL agent to resolve the issue. The customer was advised to upgrade the RHEL clients to the latest agent version to ensure proper functionality and accurate reporting of the OS version in the Device Manager.

## Notes
- It is crucial to keep client agents updated in line with operating system upgrades to avoid discrepancies in reporting and potential functionality issues.
- Regular health checks and updates should be scheduled to ensure all components are compatible and functioning as intended.