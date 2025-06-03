# Ticket Summary for Support Case

## Ticket Metadata
- **Ticket ID:** 500Qk00000CFjifIAD
- **Case Number:** 412860
- **Status:** Closed - Resolved
- **Account/Company:** TSMC
- **Contact Name:** Jay Mai
- **Product:** Netwrix Endpoint Protector
- **Component:** Client Device Recognition
- **Feature:** Client Device Recognition
- **Version:** 5.6.0.0

## Problem Description
The customer reported that COM Port devices could not be recognized by the system. They were also inquiring about the availability of a support tool for Mac, as the previously provided tool was only available for Windows.

## Environment Details
- The customer operates in a closed network environment that is 100% inaccessible to external connections.
- The current version of the EPP Server is 5.6.0.0.

## Troubleshooting Steps
1. Provided instructions for starting logs on Mac using terminal commands.
2. Suggested the use of offline patches to upgrade the EPP Server.
3. Confirmed the download link for the offline patch `MP-EPP4-ENABLE-CAP.tar.gz`.
4. Advised the customer to ensure they had at least 30% free disk space before applying patches.
5. Instructed the customer to wait for the appropriate time after applying each patch to allow for installation.
6. Clarified that the version number may not change immediately after applying certain patches, particularly from 5.6.0.0 to 5.6.5.0.

## Root Cause
The issue stemmed from the customer's network environment being completely closed, which prevented the application of necessary updates and patches. Additionally, the server version did not change due to insufficient wait times after applying patches.

## Solution
1. Instructed the customer to apply the patch from 5.6.0.0 to 5.6.5.0 and wait for 30 minutes after the upload to ensure proper installation.
2. Recommended that they check the version number after each patch application by refreshing the browser page.
3. Suggested using the OVF image for version 5.8.1.0 to simplify the upgrade process, as it would reduce the number of patches needed.

## Notes
- Ensure that the customer is aware of the importance of waiting the specified time after applying patches to avoid installation issues.
- If the version number does not change after applying patches, it may indicate that the patches were not installed correctly, and further investigation may be needed.
- For environments without internet access, offline patches are essential, and the correct sequence of patch applications must be followed.