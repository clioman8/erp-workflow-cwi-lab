# Order-to-Cash Lab

## 1. Purpose

This lab practices the Order-to-Cash workflow.

O2C covers sales order entry, availability checking, goods issue, inventory update, and sales completion.

## 2. Normal Flow

```text
Sales Order Received
→ Availability Checked
→ Goods Issued
→ Inventory Updated
→ Sales Completed
```

## 3. ECOUNT Menus

```text
주문서입력
주문서조회
판매입력
판매조회
재고조회
```

## 4. Baseline Scenario

Customer:

```text
CWI26_CUSTOMER_A
```

Item:

```text
CWI26_FG_KIT
```

Quantity:

```text
6 units
```

Warehouse:

```text
CWI26_FG
```

## 5. Event Log Rows

```csv
case_id,timestamp,process,activity,actor_role,object_code,quantity,from_location,to_location,status,exception_type,source_action_id,data_origin
O2C-001,2026-06-20 15:00:00,O2C,Sales Order Received,sales_operator,CWI26_SO_001,1,CWI26_CUSTOMER_A,CWI26_FG,completed,,ACT-0050,ecount_reconstructed
O2C-001,2026-06-20 15:05:00,O2C,Availability Checked,system,CWI26_FG_KIT,6,CWI26_FG,CWI26_CUSTOMER_A,completed,,ACT-0051,ecount_reconstructed
O2C-001,2026-06-20 15:20:00,O2C,Goods Issued,warehouse_operator,CWI26_FG_KIT,6,CWI26_FG,CWI26_CUSTOMER_A,completed,,ACT-0052,ecount_reconstructed
```

## 6. Exception Scenario: Approval Delay

```text
F6 = approval_delay
```

If approval workflow cannot be fully tested in ECOUNT demo, simulate it using synthetic event-log rows.

## 7. Metrics

Calculate:

- O2C case cycle time
- approval waiting time
- finished goods inventory reduction
- shipment delay
- role handoff count

## 8. CWI Finding

Customer-facing workflow stability depends on upstream production and internal authority flow.
