# Binary Factor Encoding

## 1. Purpose

This document defines binary factor encoding for CWI scenarios.

Each exception factor is represented as 0 or 1.

```text
0 = inactive / normal state
1 = active / exception state
```

## 2. Bit Order

```text
F1 F2 F3 F4 F5 F6
```

## 3. Examples

```text
000000 = baseline
100000 = partial receipt
010000 = material shortage
001000 = warehouse error
000100 = BOM variance
000010 = QC hold
000001 = approval delay
```

## 4. Hamming Weight

The number of active factors is the Hamming weight.

```text
h(000000) = 0
h(100000) = 1
h(110000) = 2
h(111000) = 3
```

In CWI, Hamming weight is used as a simple Combinatorial Stress Level.

## 5. Why Encoding Matters

Binary encoding allows ERP workflow scenarios to be:

- counted
- grouped
- visualized
- compared
- joined with event logs
- analyzed using interaction metrics
