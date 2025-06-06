```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BkVnFIAV
- **Case Number:** 411723
- **Status:** Closed - Resolved
- **Account/Company:** Feral Interactive
- **Contact Name:** Adebola Ogedengbe
- **Product:** Netwrix Endpoint Protector
- **Component:** Server Disk Space
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported that their EPP server deployment VM was running low on disk space, with only 87.7 GB free out of 257.28 GB (34%). They received a notification indicating that server functionality and performance could be severely affected. Despite clearing audit logs and database backups, the issue persisted. The customer also mentioned that they increased the hard disk size to 500 GB, but this change was not reflected on the server.

## Environment Details
- EPP server deployment VM
- Disk size increased to 500 GB (not reflected)
- SSH access was enabled but not usable by the customer

## Troubleshooting Steps
1. Confirmed if an audit log backup process was scheduled.
2. Advised the customer to schedule an audit log backup from the server UI.
3. Suggested checking the server for other potential disk space consumers.
4. Offered to arrange a remote session to assist with expanding the disk size.
5. Scheduled a Zoom session for further assistance.

## Root Cause
The root cause of the issue was identified as the need to expand the main disk partition and configure backend settings to archive logs pertaining to events forwarded to the SIEM.

## Solution
The support team expanded the main disk partition and made backend changes to ensure that logs related to events forwarded to the SIEM would be archived. This resolved the disk space issue, and the customer confirmed that the storage was expanded and the used space on the server appeared to have reduced.

## Notes
- Ensure that an audit log backup process is scheduled regularly to prevent similar issues in the future.
- Only support team members have SSH access to the server; customers should not attempt to SSH into the server for disk management.
- Always create a snapshot of the VM before making significant changes to the disk configuration.
```