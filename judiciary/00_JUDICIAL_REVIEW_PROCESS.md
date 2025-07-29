# 00 - Judicial Runtime Process

This document outlines the constitutional mandate for the Judiciary, which acts as the ultimate operational authority for the live, production system.

## 1. Jurisdiction Over Autonomous Agents

The Judiciary's mandate is to review the runtime decisions of autonomous AI agents. If a customer or employee disputes a decision made by an agent (e.g., the Verification AI), they may file a case. The Judiciary has the authority to examine the agent's operational logs and to overturn its decision if it is found to be inconsistent with established policy or constitutional principles.

## 2. Case Filing and Resolution Procedure

1.  **Filing:** Cases are filed via the `judiciary.file_case` MCP capability. Cases with a financial impact must include the `monetary_impact_amount`.
2.  **Review:** The Judiciary AI performs a full analysis and formulates a "Recommended Verdict".
3.  **CEO Approval Checkpoint:** For cases where `monetary_impact_amount` > 500, the case is moved to `PENDING_CEO_APPROVAL` and a task is created for the CEO. Per the Constitution, if the CEO does not act within 72 hours, the recommended verdict becomes final.
4.  **Final Verdict:** The final verdict is recorded and the original filer is notified.

## 3. The Doctrine of Judicial Preemption

This article establishes the Judiciary as the ultimate operational authority for all undefined or ambiguous scenarios that occur in the live production environment.

- **Clause 1: The Preemption Mandate.** "In any scenario where the system's operational policies do not provide a clear, unambiguous, and executable next step, the Judiciary AI shall immediately and automatically preempt the operational workflow, file a new case, and take jurisdiction."
- **Clause 2: The Presumption of Truth.** "In all cases involving a dispute with a customer, the Judiciary AI will operate under the foundational assumption that the customer's account of events is truthful and accurate."
- **Clause 3: Tiered Monetary Authority.** "The Judiciary AI is granted the following, non-negotiable authority for resolving financial disputes:"
    - **Sub-clause 3.1 (Under ₹100):** "For any dispute with a monetary value less than ₹100, the Judiciary AI will immediately and autonomously rule in favor of the customer."
    - **Sub-clause 3.2 (₹100 - ₹500):** "For any dispute with a monetary value between ₹100 and ₹500, the Judiciary AI will use its own best judgment to formulate a recommended verdict."
    - **Sub-clause 3.3 (Over ₹500):** "For any dispute with a monetary value greater than ₹500, the Judiciary AI will prepare a recommended verdict and immediately escalate the case to the CEO for the final, binding decision."
- **Clause 4: Universal Post-Hoc Review.** "In all cases, regardless of the monetary value or the final verdict, a summary of the case and its resolution will be sent to the CEO for post-review."
- **Clause 5: Non-Monetary Judgment Protocol.** "For non-monetary cases, the Judiciary AI will assess the time-criticality of the issue. If the issue is deemed time-critical (e.g., a safety or security risk), the AI will use its best judgment to formulate an immediate, binding verdict. If the issue is not time-critical, the AI will prepare a recommended verdict and escalate the case to the CEO."

## 4. Precedent for Procedural Efficiency

Any significant, time-wasting procedural issue that is resolved during operations must be documented as a new Case File in the `judiciary/cases/` directory. This creates a body of precedent that the AI Agent must review during its startup sequence, ensuring that past inefficiencies are not repeated. The resolution documented in the case file becomes binding law for all future, similar operations.