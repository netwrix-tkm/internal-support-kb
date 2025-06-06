## Ticket Metadata
- **Ticket ID:** 500Qk00000IyRCjIAN
- **Case Number:** 428514
- **Status:** Closed - Resolved
- **Account/Company:** Halodata International Pte Ltd
- **Contact Name:** Denni Prima Putra Roli
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** NONE

## Problem Description
The customer reported that their EPP server was inaccessible due to full disk storage and requested assistance to extend the disk storage. A remote session was scheduled for today at 4 PM Indonesia time.

## Environment Details
- **Server Type:** EPP Server
- **Current Storage Status:** Full

## Troubleshooting Steps
1. Confirmed the server was inaccessible due to full storage.
2. Scheduled a remote session with the customer for further assistance.
3. During the remote session, checked the status of the disk partition `/sda4`.
4. Ran a check on `/sda4` which resolved the issue.

## Root Cause
The server encountered an error and entered an initialization frame state due to the disk being full, which rendered it inaccessible.

## Solution
The issue was resolved by performing a check on the `/sda4` disk partition during the remote session, which cleared the error and restored access to the server.

## Notes
- Ensure to monitor disk usage regularly to prevent similar issues in the future.
- Consider implementing alerts for disk space thresholds to proactively manage storage capacity.