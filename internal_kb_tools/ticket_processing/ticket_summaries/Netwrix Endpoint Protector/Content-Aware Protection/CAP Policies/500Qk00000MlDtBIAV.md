## Ticket Metadata
- **Ticket ID:** 500Qk00000MlDtBIAV
- **Case Number:** 438267
- **Status:** Closed - Resolved
- **Account/Company:** Segal Benz
- **Contact Name:** Anoush d'Orville
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** 1.2

## Problem Description
The customer had two questions regarding logging capabilities in the Netwrix Endpoint Protector, specifically about monitoring all printing logs (both blocked and successful) and retaining copies of blocked files for security scanning.

## Environment Details
- The customer is using Netwrix Endpoint Protector with Content Aware Protection policies.

## Troubleshooting Steps
1. Reviewed the customer's request regarding logging of all print jobs.
2. Explained the limitations of the current logging system, which only logs incidents that trigger specific policies.
3. Provided information about the File Shadow feature that can retain copies of blocked files.
4. Advised against enabling the File Shadow feature globally due to high resource usage and potential performance impacts.

## Root Cause
The system is designed to log only incidents that trigger specific policies, which does not include successful print jobs. The request for logging all print jobs is outside the intended functionality of the product.

## Solution
- Informed the customer that it is not possible to log all printing events (both blocked and successful) as the system only logs incidents that trigger policies.
- Confirmed that the File Shadow feature can be used to retain copies of blocked files, but cautioned against enabling it globally due to its resource-intensive nature.

## Notes
- The File Shadow feature is intended for auditing specific users or computers and should not be enabled globally to avoid performance degradation.
- If the customer wishes to log all print jobs, they could theoretically use a regex to classify print jobs with specific criteria, but this is not recommended due to the potential for excessive logging and increased resource consumption.