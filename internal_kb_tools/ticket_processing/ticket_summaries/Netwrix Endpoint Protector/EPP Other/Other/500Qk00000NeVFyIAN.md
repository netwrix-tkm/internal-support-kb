## Ticket Metadata
- **Ticket ID:** 500Qk00000NeVFyIAN
- **Case Number:** 440869
- **Status:** Closed - Resolved
- **Account/Company:** The Salvation Army
- **Contact Name:** Martin Jebb
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** 5.9.2.0

## Problem Description
The customer requested an offline installer to upgrade their version of Netwrix Endpoint Protector to mitigate against the vulnerability identified as ADV-2025-010, which pertains to insufficient computational complexity in key derivation.

## Environment Details
- **Current Version:** 5.9.2.0
- **Operating System:** Ubuntu 22.04.2 LTS

## Troubleshooting Steps
1. The support technician requested the current version and Linux distribution of the EPP server from the customer.
2. The customer confirmed they were running version 5.9.2.0 on Ubuntu 22.04.2 LTS.
3. The technician provided a download link for the offline patch (5.9.4.2).
4. Instructions were given on how to apply the offline patch via the EPP UI, including a recommendation to take a snapshot of the server before applying the update.

## Root Cause
The issue stemmed from the customer's use of an outdated version of Netwrix Endpoint Protector (5.9.2.0), which was vulnerable to the identified security issue (ADV-2025-010).

## Solution
The offline patch for version 5.9.4.2 was shared with the customer. The customer was instructed to apply the patch using the EPP UI by navigating to Dashboard -> Live Update -> Offline Patch Uploader, selecting the patch, and following the prompts to complete the update.

## Notes
- It is recommended to always take a snapshot of the server before applying any patches to ensure a rollback option is available in case of issues during the update process.
- Future requests for offline patches should include the current version and operating system details to expedite the support process.