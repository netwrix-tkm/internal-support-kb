## Ticket Metadata
- **Ticket ID:** 500Qk00000OqemmIAB
- **Case Number:** 444230
- **Status:** Closed - Resolved
- **Account/Company:** Allianz Life Insurance Company of North America
- **Contact Name:** Mounica Devi Meka
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** NEA Web Report Console
- **Version:** 11.5

## Problem Description
The customer reported that a security scan detected port 81 as open for HTTP on their server, despite the configuration being set to use HTTPS on port 481.

## Environment Details
- **Server Configuration:** IIS (Internet Information Services)
- **Current Product Configuration:** HTTPS on port 481

## Troubleshooting Steps
1. Customer ran a security scan which indicated that port 81 was open for HTTP.
2. Confirmed that the product had been configured to use HTTPS on port 481.
3. Investigated IIS settings and found that port 81 was still enabled.
4. Disabled port 81 in IIS to prevent it from being detected as open.
5. Awaited the results of a follow-up security scan to confirm the resolution.

## Root Cause
The issue was caused by the IIS configuration, where port 81 remained open even after the product was configured to use HTTPS on port 481. This required manual intervention to disable the unused port.

## Solution
The resolution involved disabling port 81 in the IIS settings. After this change, the customer was advised to run another security scan to verify that the issue was resolved. The customer confirmed that subsequent scans returned no issues.

## Notes
- It is important to manually check and disable any unused ports in IIS after changing configurations to avoid similar detection issues in the future.
- Customers should be advised to run security scans after making configuration changes to ensure compliance and security.