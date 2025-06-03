```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000IKIHlIAP
- **Case Number:** 427126
- **Status:** Closed - Resolved
- **Account/Company:** Morton Community Bank
- **Contact Name:** Joel Cox
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Additional Tools
- **Version:** Not specified

## Problem Description
The customer, Morton Community Bank, inquired about the necessary configurations for integrating their new on-premise Endpoint Protector with the Netwrix Data Classification system.

## Environment Details
- The customer is implementing a new on-premise Endpoint Protector.
- The integration with Netwrix Data Classification (NDC) had not been tested at the time of the inquiry.

## Troubleshooting Steps
1. Confirmed that Netwrix Endpoint Protector and Netwrix Data Classification are separate products without direct integration.
2. Informed the customer about the current support for metadata scanning.
3. Clarified that while there is no integration, the Endpoint Protector can read metadata tags from documents classified by NDC.
4. Followed up with the customer after their support meeting with NDC to gather additional insights.

## Root Cause
The lack of integration between Netwrix Endpoint Protector and Netwrix Data Classification was the primary issue. The customer was seeking guidance on configurations that were not necessary due to the absence of direct integration.

## Solution
The issue was resolved by informing the customer that:
- There is no individual configuration required for integration since the two products are not integrated.
- The Endpoint Protector can read metadata from Office files and PDFs, allowing for some level of interaction with the data classified by NDC.

## Notes
- Future users should be aware that while metadata scanning is supported, full integration with Netwrix Data Classification is not currently available but is planned for future development.
- Customers should be encouraged to create custom dictionaries in Endpoint Protector to define patterns related to NDC metadata for enhanced functionality.
```