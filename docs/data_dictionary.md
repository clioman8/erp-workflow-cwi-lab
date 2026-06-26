# docs/data_dictionary.md

# Data Dictionary

## 1. Overview

This document defines the data files used in the ERP Workflow CWI Lab.

The repository uses:

* master data
* event logs
* scenario definitions
* exception taxonomy
* process mappings
* CWI analysis outputs
* ECOUNT practice logs

The goal is to support workflow visibility, combinatorial scenario analysis, and operational intelligence reporting.

## 2. Master Data

### data/master/items.csv

Defines items used in the fictional CWI Smart Sensor Lab.

Expected columns:

```csv
item_code,item_name,item_type,unit,barcode,standard_cost,sales_price
```

Examples:

* CWI26_RM_PCB
* CWI26_RM_SENSOR
* CWI26_RM_CABLE
* CWI26_RM_CASE
* CWI26_PKG_BOX
* CWI26_SUB_CTRL
* CWI26_FG_KIT

Column definitions:

| Column        | Meaning                                             |
| ------------- | --------------------------------------------------- |
| item_code     | unique item code                                    |
| item_name     | human-readable item name                            |
| item_type     | raw_material, packaging, subassembly, finished_good |
| unit          | unit of measure                                     |
| barcode       | optional barcode value                              |
| standard_cost | expected unit cost                                  |
| sales_price   | expected sales price                                |

### data/master/warehouses.csv

Defines warehouse locations.

Expected columns:

```csv
warehouse_code,warehouse_name,warehouse_type,description,default_processes,inventory_status,location_role,is_virtual
```

Examples:

* CWI26_RAW
* CWI26_WIP
* CWI26_FG
* CWI26_QC
* CWI26_RETURN
* CWI26_SCRAP

### data/master/business_partners.csv

Defines vendors, customers, outsourcing partners, and internal departments.

Expected columns:

```csv
partner_code,partner_name,partner_type,related_processes,description,risk_area,default_role
```

Examples:

* CWI26_VENDOR_A
* CWI26_VENDOR_B
* CWI26_CUSTOMER_A
* CWI26_CUSTOMER_B
* CWI26_OUTSOURCE_A
* CWI26_INTERNAL_QC

### data/master/bom.csv

Defines BOM relationships.

Expected columns:

```csv
parent_item,component_item,quantity_per_parent,level
```

Example:

```csv
CWI26_FG_KIT,CWI26_SUB_CTRL,1,1
CWI26_FG_KIT,CWI26_RM_SENSOR,1,1
CWI26_FG_KIT,CWI26_RM_CASE,1,1
CWI26_FG_KIT,CWI26_PKG_BOX,1,1
```

### data/master/role_matrix.csv

Defines roles and their expected workflow responsibilities.

Expected columns:

```csv
role_id,role_name,role_category,primary_processes,allowed_activities,decision_authority,approval_limit,main_risks,cwi_relevance
```

Examples of role_name:

* buyer
* warehouse_operator
* production_planner
* production_operator
* quality_checker
* sales_operator
* manager
* accountant
* system

### data/master/approval_rules.csv

Defines synthetic or conceptual approval rules.

Expected columns:

```csv
rule_id,process,trigger_condition,required_role,approver_role,threshold_value,threshold_unit,approval_activity,exception_if_delayed,default_sla_minutes,cwi_factor
```

Examples of cwi_factor:

* F3 warehouse_error
* F4 bom_variance
* F5 qc_hold
* F6 approval_delay

## 3. Event Logs

### data/event_logs/synthetic_integrated_event_log.csv

Main event log file.

Expected columns:

```csv
case_id,timestamp,process,activity,actor_role,object_code,quantity,from_location,to_location,status,exception_type,source_action_id,data_origin
```

Column definitions:

| Column           | Meaning                                        |
| ---------------- | ---------------------------------------------- |
| case_id          | workflow instance ID                           |
| timestamp        | event timestamp                                |
| process          | process family such as P2P, O2C, Manufacturing |
| activity         | workflow activity name                         |
| actor_role       | role responsible for the event                 |
| object_code      | item, order, work order, or object code        |
| quantity         | quantity involved                              |
| from_location    | source location or partner                     |
| to_location      | target location or partner                     |
| status           | event status                                   |
| exception_type   | exception marker                               |
| source_action_id | source action log ID                           |
| data_origin      | source classification                          |

