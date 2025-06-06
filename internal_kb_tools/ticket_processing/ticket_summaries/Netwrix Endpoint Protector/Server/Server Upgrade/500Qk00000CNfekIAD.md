## Ticket Metadata
- **Ticket ID:** 500Qk00000CNfekIAD
- **Case Number:** 413286
- **Status:** Closed - Resolved
- **Account/Company:** Avantor
- **Contact Name:** Karthikeyan Ravi
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.8.1.0 (implied from the context of the case)

## Problem Description
The customer, Avantor, inquired about the advisory regarding remote code execution vulnerabilities in CoSoSys Endpoint Protector (ADV-2024-002) and sought guidance on applying the necessary hotfix, which was not visible in their console.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Current Version:** 5.8.1.0 (as indicated by the customer's inquiry about compatibility with the offline patch)

## Troubleshooting Steps
1. Customer was advised to check for the hotfix under "Dashboard > Live Update".
2. Customer attempted to use the 'Check Now' button but did not see the hotfix version.
3. Support provided a link to download an offline patch for environments running version 5.9.2.0 or lower.
4. Instructions were given to use the "Offline Patch Uploader" from the "Live Update" page to apply the downloaded patch.

## Root Cause
The hotfix was not automatically applied to the customer's environment, which was running an older version of the software (5.8.1.0). The hotfix was available only through manual application, and the customer did not initially see the option in their console.

## Solution
The issue was resolved by providing the customer with a direct link to download the offline patch required for their version (5.8.1.0). The customer was instructed to upload the patch using the "Offline Patch Uploader" feature in the Netwrix Endpoint Protector console.

## Notes
- Ensure that customers are aware that for versions <= 5.9.2.0, an offline patch is necessary for upgrades.
- Always confirm the current version of the customer's software to provide accurate patching instructions.
- Advise customers to regularly check for updates in the "Live Update" section to stay informed about available patches.