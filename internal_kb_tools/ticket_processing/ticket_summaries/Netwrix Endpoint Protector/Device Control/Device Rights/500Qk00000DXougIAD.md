## Ticket Metadata
- **Ticket ID:** 500Qk00000DXougIAD
- **Case Number:** 416114
- **Status:** Closed - Resolved
- **Account/Company:** Chevron Phillips Chemical
- **Contact Name:** Jeff Schemp
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** NONE

## Problem Description
The customer requested assistance in deleting all computer entries from their Netwrix Endpoint Protector system. They had transitioned from a device and computer-based exception model to a user-based model and needed to remove all device permissions associated with computers. The customer found the GUI method for deletion cumbersome and prone to failure when selecting multiple entries.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Device Exception Model:** Transitioned from device/computer-based to user-based

## Troubleshooting Steps
1. Customer attempted to delete computers through the GUI but encountered failures when selecting large numbers.
2. Customer requested support to directly access the database to delete computer entries.
3. Support team escalated the request for a custom solution but clarified that direct database access was not supported.
4. Discussions among support staff regarding potential custom development to facilitate the deletion process.

## Root Cause
The issue stemmed from the customer's need to delete a large number of computer entries in a system that does not support bulk deletion through the GUI effectively. The request for direct database manipulation was outside the standard support scope.

## Solution
The customer manually removed the computer entries themselves after being informed that direct database access was not supported by Netwrix. The support team provided guidance on the limitations of the system and confirmed that no custom development was approved for this request.

## Notes
- Direct database manipulation is not supported by Netwrix, and customers should be informed of this limitation.
- Future requests for bulk deletion should be handled with caution, and customers should be advised on the potential challenges of using the GUI for large datasets.
- Consider documenting alternative methods or best practices for managing device permissions in user-based models to assist customers in similar situations.