## Ticket Metadata
- **Ticket ID:** 500Qk00000KXIvXIAX
- **Case Number:** 431828
- **Status:** Closed - Resolved
- **Account/Company:** Catchpoint India
- **Contact Name:** Indu Shekhar
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Allowlist / Denylist
- **Version:** 5.9.4.0

## Problem Description
The customer reported an issue with the Content Aware Protection (CAP) policy where modifications to the Default File Allowlist were not being accepted. This resulted in false positive logs for files that had already been whitelisted.

## Environment Details
- The issue was specifically noted in version 5.9.4.0 of the Netwrix Endpoint Protector.
- The problem was not reproducible in version 5.9.4.1.

## Troubleshooting Steps
1. Verified the issue in version 5.9.4.0.
2. Checked if the problem persisted after editing the CAP policy and saving the Allowlist.
3. Observed that after saving and refreshing or logging out, the Allowlist reverted to its previous state.
4. Confirmed that the issue did not occur in version 5.9.4.1.

## Root Cause
The issue was identified as a product defect in version 5.9.4.0, which prevented the proper saving of the Default File Allowlist in the CAP policy.

## Solution
The resolution involved recreating the Allowlist and re-adding it to the CAP policy. After this action, the Allowlist was successfully saved and retained its state after refreshing or logging out.

## Notes
- It is important to monitor for similar issues in future versions, especially when upgrading from version 5.9.4.0 to 5.9.4.1.
- Users should ensure they are on the latest version to avoid encountering this defect.