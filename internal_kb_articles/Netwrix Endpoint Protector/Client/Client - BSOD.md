# Netwrix Endpoint Protector: Troubleshooting BSOD and Kernel Panic Issues in the Client Component

## Overview
This document provides a comprehensive guide to troubleshooting Blue Screen of Death (BSOD) and kernel panic issues related to the Netwrix Endpoint Protector (EPP) client. These issues can occur on both Windows and Linux systems and are often triggered by conflicts with third-party software, resource allocation problems, or bugs in specific client versions. This guide includes a summary of common issues, detailed troubleshooting steps, root cause analyses, and tested solutions.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| BSOD on Windows after deploying EPP agent | BSOD with `cssdlp20.sys` error | Test newer client versions and collect dump files | Update to the latest EPP agent version | [BSOD with `cssdlp20.sys`](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DR4CyIAL/view) |
| BSOD on Windows 11 due to driver conflict | BSOD after installing DLP agent | Analyze crash dumps and identify conflicting drivers | Update or remove conflicting Fortinet driver | [Driver conflict with Fortinet](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EhgyPIAR/view) |
| Kernel panic on Linux during sync | System crash during repository sync | Enable trace logging, throttle sync, disable parallelization | Apply workarounds or update to fixed client version | [Kernel panic during sync](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JljZsIAJ/view) |
| Kernel panic on Linux due to client bug | System crash during file sync | Collect logs, disable parallelization, test new client build | Update to fixed client version | [Kernel panic due to client bug](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JlrxDIAR/view) |

---

## Detailed Issues

### 1. BSOD on Windows After Deploying EPP Agent
**Symptoms:**  
- BSOD with error referencing `cssdlp20.sys` after deploying EPP agent version 6.2.2.2.

**Troubleshooting Steps:**  
1. Analyze the dump file associated with the BSOD.
2. Test newer client versions (e.g., build 5940 or RC candidate 5941) on affected machines.
3. Request additional dump files and client logs if the issue persists.
4. Confirm the frequency of the BSOD (e.g., during boot or specific operations).

**Root Cause:**  
- Likely related to a bug in the specific version of the EPP agent (6.2.2.2).

**Solution:**  
- Update to the latest version of the EPP agent. The customer confirmed that the issue was resolved after updating.

**Warnings/Considerations:**  
- Monitor system performance after deploying updates to ensure stability.

**Source Ticket:** [BSOD with `cssdlp20.sys`](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DR4CyIAL/view)

---

### 2. BSOD on Windows 11 Due to Driver Conflict
**Symptoms:**  
- BSOD errors on Windows 11 endpoints after installing the DLP agent during a pilot program.

**Troubleshooting Steps:**  
1. Collect mini dump files and logs from affected machines.
2. Analyze crash dumps to identify potential conflicts.
3. Test the latest client version on one of the affected endpoints.
4. Identify conflicting third-party drivers (e.g., Fortinet's `AV_FortiEDRWinDriver`).

**Root Cause:**  
- Conflict between the DLP agent and Fortinet's driver.

**Solution:**  
- Contact Fortinet to update or remove the conflicting driver. The customer resolved the issue by addressing the driver conflict.

**Warnings/Considerations:**  
- Verify compatibility of third-party security software with the EPP agent before deployment.

**Source Ticket:** [Driver conflict with Fortinet](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EhgyPIAR/view)

---

### 3. Kernel Panic on Linux During Sync
**Symptoms:**  
- Kernel panic when users attempt to browse a repository directory and initiate syncing.

**Troubleshooting Steps:**  
1. Collect user reports and identify scenarios triggering the kernel panic.
2. Enable trace logging during sync operations.
3. Throttle the sync process to reduce resource strain.
4. Disable parallelization during sync operations.

**Root Cause:**  
- Likely related to resource allocation conflicts during sync operations.

**Solution:**  
- Apply the following workarounds:
  - Enable trace logging.
  - Throttle the sync process.
  - Disable parallelization.
- Monitor for updates or patches addressing the underlying issue.

**Warnings/Considerations:**  
- These workarounds mitigate the issue but do not resolve the root cause. Apply updates when available.

**Source Ticket:** [Kernel panic during sync](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JljZsIAJ/view)

---

### 4. Kernel Panic on Linux Due to Client Bug
**Symptoms:**  
- Kernel panic during file sync operations on Linux clients using the latest EPP-client version.

**Troubleshooting Steps:**  
1. Collect logs and crash reports from affected machines.
2. Test disabling parallelization and throttling the sync process.
3. Engage R&D to investigate and raise a priority ticket.
4. Provide a test build to the customer for validation.

**Root Cause:**  
- Bug in the EPP-client causing kernel panics during sync operations.

**Solution:**  
- Update to the fixed client version:  
  [EPPClient_ubuntu_18.04_v2.4.4.1004](https://download.endpointprotector.com/linux_agent/EPPLinux_v2.4.4.1004/EPPClient_ubuntu_18.04_v2.4.4.1004_x86_64.tar.gz)

**Warnings/Considerations:**  
- Keep kernel panic logs for further analysis if similar issues arise.

**Source Ticket:** [Kernel panic due to client bug](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JlrxDIAR/view)

---

## Best Practices
1. **Pre-Deployment Testing:**  
   - Test new versions of the EPP agent in a controlled environment before full deployment.
   - Verify compatibility with third-party security software.

2. **Log Collection:**  
   - Always collect detailed logs and crash dumps when issues occur. This accelerates root cause analysis.

3. **Monitor Updates:**  
   - Stay informed about new releases or patches from Netwrix that address known issues.

4. **Temporary Workarounds:**  
   - For Linux kernel panics, consider disabling parallelization or throttling sync operations as temporary measures.

5. **Communication with Third-Party Vendors:**  
   - Engage third-party vendors promptly if conflicts with their software are identified.

---

## Advanced Topics
### Handling Complex Scenarios
- **Concurrent Issues:** If multiple issues (e.g., BSOD and driver conflicts) occur simultaneously, prioritize resolving third-party conflicts before addressing EPP-client-specific bugs.
- **Custom Configurations:** For environments with unique configurations, consider engaging R&D for tailored solutions or test builds.

--- 

End of Document