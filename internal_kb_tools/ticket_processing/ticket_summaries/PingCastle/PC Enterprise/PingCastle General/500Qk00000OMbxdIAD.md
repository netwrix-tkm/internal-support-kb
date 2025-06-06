```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000OMbxdIAD
- **Case Number:** 442906
- **Status:** Closed - Resolved
- **Account/Company:** Eurofins GSC IT Poland Sp. z.o.o.
- **Contact Name:** Korepu Akhil Kumar
- **Product:** PingCastle
- **Component:** PC Enterprise
- **Feature:** PingCastle General
- **Version:** 3.2.0.1

## Problem Description
The customer, Akhil Kumar, requested guidance on migrating PingCastle-deployed domains from one server to another. They were unsure whether to uninstall the agent on the current server and reinstall it on the new server with the same or new API and encryption keys, or if there was an alternative migration method.

## Environment Details
- **Current Server:** Hosting PingCastle agent
- **New Server:** Target for migration
- **PingCastle Version:** 3.2.0.1

## Troubleshooting Steps
1. Initial inquiry regarding the migration process and key management.
2. Provided preliminary advice on stopping IIS, copying the database, and reinstalling PingCastle on the new server.
3. Scheduled a meeting to discuss migration details and address specific questions.
4. Clarified the process during the meeting, including:
   - Uninstalling the agent on the old server.
   - Installing the agent on the new server.
   - Handling API keys and encryption keys.

## Root Cause
The issue stemmed from a lack of clarity on the migration process for PingCastle, specifically regarding the handling of API keys and the necessity of uninstalling the agent from the old server before installation on the new server.

## Solution
The following steps were provided to successfully migrate PingCastle:
1. Stop IIS on the current server to ensure the database is not in use.
2. Copy the PingCastle database to the new server.
3. Import the database on the new server.
4. Install PingCastle Enterprise on the new server.
5. If the URL changes, update the agents with the new API endpoint.
6. Set up new API and encryption keys; do not use existing keys.

## Notes
- Ensure that IIS is stopped before migrating to avoid database access issues.
- The existing domains will not create duplicates due to the use of SID.
- Any keys can be reused; however, it is recommended to create new keys for clarity and security.
- Follow up with the customer to ensure they understand the migration steps and are prepared for the process.
```