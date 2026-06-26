# docs/06_cwi_metrics.md

# CWI Metrics

## 1. Overview

This document defines the main metrics used in the ERP Workflow CWI Lab.

The metrics are designed for:

* synthetic event logs
* reconstructed ECOUNT demo observations
* CWI scenario analysis
* SAP-style conceptual comparison
* future ERP workflow datasets

The metrics are not meant to replace official ERP reports.

They provide an analytical layer for workflow visibility and operational intelligence.

## 2. Minimum Event Log Schema

The minimum event log schema is:

```csv
case_id,timestamp,process,activity,actor_role,object_code,quantity,from_location,to_location,status,exception_type,source_action_id,data_origin
```

## 3. Recommended Optional Columns

Future versions may add:

```csv
scenario_id,bitmask,hamming_weight,expected_duration_minutes,actual_duration_minutes,cost_impact,approval_rule_id
```

The first version keeps the event log simple and joins scenario information from separate scenario files.

## 4. Case Cycle Time

Case cycle time measures how long one workflow instance takes.

```text
cycle_time = max(timestamp) - min(timestamp)
```

Examples:

* time from purchase order creation to goods receipt
* time from work order creation to production receipt
* time from sales order receipt to goods issue
* time from QC hold to QC release

### Interpretation

Long cycle time may indicate:

* bottleneck
* waiting
* approval delay
* shortage
* rework
* blocked inventory
* role handoff delay

## 5. Activity Frequency

Activity frequency counts how often each activity appears.

Examples:

```text
Goods Received
Inventory Updated
Work Order Created
Material Shortage Detected
QC Hold Applied
Approval Completed
```

### Interpretation

High frequency activities may indicate:

* central workflow steps
* repeated manual work
* rework
* bottleneck candidates
* process instability

## 6. Exception Frequency

Exception frequency counts each exception type.

Examples:

```text
partial_receipt
material_shortage
warehouse_error
bom_variance
qc_hold
approval_delay
```

### Interpretation

High exception frequency may indicate:

* weak process control
* unstable supplier performance
* poor master data quality
* production planning weakness
* unclear approval rules
* inventory visibility problem

## 7. Role Handoff Count

Role handoff count measures how often a case moves from one role to another.

Example:

```text
buyer → warehouse_operator → system
```

Another example:

```text
production_planner → system → production_operator → quality_checker → manager
```

### Interpretation

High handoff count can indicate:

* coordination burden
* approval complexity
* role fragmentation
* workflow risk
* training complexity

## 8. Handoff Density

Handoff density is:

```text
handoff_density = role_handoff_count / total_activity_count
```

A high value suggests that the workflow depends heavily on cross-role coordination.

## 9. Bottleneck Score

A simple bottleneck score can be defined as:

```text
bottleneck_score(activity) =
activity_frequency × average_delay_after_activity
```

If direct delay data is unavailable, activity frequency and exception co-occurrence can be used as proxies.

### Interpretation

High bottleneck score may indicate:

* activity repeatedly waits for another role
* approval threshold is too strict
* inventory status is unclear
* manual review is too frequent
* system calculation depends on unstable master data

## 10. Combinatorial Stress Level

Combinatorial Stress Level, abbreviated as CSL, measures how many exception factors are active in a scenario.

For a binary factor vector:

```text
x = (x1, x2, ..., xm)
```

CSL is:

```text
CSL = sum(xi)
```

Examples:

```text
000000 → CSL 0
100000 → CSL 1
110000 → CSL 2
111000 → CSL 3
```

This is equivalent to Hamming weight.

## 11. Scenario Coverage

Scenario coverage measures how much of the combinatorial scenario space has been tested.

If m binary factors exist, the full scenario space is:

```text
2^m
```

If n scenarios were executed:

```text
scenario_coverage = n / 2^m
```

For six factors and 22 tested scenarios:

```text
scenario_coverage = 22 / 64 = 34.375%
```

### Interpretation

Scenario coverage prevents the project from pretending that a few cases represent the entire workflow space.

## 12. Single-Factor Impact

Single-factor impact compares each single-exception scenario to the baseline.

```text
impact_i = L_i - L_0
```

Where:

* L_0 = baseline cycle time
* L_i = cycle time with factor i active

### Interpretation

This shows how much delay or disruption one exception creates.

Examples:

* partial receipt impact
* material shortage impact
* warehouse error impact
* BOM variance impact
* QC hold impact
* approval delay impact

## 13. Two-Factor Interaction Effect

Two-factor interaction effect measures whether two exceptions together create additional impact beyond their separate effects.

```text
I_ij = L_ij - L_i - L_j + L_0
```

Where:

* L_0 = baseline cycle time
* L_i = cycle time with factor i
* L_j = cycle time with factor j
* L_ij = cycle time with both factors

### Interpretation

Positive I_ij suggests that the two exceptions amplify each other.

Example:

```text
material_shortage + qc_hold
```

may create more workflow delay than the sum of each individual delay.

## 14. Authority Mismatch Count

Authority mismatch count detects events where the actor role does not match the expected decision authority.

Examples:

* sales_operator requests approval but manager approval is delayed
* production_operator enters variance but production_planner must review
* warehouse_operator tries to move QC-held stock without quality release
* buyer creates high-value purchase order requiring manager approval

This metric depends on:

```text
data/master/role_matrix.csv
data/master/approval_rules.csv
```

## 15. Knowledge Gap Signal

Knowledge gap signal is a qualitative or semi-structured marker for cases where workflow failure is caused by unclear process understanding.

Examples:

* repeated correction
* wrong warehouse selection
* BOM variance without explanation
* approval rule not followed
* backorder not escalated
* incorrect object code used
* missing traceability record

This metric is especially relevant to onboarding, ERP training, and workflow documentation analysis.

## 16. Data-Origin Ratio

Data-origin ratio measures how much of the dataset comes from each source.

Recommended data-origin labels:

```text
ecount_demo_observation
ecount_reconstructed
synthetic_only
hybrid_synthetic
sap_conceptual
```

### Interpretation

This protects the project from overstating the evidence.

A high synthetic-only ratio is not bad.

It simply means the dataset should be described as a prototype simulation rather than a real ERP extraction.

## 17. Process Variant Count

A process variant is a distinct activity sequence for the same process family.

Example baseline P2P variant:

```text
Purchase Order Created
→ Goods Received
→ Inventory Updated
```

Exception P2P variant:

```text
Purchase Order Created
→ Goods Partially Received
→ Backorder Recorded
```

### Interpretation

More variants may indicate:

* process flexibility
* exception frequency
* workflow instability
* different operational modes
* need for better standardization

## 18. Status Distribution

Status distribution counts event statuses.

Examples:

```text
completed
pending
exception
on_hold
closed_with_exception
```

### Interpretation

A high number of pending or exception statuses may indicate workflow instability.

## 19. Recommended First Metrics

For the first version of the project, compute:

1. event count by process
2. event count by activity
3. event count by actor_role
4. exception count by type
5. status count
6. case cycle time
7. role handoff count
8. data-origin ratio
9. process variant count

Then add:

1. Combinatorial Stress Level
2. scenario coverage
3. single-factor impact
4. two-factor interaction effect
5. bottleneck score
6. authority mismatch count

## 20. Final Summary

CWI metrics translate ERP workflow events into operational intelligence.

They help answer:

* where the workflow slows down
* which roles create handoff complexity
* which exceptions appear most often
* which combinations create the largest impact
* which approval rules cause delays
* which process variants indicate risk
