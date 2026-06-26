# Master Data Lab

## 1. Purpose

This lab creates the master data required for ERP workflow experiments.

Master data defines the possible workflow universe. Without stable master data, purchasing, inventory, manufacturing, sales, MRP, quality, and approval flows cannot be interpreted correctly.

## 2. ECOUNT Menus

```text
기준정보
├── 품목등록
├── 창고등록
└── 거래처등록

생산관리
└── BOM(소요량)조회
```

## 3. Items

Create or document these items.

| item_code | item_name | item_type | unit |
|---|---|---|---|
| CWI26_RM_PCB | CWI26 제어 PCB | raw_material | EA |
| CWI26_RM_SENSOR | CWI26 센서 모듈 | raw_material | EA |
| CWI26_RM_CABLE | CWI26 연결 케이블 | raw_material | EA |
| CWI26_RM_CASE | CWI26 플라스틱 케이스 | raw_material | EA |
| CWI26_PKG_BOX | CWI26 포장 박스 | packaging | EA |
| CWI26_SUB_CTRL | CWI26 제어부 반제품 | subassembly | EA |
| CWI26_FG_KIT | CWI26 스마트 센서 키트 | finished_good | EA |

Save the public version to:

```text
data/master/items.csv
```

## 4. Warehouses

| warehouse_code | warehouse_name | inventory_status |
|---|---|---|
| CWI26_RAW | Raw Material Warehouse | available |
| CWI26_WIP | Work-in-Process Warehouse | in_process |
| CWI26_FG | Finished Goods Warehouse | available |
| CWI26_QC | Quality Hold Warehouse | blocked |
| CWI26_RETURN | Return Inspection Warehouse | blocked |
| CWI26_SCRAP | Scrap Warehouse | scrapped |

Save the public version to:

```text
data/master/warehouses.csv
```

## 5. Business Partners

| partner_code | partner_type | related_processes |
|---|---|---|
| CWI26_VENDOR_A | vendor | P2P;Manufacturing |
| CWI26_VENDOR_B | vendor | P2P;Manufacturing |
| CWI26_CUSTOMER_A | customer | O2C |
| CWI26_CUSTOMER_B | customer | O2C |
| CWI26_OUTSOURCE_A | outsourcing_partner | Manufacturing;P2P |
| CWI26_INTERNAL_QC | internal_department | Manufacturing;Traceability |

Save the public version to:

```text
data/master/business_partners.csv
```

## 6. BOM

Subassembly BOM:

```text
CWI26_SUB_CTRL = 1 x CWI26_RM_PCB + 2 x CWI26_RM_CABLE
```

Finished good BOM:

```text
CWI26_FG_KIT = 1 x CWI26_SUB_CTRL + 1 x CWI26_RM_SENSOR + 1 x CWI26_RM_CASE + 1 x CWI26_PKG_BOX
```

Save the public version to:

```text
data/master/bom.csv
```

## 7. Action Log Examples

```csv
ACT-0001,2026-06-20 10:00,LAB-01,품목등록,create,item,CWI26_RM_PCB,CWI26 제어 PCB,EA unit and barcode entered,Item master created,Created in demo list,EV-001,Sanitized screenshot saved,ecount_demo_observation
ACT-0002,2026-06-20 10:30,LAB-01,창고등록,create,warehouse,CWI26_RAW,Raw Material Warehouse,Raw material warehouse created,Warehouse master created,Created in demo list,EV-002,Sanitized screenshot saved,ecount_demo_observation
```

## 8. CWI Finding

ERP workflow behavior begins before transactions. It begins at the master-data rule level.
