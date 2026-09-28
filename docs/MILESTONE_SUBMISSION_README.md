# Milestone 1 & 2 — Submission Guide

Based on `instructions.text` at the repository root.

---

## Evaluation overview

| Milestone | Criterion | Marks |
|-----------|-----------|-------|
| **Milestone 1 (M1)** | Problem Domain Identification and Analysis | **3** |
| **Milestone 2 (M2)** | Review of Existing Systems and Project Feasibility | **3** |
| **M2** | Objectives and Methodology of the Proposed Work | **3** |
| **M2** | Relevance of Algorithms / Techniques | **3** |
| **M2** | Synchronization of Project Design & Implementation | **3** |
| | **Total** | **15** |

> Note: M2 evaluation is **12 marks** on the four M2 criteria; M1 adds **3 marks** for problem domain. The combined report must cover **both M1 and M2**.

---

## What to submit

1. **One combined report** (PDF recommended) covering all criteria below.  
   - Source draft: [MILESTONE_M1_M2_COMBINED_REPORT.md](MILESTONE_M1_M2_COMBINED_REPORT.md) — export or copy into your institute template.
2. **Only one team member** submits on behalf of the entire team (no duplicate submissions).
3. **Partial implementation demo** during viva/evaluation (see checklist).
4. **Individual marks** depend on each member’s contribution — align with [TEAM_WORK_DIVISION.md](TEAM_WORK_DIVISION.md).

---

## Report section map ( graders’ checklist )

Use these headings in the submitted PDF so evaluators can map sections to marks.

### Milestone 1 — Problem Domain Identification and Analysis (3 marks)

Include:

- Problem statement: duplicate/inconsistent material masters in large enterprises (CPSE/ERP context).
- Impact: excess inventory, fragmented procurement, poor demand analysis.
- Secondary problem: forecasting need after harmonization.
- Stakeholders: procurement, stores, finance, IT/ERP teams.
- Scope and boundaries (recommendation-only procurement, human approval).

**Report section:** §1 in [MILESTONE_M1_M2_COMBINED_REPORT.md](MILESTONE_M1_M2_COMBINED_REPORT.md)

### Milestone 2 — Review of Existing Systems and Project Feasibility (3 marks)

Include:

- How ERPs and MDM tools handle material masters (strengths/limitations).
- Related work: deduplication, entity resolution, demand forecasting in supply chain.
- Feasibility: open stack (FastAPI, PostgreSQL, pgvector, React), sample CSV demo without live SAP.
- Risks: data quality, false duplicate merges, model accuracy — and mitigations (spec conflict checks, human-in-the-loop).

**Report section:** §2

### Milestone 2 — Objectives and Methodology (3 marks)

Include:

- Primary and secondary objectives (harmonize → forecast → procure).
- Methodology: modular pipeline (ingest → NLP → resolve → standardize → forecast → recommend).
- Data collection approach (CSV/Excel/API).
- Evaluation methodology for ML (train/validation split, MAE/RMSE/MAPE).

**Report section:** §3

### Milestone 2 — Relevance of Algorithms / Techniques (3 marks)

Include:

- NLP/NER, regex, embeddings for material understanding.
- Entity resolution and vector search (pgvector).
- Time-series: moving average, ETS, ARIMA, gradient boosting; optional deep models.
- Procurement rule engine + safety stock / lead time logic.
- Why not “LLM-only” or “autonomous purchasing.”

**Report section:** §4

### Milestone 2 — Synchronization of Design & Implementation (3 marks)

Include:

- Architecture diagram aligned with `prompt.text`.
- **Current implementation status** (honest): what exists in repo vs planned.
- Traceability table: design module → API/service → UI screen.
- Next sprint plan tied to demo requirements.

**Report section:** §5–§6

---

## Viva / demo checklist

Prepare to show:

| Item | Status in repo | Talking points |
|------|------------------|----------------|
| Problem & objectives | Report + `prompt.text` | 2-minute pitch |
| Architecture | Report §5 | Frontend / API / DB / ML layers |
| Live API | **Yes** — FastAPI running | Swagger `/docs`, root health |
| Material CSV ingest | **Yes** | `POST /api/ingestion/materials`, sample CSV |
| Duplicate / NLP / forecast UI | **Not yet** | Show roadmap + mock screenshots if available |
| Team contributions | [TEAM_WORK_DIVISION.md](TEAM_WORK_DIVISION.md) | Each member explains their module |

**Minimum acceptable partial demo:** ingest sample `backend/data/sample/materials.csv`, query DB or API response with inserted count; walk through planned duplicate and forecast flow on slides or wireframes.

---

## Files in this repository for submission

| File | Role |
|------|------|
| [MILESTONE_M1_M2_COMBINED_REPORT.md](MILESTONE_M1_M2_COMBINED_REPORT.md) | Main report body |
| [WORK_DONE_AND_REMAINING.md](WORK_DONE_AND_REMAINING.md) | Evidence for design vs implementation sync |
| [TEAM_WORK_DIVISION.md](TEAM_WORK_DIVISION.md) | Individual contribution narrative |
| `prompt.text` | Full design reference |
| `backend/`, `frontend/` | Code evidence |

---

## Before you submit

- [ ] Convert report to PDF with team name, roll numbers, guide name (per institute format).
- [ ] One nominated submitter uploads once.
- [ ] All three members can explain their assigned modules in viva.
- [ ] Backend demo rehearsed (DB running, `.env` set, sample CSV ready).
- [ ] Report explicitly states **partial implementation** and **next milestones** (integrity with §5 of combined report).
