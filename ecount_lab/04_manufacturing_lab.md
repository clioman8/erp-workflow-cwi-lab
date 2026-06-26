# Manufacturing Lab

## 1. Purpose

This lab practices BOM-based manufacturing.

Manufacturing connects master data, inventory, production planning, material issue, production receipt, quality hold, and finished goods availability.

## 2. Normal Flow

```text
Work Order Created
→ BOM Components Calculated
→ Material Issued
→ Production Receipt Created
→ Inventory Updated
```

## 3. ECOUNT Menus

```text
BOM(소요량)조회
작업지시서입력
작업지시서조회
생산입고 I
생산입고 II
생산입고조회
재고조회
```

## 4. Baseline Scenario

Produce:

```text
CWI26_FG_KIT = 10 units
```

Expected consumption:

```text
1 x CWI26_SUB_CTRL
1 x CWI26_RM_SENSOR
1 x CWI26_RM_CASE
1 x CWI26_PKG_BOX
```

## 5. Event Log Rows

```csv
case_id,timestamp,process,activity,actor_role,object_code,quantity,from_location,to_location,status,exception_type,source_action_id,data_origin
MFG-001,2026-06-20 13:00:00,Manufacturing,Work Order Created,production_planner,CWI26_WO_001,1,,CWI26_WIP,completed,,ACT-0040,ecount_reconstructed
MFG-001,2026-06-20 13:05:00,Manufacturing,BOM Components Calculated,system,CWI26_FG_KIT_BOM,10,,CWI26_WIP,completed,,ACT-0041,ecount_reconstructed
MFG-001,2026-06-20 13:30:00,Manufacturing,Production Receipt Created,production_operator,CWI26_FG_KIT,10,CWI26_WIP,CWI26_FG,completed,,ACT-0046,ecount_reconstructed
```

## 6. Exception Scenario: Material Shortage

```text
F2 = material_shortage
```

Create a work order for 15 kits when enough sensors are not available. Put the work order on hold.

## 7. Exception Scenario: BOM Variance

```text
F4 = bom_variance
```

Standard BOM requires 20 cables for 10 kits. Actual usage is 22 cables. Record variance.

## 8. Metrics

Calculate:

- manufacturing cycle time
- material issue count
- BOM variance quantity
- shortage quantity
- production completion status
- role handoff count
- exception impact

## 9. CWI Finding

Manufacturing risk emerges from combinations of master data, inventory, production rules, and exception states.
