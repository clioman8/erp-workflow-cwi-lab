# Sample CWI Report\n\n## 1. Overview\n\nThis report summarizes starter CWI metrics from the synthetic integrated ERP workflow event log.\n\n## 2. Activity Counts\n| activity                   |   count |
|:---------------------------|--------:|
| Purchase Order Created     |       1 |
| Goods Received             |       1 |
| Inventory Updated          |       1 |
| Work Order Created         |       1 |
| BOM Components Calculated  |       1 |
| Production Receipt Created |       1 |
| Sales Order Received       |       1 |
| Availability Checked       |       1 |
| Goods Issued               |       1 |
| Goods Partially Received   |       1 |\n\n## 3. Exception Counts\n| exception_type    |   count |
|:------------------|--------:|
| partial_receipt   |       1 |
| material_shortage |       1 |
| warehouse_error   |       1 |
| bom_variance      |       1 |
| qc_hold           |       1 |
| approval_delay    |       1 |\n\n## 4. Case Cycle Times\n| case_id   | case_start          | case_end            |   cycle_time_minutes |
|:----------|:--------------------|:--------------------|---------------------:|
| MFG-001   | 2026-06-20 13:00:00 | 2026-06-20 13:30:00 |                   30 |
| MFG-002   | 2026-06-21 13:10:00 | 2026-06-21 13:10:00 |                    0 |
| MFG-003   | 2026-06-22 13:25:00 | 2026-06-22 13:25:00 |                    0 |
| MFG-004   | 2026-06-23 14:00:00 | 2026-06-23 14:00:00 |                    0 |
| O2C-001   | 2026-06-20 15:00:00 | 2026-06-20 15:20:00 |                   20 |
| O2C-002   | 2026-06-24 09:10:00 | 2026-06-24 09:10:00 |                    0 |
| P2P-001   | 2026-06-20 09:00:00 | 2026-06-20 10:30:00 |                   90 |
| P2P-002   | 2026-06-21 10:00:00 | 2026-06-21 10:00:00 |                    0 |
| P2P-003   | 2026-06-22 09:15:00 | 2026-06-22 09:15:00 |                    0 |\n\n## 5. Role Handoff Counts\n| case_id   |   role_handoff_count |
|:----------|---------------------:|
| MFG-001   |                    2 |
| MFG-002   |                    0 |
| MFG-003   |                    0 |
| MFG-004   |                    0 |
| O2C-001   |                    2 |
| O2C-002   |                    0 |
| P2P-001   |                    2 |
| P2P-002   |                    0 |
| P2P-003   |                    0 |\n\n## 6. Interpretation\n\nCWI interprets ERP workflow behavior as combinations of activities, roles, constraints, exceptions, and operational outcomes.