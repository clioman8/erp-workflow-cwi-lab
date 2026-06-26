# Pascal to Workflow

## 1. Core Idea

The starting point of CWI is the idea that small local rules can generate large global structures.

In Pascal’s Triangle, a simple recursive rule creates a structured triangle of binomial coefficients.

In ERP workflows, small operational rules create larger workflow behavior.

Examples of local workflow rules:

- purchase order must be created before goods receipt
- BOM components must exist before production
- material availability must be checked before work order completion
- QC hold must be released before shipment
- approval must be completed before a high-value transaction continues

## 2. Mathematical Analogy

| Pascal / Binomial Structure | ERP Workflow Structure |
|---|---|
| local addition rule | local business rule |
| binomial coefficient | number of workflow scenarios |
| row of Pascal’s Triangle | scenario distribution by active factors |
| modulo-2 pattern | binary exception encoding |
| Sierpiński-like structure | digital scenario map |
| global pattern | end-to-end workflow behavior |

## 3. CWI Translation

CWI translates:

```text
local mathematical rule → workflow rule
combination of factors → exception scenario
digital mark → active/inactive factor
global pattern → operational behavior
```

## 4. Final Statement

Pascal’s Triangle is not used as a literal ERP model.

It is used as a structural inspiration for designing and enumerating workflow scenario spaces.
