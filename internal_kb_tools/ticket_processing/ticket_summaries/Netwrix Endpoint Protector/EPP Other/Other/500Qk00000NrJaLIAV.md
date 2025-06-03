## Ticket Metadata
- **Ticket ID:** 500Qk00000NrJaLIAV
- **Case Number:** 441430
- **Status:** Closed - Resolved
- **Account/Company:** Barthelmeß EDV-Service GmbH
- **Contact Name:** Alexander Support
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** Not specified

## Problem Description
The customer reported that they had lost the password for WEB-UI access and required support to reset the password.

## Environment Details
- The issue occurred within the Netwrix Endpoint Protector platform.

## Troubleshooting Steps
1. Contacted the client via 3CX to arrange a remote session.
2. Established a remote connection to the server via SSH.
3. Created a snapshot of the current system state for backup purposes.
4. Followed procedure 4 from the backend to change the password for the root admin.
5. Tested the new login credentials to ensure successful access.
6. Confirmed that the client was able to log in and change the password successfully.

## Root Cause
The root cause of the issue was identified as the client forgetting their EPP login password.

## Solution
The issue was resolved by changing the password for the root admin through the backend procedure. After the password reset, the client was able to log in without any issues and confirmed that they could change the password as needed.

## Notes
- It is advisable to remind clients to securely store their passwords to prevent similar issues in the future.
- Always create a snapshot before making significant changes to the system to ensure a recovery point is available.