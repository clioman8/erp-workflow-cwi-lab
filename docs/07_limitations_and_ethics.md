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
