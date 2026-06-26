## 3. Binomial Coefficients and Scenario Space

The binomial coefficient counts the number of ways to choose k factors from n factors.

In CWI, this becomes a way to count workflow exception scenarios.

If there are m binary exception factors, then the total number of possible scenarios is:

```text
2^m
```

If m = 6, then there are:

```text
2^6 = 64
```

possible exception combinations.

For six factors:

```text
F1 = partial_receipt
F2 = material_shortage
F3 = warehouse_error
F4 = bom_variance
F5 = qc_hold
F6 = approval_delay
```

A scenario can be represented as a binary vector.

```text
000000 = no exception
100000 = partial receipt only
010000 = material shortage only
110000 = partial receipt + material shortage
```

## 4. Pascal Row Interpretation

For six factors, Pascal row 6 is:

```text
1, 6, 15, 20, 15, 6, 1
```

This means:

| Active exception count | Number of scenarios |
| ---------------------: | ------------------: |
|                      0 |                   1 |
|                      1 |                   6 |
|                      2 |                  15 |
|                      3 |                  20 |
|                      4 |                  15 |
|                      5 |                   6 |
|                      6 |                   1 |

This helps define a practical experiment design.

Instead of testing all 64 scenarios at once, the project can start with:

```text
C(6,0) + C(6,1) + C(6,2)
= 1 + 6 + 15
= 22 scenarios
```

This produces:

* 1 baseline scenario
* 6 single-factor scenarios
* 15 two-factor interaction scenarios

## 5. Binary Encoding

Each scenario is encoded as a bitmask.

Example:

```text
CWI-000000 = baseline
CWI-100000 = partial receipt
CWI-010000 = material shortage
CWI-001000 = warehouse error
CWI-000100 = BOM variance
CWI-000010 = QC hold
CWI-000001 = approval delay
```

The number of active exception factors is the Hamming weight.

```text
h(x) = sum of active bits
```

Examples:

```text
h(000000) = 0
h(100000) = 1
h(110000) = 2
h(111000) = 3
```

This allows workflow stress to be modeled by the number and combination of active exceptions.

## 6. Modulo-2 and Digital Pattern View

Pascal’s Triangle modulo 2 reveals hidden digital structures.

CWI does not claim that ERP workflows literally follow Pascal’s Triangle.

Instead, CWI borrows the digital perspective.

A workflow scenario can be treated as a binary object.

A set of exceptions can be marked as active or inactive.

The resulting pattern can be visualized, counted, grouped, and analyzed.

This makes the workflow easier to reason about.

## 7. From Algebra to Workflow

The mathematical analogy can be summarized as follows.

| Mathematical structure   | Workflow structure           |
| ------------------------ | ---------------------------- |
| Binomial coefficient     | Number of workflow scenarios |
| Pascal’s Triangle        | Scenario-space organization  |
| Local recursive rule     | Local workflow rule          |
| Modulo-2 digital pattern | Binary exception encoding    |
| Combination of k factors | k active workflow exceptions |
| Global pattern           | End-to-end workflow behavior |

## 8. Interaction Effects

CWI is not only interested in single exceptions.

It is especially interested in interactions.

If two exceptions occur together, the total delay may be larger than the sum of each separate delay.

Example:

```text
material_shortage + qc_hold
```

This may create more workflow stress than either factor alone.

A simple interaction effect can be defined as:

```text
I_ij = L_ij - L_i - L_j + L_0
```

Where:

* L_0 = baseline cycle time
* L_i = cycle time with factor i
* L_j = cycle time with factor j
* L_ij = cycle time with both factors i and j

If I_ij is positive, the combined scenario creates additional delay beyond the two separate effects.

## 9. Why This Matters

ERP workflows often fail not because of one large error, but because of several small conditions occurring together.

Examples:

* partial receipt + wrong warehouse
* material shortage + approval delay
* BOM variance + QC hold
* urgent sales order + inventory mismatch
* production delay + shipment deadline

CWI uses combinatorial thinking to identify these risky combinations.

## 10. Final Summary

The mathematical foundation of CWI is not abstract decoration.

It provides a practical way to:

* define exception factors
* enumerate workflow scenarios
* encode scenarios as bitmasks
* measure combinatorial stress
* identify interaction effects
* connect local workflow rules to global operational patterns

CWI therefore extends the idea of “small rules create large patterns” from Pascal’s Triangle into ERP workflow intelligence.
