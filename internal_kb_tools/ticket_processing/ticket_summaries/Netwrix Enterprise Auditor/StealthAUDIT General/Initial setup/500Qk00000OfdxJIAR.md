## Ticket Metadata
- **Ticket ID:** 500Qk00000OfdxJIAR
- **Case Number:** 443784
- **Status:** Closed - Resolved
- **Account/Company:** Broadview Federal Credit Union (Formally Capital Communications Federal Credit Union (CAP COM))
- **Contact Name:** Marc Payzant
- **Product:** Netwrix Enterprise Auditor
- **Component:** Active Directory Activity Collection
- **Feature:** Initial setup
- **Version:** 11.6

## Problem Description
The customer required assistance in setting up the AD_ActivityCollection Job within the Netwrix Access Analyzer (Netwrix Enterprise Auditor). The job was not configured to collect data, which was impacting their monitoring capabilities.

## Environment Details
- The Domain Controller (DC) agent was monitored by NTP (Network Time Protocol).
- Logs were being stored in NAM (Netwrix Access Manager).

## Troubleshooting Steps
1. Launched the Netwrix Access Analyzer (NAA) console.
2. Expanded the Active Directory group.
3. Expanded the "6.Activity" section.
4. Expanded the "0.Collection" and selected the AD_ActivityCollection.

## Root Cause
The AD_ActivityCollection Job was not configured to collect data, which was the primary reason for the customer's inability to monitor Active Directory activities effectively.

## Solution
Provided step-by-step instructions on how to configure the AD_ActivityCollection Job in the Netwrix Access Analyzer/Enterprise Auditor. The instructions included:
- Accessing the NAA console.
- Navigating through the Active Directory settings to properly set up the collection job.

For detailed configuration steps, refer to the following link: [Netwrix Help Center - AD Activity Collection](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Solutions/ActiveDirectory/Activity/AD_ActivityCollection.htm)

## Notes
- Ensure that the AD_ActivityCollection Job is configured immediately after installation to avoid monitoring gaps.
- Regularly verify the configuration to ensure data collection is functioning as expected.
- Monitor logs in NAM to confirm that data is being collected and stored correctly.