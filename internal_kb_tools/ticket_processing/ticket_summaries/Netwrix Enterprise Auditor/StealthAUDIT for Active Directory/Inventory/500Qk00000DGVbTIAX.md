## Ticket Metadata
- **Ticket ID:** 500Qk00000DGVbTIAX
- **Case Number:** 415453
- **Status:** Closed - Resolved
- **Account/Company:** EagleBank
- **Contact Name:** Esayas Gonfa
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Inventory
- **Version:** Not specified

## Problem Description
The customer reported that the structure of the `SA_ADInventory_ExtendedAttributesPivotView` table had changed following an update, resulting in the missing column `physicalDeliveryOfficeName`. This absence caused errors when generating reports for User Member Audit 1 and User Member Audit 2.

## Environment Details
- The issue occurred in the context of the Netwrix Enterprise Auditor platform.
- The data collection was performed using StealthAUDIT for Active Directory.

## Troubleshooting Steps
1. Verified that the `1-AD_Scan` job was configured to collect extended attributes.
2. Ran a full scan (no differential) to ensure all data was collected.
3. Dropped and recreated the `SA_ADInventory_ExtendedAttributesPivotView`, but the same error persisted.
4. Attempted to view the view in SQL Server Management Studio (SSMS) and encountered the error: 
   ```
   FOR XML could not serialize the data for node 'NoName' because it contains a character (0x0000) which is not allowed in XML.
   ```
5. Investigated the `SA_ADInventory_ExtendedAttributes` table for invalid characters.
6. Created a SQL analysis task on the `ADI1_AD-Scan` job to address malformed data.

## Root Cause
The issue was caused by malformed or incorrectly formatted data in the attributes collected, specifically the presence of a null character (0x0000) in the data, which is not allowed in XML serialization.

## Solution
To resolve the issue, a SQL script was executed as part of a newly created SQL analysis task on the `ADI1_AD-Scan` job. The script updated the `SA_ADInventory_ExtendedAttributes` table to remove the problematic characters:
```sql
UPDATE [dbo].[SA_ADInventory_ExtendedAttributes]
SET [value] = SUBSTRING([Value], 0, Len([Value]) - 1)
WHERE [value] LIKE '%' + char(10) + char(0)
```
This adjustment allowed the `SA_ADInventory_ExtendedAttributesPivotView` to populate correctly, enabling the generation of the required reports without errors.

## Notes
- It is important to monitor for similar issues related to malformed data in future updates.
- Ensure that data validation checks are in place to prevent the introduction of invalid characters during data collection.
- Consider documenting any changes to table structures in future updates to avoid confusion regarding missing columns.