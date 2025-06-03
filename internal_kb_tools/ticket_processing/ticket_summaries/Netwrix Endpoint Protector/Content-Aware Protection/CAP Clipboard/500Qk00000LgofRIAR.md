## Ticket Metadata
- **Ticket ID:** 500Qk00000LgofRIAR
- **Case Number:** 435241
- **Status:** Closed - Resolved
- **Account/Company:** QBurst
- **Contact Name:** Sabeesh Thomas
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Clipboard
- **Version:** None

## Problem Description
The customer reported that Content-Aware Protection (CAP) policies were not functioning correctly on multiple machines, allowing users to copy and paste content even when it was supposed to be blocked. This issue needed to be resolved before an upcoming client audit.

## Environment Details
- **Affected Systems:** More than 90 Ubuntu 22.04 systems
- **Initial Build Version:** 2.4.4.1004

## Troubleshooting Steps
1. Verified the configuration of the CAP policies and regex settings for clipboard restrictions.
2. Observed that the EPP clients on Ubuntu 22.04 endpoints were intermittently unresponsive, requiring manual restart of the service.
3. Collected logs and video evidence from the customer to analyze the issue further.
4. Provided test builds to the customer for evaluation.
5. Identified that the clipboard restrictions were not enforced due to a flaw in the regex implementation in the initial build.

## Root Cause
The initial Linux build "2.4.4.1004" did not enforce clipboard restrictions correctly due to a basic/simple regular expression that failed to detect all text, allowing users to bypass the clipboard restrictions.

## Solution
The issue was resolved by providing the customer with a test build "v2.4.4.1," which corrected the clipboard restriction functionality. After deploying this build, the clipboard restrictions were enforced as intended, and the case was closed.

## Notes
- Ensure that regex configurations for clipboard restrictions are thoroughly tested before deployment to prevent similar issues.
- Monitor the performance of EPP clients on Ubuntu systems, especially after updates, to catch any potential service interruptions early.
- Customer feedback indicated appreciation for the timely support provided, highlighting the importance of quick resolution in critical situations.