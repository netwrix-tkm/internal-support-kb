```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000GaGWcIAN
- **Case Number:** 422824
- **Status:** Closed - Resolved
- **Account/Company:** IGA Airport
- **Contact Name:** Yunus İçin
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** NONE

## Problem Description
The customer, IGA Airport, requested assistance in updating the External Storage Setting field on their Endpoint Protector (EPP) appliance. They needed to mount a new storage solution (DELL ECS) using a specific NFS command but were unable to do so due to the appliance's limitations.

## Environment Details
- The customer was transitioning from an unsupported storage solution to DELL ECS.
- The command attempted for mounting was:
  ```bash
  mount -t nfs -o 'vers=3,nolock,rsize=524288,wsize=524288' a1ecsnfsvh01p.igairport.aero:/ecs_nfsshare/EPP/ /path
  ```

## Troubleshooting Steps
1. Confirmed the customer's request to mount external storage on the EPP appliance.
2. Investigated the compatibility of EPP with DELL ECS and the NFS mounting command.
3. Communicated with the R&D team regarding the support for custom mounts.
4. Provided information that EPP only supports WebUI integration with standard/format compatible targets (SMBv1/v2, FTP).
5. Suggested the customer adjust their storage format to one that is supported by EPP.

## Root Cause
The issue stemmed from the EPP appliance's limitation in supporting custom mounts. The appliance does not allow backend mounting of external storage, which is necessary for the customer's intended use case.

## Solution
The customer resolved the issue independently after receiving guidance on the limitations of the EPP appliance. They were advised to use supported storage formats and configurations. The customer confirmed that they had successfully mounted the storage and requested the ticket to be closed.

## Notes
- Future customers should be informed that EPP does not support custom mounts and only allows integration with standard storage formats.
- It is recommended to verify the compatibility of any new storage solutions with EPP before implementation to avoid similar issues.
```