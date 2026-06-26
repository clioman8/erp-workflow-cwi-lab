# docs/04_process_catalog.md

# Process Catalog

## 1. Overview

This document defines the ERP workflow processes used in the ERP Workflow CWI Lab.

The purpose of this catalog is to standardize process names, activity names, roles, objects, and exception types so that ECOUNT demo observations and synthetic event logs can be analyzed consistently.

The current project scope includes:

* Procure-to-Pay
* Order-to-Cash
* Manufacturing
* Inventory and Traceability
* Quality Hold
* Approval Flow
* Planning / MPS / MRP

## 2. Procure-to-Pay

Procure-to-Pay, abbreviated as P2P, covers purchasing, goods receipt, inventory update, and supplier-side exception handling.

### Normal Flow

```text
Purchase Order Created
→ PO Line Added
→ Goods Received
→ Inventory Updated
→ Purchase Completed
```

### Main Roles

* buyer
* warehouse_operator
* accountant
* manager
* system

### Main Objects

* purchase_order
* vendor
* item
* warehouse
* goods receipt
* inventory record
* invoice

### ECOUNT Menus

```text
발주서입력
발주서조회
구매입력
구매조회
재고조회
```

### Common Exceptions

* partial_receipt
* supplier_delay
* wrong_item_received
* warehouse_error
* quantity_mismatch
* invoice_mismatch
* approval_delay

### CWI Question

Which purchasing conditions create receiving delays, backorders, inventory mismatch, or downstream production risk?

## 3. Order-to-Cash

Order-to-Cash, abbreviated as O2C, covers customer order entry, availability checking, goods issue, shipment, and sales completion.

### Normal Flow

```text
Sales Order Received
→ Availability Checked
→ Approval Completed
→ Goods Issued
→ Inventory Updated
→ Sales Completed
```

### Main Roles

* sales_operator
* warehouse_operator
* manager
* accountant
* system

### Main Objects

* sales_order
* customer
* finished_good
* warehouse
* shipment
* receivable

### ECOUNT Menus

```text
주문서입력
주문서조회
판매입력
판매조회
재고조회
```

### Common Exceptions

* approval_delay
* urgent_order
* inventory_shortage
* shipment_delay
* customer_order_change
* return_request
* availability_mismatch

### CWI Question

Which sales, approval, and inventory conditions delay shipment or create customer-facing workflow instability?

## 4. Manufacturing

Manufacturing covers BOM-based production, work orders, material issue, production receipt, and finished-goods inventory update.

### Normal Flow

```text
Work Order Created
→ BOM Components Calculated
→ Material Issued
→ Production Receipt Created
→ Inventory Updated
```

### Main Roles

* production_planner
* production_operator
* warehouse_operator
* quality_checker
* manager
* system

### Main Objects

* work_order
* BOM
* raw_material
* subassembly
* finished_good
* WIP warehouse
* finished goods warehouse

### ECOUNT Menus

```text
BOM(소요량)조회
작업지시서입력
작업지시서조회
생산입고 I
생산입고 II
생산입고조회
재고조회
```

### Common Exceptions

* material_shortage
* bom_variance
* qc_hold
* production_delay
* incomplete_output
* scrap
* rework
* warehouse_error

### CWI Question

Which combinations of BOM, inventory, QC, warehouse, and approval factors increase production cycle time?

## 5. Inventory and Traceability

Inventory and traceability cover warehouse movement, stock visibility, item tracking, lot tracking, serial tracking, and inventory correction.

### Normal Flow

```text
Inventory Movement Created
→ Warehouse Updated
→ Quantity Verified
→ Traceability Record Updated
```

### Main Roles

* warehouse_operator
* production_operator
* quality_checker
* system

### Main Objects

* item
* warehouse
* lot
* serial number
* inventory transaction
* transfer record

### ECOUNT Menus

```text
재고조회
재고조정
구매입력
판매입력
생산입고
Lot/Serial 관련 메뉴
바코드 관련 메뉴
```

### Common Exceptions

