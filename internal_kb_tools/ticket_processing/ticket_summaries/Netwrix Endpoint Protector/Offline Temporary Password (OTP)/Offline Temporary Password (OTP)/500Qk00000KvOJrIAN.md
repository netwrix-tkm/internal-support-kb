## Ticket Metadata
- **Ticket ID:** 500Qk00000KvOJrIAN
- **Case Number:** 433130
- **Status:** Closed - Resolved
- **Account/Company:** IHK Region Stuttgart
- **Contact Name:** Florian Bartl
- **Product:** Netwrix Endpoint Protector
- **Component:** Offline Temporary Password (OTP)
- **Feature:** Offline Temporary Password (OTP)
- **Version:** 5.9.4.1

## Problem Description
The customer reported that the generated Offline Temporary Password (OTP) for users and/or computers was not functioning correctly. After entering the OTP in the web interface, the client displayed an error message stating "Ungültiger Freischaltcode" (Invalid activation code).

## Environment Details
- The issue was identified in customers who upgraded to server version 5.9.4.1 before December 24, 2024.

## Troubleshooting Steps
1. Verified the OTP generation process in the web interface.
2. Attempted to enter the OTP on the client device to reproduce the error.
3. Confirmed the error message "Ungültiger Freischaltcode" appeared after correct OTP entry.
4. Identified that the issue was related to a bug in the server version.

## Root Cause
The issue was caused by a bug present in the server version 5.9.4.1, affecting the functionality of the OTP feature for users and computers.

## Solution
An offline patch was provided to resolve the issue. The customer was instructed to apply the following patch:
```
http://download.endpointprotector.com/offline_agent_patches/MP-HWA-EPP4-U0066-M0001.tar.gz
```
After applying the patch, the customer confirmed that the OTP functionality was restored and working correctly.

## Notes
- Ensure that customers who upgrade to server version 5.9.4.1 before December 24, 2024, are informed about this bug and the availability of the patch.
- Recommend testing OTP functionality after any server upgrades to catch similar issues early.