## Ticket Metadata
- **Ticket ID:** 500Qk00000HsuppIAB
- **Case Number:** 425992
- **Status:** Closed - Resolved
- **Account/Company:** Advent Health System
- **Contact Name:** Paul Williams
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Upgrade
- **Version:** 11.6

## Problem Description
The customer reported an issue with the Netwrix Enterprise Auditor (NEA) where the FS Proxies were unable to establish a secure stream. This issue necessitated an upgrade to patch the problem.

## Environment Details
- **Current Version Prior to Upgrade:** NEA v11.6.0.117
- **FS Proxy Version Prior to Upgrade:** NEA FS Proxy v11.6.0.36

## Troubleshooting Steps
1. Identified the need to upgrade NEA to version 11.6.117 to address the secure stream issue.
2. Planned the upgrade process for both NEA and FS Proxy components.
3. Executed the upgrade to NEA v11.6.0.117 and NEA FS Proxy v11.6.0.36.

## Root Cause
The root cause of the issue was identified as a product defect in the previous versions of NEA and FS Proxy that prevented the establishment of a secure stream.

## Solution
The issue was resolved by upgrading the Netwrix Enterprise Auditor to version 11.6.117 and the FS Proxy to version 11.6.0.36. This upgrade patched the defect that was causing the secure stream connection failure.

## Notes
- Ensure that all components are kept up to date to avoid similar issues in the future.
- Monitor the system after upgrades to confirm that all functionalities are operating as expected.