```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000MtOpqIAF
- **Case Number:** 438711
- **Status:** Closed - Resolved
- **Account/Company:** Canada Guaranty
- **Contact Name:** Jaimie Trotman
- **Product:** Netwrix Endpoint Protector
- **Component:** eDiscovery
- **Feature:** eD Policies
- **Version:** Not specified

## Problem Description
The customer needed to perform eDiscovery scans on their file shares to locate tagged documents containing specific custom content. Due to the large size of their file shares, they wanted to limit the scans to specific file types (Word and PDF) but were concerned that using the Policy Denylist would report all documents instead of filtering for the desired content.

## Environment Details
- The customer operates a large file share environment requiring efficient scanning for compliance and data protection.

## Troubleshooting Steps
1. Clarified the functionality of the eDiscovery module and its similarity to the Content Aware Protection (CAP) module.
2. Suggested using the eDiscovery policy to scan for specific sensitive content without scanning all files of a specific type.
3. Recommended adding unwanted file types to the Allowlist and leaving the desired file types unchecked.
4. Discussed the global application of MIME Type allowlists affecting all CAP and eDiscovery policies.
5. Proposed using regex patterns to match specific search criteria as an alternative solution.

## Root Cause
The initial misunderstanding stemmed from the customer's concern that the global settings for file type allowlists would interfere with their existing CAP protections and lead to potential data exfiltration risks.

## Solution
The issue was resolved by advising the customer to:
- Use the Allowlist to specify which file types to scan (i.e., Word and PDF) while ensuring that other file types are not selected.
- Consider using regex patterns to refine their search criteria for specific content without impacting the overall scanning process.

## Notes
- The settings in the MIME Type allowlists apply globally, affecting all policies, which may lead to unintended consequences if not managed carefully.
- It is recommended to use regex patterns sparingly, as excessive use may degrade the performance of the Endpoint Protector server.
- Future users should be aware of the implications of global settings on both eDiscovery and CAP policies to avoid conflicts.
```