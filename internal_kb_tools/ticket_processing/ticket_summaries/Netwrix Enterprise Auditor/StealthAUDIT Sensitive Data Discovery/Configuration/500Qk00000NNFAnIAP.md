## Ticket Metadata
- **Ticket ID:** 500Qk00000NNFAnIAP
- **Case Number:** 440125
- **Status:** Closed - Resolved
- **Account/Company:** Netwrix Technical Support
- **Contact Name:** Tay Caliguiri
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT Sensitive Data Discovery
- **Feature:** Configuration
- **Version:** 11.6

## Problem Description
The customer reported an issue where a test false positive created for a file containing sensitive data was not being marked as excluded in the Sensitive Data Discovery (SDD) feature. The customer noted that while the SDD feature was not functioning as expected for file systems (FS), it was working correctly for SharePoint (SP).

## Environment Details
- **Product Version:** 11.6
- **Build Number:** 135

## Troubleshooting Steps
1. The customer created a test false positive on a file with sensitive data.
2. Various paths were attempted to configure the false positive, ensuring all SDD criteria were selected.
3. The customer confirmed that the SDD feature worked correctly for SharePoint but not for file systems.

## Root Cause
The issue was identified as a configuration error where the path to the file was not specified correctly. The false positive must be in UNC/Share format and directly point to the file for it to be recognized by the SDD feature.

## Solution
To resolve the issue, the customer was advised to ensure that the path to the file was specified in the correct UNC/Share format. This adjustment allowed the SDD feature to correctly recognize and mark the file as excluded.

## Notes
- Ensure that all paths used in the SDD configuration are in UNC/Share format when working with file systems.
- This issue does not affect the functionality of the SDD feature for SharePoint, which operates independently of file system configurations.