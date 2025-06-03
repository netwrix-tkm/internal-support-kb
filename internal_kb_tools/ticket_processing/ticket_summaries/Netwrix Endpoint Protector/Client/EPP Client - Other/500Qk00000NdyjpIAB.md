## Ticket Metadata
- **Ticket ID:** 500Qk00000NdyjpIAB
- **Case Number:** 440838
- **Status:** Closed - Resolved
- **Account/Company:** Volksoft Consulting Pvt. Ltd
- **Contact Name:** GANDAY RAKESH KUMAR
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client - Other
- **Feature:** Database Configuration/Capacity
- **Version:** NONE

## Problem Description
The customer reported receiving a "Low Disk Space" error message on their server, indicating that the storage was nearly full.

## Environment Details
- The server was running on a virtual machine environment.
- The initial disk space usage was reported at 95%.

## Troubleshooting Steps
1. **Initial Remote Session (10/04/2025):**
   - Connected remotely to assist the client.
   - Removed shadows older than 60 days, reducing disk usage from 95% to 40%.
   - Client was satisfied with the initial fix.

2. **Follow-Up Session (09/05/2025):**
   - Client reported the issue reoccurred.
   - Scheduled another remote session.

3. **Second Remote Session (15/05/2025):**
   - Discovered a 34 GB file occupying 94% of the root directory.
   - Removed the file, reducing usage to 14%.

4. **Final Remote Session (21/05/2025):**
   - Identified that the occupied storage was within the `/usr` log directory, not shadows.
   - Removed unnecessary files totaling around 48 GB and addressed a persistent banner issue.
   - Agreed to close the case after confirming resolution.

## Root Cause
The initial low disk space issue was primarily caused by the accumulation of old shadow files. Subsequent issues were due to large files and unnecessary log files occupying significant disk space.

## Solution
The issue was resolved by:
- Deleting old shadow files that were no longer needed.
- Identifying and removing large files that were consuming excessive disk space.
- Cleaning up unnecessary log files in the `/usr` directory.

## Notes
- It is crucial for clients to create snapshots of their virtual machines before performing significant changes to avoid potential data loss.
- Regular monitoring of disk space and periodic cleanup of unnecessary files can prevent similar issues in the future.