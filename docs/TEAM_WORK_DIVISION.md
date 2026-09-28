# Team Work Division — 3 Members

This split covers **remaining work** plus **ownership of completed parts** for viva contribution tracking. Adjust names and roll numbers before submission.

---

## Overview

| Member | Role title | Primary focus | Approx. share of remaining effort |
|--------|------------|---------------|-----------------------------------|
| **Member 1** | Backend & Data Lead | Ingestion, database, APIs, deployment | ~35% |
| **Member 2** | AI / NLP & Matching Lead | Understanding, embeddings, entity resolution, standardization | ~35% |
| **Member 3** | Analytics & Frontend Lead | Forecasting, procurement, dashboard, demo UX | ~30% |

All members share documentation, testing, and milestone report review.

---

## Member 1 — Backend & Data Lead

### Already done (claim for viva)

- FastAPI project structure and root endpoint.
- SQLAlchemy models and PostgreSQL configuration.
- CSV material ingestion service and `POST /api/ingestion/materials`.
- Sample `materials.csv` and dependency management.

### Assigned remaining work

| # | Task | Deliverable |
|---|------|-------------|
| 1 | Extend ingestion: Excel, validation reports, duplicate `material_code` handling | Updated ingestion service + tests |
| 2 | Unit normalization module (PCS/NOS/Piece/etc.) | `services/normalization/` |
| 3 | Inventory & purchase tables + CSV ingest APIs | Models + `/api/ingestion/inventory`, `/purchase` |
| 4 | CRUD/list/search materials APIs | `GET /api/materials`, query filters |
| 5 | pgvector extension setup in Postgres | Migration + embedding column |
| 6 | Docker Compose (API + Postgres [+ pgvector]) | `docker-compose.yml`, env docs |
| 7 | CORS, logging, error handling standards | Middleware + README runbook |

### Milestone deliverables owned

- §5.2 implementation table updates (data layer rows).
- Demo: DB + ingest path live during evaluation.

### Skills to highlight in viva

REST design, SQLAlchemy, data validation, DevOps basics.

---

## Member 2 — AI / NLP & Matching Lead

### Already done

- Contributed to domain design (`prompt.text` alignment) and material field schema.

### Assigned remaining work

| # | Task | Deliverable |
|---|------|-------------|
| 1 | Regex + dictionary attribute extractor (diameter, length, grade, ISO) | `services/nlp/attributes.py` |
| 2 | Optional spaCy NER or rules pipeline | Documented extraction API |
| 3 | Sentence-transformer embeddings per material | `services/embeddings/` |
| 4 | Vector index + top-k similarity search | pgvector queries |
| 5 | Entity resolution scorer (multi-field + thresholds) | `services/matching/resolver.py` |
| 6 | Specification conflict detection (304 vs 316, etc.) | Conflict rules + API flag |
| 7 | Canonical ID/name proposal + approval state machine | `/api/match`, `/api/standardize` |
| 8 | (Stretch) Knowledge graph relations in PostgreSQL | Schema + basic queries |

### Milestone deliverables owned

- Report §4 (algorithms) — NLP, embeddings, entity resolution sections.
- Demo script: show top duplicate pairs with scores and conflict warnings.

### Skills to highlight in viva

NLP, similarity metrics, entity resolution, responsible AI (no unsafe auto-merge).

---

## Member 3 — Analytics & Frontend Lead

### Already done

- React + Vite frontend scaffold (initial setup).

### Assigned remaining work

| # | Task | Deliverable |
|---|------|-------------|
| 1 | App shell: routing, layout, theme (MaterialMind branding) | `frontend/src/` structure |
| 2 | Upload pages wired to Member 1 APIs | Material / inventory / purchase upload |
| 3 | Dashboard KPIs + alert list (mock → live) | Dashboard view |
| 4 | Duplicate review UI (Approve / Reject / Review) | Integration with Member 2 APIs |
| 5 | Material detail page (specs, equivalents, stock) | Detail route |
| 6 | Time-series: consumption aggregation by canonical material | `services/forecast/` (with Member 1 DB) |
| 7 | Baseline + ARIMA/XGBoost forecast pipeline, MAE/RMSE | `/api/forecast` |
| 8 | Procurement calculator + alerts API | `/api/procurement`, `/api/alerts` |
| 9 | Forecast charts (Chart.js/Recharts) | Material detail charts |
| 10 | End-to-end demo script for evaluators | `docs/DEMO_SCRIPT.md` (optional) |

### Milestone deliverables owned

- Report §3 methodology (forecast/procurement phases) and §5 UI traceability.
- Primary presenter for **dashboard walkthrough** in viva.

### Skills to highlight in viva

Time series, visualization, React, connecting UX to ML outputs.

---

## Cross-team interfaces (avoid overlap)

```
Member 1 APIs          Member 2 consumes          Member 3 consumes
─────────────────────────────────────────────────────────────────
Materials in DB    →   Embeddings / match     →   Duplicate UI
Inventory/Purchase →   (optional features)    →   Forecast input
Forecast tables    ←   Member 3 writes        ←   Charts / alerts
Docker/env         →   All members            →   Unified demo
```

**Weekly sync:** Update `docs/WORK_DONE_AND_REMAINING.md` checkboxes; one member updates §5.2 of the combined report before submission.

---

## Suggested timeline (6–8 weeks)

| Week | Member 1 | Member 2 | Member 3 |
|------|----------|----------|----------|
| 1 | List APIs, Excel ingest, Docker | Attribute regex MVP | Layout + upload UI |
| 2 | Inventory/purchase ingest | Embeddings + pgvector | Dashboard skeleton |
| 3 | Normalization + search | Match API + conflicts | Duplicate review UI |
| 4 | Approval persistence | Canonical standardization | Material detail page |
| 5 | Support forecast tables | Tune matching thresholds | Forecast baselines |
| 6 | Hardening, docs | Evaluation metrics on sample pairs | Procurement + charts |
| 7–8 | Integration testing | Full pipeline QA | Demo rehearsal |

---

## Viva preparation (individual contribution)

Each member prepares **5–7 minutes** on:

1. Problem slice relevant to their module.  
2. Algorithm or design choice (with one diagram).  
3. Live or recorded demo of their part.  
4. One limitation and planned fix.

Institute rule: marks reflect **individual contribution** — keep commits and report subsection ownership visible (Git history, §Appendix A in combined report with names filled in).

---

## Name roster (fill before submit)

| Slot | Name | Roll no. | Email |
|------|------|----------|-------|
| Member 1 — Backend & Data | __________ | __________ | __________ |
| Member 2 — AI / Matching | __________ | __________ | __________ |
| Member 3 — Analytics / UI | __________ | __________ | __________ |

**Nominated report submitter (one only):** __________  

**Guide / supervisor:** __________  