* warehouse_error
* quantity_mismatch
* lot_mismatch
* serial_tracking_error
* inventory_adjustment
* blocked_stock
* missing_traceability

### CWI Question

Which inventory or traceability errors propagate into purchasing, production, quality, or sales workflows?

## 6. Quality Hold

Quality hold covers blocked inventory, inspection status, release decisions, scrap, and rework.

### Normal Flow

```text
QC Hold Applied
→ Defect Checked
→ QC Decision Made
→ QC Released or Scrapped
→ Inventory Updated
```

### Main Roles

* quality_checker
* production_planner
* warehouse_operator
* manager
* system

### Main Objects

* raw_material
* finished_good
* QC warehouse
* defect record
* release approval
* scrap record

### ECOUNT Representation

In this project, quality hold may be represented by:

```text
CWI26_QC warehouse
status = on_hold
exception_type = qc_hold
```

If ECOUNT demo access does not support the full quality workflow, QC hold is modeled using hybrid or synthetic event logs.

### Common Exceptions

* qc_hold
* release_delay
* defect_found
* rework_required
* scrap_required
* blocked_inventory

### CWI Question

How does QC hold interact with material shortage, production delay, sales order pressure, and approval delay?

## 7. Approval Flow

Approval flow is modeled as a workflow constraint.

In ECOUNT demo practice, direct role-based approval testing may be limited. Therefore, approval flow is partly represented through synthetic event logs and approval rules.

### Normal Flow

```text
Approval Requested
→ Approval Reviewed
→ Approval Completed
→ Next Activity Released
```

### Main Roles

* requester
* manager
* accountant
* quality_checker
* production_planner

### Main Objects

* purchase order
* sales order
* work order
* QC release
* BOM variance
* invoice exception

### Common Exceptions

* approval_delay
* approval_rejection
* authority_mismatch
* late_escalation
* threshold_violation

### CWI Question

Which approval thresholds or role dependencies create workflow bottlenecks?

## 8. Planning / MPS / MRP

Planning covers customer demand, inventory checking, BOM explosion, shortage identification, and replenishment planning.

### Normal Flow

```text
Demand Created
→ Inventory Checked
→ BOM Requirements Calculated
→ Shortage Identified
→ Purchase or Production Plan Suggested
```

### Main Roles

* sales_operator
* production_planner
* buyer
* warehouse_operator
* system

### Main Objects

* sales order
* demand plan
* finished good
* BOM
* raw material
* purchase order
* work order

### Common Exceptions

* material_shortage
* demand_spike
* planning_delay
* supplier_delay
* inventory_mismatch
* capacity_shortage

### CWI Question

How does customer demand expand through BOM, inventory, purchasing, and production rules?

## 9. Integrated Workflow View

ERP workflows are connected.

A P2P delay can create material shortage.

A material shortage can delay manufacturing.

A manufacturing delay can reduce finished goods availability.

A finished goods shortage can delay O2C shipment.

A QC hold can block both inventory and customer delivery.

An approval delay can freeze an otherwise valid transaction.

This means ERP workflow risk is often combinatorial rather than isolated.

## 10. Process Family Summary

| Process       | Main Input           | Main Output               | CWI Focus                         |
| ------------- | -------------------- | ------------------------- | --------------------------------- |
| P2P           | purchase need        | received inventory        | supplier and receiving exceptions |
| O2C           | customer demand      | shipped goods             | demand, approval, shipment        |
| Manufacturing | BOM and work order   | finished goods            | production exceptions             |
| Inventory     | movement records     | stock visibility          | traceability and correctness      |
| QC            | inspection decision  | released or blocked stock | blocked-flow analysis             |
| Approval      | threshold condition  | release or delay          | role and authority bottleneck     |
| Planning      | demand and inventory | replenishment signal      | shortage and propagation          |

## 11. Final Summary

The process catalog defines the common workflow language of this project.

All event logs, role matrices, approval rules, metrics, diagrams, and reports should use the process families and activity names defined here.
