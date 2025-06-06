## Ticket Metadata
- **Ticket ID:** 500Qk00000NeOSzIAN
- **Case Number:** 440861
- **Status:** Closed - Resolved
- **Account/Company:** DMC Sec Graphics Ministry of Defence
- **Contact Name:** Roger Garland
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server LiveUpdate
- **Version:** 5.9.4.2

## Problem Description
The customer requested assistance in updating their Netwrix Endpoint Protector to version 5.9.4.2 due to a security advisory. The update was not available through the live update feature.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Issue Type:** Security Policy/Compliance
- **Ticket Type:** Unexpected Behavior

## Troubleshooting Steps
1. Customer reported that the update to version 5.9.4.2 was not being offered via the live update.
2. Support provided the customer with a download link for the offline patch.
3. Instructions were given to apply the offline patch through the Dashboard -> Live Update -> Offline Patch Uploader.

## Root Cause
The update to version 5.9.4.2 was not available through the live update feature, likely due to the timing of the release or configuration settings within the customer's environment.

## Solution
The issue was resolved by providing the customer with the offline patch for version 5.9.4.2. The customer was instructed to download the patch from the provided link and apply it using the Offline Patch Uploader in the Netwrix Endpoint Protector Dashboard. The specific steps included:
- Accessing the Dashboard.
- Navigating to Live Update.
- Selecting the Offline Patch Uploader.
- Uploading the downloaded patch file.
- Applying the update and confirming the successful application.

## Notes
- It is recommended that customers take a snapshot of their EPP Server before applying any patches to ensure they can revert back if necessary.
- Future updates should be monitored closely to ensure they are available through the live update feature, and customers should be informed about the availability of offline patches when necessary.