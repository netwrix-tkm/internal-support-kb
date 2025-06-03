## Ticket Metadata
- **Ticket ID:** 500Qk00000MOcdpIAD
- **Case Number:** 437331
- **Status:** Closed - Resolved
- **Account/Company:** Black Sesame Technologies
- **Contact Name:** Tai Ting Tseng
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server
- **Feature:** Reports and Analysis
- **Version:** 5.9.4.1

## Problem Description
The customer reported that logs under the "Report and Analysis" section were incomplete, with several days of logs missing from their view compared to other users.

## Environment Details
- The issue was observed in the Netwrix Endpoint Protector platform, specifically in the Reports and Analysis feature.
- The customer was using an account with limited visibility, only able to view logs for certain departments.

## Troubleshooting Steps
1. The customer confirmed the server version was 5.9.4.1.
2. The customer created a new user with the same rights to check if the issue persisted.
3. The support team requested screenshots of the logs from both the customer and their colleague for comparison.
4. The support team inquired about the filtering conditions used by the customer and their colleague.
5. A remote session was scheduled to investigate the issue further.

## Root Cause
The root cause of the issue was identified as the customer's EPP admin account lacking visibility over all relevant departments. This restriction prevented the customer from seeing all logs.

## Solution
To resolve the issue, the support team added two additional departments to the customer's admin account. After this adjustment, the logs became visible to the customer.

## Notes
- Ensure that admin accounts have the appropriate visibility settings to access all necessary logs.
- For future cases, verify department access and visibility settings as a first step in troubleshooting log visibility issues.