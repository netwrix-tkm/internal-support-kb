## Ticket Metadata
- **Ticket ID:** 500Qk00000DaJSrIAN
- **Case Number:** 416208
- **Status:** Closed - Resolved
- **Account/Company:** Bundesministerium für Justiz
- **Contact Name:** Wolfgang Schlapschy
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** NONE

## Problem Description
The customer reported that global rights for USB storage devices were not applying correctly. While some USB devices were functioning as intended under global rights, others required explicit device rights to work.

## Environment Details
- The deployment involved denying access to USB storage devices for standard users.
- Specific USB devices were intended to be allowed for use on all devices through global rights configuration.

## Troubleshooting Steps
1. Verified the configuration of global rights for the USB devices.
2. Tested the functionality of two different USB sticks:
   - Stick ID: `04013DC910CCD36F79DA7593679F9FBDDE0C051D52247197BD4B381C9C7A1B64625300000000000000000000A0DA2FEBFF9A01189155810749AE06B2` - Worked with global rights.
   - Stick ID: `0401B71537A572D8A0BDF55361143FC4DB5815A8F8F8D27F970878C91D15F5DBF52100000000000000000000FB2EC82A000D0F189155810749AE010C` - Did not work with global rights and required explicit device rights.
3. Confirmed that the rights were applied correctly for the non-functioning USB stick.

## Root Cause
The issue was identified as a misconfiguration or limitation in the global rights settings that prevented the specific USB stick from being recognized under the global rights policy.

## Solution
The issue was resolved by confirming that the global rights were correctly applied. The customer was advised to continue using explicit device rights for the problematic USB stick until a more permanent solution could be implemented in the global rights configuration.

## Notes
- It is important to ensure that all USB devices intended for global rights are properly configured and tested.
- For devices that do not respond to global rights, consider using explicit device rights as a temporary workaround.
- Future updates to the Netwrix Endpoint Protector may address limitations in global rights functionality.