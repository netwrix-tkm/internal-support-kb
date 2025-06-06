## Ticket Metadata
- **Ticket ID:** 500Qk00000DwAYzIAN
- **Case Number:** 416953
- **Status:** Closed - Resolved
- **Account/Company:** Demoulas Super Markets
- **Contact Name:** Brian Pavnick
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SharePoint
- **Feature:** Activity Auditing
- **Version:** 11.6

## Problem Description
The customer reported multiple instances of "C:13 Unknown event type, consider adding to SharePointOnlineEventTypeMappings in SharePointActivityMappings.xml" stemming from SPAC jobs. The specific unknown event types included SharingLinkUsed, SharingLinkCreated, CommentsDisabled, CommentCreated, AddedToSharingLink, FileTranscriptContentAccessed, TeamsMeetingRecordingUploaded, and DLPRuleMatch.

## Environment Details
- The issue occurred in the context of SharePoint Online activity monitoring using Netwrix Enterprise Auditor.
- The version of the product in use was 11.6.

## Troubleshooting Steps
1. Reviewed the error messages and identified the unknown event types.
2. Consulted documentation regarding the SharePointActivityMappings.xml file.
3. Discussed the issue internally and with R&D to determine if a fix was in progress.
4. Monitored updates from R&D regarding the hotfix for the identified event types.

## Root Cause
The root cause of the issue was identified as new activity event types being captured by Activity Monitor agents monitoring SharePoint Online that did not have associated mappings in the SharePointActivityMappings.xml file.

## Solution
The issue was resolved through the release of a hotfix, specifically "stealthaudit-hotfix-11.6.0.052". Additionally, the problem was fully addressed in the NEA version 11.6.0.112, which was released on October 4, 2024, and included mappings for the event types outlined in the symptoms.

## Notes
- It is recommended to monitor for any new event types that may arise in the future and ensure they are added to the SharePointActivityMappings.xml file to prevent similar issues.
- Customers experiencing similar issues should consider opening a support case for each new unknown event type until a comprehensive update is provided by R&D.