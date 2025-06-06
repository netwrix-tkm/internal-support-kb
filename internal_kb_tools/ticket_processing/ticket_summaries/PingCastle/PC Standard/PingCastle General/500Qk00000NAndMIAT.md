## Ticket Metadata
- **Ticket ID:** 500Qk00000NAndMIAT
- **Case Number:** 439594
- **Status:** Closed - Resolved
- **Account/Company:** USU Software AG
- **Contact Name:** Dominik Padych
- **Product:** PingCastle
- **Component:** PC Standard
- **Feature:** PingCastle General
- **Version:** 3.3.0.1

## Problem Description
The customer reported that after updating the license key for PingCastle, the application was running in the free edition instead of the licensed version. The logs indicated that the license was not being recognized, and the customer was unable to perform full health checks.

## Environment Details
- The customer was using PingCastle version 3.3.0.1.
- The license was applied in the `PingCastle.exe.conf` file.

## Troubleshooting Steps
1. The customer confirmed that the license was applied correctly in the configuration file.
2. The customer ran PingCastle with the `--log` argument but found no errors related to licensing.
3. The support team requested the customer to upload logs and configuration files for further analysis.
4. The support team tested the customer's license in a lab environment and confirmed it was not functioning.
5. The support team contacted the licensing team to request a new license for the customer.

## Root Cause
The root cause of the issue was identified as a bad or invalid license key that was not functioning correctly with the PingCastle application.

## Solution
The issue was resolved by providing the customer with a new, valid license key. The new license was tested and confirmed to work correctly, allowing the customer to run PingCastle as intended.

## Notes
- Ensure that the correct version of PingCastle is installed before applying a new license.
- If a license appears to be invalid, it is advisable to test it in a controlled environment to confirm its status before contacting support.
- Always verify that the configuration file is correctly set up with the new license key after any updates.