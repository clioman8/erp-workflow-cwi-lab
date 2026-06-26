# docs/05_sap_public_edition_crosswalk.md

# SAP Public Edition Crosswalk

## 1. Purpose

This document maps ECOUNT-based ERP practice concepts to SAP S/4HANA Cloud Public Edition concepts at a high level.

This is a conceptual crosswalk.

It is not a claim of one-to-one transaction equivalence.

The purpose is to connect hands-on ECOUNT workflow practice with enterprise ERP concepts used in SAP-style process thinking.

## 2. Why SAP Is Used as a Comparison Layer

Direct SAP practice access may be limited by paid Learning Hub or practice-system requirements.

Therefore, this project uses SAP S/4HANA Cloud Public Edition primarily as:

* a conceptual comparison layer
* a terminology reference
* a standard enterprise ERP process model
* a future extension target
* a way to compare ECOUNT workflows with larger-scale ERP architecture

ECOUNT is used as the practical demo environment.

Synthetic event logs are used for repeatable CWI analysis.

## 3. Crosswalk Principles

### Principle 1: Map processes before screens

The project maps generic workflow logic before comparing specific screens or applications.

### Principle 2: Use generic ERP concepts

When exact SAP app-level access is unavailable, use generic ERP process language.

### Principle 3: Avoid false equivalence

ECOUNT menus and SAP apps should not be treated as identical.

### Principle 4: Mark mapping confidence

Each mapping should have a confidence level.

### Principle 5: Be honest about evidence

Use the phrase:

```text
SAP-style conceptual comparison
```

Do not claim:

```text
SAP implementation
SAP configuration
SAP integration
SAP production deployment
```

unless those are actually implemented later.

## 4. Process-Level Crosswalk

| ECOUNT concept | Generic ERP process              | SAP-style concept                            | Mapping level            | Confidence |
| -------------- | -------------------------------- | -------------------------------------------- | ------------------------ | ---------- |
| 발주서입력          | Purchase Order                   | Purchase Order                               | process                  | high       |
| 구매입력           | Goods Receipt / Purchase Posting | Procurement Execution                        | process                  | medium     |
| 구매조회           | Purchase Monitoring              | Purchase Order / Goods Receipt Monitoring    | reporting                | medium     |
| 품목등록           | Item Master                      | Product / Material Master                    | master data              | high       |
| 창고등록           | Warehouse / Storage Location     | Plant / Storage Location / Warehouse concept | master data              | medium     |
| 거래처등록          | Business Partner                 | Business Partner                             | master data              | high       |
| 주문서입력          | Sales Order                      | Sales Order                                  | process                  | high       |
| 판매입력           | Goods Issue / Sales Posting      | Outbound Delivery / Billing-related process  | process                  | medium     |
| BOM(소요량)조회     | Bill of Materials                | BOM                                          | master data / production | high       |
| 작업지시서입력        | Work Order                       | Production Order                             | process                  | high       |
| 생산입고           | Production Receipt               | Goods Receipt from Production                | process                  | medium     |
| 재고조회           | Inventory Visibility             | Stock Overview                               | reporting                | high       |
| 품질보류창고         | QC Hold / Blocked Stock          | Quality Inspection / Blocked Stock concept   | process                  | medium     |
| 전자결재           | Approval Workflow                | Flexible Workflow / Approval concept         | workflow                 | medium     |

## 5. P2P Crosswalk

### ECOUNT Practice Flow

```text
발주서입력
→ 구매입력
→ 재고조회
```

### Generic ERP Flow

```text
Purchase Order
→ Goods Receipt
→ Inventory Update
```

### SAP-Style Flow

```text
Purchase Order
→ Goods Receipt
→ Stock Update
→ Invoice / Payment process
```

### CWI Interpretation

CWI focuses on event sequence, role handoff, inventory status, exception propagation, and delay.

The exact screen is less important than the workflow behavior.

## 6. O2C Crosswalk

### ECOUNT Practice Flow

```text
주문서입력
→ 판매입력
→ 재고조회
```

