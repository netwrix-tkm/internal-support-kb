## Ticket Metadata
- **Ticket ID:** 500Qk00000KTPqpIAH
- **Case Number:** 431763
- **Status:** Closed - Resolved
- **Account/Company:** FcBrasil
- **Contact Name:** Lucas Cavalcante
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** DPI - Other
- **Version:** 4.9

## Problem Description
The customer reported that Data Protection Integration (DPI) could be enabled in global settings, computer settings, and user settings, but it could not be enabled in group settings.

## Environment Details
- The issue was observed in the Netwrix Endpoint Protector platform.
- The customer was using a test computer with custom settings that affected the DPI functionality.

## Troubleshooting Steps
1. Verified that DPI was enabled in global, computer, and user settings.
2. Attempted to enable DPI in group settings but encountered failures.
3. Scheduled a remote session for further investigation on January 15th.
4. Restored global settings on the test computer to default.

## Root Cause
The issue was caused by the presence of custom settings on the test computer, which prevented the successful application of group settings for DPI.

## Solution
The issue was resolved by restoring the global settings on the test computer to their default values. After this restoration, the group settings for DPI were successfully applied.

## Notes
- Ensure that custom settings do not interfere with group configurations in future cases.
- It is advisable to check for any custom configurations before troubleshooting similar issues to expedite resolution.