# Combinatorial Scenario Design

## 1. Purpose

This document defines how CWI uses combinatorial scenario design.

ERP workflows often fail because several small exceptions occur together.

CWI models those exceptions as binary factors.

## 2. Six Factors

```text
F1 = partial_receipt
F2 = material_shortage
F3 = warehouse_error
F4 = bom_variance
F5 = qc_hold
F6 = approval_delay
```

## 3. Scenario Space

With six binary factors:

```text
2^6 = 64
```

## 4. First Experiment

Instead of testing all 64 scenarios, start with:

```text
C(6,0) + C(6,1) + C(6,2)
= 1 + 6 + 15
= 22 scenarios
```

This covers:

- baseline scenario
- single-factor scenarios
- two-factor interaction scenarios

## 5. Interpretation

The first 22 scenarios are enough to study baseline behavior, individual exception impact, and basic two-factor interaction effects.

## 6. Future Extension

Later versions can add:

- three-factor scenarios
- weighted factor design
- randomized scenarios
- empirical ECOUNT-based scenario testing
- SAP-style scenario comparison
