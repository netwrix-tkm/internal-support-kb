## Ticket Metadata
- **Ticket ID:** 500Qk00000MHRLmIAP
- **Case Number:** 436931
- **Status:** Closed - Resolved
- **Account/Company:** Central Bank of Trinidad and Tobago
- **Contact Name:** Ryan Tyson
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Activity
- **Version:** 11.6

## Problem Description
The customer was licensed for Active Directory (AD) Activity monitoring in Netwrix Enterprise Auditor (NEA), but the configuration had not been completed after migrating the implementation to a new environment. The AD job group was not set up correctly, leading to a lack of data collection.

## Environment Details
- The customer had migrated from an old deployment to a new environment.
- The Network Activity Monitoring (NAM) did not have any Domain Controllers (DCs) added, only File Servers (FS).
- The customer was also licensed for Network Traffic Analysis (NTP) for AD.

## Troubleshooting Steps
1. Confirmed if NTP was actively auditing AD activity.
2. Deployed NAM agents on the DCs.
3. Configured NTP for AD activity and set up forwarding to NAM agents.
4. Attempted to configure archiving of AD activity.
5. Investigated issues with API connectivity due to environmental problems.
6. Restored operation of NTP agents and configured NTM for AD policy to send data to NAM agents.

## Root Cause
The primary issue was that the AD Activity collection was never configured after the migration to the new environment. Additionally, there were environmental issues affecting API connectivity, which hindered the configuration process.

## Solution
- Successfully configured AD activity collection in NEA.
- Restored the operation of NTP agents and configured the NTM for AD policy to send data to NAM agents.
- Deployed NAM agents to the DCs and configured archiving of AD activity.
- Although there were issues with the API connection, the AD activity collection was successfully established using an alternative archive method.

## Notes
- Ensure that all necessary components are configured after migrating to a new environment to avoid similar issues.
- Monitor the API connectivity closely, as environmental issues can lead to configuration failures.
- Future deployments should include a checklist to confirm that all job groups and agents are properly set up before closing the ticket.