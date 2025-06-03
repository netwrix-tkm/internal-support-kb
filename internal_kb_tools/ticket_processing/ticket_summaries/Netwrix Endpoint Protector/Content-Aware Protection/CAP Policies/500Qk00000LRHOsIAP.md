## Ticket Metadata
- **Ticket ID:** 500Qk00000LRHOsIAP
- **Case Number:** 434529
- **Status:** Closed - Resolved
- **Account/Company:** LDS Infotech Pvt. Ltd
- **Contact Name:** Pranay Labde
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** NONE

## Problem Description
The customer reported receiving a pop-up message indicating that a web upload was blocked, despite not attempting to upload any files on the website in question.

## Environment Details
- The issue was related to the Netwrix Endpoint Protector, specifically under the Content-Aware Protection (CAP) policies.

## Troubleshooting Steps
1. The customer confirmed that the file was blocked even though it did not contain the data that triggered the block.
2. Internal checks were initiated to further investigate the issue.

## Root Cause
The root cause of the issue was identified as the Metadata Scanning feature being overly sensitive, leading to false positives in upload detection.

## Solution
To resolve the issue, the Metadata Scanning feature was turned off. This adjustment reduced the number of upload reports and eliminated the unnecessary blocking of uploads that were not actually occurring.

## Notes
- It is important to monitor the impact of turning off Metadata Scanning, as it may reduce the effectiveness of content monitoring.
- Future cases involving false positives in upload detection should consider reviewing the settings of Metadata Scanning and adjusting them as necessary to prevent similar issues.