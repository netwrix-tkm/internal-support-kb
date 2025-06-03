```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000IMCoAIAX
- **Case Number:** 427192
- **Status:** Closed - Resolved
- **Account/Company:** TrustingSocial
- **Contact Name:** Linh Hoang
- **Product:** Netwrix Endpoint Protector
- **Component:** CAP (Content Aware Protection)
- **Feature:** Client Requests
- **Version:** 5.9.4.1

## Problem Description
The customer reported that the CAP report was showing an incorrect count of matched items. Specifically, when a file containing 20 emails and 16 phone numbers was processed, the report indicated a count of 18, with 16 phone entries and 2 email entries matched. The customer expected the count to reflect all unique entries, totaling 20.

## Environment Details
- The issue was tested on a file containing 20 emails and 16 phone numbers.
- The CAP policy was set to block and report, with the ignore threshold turned OFF.

## Troubleshooting Steps
1. A remote session was created to analyze the issue, but the customer was unable to attend.
2. The support team provided a test build (version 3.0.4.0024) to collect additional logs and better understand the data being sent to the server.
3. The customer was asked to reproduce the issue with the test build and provide new logs.
4. The support team reviewed the logs and confirmed that the EPP counts only unique threats.
5. The customer was advised to ensure that the test file contained unique entries to achieve the expected count.

## Root Cause
The root cause of the issue was identified as a misunderstanding of how the EPP counts threats. The EPP only counts unique threats, meaning if the same email or phone number appears multiple times in the file, it is counted only once. Additionally, the customer had set the threat threshold incorrectly, which affected the reporting.

## Solution
The issue was resolved by clarifying the counting mechanism of the EPP to the customer. The support team explained that:
- EPP counts only unique threats.
- If duplicates exist, they will only contribute to the count once.
- The customer was advised to adjust the threat threshold to match their requirements (e.g., setting it to 20 for the test scenario).

The customer confirmed understanding of the counting process and acknowledged that the behavior was as expected.

## Notes
- Ensure that test files used for CAP policies contain unique entries to avoid confusion in reporting.
- The threat threshold should be set according to the specific requirements of the policy to ensure accurate detection and reporting.
- Future cases should include a clear explanation of how the EPP counts threats to prevent similar misunderstandings.
```