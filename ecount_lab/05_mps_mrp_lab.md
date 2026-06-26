# MPS and MRP Lab

## 1. Purpose

This lab observes MPS and MRP-style planning logic.

The goal is to understand how demand, inventory, BOM, safety stock, and lead time create purchasing or production requirements.

## 2. Planning Flow

```text
Demand Created
→ Inventory Checked
→ BOM Requirements Calculated
→ Shortage Identified
→ Purchase or Production Plan Suggested
```

## 3. ECOUNT Menus

```text
MPS
MRP
BOM(소요량)조회
주문서입력
발주서입력
재고조회
```

If MPS/MRP menus are unavailable in the demo, reconstruct the scenario using sales demand, inventory, and BOM requirements.

## 4. Scenario

Demand:

```text
CWI26_CUSTOMER_B orders 30 units of CWI26_FG_KIT.
```

Current inventory assumption:

```text
CWI26_FG_KIT = 4 units
```

Planning need:

```text
30 demanded - 4 available = 26 additional kits required
```

Expected component requirement:

```text
CWI26_SUB_CTRL = 26
CWI26_RM_SENSOR = 26
CWI26_RM_CASE = 26
CWI26_PKG_BOX = 26
```

## 5. Event Log Rows

```csv
case_id,timestamp,process,activity,actor_role,object_code,quantity,from_location,to_location,status,exception_type,source_action_id,data_origin
MRP-001,2026-06-27 09:00:00,Planning,Demand Created,sales_operator,CWI26_SO_MRP_001,30,CWI26_CUSTOMER_B,CWI26_FG,completed,material_shortage,ACT-0200,ecount_reconstructed
MRP-001,2026-06-27 09:10:00,Planning,Inventory Checked,system,CWI26_FG_KIT,4,CWI26_FG,CWI26_CUSTOMER_B,completed,material_shortage,ACT-0201,ecount_reconstructed
MRP-001,2026-06-27 09:30:00,Planning,MRP Requirement Calculated,system,CWI26_FG_KIT,26,,CWI26_FG,pending,material_shortage,ACT-0202,hybrid_synthetic
MRP-001,2026-06-27 09:40:00,Planning,Component Shortage Identified,system,CWI26_RM_SENSOR,16,CWI26_RAW,CWI26_WIP,exception,material_shortage,ACT-0202,hybrid_synthetic
```

## 6. Metrics

Calculate:

- demand quantity
- available inventory
- shortage quantity
- number of shortage components
- planning response time
- generated replenishment actions
- role handoff count

## 7. CWI Finding

Demand is not a single event. It expands through BOM, inventory, purchasing, production, and planning rules.