### Generic ERP Flow

```text
Sales Order
→ Availability Check
→ Goods Issue
→ Sales Completion
```

### SAP-Style Flow

```text
Sales Order
→ Delivery / Goods Issue
→ Billing / Receivables
```

### CWI Interpretation

CWI focuses on demand, availability, approval, shipment timing, and customer-facing delay.

## 7. Manufacturing Crosswalk

### ECOUNT Practice Flow

```text
BOM 등록
→ 작업지시서입력
→ 생산입고
→ 재고조회
```

### Generic ERP Flow

```text
BOM
→ Work Order
→ Material Issue
→ Production Receipt
→ Inventory Update
```

### SAP-Style Flow

```text
BOM
→ Production Order
→ Goods Issue
→ Confirmation
→ Goods Receipt
```

### CWI Interpretation

CWI focuses on BOM dependency, material shortage, variance, QC hold, and production bottleneck.

## 8. Inventory Crosswalk

### ECOUNT Practice Flow

```text
재고조회
→ 재고조정
→ 창고 이동
→ Lot/Serial 추적
```

### Generic ERP Flow

```text
Stock Overview
→ Inventory Adjustment
→ Stock Transfer
→ Traceability
```

### SAP-Style Flow

```text
Stock Overview
→ Goods Movement
→ Transfer Posting
→ Batch / Serial Tracking
```

### CWI Interpretation

CWI focuses on warehouse accuracy, stock status, blocked inventory, and traceability risk.

## 9. Master Data Crosswalk

| CWI master data | ECOUNT                  | SAP-style concept                            |
| --------------- | ----------------------- | -------------------------------------------- |
| item            | 품목                      | Product / Material                           |
| warehouse       | 창고                      | Plant / Storage Location / Warehouse concept |
| vendor          | 거래처                     | Business Partner - Supplier                  |
| customer        | 거래처                     | Business Partner - Customer                  |
| BOM             | BOM                     | Bill of Materials                            |
| role            | synthetic role matrix   | business role / authorization concept        |
| approval rule   | synthetic approval rule | workflow / approval configuration concept    |
| QC location     | 품질보류창고                  | inspection / blocked stock concept           |

## 10. Data Mapping Crosswalk

| CWI event-log field | ECOUNT source                   | SAP-style interpretation |
| ------------------- | ------------------------------- | ------------------------ |
| case_id             | reconstructed case ID           | process instance         |
| timestamp           | action log / reconstructed time | event time               |
| process             | P2P, O2C, Manufacturing         | business process area    |
| activity            | standardized activity           | business event           |
| actor_role          | synthetic role                  | business role            |
| object_code         | item/order/work order code      | business object          |
| quantity            | transaction quantity            | posted quantity          |
| from_location       | supplier/source warehouse       | source object/location   |
| to_location         | customer/target warehouse       | target object/location   |
| status              | event status                    | process status           |
| exception_type      | CWI exception marker            | exception / variant      |
| data_origin         | evidence label                  | source classification    |

## 11. Limitations

This crosswalk does not claim:

* SAP configuration experience
* SAP implementation authority
* production SAP data access
* direct SAP integration
* one-to-one ECOUNT-to-SAP transaction mapping
* certified SAP module development

The correct public wording is:

```text
SAP-style conceptual comparison layer
```

Not:

```text
SAP-integrated implementation
```

## 12. Future Extension

If SAP practice access becomes available later, this crosswalk can be extended into:

* SAP Fiori app observation notes
* SAP process event logs
* SAP-style role mapping
* SAP workflow approval comparison
* SAP-to-ECOUNT process variance analysis
* SAP BTP-based CWI dashboard prototype

## 13. Final Summary

ECOUNT provides hands-on workflow practice.

SAP provides enterprise-level terminology and process comparison.

CWI provides the analytical layer that connects them.

The project therefore remains honest:

```text
ECOUNT-based ERP workflow lab
+ synthetic event logs
+ SAP-style conceptual comparison
+ CWI analysis
```
