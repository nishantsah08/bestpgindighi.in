# Chapter 7: CI/CD Pipeline

**Version:** 1.0
**Date:** 2025-07-23

## 7.1 Pipeline Orchestrator

All CI/CD pipelines will be managed and executed using **GitHub Actions**, providing seamless integration with our source code repository.

## 7.2 Pipeline Stages

Every push to a `feature` or `develop` branch will trigger the CI pipeline. A push to the `main` branch will trigger the full CI/CD pipeline.

### 7.2.1 Diagram: The CI/CD Pipeline Stages

- **Visual Asset:** `![CI/CD Pipeline Stages](./assets/visuals/07_cicd_pipeline.svg)`
- **Source Code (Mermaid):**
  ```mermaid
  gantt
      title CI/CD Pipeline
      dateFormat  X
      axisFormat  %s

      section CI (On Every Push)
      Lint & Static Analysis :crit, 0, 2
      Unit & Integration Tests :crit, after 0, 4
      Build Docker Image :crit, after 2, 3

      section CD (On Merge to Main)
      Push to Artifact Registry :crit, after 5, 2
      Deploy to Staging :crit, after 7, 3
      Run End-to-End Tests :crit, after 10, 4
      Deploy to Production :crit, after 14, 3
  ```

## 7.3 Branching Strategy (GitFlow)

We will use the GitFlow branching model to manage development and releases in a structured way.

### 7.3.1 Diagram: The GitFlow Branching Model

- **Visual Asset:** `![GitFlow Branching Model](./assets/visuals/07_gitflow.svg)`
- **Source (ASCII Art):**
  ```
  main   ------------------------------------o----->
          \
  develop  ----o-----------o---------------o----->
              |           |               |
  feature/A --o--         |               |
  feature/B -------------o--             |
  release/1.0 ---------------------------o----->
  ```