Recommended data_origin values:

```text
ecount_demo_observation
ecount_reconstructed
synthetic_only
hybrid_synthetic
sap_conceptual
```

Recommended status values:

```text
completed
pending
exception
on_hold
closed_with_exception
```

## 4. Scenario Data

### data/scenarios/factor_definitions.csv

Defines binary exception factors.

Expected columns:

```csv
factor_code,factor_name,0_state,1_state,ecount_possible
```

Example factors:

| factor_code | factor_name       |
| ----------- | ----------------- |
| F1          | partial_receipt   |
| F2          | material_shortage |
| F3          | warehouse_error   |
| F4          | bom_variance      |
| F5          | qc_hold           |
| F6          | approval_delay    |

### data/scenarios/scenario_design.csv

Defines combinatorial scenario design.

Expected columns:

```csv
scenario_id,bitmask,hamming_weight,F1,F2,F3,F4,F5,F6,execution_mode
```

Example:

```csv
CWI-000000,000000,0,0,0,0,0,0,0,ecount_observed
CWI-100000,100000,1,1,0,0,0,0,0,ecount_observed
CWI-010010,010010,2,0,1,0,0,1,0,hybrid
```

### data/scenarios/exception_taxonomy.csv

Defines exception types.

Expected columns:

```csv
exception_type,description,related_factor,process,expected_effect,ecount_possible,synthetic_handling
```

Examples:

* partial_receipt
* material_shortage
* warehouse_error
* bom_variance
* qc_hold
* approval_delay

## 5. Mapping Data

### data/mappings/ecount_sap_process_crosswalk.csv

Maps ECOUNT concepts to generic ERP and SAP-style concepts.

Expected columns:

```csv
ecount_process,generic_process,sap_concept,mapping_level,confidence,notes
```

### data/mappings/activity_codebook.csv

Defines standardized activity names.

Expected columns:

```csv
activity,process,description,expected_actor_role,normal_or_exception
```

### data/mappings/field_mapping.csv

Maps raw or reconstructed fields to CWI event-log fields.

Expected columns:

```csv
source_field,target_field,transformation_rule,notes
```

## 6. ECOUNT Lab Data

### ecount_lab/practice_action_log.csv

Records manual ECOUNT practice actions.

Expected columns:

```csv
action_id,timestamp,lab_id,ecount_menu,action_type,object_type,object_code,object_name,input_summary,expected_effect,observed_effect,evidence_ref,notes,data_origin
```

This file connects hands-on ECOUNT observation to reconstructed event logs.

Recommended lab_id values:

```text
LAB-00
LAB-01
LAB-02
LAB-03
LAB-04
LAB-05
LAB-06
LAB-07
```

## 7. Report Outputs

Reports may include:

```text
reports/sample_cwi_report.md
reports/ecount_practice_results.md
reports/sap_comparison_notes.md
reports/p2p_lab_notes.md
reports/o2c_lab_notes.md
reports/manufacturing_lab_notes.md
reports/combinatorial_exception_report.md
```

Generated CSV reports may include:

```text
case_cycle_times.csv
activity_counts.csv
exception_counts.csv
role_handoff_counts.csv
bottleneck_scores.csv
scenario_coverage.csv
authority_mismatch_counts.csv
```

## 8. Visual Outputs

Visuals may include:

```text
visuals/pascal_to_workflow.png
visuals/combinatorial_scenario_map.png
visuals/p2p_process_map.png
visuals/o2c_process_map.png
visuals/manufacturing_process_map.png
visuals/bottleneck_chart.png
visuals/interaction_matrix.png
visuals/authority_mismatch_matrix.png
visuals/traceability_chain.png
```

## 9. Data-Origin Policy

Every dataset must be clear about its source.

Use `data_origin` to distinguish:

| data_origin             | Meaning                                 |
| ----------------------- | --------------------------------------- |
| ecount_demo_observation | directly observed in ECOUNT demo        |
| ecount_reconstructed    | reconstructed from ECOUNT practice flow |
| synthetic_only          | fully synthetic scenario                |
| hybrid_synthetic        | partly observed and partly simulated    |
| sap_conceptual          | SAP-style comparison only               |

## 10. Final Summary

The data structure supports three goals.

First, it records ECOUNT ERP demo workflow observations.

Second, it converts observations into event-log format.

Third, it applies CWI metrics and combinatorial scenario analysis to understand workflow behavior.
