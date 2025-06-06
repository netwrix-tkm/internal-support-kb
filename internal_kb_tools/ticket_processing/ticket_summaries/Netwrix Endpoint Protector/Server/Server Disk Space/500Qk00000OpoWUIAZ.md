## Ticket Metadata
- **Ticket ID:** 500Qk00000OpoWUIAZ
- **Case Number:** 444162
- **Status:** Closed - Resolved
- **Account/Company:** Eugen Forschner GmbH
- **Contact Name:** Patric Schleicher
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported an error message on the server dashboard indicating low disk space. Despite deleting logs older than the current month, the issue persisted. The message stated that only 10.75 GB of 40.69 GB was free (26%), warning that the functionality and performance of the EPP server could be significantly impacted.

## Environment Details
- The server was running Netwrix Endpoint Protector.
- The disk space was critically low, affecting server performance.

## Troubleshooting Steps
1. Requested access to the hosted server to check the low disk space message.
2. Connected with the customer to review the situation.
3. Confirmed that six months of file shadows were still present and could be deleted.
4. Discussed configuring the Audit Log Backup to run, which had not been previously set up due to innods being at 22%.
5. Advised the customer to select only a few computers for shadowing instead of applying it globally.

## Root Cause
The root cause of the issue was the accumulation of file shadows over six months, which contributed to the low disk space. The Audit Log Backup had not been configured to run, leading to further disk space depletion.

## Solution
The issue was resolved by:
- Deleting the unnecessary file shadows as confirmed by the customer.
- Configuring the Audit Log Backup to run immediately, which would help manage the logs stored in the database.
- Adjusting the shadowing settings to apply only to a limited number of computers, reducing the overall log generation.

## Notes
- It is important to regularly monitor disk space and configure log backups to prevent similar issues in the future.
- Customers should be advised to periodically review and delete old logs and file shadows to maintain optimal server performance.