```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CfEMfIAN
- **Case Number:** 414045
- **Status:** Closed - Resolved
- **Account/Company:** IP Steel
- **Contact Name:** Luc Vantroost
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Settings
- **Version:** 1.2

## Problem Description
The client, Ministry French Defense Center, reported issues with user keys that were authorized in the console but blocked by the local agent, even after a forced re-read of policies. Additionally, an "internal server error 500" occurred after attempting to re-read configurations, and the client expressed a need to delete Device, User, and Machine objects that had not been seen for a specified duration.

## Environment Details
- The database contained over 200,000,000 objects, leading to performance issues.
- The console interface only allowed selection of a maximum of 1,000 objects at a time, filtered by "last seen."

## Troubleshooting Steps
1. Attempted to re-read configurations via the console, which resulted in an internal server error (500).
2. Discussed the issue with the client and scheduled a remote session for further investigation.
3. Explored the possibility of automating the deletion of objects based on their last seen date.

## Root Cause
The internal server error (500) was likely caused by the excessive size of the database, which hindered the console's ability to process requests efficiently. The limitations in the console's interface for selecting objects also contributed to the client's difficulties in managing the database.

## Solution
A remote session was conducted to address the client's concerns. During this session, a procedure was provided to automate the deletion of Device, User, and Machine objects that had not been seen for a specified duration. This solution allowed the client to manage their database more effectively and prevent future performance issues.

## Notes
- It is important to monitor the size of the database regularly to avoid performance degradation.
- Consider implementing automated scripts for purging old objects to maintain optimal performance.
- Ensure that clients are aware of the limitations of the console interface regarding object selection.
```