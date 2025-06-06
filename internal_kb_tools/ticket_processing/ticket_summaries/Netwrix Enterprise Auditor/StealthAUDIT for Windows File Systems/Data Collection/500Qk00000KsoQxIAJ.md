## Ticket Metadata
- **Ticket ID:** 500Qk00000KsoQxIAJ
- **Case Number:** 432976
- **Status:** Closed - Resolved
- **Account/Company:** Kyndryl
- **Contact Name:** Fenilkumar S
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Data Collection
- **Version:** 11.5

## Problem Description
The customer reported that the File Types report job was timing out, resulting in no detailed data being available in the report despite the Pie Chart displaying correctly. After increasing the job timeout, the job completed successfully, but detailed data remained absent. Additionally, removing the filter from the report caused the job to fail with a severe error message.

## Environment Details
- **Report Job:** FS_FileTypes
- **Filter Configuration:** File Size Less or Equal to 100
- **Timeout Setting:** Initially set to a lower value, increased to 7 days.

## Troubleshooting Steps
1. Increased the timeout for the FS_FileTypes report job to 7 days.
2. Verified that the FS_FileTypes job completed successfully after the timeout increase.
3. Attempted to remove the filter from the report to check if detailed data would appear.
4. Observed that removing the filter caused the job to fail with the error: 
   ```
   "A severe error occurred on the current command. The results, if any, should be discarded. Operation canceled by user. The statement has been terminated."
   ```

## Root Cause
The initial issue was caused by the FS_FileTypes report job timing out due to a low timeout setting. The subsequent failure when removing the filter was likely due to an underlying issue with the report's configuration or data processing that was exacerbated by the absence of the filter.

## Solution
The issue was resolved by increasing the timeout for the FS_FileTypes report job to 7 days. This adjustment allowed the job to complete successfully, resulting in both the Pie Chart and the detailed data being populated correctly. The timeout was increased by:
- Right-clicking the FS_FileTypes job
- Selecting "Properties"
- Modifying the "Timeout" parameter in the "General" tab.

## Notes
- Ensure that timeout settings are appropriately configured for report jobs that may process large datasets to prevent similar issues in the future.
- If encountering severe errors when modifying report filters, consider reviewing the report configuration and data integrity before further troubleshooting.