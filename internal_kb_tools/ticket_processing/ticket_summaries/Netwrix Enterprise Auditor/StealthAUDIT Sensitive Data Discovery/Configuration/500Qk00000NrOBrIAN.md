## Ticket Metadata
- **Ticket ID:** 500Qk00000NrOBrIAN
- **Case Number:** 441440
- **Status:** Closed - Resolved
- **Account/Company:** WellSpan Health
- **Contact Name:** John Masgalas
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT Sensitive Data Discovery
- **Feature:** Configuration
- **Version:** 11.6

## Problem Description
The customer inquired whether wildcards could be used for configuring Sensitive Data False Positives in Netwrix Enterprise Auditor. Specifically, they asked if patterns like `pcnamefolder1*.txt` or `pcnamefolder1data*.txt` were valid.

## Environment Details
- **Product Version:** Netwrix Enterprise Auditor v11.6

## Troubleshooting Steps
1. Reviewed the documentation regarding the use of wildcards in Sensitive Data False Positives.
2. Conducted internal testing to verify the functionality of wildcards in the specified context.
3. Confirmed that the false positive settings must be configured before running the full FileSystem collection.

## Root Cause
The issue stemmed from a lack of clarity regarding the configuration process for false positives in the Netwrix Enterprise Auditor. The customer was unsure if wildcards were supported in the exclusion filters.

## Solution
The resolution involved confirming that wildcards are indeed supported for Sensitive Data False Positives. The customer was instructed to:
- Navigate to **Settings > Sensitive Data > False Positives** to set the appropriate filters.
- Ensure that these settings are configured prior to executing the full FileSystem collection.

## Notes
- It is important to configure false positive exclusion filters before running the full FileSystem collection to ensure that the desired files are excluded from sensitive data detection.
- For future reference, users should consult the following documentation for guidance on adding false positive exclusion filters:
  - [Adding False Positive Exclusion Filters](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/Settings/SensitiveData/Exclusions/Add.htm)
  - [NEA v11.6 - False Positives Tab](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/Settings/SensitiveData/Exclusions/Overview.htm)