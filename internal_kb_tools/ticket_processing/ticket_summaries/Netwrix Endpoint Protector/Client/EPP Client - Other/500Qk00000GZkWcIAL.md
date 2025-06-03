## Ticket Metadata
- **Ticket ID:** 500Qk00000GZkWcIAL
- **Case Number:** 422789
- **Status:** Closed - Resolved
- **Account/Company:** CLA Global TS Holdings Pte Ltd
- **Contact Name:** Stephen Goh
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client
- **Feature:** EPP Client - Other
- **Version:** None

## Problem Description
The customer reported an issue where unplugging an earpiece from the 3.5mm jack caused the sound/volume panel to hang, as well as causing meeting software to hang when selecting a sound device. This issue was linked to the re-enabling of a second Realtek audio device after unplugging, which led to Windows attempting to access a non-existent device resource.

## Environment Details
- Affected devices: Multiple laptop models
- Operating Systems: Windows 10, Windows 11
- Audio Device: Realtek integrated audio (not external USB audio devices)

## Troubleshooting Steps
1. Verified the issue by unplugging the earpiece and observing the system behavior.
2. Checked the device control list in the EPP client for audio devices.
3. Downgraded the EPP client to version 5.9.2.8, which resolved the issue.
4. Upgraded back to EPP client version 6, which caused the issue to reoccur.
5. Identified that the "Microsoft / Realtek(R) Audio" device appeared in the EPP v6 client but not in v5.
6. Tested the issue across multiple laptops to confirm replication.

## Root Cause
The root cause was identified as a conflict introduced in the EPP client version 6, where the second Realtek audio device was incorrectly re-enabled upon unplugging the audio device. This caused Windows to attempt to access a resource that no longer existed.

## Solution
The issue was resolved by updating the EPP client to version 6.2.4.2. This version included fixes for the audio issues that were affecting the Realtek audio devices.

## Notes
- Users experiencing similar audio issues should be advised to ensure they are using the latest version of the EPP client.
- If issues persist after an upgrade, consider downgrading to a previous stable version until a fix is confirmed in a newer release.
- Monitor for any further updates or patches related to audio device management in future EPP client releases.