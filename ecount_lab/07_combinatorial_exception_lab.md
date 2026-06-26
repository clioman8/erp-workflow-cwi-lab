# Combinatorial Exception Lab

## 1. Purpose

This lab is the core CWI experiment.

It designs and analyzes workflow exception combinations using binary factor encoding and combinatorial scenario design.

## 2. CWI Principle

```text
Small local workflow rules create large global workflow patterns.
```

Each exception is treated as a binary factor. A workflow scenario is represented as a bitmask.

## 3. Exception Factors

| factor_code | factor_name | 0_state | 1_state | execution_mode |
|---|---|---|---|---|
| F1 | partial_receipt | full_receipt | partial_receipt | ecount_observed |
| F2 | material_shortage | sufficient | shortage | ecount_observed |
| F3 | warehouse_error | correct_warehouse | wrong_warehouse | ecount_observed |
| F4 | bom_variance | standard_usage | usage_variance | ecount_observed |
| F5 | qc_hold | released | on_hold | hybrid |
| F6 | approval_delay | on_time | delayed | synthetic_only |

## 4. Scenario Space

With six binary factors:

```text
2^6 = 64
```

First experiment:

```text
C(6,0) + C(6,1) + C(6,2) = 1 + 6 + 15 = 22 scenarios
```

## 5. Scenario ID Rule

Bit order:

```text
F1 F2 F3 F4 F5 F6
```

Examples:

```text
CWI-000000 = baseline
CWI-100000 = F1 only
CWI-010000 = F2 only
CWI-101000 = F1 + F3
```

## 6. Recommended First Execution

Baseline:

```text
CWI-000000
```

Single-factor scenarios:

```text
CWI-100000
CWI-010000
CWI-001000
CWI-000100
CWI-000010
CWI-000001
```

Two-factor starting scenarios:

```text
CWI-101000 = partial_receipt + warehouse_error
CWI-010010 = material_shortage + qc_hold
CWI-000101 = bom_variance + approval_delay
```

## 7. Metrics

Calculate:

- scenario count
- scenario coverage
- Hamming weight
- baseline cycle time
- single-factor impact
- two-factor interaction effect
- role handoff count
- bottleneck activity
- exception frequency
- status distribution

## 8. CWI Finding

ERP workflow risk often emerges from combinations of small exceptions rather than from one isolated error.

This lab connects:

```text
Pascal / binomial scenario space
→ binary exception encoding
→ ERP event logs
→ workflow metrics
→ operational intelligence
```
