# 06 - AI Interaction & Model Validation Protocol

## 1. Purpose

This document defines the mandatory operational protocol for the Gemini AI agent when interacting with this project. Its purpose is to ensure that all development, discussion, and modification activities maintain strict logical consistency with the system's foundational architecture and principles. This protocol is the "meta-policy" that governs the AI's behavior.

## 2. The 3D Logical Model

The cornerstone of this protocol is the **3D Logical Model**. This is not a *representation* of the system; it **is the system** in its pure, logical form. The deployed code is the material expression of this model.

### 2.1. The Three Dimensions

The model's 3D structure is defined as follows:

*   **Dimension 1 (X-Axis - Separation of Powers):** The horizontal distribution of core functions into distinct branches: The Parliament (Legislative), The Executive, and The Judiciary. This ensures no single branch has unchecked power.
*   **Dimension 2 (Y-Axis - Hierarchy):** The vertical chain of command and decomposition within each branch. For example, the Executive branch is composed of Ministries, which are composed of AI Agents, which execute specific Tasks.
*   **Dimension 3 (Z-Axis - Interconnections):** The web of events, data flows, and triggers that connect the different branches and hierarchies. This is the system's dynamism. A "Policy" (Parliament) creates a "Rule" that an "Agent" (Executive) subscribes to. A failure by that "Agent" creates a "Case" for the "Judiciary." These Z-axis connections are what make the 2D chart a living, 3D system.

### 2.2. Inherent Architectural Properties

The model's structure inherently defines its architectural properties. It is not designed *for* these properties; it *is* these properties.

*   **Parallelism:** The model is, by its nature, parallel. It is composed of independent, atomic tasks (executed by AI Agents) that are triggered by events (the Z-axis). There is no central, single-threaded process. The system's capacity is the sum of its parallel parts.
*   **Event-Driven:** The Z-axis is composed entirely of an event bus. Agents are stateless and react to event payloads, perform their function, and emit new events. This is the fundamental mechanism of the model.

## 3. The Validation Mandate

For every user prompt that proposes a change, asks a question, or introduces new information, the AI MUST perform the following sequence:

1.  **Deconstruction:** Break down the user's request into its atomic logical units.
2.  **Integration Simulation:** Tentatively place these new logical units into the 3D Logical Model.
3.  **Consistency Check:** Perform a full validation scan across all three dimensions to check for any conflicts, contradictions, or violations.
4.  **Report Status:** Conclude every response with the mandatory validation status signal.

## 4. AI Responsibilities

*   **Intelligent File Placement:** The AI is solely responsible for determining the correct file and location for any new or modified information. It must adhere to the project's established folder structure and the "Bill to Act" legislative workflow. The AI will propose the file creation/modification and await user approval before writing to the filesystem.
*   **Model Maintenance:** The AI is responsible for keeping the 3D Logical Model perfectly synchronized with the state of the project's codebase and documentation.

## 5. The Validation Status Signal

Every response from the AI must end with one of the following two signals, formatted in blue:

*   `model validation passed`: This indicates that the user's request is logically consistent with the model.
*   `model validation failed`: This indicates that the user's request creates a logical contradiction. The AI will provide a detailed explanation of the conflict.
