## Ticket Metadata
- **Ticket ID:** 500Qk00000OoLmcIAF
- **Case Number:** 444089
- **Status:** Closed - Resolved
- **Account/Company:** UCLA Health
- **Contact Name:** Eric Caparros
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** 5.9.4.1

## Problem Description
The client reported encountering a 'low disk space' error on their Netwrix Endpoint Protector server.

## Environment Details
- The issue was observed on version 5.9.4.1 of the Netwrix Endpoint Protector.
- Previous tickets related to the same issue were noted, indicating a recurring problem.

## Troubleshooting Steps
1. Requested customer approval to access the backend of the server for further investigation.
2. Upon receiving approval, connected to the hosted EPP server.
3. Performed a disk cleanup procedure to free up space.

## Root Cause
The root cause of the issue was insufficient disk space on the server, which had been a recurring problem for the client.

## Solution
The issue was resolved by executing a disk cleanup procedure, which successfully cleared up the necessary disk space on the server.

## Notes
- This issue has been recurring every few months for the client, suggesting a need for ongoing monitoring of disk space.
- It was noted that newer EPP appliances have a larger allocated space on the system partition (50GB compared to the old 20GB), which may help mitigate similar issues in the future.
- Consider advising clients on regular maintenance and monitoring of disk space to prevent recurrence of this issue.