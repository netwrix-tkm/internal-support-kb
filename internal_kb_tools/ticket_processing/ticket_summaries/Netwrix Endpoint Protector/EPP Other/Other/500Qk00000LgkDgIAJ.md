## Ticket Metadata
- **Ticket ID:** 500Qk00000LgkDgIAJ
- **Case Number:** 435234
- **Status:** Closed - Resolved
- **Account/Company:** Tradebyte Software GmbH
- **Contact Name:** Paulius Tunkevicius
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** 9.3

## Problem Description
The customer reported that port 587 is set to HTTP instead of SMTP by default in the Netwrix Endpoint Protector configuration. According to the documentation, this port should be configured as SMTP.

## Environment Details
- The issue was observed in the Deep Packet Inspection section under Content Aware Protection in the user interface.

## Troubleshooting Steps
1. Clarified the customer's query regarding the port configuration.
2. Verified internally whether this was a bug in the system.
3. Raised a case with the R&D team to investigate the issue further.
4. Updated the steps to reproduce the issue in the UI.

## Root Cause
The investigation revealed that this was not a bug but rather a UI issue. The Deep Packet Inspection Predefined Ports section incorrectly displayed port 587 as HTTP instead of SMTP. However, the functionality of the system was not affected, and operations continued as expected.

## Solution
A ticket was raised to correct the UI display in the Deep Packet Inspection - Predefined Ports section, changing the designation of port 587 from HTTP to SMTP. The issue was marked as resolved once the necessary changes were documented.

## Notes
- It is important to note that while the UI displayed an incorrect configuration, the underlying functionality was not impacted. Future cases should verify whether the issue affects functionality or is purely a display concern.
- Ensure to keep documentation updated to reflect any changes made to the UI for clarity in future support cases.