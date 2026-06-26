# Procure-to-Pay Lab

## 1. Purpose

This lab practices the Procure-to-Pay workflow.

P2P covers purchase order creation, goods receipt, inventory update, and supplier-side exception handling.

## 2. Normal Flow

```text
Purchase Order Created
→ PO Line Added
→ Goods Received
→ Inventory Updated
→ Purchase Completed
```

## 3. ECOUNT Menus

```text
발주서입력
발주서조회
구매입력
구매조회
재고조회
```

## 4. Baseline Scenario

Create a purchase order from `CWI26_VENDOR_A` and receive goods into `CWI26_RAW`.

| item_code | quantity | supplier | target warehouse |
|---|---:|---|---|
| CWI26_RM_PCB | 20 | CWI26_VENDOR_A | CWI26_RAW |
| CWI26_RM_SENSOR | 20 | CWI26_VENDOR_A | CWI26_RAW |
| CWI26_RM_CABLE | 50 | CWI26_VENDOR_A | CWI26_RAW |
| CWI26_RM_CASE | 20 | CWI26_VENDOR_A | CWI26_RAW |
| CWI26_PKG_BOX | 20 | CWI26_VENDOR_B | CWI26_RAW |

## 5. Event Log Rows

```csv
case_id,timestamp,process,activity,actor_role,object_code,quantity,from_location,to_location,status,exception_type,source_action_id,data_origin
P2P-001,2026-06-20 09:00:00,P2P,Purchase Order Created,buyer,CWI26_PO_001,1,CWI26_VENDOR_A,CWI26_RAW,completed,,ACT-0020,ecount_reconstructed
P2P-001,2026-06-20 10:00:00,P2P,Goods Received,warehouse_operator,CWI26_RM_PCB,20,CWI26_VENDOR_A,CWI26_RAW,completed,,ACT-0026,ecount_reconstructed
P2P-001,2026-06-20 10:30:00,P2P,Inventory Updated,system,CWI26_RM_PCB,20,,CWI26_RAW,completed,,ACT-0031,ecount_reconstructed
```

## 6. Exception Scenario: Partial Receipt

```text
F1 = partial_receipt
```

Order 20 units of `CWI26_RM_PCB`, receive only 12, and record 8 units as backorder.

## 7. Exception Scenario: Wrong Warehouse

```text
F3 = warehouse_error
```

Receive `CWI26_RM_CASE` into `CWI26_QC` instead of `CWI26_RAW`, detect the error, then transfer it to the correct warehouse.

## 8. Metrics

Calculate:

- P2P case cycle time
- event count
- exception frequency
- role handoff count
- backorder quantity
- delay between receipt and correction

## 9. CWI Finding

Supplier-side exceptions create downstream workflow risk.
