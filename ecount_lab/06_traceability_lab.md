# Traceability Lab

## 1. Purpose

This lab studies traceability.

Traceability means the ability to follow items, lots, serial numbers, warehouse movements, QC status, and production history across the ERP workflow.

## 2. Traceability Flow

```text
Item Received
→ Lot or Serial Assigned
→ Material Issued
→ Production Receipt Created
→ QC Hold or Release
→ Goods Issued
→ Traceability Record Reviewed
```

## 3. ECOUNT Menus

```text
재고조회
재고조정
바코드
Lot/Serial 관련 메뉴
구매입력
판매입력
생산입고
```

## 4. Traceability Targets

| object_code | tracking_type | reason |
|---|---|---|
| CWI26_RM_PCB | lot | raw material batch tracking |
| CWI26_RM_SENSOR | lot | supplier quality tracking |
| CWI26_FG_KIT | serial | finished goods shipment tracking |

## 5. Event Log Rows

```csv
case_id,timestamp,process,activity,actor_role,object_code,quantity,from_location,to_location,status,exception_type,source_action_id,data_origin
TRC-001,2026-06-28 09:00:00,Traceability,Lot Received,warehouse_operator,CWI26_RM_SENSOR,20,CWI26_VENDOR_A,CWI26_RAW,completed,,ACT-0300,ecount_reconstructed
TRC-001,2026-06-28 10:00:00,Traceability,Lot Material Issued,production_operator,CWI26_RM_SENSOR,10,CWI26_RAW,CWI26_WIP,completed,,ACT-0301,ecount_reconstructed
TRC-001,2026-06-28 11:00:00,Traceability,Serial Finished Goods Created,production_operator,CWI26_FG_KIT,10,CWI26_WIP,CWI26_FG,completed,,ACT-0302,hybrid_synthetic
TRC-001,2026-06-28 13:00:00,Traceability,Serial Goods Shipped,warehouse_operator,CWI26_FG_KIT,6,CWI26_FG,CWI26_CUSTOMER_A,completed,,ACT-0303,hybrid_synthetic
```

## 6. Exception Scenario: QC Hold

```text
F5 = qc_hold
```

Finished goods are produced but moved to `CWI26_QC` instead of `CWI26_FG`. They are released later.

## 7. Metrics

Calculate:

- lot-to-production linkage count
- serial-to-customer linkage count
- QC hold duration
- blocked inventory quantity
- role handoff count
- traceability completeness score

## 8. CWI Finding

Traceability is workflow memory. It connects material history, production execution, quality status, and customer shipment into one operational chain.
