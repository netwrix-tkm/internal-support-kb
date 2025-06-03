```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BggcPIAR
- **Case Number:** 411556
- **Status:** Closed - Resolved
- **Account/Company:** Get On Technology Co.
- **Contact Name:** Calvin Chou
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Allowlist / Denylist
- **Version:** Not specified

## Problem Description
The customer requested assistance in setting up a policy to scan and block files containing credit card information while allowing files without such information to be transferred.

## Environment Details
The customer was unsure of the version of the DLP server they were using.

## Troubleshooting Steps
1. Informed the customer to check the version in the lower right corner of the UI.
2. Suggested creating a Content-Aware Protection (CAP) policy by selecting the credit card option in the predefined content tab.
3. Advised the customer to deselect file types from the policy to ensure only files containing credit card information would be blocked.
4. Provided a link to the relevant documentation for further guidance.

## Root Cause
The initial configuration of the CAP policy was set to check all file types, which caused files without credit card information to be blocked inadvertently.

## Solution
The issue was resolved by instructing the customer to:
- Deselect the file types from the policy settings.
- Enable the policy after making the changes.
- Use a valid credit card number format for testing, as certain formats (e.g., 1111-2222-3333-4444) may not be detected by the system.

## Notes
- Ensure that the predefined content selected in the policy is appropriate for the intended use case to avoid false positives.
- Valid credit card numbers should be used for testing to confirm the policy's effectiveness.
- Always verify the version of the DLP server to ensure compatibility with the provided instructions.
```