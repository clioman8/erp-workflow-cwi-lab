# docs/01_cwi_definition.md

# Combinatorial Workflow Intelligence Definition

## 1. Overview

Combinatorial Workflow Intelligence, abbreviated as CWI, is a project-defined analytical framework for studying ERP workflows as combinations of activities, roles, handoffs, constraints, exceptions, and operational outcomes.

This project applies CWI to ERP-style workflows using ECOUNT ERP demo workflows, synthetic event logs, and SAP S/4HANA Cloud Public Edition as a conceptual comparison layer.

The main goal is to understand how small operational rules and local exceptions generate large workflow patterns across purchasing, inventory, production, sales, quality, approval, and reporting processes.

## 2. Why CWI Is Needed

ERP systems record business activities such as purchase orders, goods receipts, work orders, production receipts, sales orders, shipments, inventory updates, and approvals.

However, real work rarely follows a clean linear path.

Examples of real workflow issues include:

* partial receipt
* material shortage
* wrong warehouse posting
* BOM variance
* QC hold
* approval delay
* backorder
* inventory mismatch
* role handoff delay
* missing master data
* process rework

A normal ERP screen may show transaction records, but it does not always explain how these events combine to create bottlenecks, delays, or operational risk.

CWI attempts to fill this gap.

## 3. Core Definition

CWI is defined as:

> A framework for analyzing how combinations of workflow events, roles, constraints, approvals, exceptions, and operational rules generate observable process patterns in ERP systems.

In simpler terms:

> CWI studies how ERP work gets done, where it gets blocked, and which combinations of conditions make the workflow unstable.

## 4. CWI Is Not

CWI is not a replacement for ERP.

CWI is not an official SAP or ECOUNT module.

CWI is not a legal or accounting system.

CWI is not a claim that every workflow can be fully explained by mathematics.

CWI is an analytical layer placed on top of ERP-style data.

## 5. CWI Is

CWI is:

* an event-log analysis framework
* a workflow visibility framework
* a role and handoff analysis framework
* a combinatorial scenario design method
* an operational intelligence prototype
* a bridge between ERP data and workflow reasoning

## 6. Basic CWI Objects

CWI uses the following core objects.

### Event

An event is a recorded workflow action.

Examples:

* Purchase Order Created
* Goods Received
* Work Order Created
* BOM Components Calculated
* Material Shortage Detected
* Production Receipt Created
* Sales Order Received
* Approval Completed

### Case

A case is one complete workflow instance.

Examples:

* one purchase order
* one production order
* one sales order
* one return case
* one QC hold case

### Activity

An activity is the type of work performed.

Examples:

* receive goods
* issue material
* check availability
* approve sales order
* release QC hold

### Role

A role is the actor or system position responsible for an activity.

Examples:

* buyer
* warehouse_operator
* production_planner
* production_operator
* quality_checker
* sales_operator
* manager
* accountant
* system

### Exception

An exception is a condition that interrupts, delays, or changes the normal workflow.

Examples:

* partial_receipt
* material_shortage
* warehouse_error
* bom_variance
* qc_hold
* approval_delay

### Factor

A factor is a binary or categorical variable used in scenario design.

Example:

* F1 = partial_receipt
* F2 = material_shortage
* F3 = warehouse_error
* F4 = bom_variance
* F5 = qc_hold
* F6 = approval_delay

## 7. CWI Research Question

The central research question is:

> How do local ERP rules, role constraints, and exception combinations generate global workflow behavior?

This can be expanded into smaller questions.

* Which activities appear most often?
* Which roles create the most handoffs?
* Which exception types increase cycle time?
* Which factor combinations produce the highest workflow stress?
* Which activities become bottlenecks?
* Which approval rules create delays?
* Which master-data errors propagate through the workflow?
* Which process variants are normal and which are risky?

## 8. Project Scope

This repository focuses on three ERP workflow families.

### Procure-to-Pay

Purchase order, goods receipt, inventory update, invoice, and payment-related workflow.

### Order-to-Cash

Sales order, availability check, shipment, sales posting, and customer-facing workflow.

### Manufacturing

BOM, work order, material issue, production receipt, QC hold, variance, and finished-goods inventory workflow.

## 9. ECOUNT and SAP Roles

ECOUNT is used as the practical demo environment.

SAP S/4HANA Cloud Public Edition is used as the conceptual comparison layer.

Synthetic event logs are used when direct ERP event extraction is unavailable or impractical.

## 10. Final Summary

CWI treats ERP workflows as structured combinations.

The project does not only ask:

> What happened?

It asks:

> Which combination of roles, events, rules, and exceptions caused the workflow to behave this way?
