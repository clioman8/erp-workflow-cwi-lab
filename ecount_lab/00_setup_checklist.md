# ECOUNT CWI Lab Setup Checklist

## 1. Purpose

This checklist prepares the ECOUNT ERP demo environment for the ERP Workflow CWI Lab.

The goal is to use ECOUNT as a practical workflow observation environment and to convert observed workflows into reconstructed event logs for Combinatorial Workflow Intelligence analysis.

This lab does not claim production ERP deployment. It uses ECOUNT demo workflows, CWI-prefixed master data, reconstructed event logs, and synthetic exception scenarios.

## 2. Core Rule

Use the prefix below for all project-created records.

```text
CWI26_
```

This makes project data easier to identify, filter, export, sanitize, and separate from shared demo records.

## 3. Repository Paths

Create the following folders before practice.

```text
ecount_lab/evidence/screenshots/
ecount_lab/evidence/exports/
data/master/
data/event_logs/
data/scenarios/
data/mappings/
reports/
visuals/
```

## 4. Practice Action Log

Create:

```text
ecount_lab/practice_action_log.csv
```

Header:

```csv
action_id,timestamp,lab_id,ecount_menu,action_type,object_type,object_code,object_name,input_summary,expected_effect,observed_effect,evidence_ref,notes,data_origin
```

Example:

```csv
ACT-0001,2026-06-20 10:00,LAB-01,품목등록,create,item,CWI26_RM_PCB,CWI26 제어 PCB,EA unit and barcode entered,Item master created,Created in demo list,EV-001,Sanitized screenshot saved,ecount_demo_observation
```

## 5. Evidence Rule

Public screenshots must be sanitized.

Rules:

- show only CWI26-prefixed data
- crop unrelated demo rows
- hide emails, phone numbers, names, IDs, account information, and unrelated records
- never upload credentials or login information
- never upload raw shared demo exports

## 6. Lab Sequence

Recommended order:

```text
00_setup_checklist
01_master_data_lab
02_p2p_lab
03_o2c_lab
04_manufacturing_lab
05_mps_mrp_lab
06_traceability_lab
07_combinatorial_exception_lab
```

## 7. Data-Origin Labels

Use these values consistently.

| Label | Meaning |
|---|---|
| ecount_demo_observation | directly observed in ECOUNT demo |
| ecount_reconstructed | reconstructed from ECOUNT practice flow |
| synthetic_only | fully synthetic scenario |
| hybrid_synthetic | partly observed and partly simulated |
| sap_conceptual | SAP-style comparison only |

## 8. CWI Setup Principle

CWI asks:

```text
Which local rules, roles, approvals, inventory movements, and exceptions create the global workflow pattern?
```

The project studies how ERP transactions combine into operational behavior.
