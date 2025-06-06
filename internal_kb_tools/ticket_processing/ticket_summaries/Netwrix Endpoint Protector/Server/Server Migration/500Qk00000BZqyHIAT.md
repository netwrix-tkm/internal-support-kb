## Ticket Metadata
- **Ticket ID:** 500Qk00000BZqyHIAT
- **Case Number:** 411397
- **Status:** Closed - Resolved
- **Account/Company:** MRM-Mccann
- **Contact Name:** Hemant Mistry
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Migration
- **Version:** 5.9.3.0

## Problem Description
The customer requested assistance in migrating their Netwrix Endpoint Protector (EPP) virtual appliance from an on-premise VMware environment to their Azure tenant.

## Environment Details
- Current EPP version: 5.9.3.0
- Target environment: Microsoft Azure

## Troubleshooting Steps
1. Assigned the ticket to the appropriate support team covering the customer's time zone.
2. Provided the customer with detailed steps for obtaining the Blob SAS URL required for the migration.
3. Instructed the customer to create a storage account and container in Azure, as EPP is not available in the Azure Marketplace.
4. Confirmed that the customer needed to ensure both the on-premise and Azure EPP versions matched for a successful migration.
5. Assisted the customer in generating the Blob SAS URL and uploading the EPP image to Azure.
6. Increased the memory allocation for Nginx as part of the troubleshooting process.

## Root Cause
The initial issue stemmed from the customer's lack of a proper Blob SAS URL, which is essential for uploading the EPP image to Azure. Additionally, insufficient memory allocation for Nginx caused performance issues during the migration process.

## Solution
The issue was resolved by:
- Providing the customer with the correct steps to generate the Blob SAS URL.
- Increasing the memory allocation for Nginx, which improved the performance and allowed the migration to proceed smoothly.
- Confirming that the EPP image was successfully uploaded to the specified Azure blob.

## Notes
- Ensure that the EPP versions are consistent between the on-premise and Azure environments to avoid migration issues.
- Always verify memory settings for Nginx when performing migrations to prevent performance bottlenecks.
- Document the Blob SAS URL generation process clearly for future reference to assist customers in similar situations.