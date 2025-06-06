## Ticket Metadata
- **Ticket ID:** 500Qk00000DrBfOIAV
- **Case Number:** 416782
- **Status:** Closed - Resolved
- **Account/Company:** Dew Solutions Pvt Ltd
- **Contact Name:** Bhogendra Kumar
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Migration
- **Version:** Not specified

## Problem Description
The customer reported that they were using a `c5a.xlarge` instance on AWS Cloud, which was flagged by AWS Compute Optimizer as over-provisioned in terms of CPU, EBS throughput, network bandwidth, and network packets per second (PPS). The customer requested recommendations for a more optimized instance type to reduce costs without impacting performance.

## Environment Details
- Current Instance Type: `c5a.xlarge`
- Suggested Instance Types: `t3.medium` (2 CPUs, 4GB RAM) and `t3.large` (2 CPUs, 8GB RAM)

## Troubleshooting Steps
1. Reviewed the customer's current instance type and AWS Compute Optimizer recommendations.
2. Suggested trying `t3.medium` as the first step for optimization.
3. Recommended `t3.large` if `t3.medium` did not meet performance needs.
4. Followed up with the customer to check if they had implemented the suggested changes.
5. Clarified that the original issue was related to CPU and RAM, but later discussions revealed that the customer was facing a separate issue related to storage partition size.

## Root Cause
The initial issue was due to the customer's use of an over-provisioned instance type (`c5a.xlarge`) as identified by AWS Compute Optimizer. The customer later indicated that their ongoing issues were related to storage partition size rather than CPU and RAM.

## Solution
The customer was advised to switch to a `t3.medium` instance for cost savings. If additional resources were needed, they could upgrade to a `t3.large`. The customer confirmed that they would consider these options, and the ticket was closed upon their confirmation that the suggestions were satisfactory.

## Notes
- It is important to differentiate between issues related to instance type and those related to storage or other configurations.
- For future cases, ensure that customers are aware of the implications of changing instance types on their applications and workloads.
- Encourage customers to raise separate tickets for distinct issues to maintain clarity and organization in support requests.