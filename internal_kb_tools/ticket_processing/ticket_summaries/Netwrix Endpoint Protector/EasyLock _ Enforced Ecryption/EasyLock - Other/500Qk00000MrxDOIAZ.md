## Ticket Metadata
- **Ticket ID:** 500Qk00000MrxDOIAZ
- **Case Number:** 438632
- **Status:** Closed - Resolved
- **Account/Company:** Bennett Jones Services Limited
- **Contact Name:** Karan Bhagat
- **Product:** Netwrix Endpoint Protector
- **Component:** EasyLock / Enforced Encryption
- **Feature:** EasyLock - Other
- **Version:** 6.2.3.1010

## Problem Description
Users reported that the default functionality of EasyLock in the Netwrix Endpoint Protector was restricting their ability to open multiple documents simultaneously from an EPP encrypted USB. When attempting to open a second document, users received a warning message instructing them to close the previous file.

## Environment Details
- Users were operating with EasyLock version 6.2.3.1010.
- The issue was observed specifically with PDF files opened in Adobe Reader.

## Troubleshooting Steps
1. Confirmed the version of EasyLock being used by the customer.
2. Conducted internal testing to replicate the reported behavior.
3. Engaged in a remote session with the customer to observe the issue firsthand.
4. Generated logs and recorded the behavior during the remote session.
5. Communicated findings to the development team for further investigation.

## Root Cause
The behavior observed is by design in EasyLock. EasyLock allows only one file to be opened at a time due to the way it handles file encryption and decryption. When a file is opened, it is decrypted into a temporary location, and upon closing, it must be re-encrypted. Adobe Reader locks the file when opened, preventing EasyLock from re-encrypting it, which leads to the warning message when attempting to open another file.

## Solution
The resolution involved clarifying the intended functionality of EasyLock to the customer. It was explained that:
- Each file can only be opened one at a time due to the encryption process.
- Users should close the file in Adobe Reader before attempting to open another file from the EasyLock container.
- Notepad can open files in shared mode, allowing multiple instances, unlike Adobe Reader.

No changes to the software were necessary, as the behavior was consistent with the designed functionality of EasyLock.

## Notes
- Users should be made aware that EasyLock's limitation of opening one file at a time is a feature, not a bug.
- Consider providing documentation or training to users on how to effectively use EasyLock, especially regarding file handling with different applications (e.g., Notepad vs. Adobe Reader).
- Future updates or changes to EasyLock should be communicated to users to ensure they are aware of any modifications to functionality.