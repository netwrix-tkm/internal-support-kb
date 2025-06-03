```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000LgnUsIAJ
- **Case Number:** 435237
- **Status:** Closed - Resolved
- **Account/Company:** Martin-Baker
- **Contact Name:** Conor Lane
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device not recognized
- **Version:** Not specified

## Problem Description
The customer reported a security gap where the inbuilt SD Card Reader on a computer was not being controlled by the Netwrix Endpoint Protector (EPP) Client. Users could access SD Cards with read-write permissions, while external USB SD Card Readers were correctly blocked by EPP.

## Environment Details
- The issue was observed on computers equipped with inbuilt SD Card Readers.
- The EPP Client was installed and functioning correctly for USB-connected devices.

## Troubleshooting Steps
1. Collected logs from the affected systems to analyze the behavior of the EPP Client with the inbuilt SD Card Reader.
2. Investigated the identification capabilities of SD Cards versus USB storage devices.
3. Confirmed that EPP was blocking access to USB-connected SD Card Readers as intended.

## Root Cause
The root cause of the issue was identified as the inability of the EPP Client to properly recognize inbuilt SD Card Readers. This was due to the lack of a persistent serial number for SD Cards, which changes upon formatting and can be modified by users. Consequently, the EPP Client could not enforce control over these devices in the same manner as USB storage devices.

## Solution
The resolution involved confirming that the EPP Client cannot control SD Cards through the inbuilt SD Card Reader. The only feasible method to manage access is to control the SD Card Reader itself on the machines where users have access to SD Cards. The customer was informed of this limitation and advised on the current capabilities of the EPP Client.

## Notes
- It is important to communicate to customers that SD Cards cannot be controlled like USB storage devices due to their identification limitations.
- Future considerations for controlling SD Cards should focus on managing the SD Card Reader hardware rather than the SD Cards themselves.
- Ensure that security policies are in place to mitigate risks associated with inbuilt SD Card Readers, especially in environments where sensitive data is handled.
```