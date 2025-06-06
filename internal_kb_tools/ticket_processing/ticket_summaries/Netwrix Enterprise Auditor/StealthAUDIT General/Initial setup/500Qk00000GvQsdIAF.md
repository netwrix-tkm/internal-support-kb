## Ticket Metadata
- **Ticket ID:** 500Qk00000GvQsdIAF
- **Case Number:** 423690
- **Status:** Closed - Resolved
- **Account/Company:** Saginaw Chippewa Indian Tribe
- **Contact Name:** Amy Gates
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.6

## Problem Description
The customer reported that their CDSA job was failing after an upgrade from Netwrix Enterprise Auditor (NEA) version 11.5 to version 11.6, with specific errors indicating that multiple properties, such as "1to2Years," were not found.

## Environment Details
- **Previous Version:** NEA 11.5
- **Current Version:** NEA 11.6
- **Job Type:** CDSA Job

## Troubleshooting Steps
1. Conducted a call with the customer to discuss the issue.
2. Created a new instance of the CDSA job named "CDSA1."
3. Ran the new CDSA job, which executed successfully without errors.
4. Verified that the generated PowerPoint presentation files were populated correctly.
5. Reviewed the logs for any specific module failures associated with the CDSA job.
6. Suggested replacing the old version of the CDSA job with the new version available in NEA 11.6.
7. Recommended enabling DEBUG logging for more detailed error information.

## Root Cause
The failure of the CDSA job was attributed to the upgrade from NEA 11.5 to 11.6, which introduced changes that rendered the previous job configuration incompatible. The specific properties that were missing were likely related to the old job setup.

## Solution
The issue was resolved by creating a new CDSA job instance ("CDSA1") after the upgrade to NEA 11.6. This new job ran successfully without errors and generated the required reports. It was confirmed that the new job configuration was compatible with the updated software version.

## Notes
- Ensure that all relevant jobs are run prior to executing the CDSA job, especially if the customer is not licensed for certain modules.
- For future reference, consider replacing old job versions with new ones after an upgrade to avoid compatibility issues.
- Documentation links for the CDSA job and instant jobs were provided for further guidance:
  - [CDSA Job Documentation](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/CDSA/Job.htm)
  - [Instant Jobs Overview](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/Jobs/InstantJobs/Overview.htm)
  - [CDSA Presentation Documentation](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/CDSA/Presentation.htm)