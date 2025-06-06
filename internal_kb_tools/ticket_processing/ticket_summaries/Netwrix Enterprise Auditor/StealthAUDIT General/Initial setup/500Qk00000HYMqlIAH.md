## Ticket Metadata
- **Ticket ID:** 500Qk00000HYMqlIAH
- **Case Number:** 425193
- **Status:** Closed - Resolved
- **Account/Company:** IBM - Etihad Airways
- **Contact Name:** Praveen Huilgol
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.5.0.230

## Problem Description
The customer reported a TLS vulnerability related to the StealthAUDIT servers, specifically concerning the use of TLS 1.0, which is considered outdated and insecure. The customer requested assistance in addressing this vulnerability.

## Environment Details
- Operating System: Windows Server 2019
- Browser Used: Firefox (for loading AIC)

## Troubleshooting Steps
1. The customer confirmed that TLS 1.0 was enabled on the StealthAUDIT server.
2. Netwrix support requested additional information regarding the vulnerability notification received by the customer.
3. Support escalated the case to management for further assistance.
4. The customer was advised to disable TLS 1.0 to assess if the application would function properly without it.
5. The customer expressed concerns about disabling TLS 1.0 in a production environment without confirming its impact on the application.
6. Further discussions clarified that Netwrix Enterprise Auditor does not require TLS 1.0 and relies on the operating system for security standards.

## Root Cause
The root cause of the issue was the outdated configuration allowing TLS 1.0 on the server, which was enabled during a previous setup to accommodate older browser requirements (specifically Internet Explorer). This configuration was no longer necessary as the environment had transitioned to using Firefox.

## Solution
The issue was resolved by disabling TLS 1.0 on the server. The customer confirmed that after disabling TLS 1.0, the application continued to function properly, thus addressing the vulnerability.

## Notes
- It is important to regularly review and update security protocols to ensure compliance with current standards.
- Future configurations should avoid enabling outdated protocols like TLS 1.0 unless absolutely necessary, and alternatives should be explored to maintain security.
- Always test changes in a controlled environment before applying them to production systems to mitigate risks.