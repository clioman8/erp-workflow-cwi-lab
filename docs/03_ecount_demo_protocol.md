# docs/03_ecount_demo_protocol.md

# ECOUNT Demo Protocol

## 1. Purpose

This document defines how the ECOUNT ERP demo environment is used in this project.

ECOUNT is used as a practical ERP demo environment for observing and reconstructing workflow behavior.

The goal is not to claim full production ERP implementation experience.

The goal is to use ECOUNT as a controlled workflow laboratory for CWI analysis.

## 2. Data Safety Rule

The ECOUNT demo environment may contain shared sample data.

This project must not expose data created by other users.

Public repository materials should contain only:

* self-created CWI-prefixed records
* sanitized screenshots
* reconstructed event logs
* synthetic data
* generalized workflow notes

## 3. Naming Prefix

All project-created demo records should use the prefix:

```text
CWI26_
```

This makes project data easier to identify, filter, export, and sanitize.

Examples:

```text
CWI26_RM_PCB
CWI26_RM_SENSOR
CWI26_FG_KIT
CWI26_VENDOR_A
CWI26_CUSTOMER_A
CWI26_RAW
CWI26_WIP
CWI26_FG
```

## 4. Demo Company Scenario

The fictional operating scenario is:

```text
CWI Smart Sensor Lab
```

The company purchases raw materials, produces a smart sensor kit, stores finished goods, and ships them to customers.

The scenario includes:

* raw material purchasing
* inventory receiving
* BOM-based production
* finished goods receipt
* sales order shipment
* QC hold
* warehouse correction
* approval delay simulation
* exception tracking

## 5. Master Data Setup

The first lab creates master data.

### Warehouses

* CWI26_RAW
* CWI26_WIP
* CWI26_FG
* CWI26_QC
* CWI26_RETURN
* CWI26_SCRAP

### Business Partners

* CWI26_VENDOR_A
* CWI26_VENDOR_B
* CWI26_CUSTOMER_A
* CWI26_CUSTOMER_B
* CWI26_OUTSOURCE_A
* CWI26_INTERNAL_QC

### Items

* CWI26_RM_PCB
* CWI26_RM_SENSOR
* CWI26_RM_CABLE
* CWI26_RM_CASE
* CWI26_PKG_BOX
* CWI26_SUB_CTRL
* CWI26_FG_KIT

### BOM

Subassembly BOM:

```text
CWI26_SUB_CTRL =
1 x CWI26_RM_PCB
2 x CWI26_RM_CABLE
```

Finished good BOM:

```text
CWI26_FG_KIT =
1 x CWI26_SUB_CTRL
1 x CWI26_RM_SENSOR
1 x CWI26_RM_CASE
1 x CWI26_PKG_BOX
```

## 6. Practice Action Log

Every manual action in ECOUNT should be recorded in:

```text
ecount_lab/practice_action_log.csv
```

Recommended columns:

```csv
action_id,timestamp,lab_id,ecount_menu,action_type,object_type,object_code,object_name,input_summary,expected_effect,observed_effect,evidence_ref,notes,data_origin
```

Example:

```csv
ACT-0001,2026-06-20 10:00,LAB-01,품목등록,create,item,CWI26_RM_PCB,CWI26 제어 PCB,EA unit and barcode entered,Item master created,Created in demo list,EV-001,Sanitized screenshot saved,ecount_demo_observation
```

## 7. Event Log Reconstruction

ECOUNT may not provide a complete process-mining event log directly.

Therefore, this project reconstructs event logs from:

* manual action logs
* exported lists
* screenshots
* observed workflow sequence
* synthetic exception scenarios

The reconstructed event log is stored in:

```text
data/event_logs/synthetic_integrated_event_log.csv
```

## 8. Evidence Policy

Screenshots may be used as private evidence.

Public screenshots must be sanitized.

Sanitization rules:

* show only CWI26-prefixed records
* crop unrelated rows
* blur or remove names, phone numbers, emails, addresses, IDs, or other private data
* avoid showing other users’ demo data
* do not expose login information

Recommended evidence folder:

```text
ecount_lab/evidence/screenshots/
```

## 9. Lab Sequence

The recommended lab sequence is:

1. Master data setup
2. P2P purchasing and receiving
3. Manufacturing BOM and work order
4. Production receipt and inventory update
5. O2C sales order and shipment
6. MPS/MRP observation
7. Traceability and QC hold simulation
8. Combinatorial exception scenario design

## 10. Public Repository Policy

The public repository should contain:

* sanitized summaries
* synthetic event logs
* master data CSVs
* process diagrams
* analysis scripts
* CWI reports

The public repository should not contain:

* raw screenshots with unrelated data
* private ECOUNT account information
* customer data
* login credentials
* other users’ demo records
* unsanitized exports

## 11. Final Summary

ECOUNT is used as a workflow laboratory.

The project does not depend on perfect ERP data extraction.

Instead, it combines demo observation, synthetic event reconstruction, and combinatorial scenario design to study ERP workflow intelligence.
