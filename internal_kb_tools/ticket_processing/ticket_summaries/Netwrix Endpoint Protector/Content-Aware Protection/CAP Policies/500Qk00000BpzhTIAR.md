## Ticket Metadata
- **Ticket ID:** 500Qk00000BpzhTIAR
- **Case Number:** 411957
- **Status:** Closed - Resolved
- **Account/Company:** Laykon Distributor
- **Contact Name:** Faruk Sarı
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** Not specified

## Problem Description
The customer requested the ability to manage file locations on a network share by marking certain project folders as sensitive for different users. They wanted to log activities in specific folders, block file transfers to USB devices while allowing email transfers, and configure exception rules for File Location Denylist.

## Environment Details
- **Network Share IP:** 192.168.2.200
- **Use Case:** Multiple employees accessing project folders on a shared network.

## Troubleshooting Steps
1. Reviewed the customer's request for specific file location management capabilities.
2. Confirmed the current limitations of the Netwrix Endpoint Protector regarding exception rules for File Location Denylist.
3. Investigated the possibility of logging activities and blocking USB transfers entirely.
4. Communicated with the development team regarding potential feature requests and roadmap considerations.

## Root Cause
The Netwrix Endpoint Protector does not currently support the requested functionality of selectively blocking USB transfers from specific folders while allowing other types of transfers (e.g., email). The system can either log activities or block USB devices entirely, but it cannot differentiate actions based on file location.

## Solution
Informed the customer that:
- Logging activities from the specified location is possible with file trace for network shares enabled.
- USB devices can be blocked entirely, preventing any file transfers from that location.
- No current feature request exists for the specific functionality they requested, and it is not on the roadmap for future development.

## Notes
- Customers can submit feature requests for future consideration, but there is no guarantee of implementation.
- It is important to communicate the limitations of the current system clearly to avoid misunderstandings regarding capabilities.