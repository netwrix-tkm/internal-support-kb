## Ticket Metadata
- **Ticket ID:** 500Qk00000MfRyrIAF
- **Case Number:** 438034
- **Status:** Closed - Resolved
- **Account/Company:** CRH
- **Contact Name:** Martin Brooks
- **Product:** PingCastle
- **Component:** PC Professional
- **Feature:** PingCastle General
- **Version:** 3.3

## Problem Description
The customer reported that after uploading an XML file for a domain to the PingCastle Pro portal, the audit data view did not display any example findings for each topic, while another domain report did show findings.

## Environment Details
- The issue occurred in the PingCastle Pro portal.
- The scan was initially performed on the EMAT.CRH.COM domain, while the free version report was generated on the HBD.INT domain.

## Troubleshooting Steps
1. Conducted a PingCastle scan.
2. Uploaded the resulting XML file to the PingCastle Pro web portal.
3. Compared the HTML file of the free version report with the Pro version's uploaded audit data.
4. Identified that the free version included more detailed findings and examples.
5. Confirmed that the absence of the `--full` scan parameter was the likely cause of missing example findings.
6. Suggested re-running the PingCastle scan with the `--full` parameter.

## Root Cause
The root cause of the issue was that the initial scan was conducted without the `--full` parameter, which is necessary for performing a comprehensive scan that collects detailed information, including example findings for the audit data view.

## Solution
The issue was resolved by advising the user to:
1. Re-run the PingCastle scan using the `--full` parameter.
2. Upload the new XML file to the PingCastle Pro portal.
3. Verify that the audit data view now displays the expected example findings.

After following these steps, the user confirmed that the issue was resolved and the expected data was visible.

## Notes
- Ensure that the `--full` parameter is always used when conducting scans that require detailed findings.
- Future users should be reminded to check the parameters used during scans if they encounter similar issues with missing data in the audit views.