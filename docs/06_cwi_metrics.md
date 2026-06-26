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

# docs/07_limitations_and_ethics.md

# Limitations and Ethics

## 1. Purpose

This document defines the limitations and ethical boundaries of the ERP Workflow CWI Lab.

The project uses ECOUNT demo workflows, synthetic event logs, reconstructed observations, and SAP-style conceptual comparison.

It is important not to overstate what the project proves.

## 2. Main Limitations

### Demo Environment Limitation

ECOUNT is used as a demo environment.

The demo environment may not reflect full production ERP usage.

Some role, approval, customization, data-governance, and export features may be limited.

### Synthetic Data Limitation

Many event logs in this repository are synthetic or reconstructed.

They are designed for workflow analysis and CWI demonstration.

They are not real corporate transaction logs.

### SAP Access Limitation

SAP S/4HANA Cloud Public Edition is used as a conceptual comparison layer.

This project does not claim direct SAP implementation, SAP customization, SAP production data access, or SAP integration unless explicitly implemented later.

### Process Mapping Limitation

ECOUNT and SAP concepts are compared at the process level.

The project does not claim one-to-one equivalence between ECOUNT menus and SAP apps or transactions.

### Metric Limitation

CWI metrics are prototype metrics.

They are useful for research and portfolio demonstration, but they should not be treated as validated enterprise KPIs without additional real-world testing.

## 3. Ethical Principles

### Principle 1: No Private Data Exposure

Do not upload private ERP data, customer information, personal information, credentials, account information, or internal company files.

### Principle 2: Use Synthetic and Sanitized Data

Public repository data should be synthetic, anonymized, reconstructed, or sanitized.

### Principle 3: Do Not Misrepresent Experience

The project should clearly state whether data is:

* synthetic
* reconstructed
* ECOUNT demo observation
* SAP conceptual comparison
* future implementation target

### Principle 4: Respect Platform Boundaries

Do not scrape, abuse, overload, or misuse ERP demo systems.

Use demo environments only for legitimate learning, workflow observation, and prototype analysis.

### Principle 5: Separate Observation from Claim

Correct observation:

```text
This workflow was tested in an ECOUNT demo environment.
```

Incorrect claim:

```text
This is validated across real companies.
```

## 4. Evidence Classification

Recommended evidence labels:

| Label                   | Meaning                                 |
| ----------------------- | --------------------------------------- |
| ecount_demo_observation | observed directly in ECOUNT demo        |
| ecount_reconstructed    | reconstructed from ECOUNT practice flow |
| synthetic_only          | fully synthetic scenario                |
| hybrid_synthetic        | partly observed and partly simulated    |
| sap_conceptual          | SAP-style concept comparison only       |

## 5. Screenshot Policy

Screenshots may be used only if sanitized.

Public screenshots should:

* show only CWI26-prefixed records
* hide unrelated rows
* remove personal information
* remove login data
* remove account information
* remove other users’ demo entries

## 6. Repository Safety

The public repository should not include:

* raw exports containing unrelated data
* private screenshots
* credentials
* cookies
* tokens
* account IDs
* customer information
* real company transaction data
* unsanitized Excel files

Use `.gitignore` to exclude:

```text
raw/
private/
credentials/
unredacted/
.env
.env.*
```

## 7. Correct Public Wording

Use:

```text
ECOUNT-based ERP workflow lab
synthetic event logs
SAP-style conceptual comparison
CWI prototype
workflow intelligence analysis
```

Avoid:

```text
SAP implementation
real ERP deployment
production ERP integration
certified SAP module
official ECOUNT extension
validated enterprise system
```

unless those claims become true in a later stage.

## 8. Academic and Portfolio Honesty

This project is a portfolio and research prototype.

It is acceptable to say:

```text
This project proposes a CWI framework and demonstrates it with ECOUNT demo workflows and synthetic event logs.
```

It is not acceptable to say:

```text
This project proves enterprise ERP performance improvement in production environments.
```

## 9. Data-Origin Transparency

Every dataset should clearly identify its origin.

Recommended values:

* ecount_demo_observation
* ecount_reconstructed
* synthetic_only
* hybrid_synthetic
* sap_conceptual

A synthetic dataset is still useful if it is labeled honestly.

## 10. Final Summary

This project’s credibility depends on honest boundaries.

Its value comes from:

* clear structure
* transparent data labeling
* workflow reasoning
* mathematical scenario design
* careful public documentation
* ethical handling of ERP demo data
