# Work Done & Work Remaining — MaterialMind AI

This document maps the full design in `prompt.text` to the current codebase and lists what is left to build.

---

## Executive summary

| Area | Status | Approx. completion |
|------|--------|-------------------|
| Project scaffolding (backend + frontend repos) | Done | 100% |
| Module 1 — Data ingestion (full spec) | Partial | ~20% |
| Module 2 — NLP material understanding | Not started | 0% |
| Module 3 — Entity resolution & vector search | Not started | 0% |
| Module 4 — Standardization & human approval | Not started | 0% |
| Module 5 — Time-series intelligence | Not started | 0% |
| Module 6 — Procurement intelligence & alerts | Not started | 0% |
| Knowledge graph | Not started | 0% |
| Dashboard & material detail UI | Not started | ~2% (Vite scaffold only) |
| Deployment (Docker, auth, CI/CD) | Not started | 0% |
| **Full platform (per `prompt.text`)** | **In progress** | **~10–12%** |

---

## Work done (implemented)

### Backend foundation

- **FastAPI application** (`backend/app/main.py`) with health-style root endpoint.
- **PostgreSQL + SQLAlchemy 2.x** setup (`backend/db/database.py`, `backend/core/config.py` via `DATABASE_URL` in `.env`).
- **Material master model** (`backend/models/material.py`): `material_code`, `description`, `category`, `unit`, `manufacturer`, `supplier`, `specification`.
- **Table creation** on startup via `Base.metadata.create_all`.

### Data ingestion (partial Module 1)

- **CSV upload API** — `POST /api/ingestion/materials` (`backend/api/ingestion.py`).
- **Column validation** against required fields (`backend/services/ingestion/ingestion_service.py`).
- **Missing values** filled with empty strings before insert.
- **Sample dataset** — `backend/data/sample/materials.csv` (6 example materials).
- **Dependencies** pinned in `backend/requirements.txt` (FastAPI, pandas, psycopg2, etc.).

### Frontend

- **React + Vite** project initialized (`frontend/`).
- **No MaterialMind screens** — still the default counter demo (`frontend/src/App.jsx`).

### Documentation & planning

- Full system design captured in `prompt.text`.
- Milestone criteria in `instructions.text`.

---

## Work remaining (by module)

### Module 1 — Data ingestion (remaining ~80%)

| Task | Priority |
|------|----------|
| Data cleaning rules (trim, dedupe codes, invalid row handling) | High |
| Unit normalization (PCS / NOS / Piece → canonical unit) | High |
| Excel (`.xlsx`) upload support | Medium |
| Inventory CSV/API ingestion (`opening_stock`, `consumed`, dates, etc.) | High |
| Purchase history ingestion (`quantity`, `price`, `lead_time`, etc.) | High |
| Optional fields: warehouse, department, PO number | Medium |
| Ingestion job status, error reports, batch id | Medium |

### Module 2 — NLP material understanding

| Task | Priority |
|------|----------|
| Regex + domain dictionaries for bolts, grades, ISO standards | High |
| NER / attribute extraction (material, type, diameter, length, standard) | High |
| Sentence embeddings for descriptions | High |
| Optional LLM-assisted extraction (not sole dependency) | Medium |
| Persist extracted attributes on material records | High |

### Module 3 — Entity resolution & safety

| Task | Priority |
|------|----------|
| Multi-signal similarity (description, spec, unit, category, manufacturer) | High |
| Classification: SAME / SIMILAR / EQUIVALENT / DIFFERENT | High |
| **Specification conflict detection** (e.g. Grade 304 vs 316) | High |
| pgvector (or FAISS) embeddings + nearest-neighbor search | High |
| `/match`, `/search` APIs | High |

### Module 4 — Standardization

| Task | Priority |
|------|----------|
| Canonical material ID and standard name generation | High |
| Map legacy codes → canonical record | High |
| Human-in-the-loop: Approve / Reject / Review | High |
| Audit log of user decisions | Medium |

### Knowledge graph (advanced)

| Task | Priority |
|------|----------|
| Relationships: category, spec, supplier, warehouse, equivalence | Medium |
| Neo4j or relational graph in PostgreSQL | Medium |
| Graph-backed queries for procurement | Low (later) |

### Module 5 — Time-series intelligence

| Task | Priority |
|------|----------|
| Demand, inventory, and price history models + APIs | High |
| Baselines: moving average, exponential smoothing | High |
| ARIMA/SARIMA; ML (XGBoost/LightGBM) with lag features | High |
| Demand pattern detection (stable / seasonal / intermittent) | Medium |
| Model selection via MAE, RMSE, MAPE/sMAPE | High |
| Optional LSTM/TFT/PatchTST comparison | Low |
| Forecast horizons: 1/2/3 months; stockout date projection | High |

### Module 6 — Procurement intelligence

| Task | Priority |
|------|----------|
| Reorder quantity: demand + lead time + safety stock − inventory | High |
| Smart alerts: stockout, duplicate risk, demand spike, price trend | High |
| `/procurement`, `/recommendations`, `/alerts` APIs | High |
| No autonomous ordering — recommend only | Required (design) |

### Frontend & UX

| Task | Priority |
|------|----------|
| Upload flows for material / inventory / purchase files | High |
| Dashboard KPIs (materials, duplicates, stock risk, forecast accuracy) | High |
| Duplicate review & approval UI | High |
| Material detail page (specs, equivalents, forecast, procurement) | High |
| Charts for historical vs forecast demand | High |
| Connect frontend to FastAPI (CORS, env base URL) | High |

### Platform & deployment

| Task | Priority |
|------|----------|
| `requirements.txt` / lockfiles documented; README run steps | Medium |
| Docker Compose (API + Postgres + pgvector) | High |
| OpenAPI docs polish, logging, authentication | Medium |
| CI/CD pipeline | Low |

---

## Suggested build order (critical path)

1. Finish ingestion (inventory + purchases) and list/search materials APIs.  
2. NLP attributes + embeddings + duplicate detection API.  
3. Approval workflow + canonical materials.  
4. Forecasting engine on historical consumption.  
5. Procurement recommendations + dashboard UI.  
6. Docker demo: upload sample → duplicates → forecast → reorder suggestion.

---

## Demo readiness vs evaluation

`instructions.text` requires **at least a partial demonstration** during evaluation.

**Demonstrable today:** CSV material upload into PostgreSQL via API.

**Minimum demo for next milestone:** Upload sample CSV → show stored materials in API/Swagger → (stretch) first duplicate pairs on similar descriptions.

**Target final demo (from `prompt.text`):** Large upload → duplicate groups → standardization → demand forecast → stockout risks → reorder quantities on an interactive dashboard.
