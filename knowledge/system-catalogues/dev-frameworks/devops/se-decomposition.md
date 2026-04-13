# DevOps — SE Decomposition

Extracted from `projects/systems-introduction-book/docs/part3/frameworks.md`
§2.7. IDs use the `DO*` prefix as in the source.

## Goals (DOG)

- **DOG1** — Deliver software changes to production rapidly, reliably, and continuously
- **DOG2** — Eliminate the wall between development and operations
- **DOG3** — Reduce mean time to recovery (MTTR) and increase deployment frequency

## Requirements (DOR)

- **DOR1** — Automated build, test, and deployment pipeline (CI/CD)
- **DOR2** — Infrastructure as Code (IaC) — environments reproducible from version control
- **DOR3** — Monitoring and observability in production — logs, metrics, traces
- **DOR4** — Shared ownership — developers responsible for operational quality
- **DOR5** — Feature flags, canary releases, blue-green deployments for safe rollout
- **DOR6** — Automated security scanning integrated into the pipeline (DevSecOps)

## Functions (DOF)

- **DOF1** — Continuous Integration — merge, build, and unit-test on every commit
- **DOF2** — Continuous Delivery — automated pipeline from commit to production-ready artifact
- **DOF3** — Continuous Deployment — automated release to production (optional, full automation)
- **DOF4** — Monitoring & alerting — detect issues in production, trigger response
- **DOF5** — Incident response — diagnose, fix, deploy hotfix, post-mortem
- **DOF6** — Infrastructure management — provision, scale, patch, secure environments

## Logical Architecture (DOL)

- **DOL1** — Pipeline Subsystem — CI/CD orchestration, build agents, artifact repository
- **DOL2** — Infrastructure Subsystem — IaC, container orchestration, cloud management
- **DOL3** — Observability Subsystem — logging, metrics, tracing, dashboards
- **DOL4** — Security Subsystem — SAST, DAST, dependency scanning, secrets management

## Physical Implementation (DOP)

- **DOP1** — CI/CD tools (Jenkins, GitHub Actions, GitLab CI, Azure Pipelines)
- **DOP2** — Container runtime (Docker, Kubernetes), IaC tools (Terraform, Ansible)
- **DOP3** — Monitoring stack (Prometheus, Grafana, ELK, Datadog)
- **DOP4** — Security scanners (SonarQube, Snyk, Trivy), secrets vault (HashiCorp Vault)
