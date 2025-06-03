## Ticket Metadata
- **Ticket ID:** 500Qk00000KFpBbIAL
- **Case Number:** 431185
- **Status:** Closed - Resolved
- **Account/Company:** OneSpan Canada, Inc.
- **Contact Name:** Anthony Nafarrete
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** 5941

## Problem Description
The customer inquired about the capability of Netwrix Endpoint Protector (EPP) to operate in an offline mode for IoT devices that do not have network connectivity. They have approximately 100 IoT devices in their Digipass factories that rely on a Windows registry file for managing allowed/denied devices, which is created on the software server.

## Environment Details
- **Device Type:** IoT devices
- **Network Connectivity:** No network connectivity for the devices
- **Registry File:** Contains encrypted values for allowed/denied devices, decrypted by the client software.

## Troubleshooting Steps
1. Reviewed the functionality of the Netwrix Endpoint Protector in relation to offline operations.
2. Discussed the process of importing the registry file into the client software without server contact.
3. Confirmed the encryption and decryption process of the registry file values.

## Root Cause
The inquiry was based on the need for clarification regarding the offline capabilities of the Netwrix Endpoint Protector, particularly how it handles device control when the client cannot connect to the server.

## Solution
During a discussion with the customer, it was confirmed that Netwrix Endpoint Protector does support offline functionality. The client can import the registry file directly, allowing the software to manage device rights without needing to contact the server.

## Notes
- Ensure that the registry file is correctly formatted and contains the necessary encrypted values for the device control to function properly in offline mode.
- Future inquiries regarding offline capabilities should reference this case for clarification on the functionality of the Netwrix Endpoint Protector in similar environments.