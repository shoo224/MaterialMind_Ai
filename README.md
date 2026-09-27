# MaterialMind AI

**AI-Powered Material Harmonization, Demand Forecasting & Procurement Intelligence Platform**

Inspired by SIH26099 — AI-driven standardization and harmonization of material codes across CPSEs, extended with time-series forecasting and procurement intelligence.

## Quick links

| Document | Purpose |
|----------|---------|
| [docs/WORK_DONE_AND_REMAINING.md](docs/WORK_DONE_AND_REMAINING.md) | Implementation status — completed vs pending modules |
| [docs/MILESTONE_SUBMISSION_README.md](docs/MILESTONE_SUBMISSION_README.md) | Milestone 1 & 2 evaluation criteria and submission checklist |
| [docs/MILESTONE_M1_M2_COMBINED_REPORT.md](docs/MILESTONE_M1_M2_COMBINED_REPORT.md) | Combined academic report for M1 + M2 submission |
| [docs/TEAM_WORK_DIVISION.md](docs/TEAM_WORK_DIVISION.md) | Three-member task split and ownership |

## Repository layout

```
MaterialMind_Ai/
├── backend/          # FastAPI, SQLAlchemy, ingestion service
├── frontend/         # React + Vite (scaffold; UI not started)
├── prompt.text       # Full system design specification
└── instructions.text # Milestone 1 & 2 submission criteria
```

## Current snapshot

- **Backend:** FastAPI app with PostgreSQL material master CSV ingestion (`POST /api/ingestion/materials`).
- **Frontend:** Default Vite + React template — not connected to the API yet.
- **Overall progress:** Early foundation (~10–12% of the full design in `prompt.text`).

See [docs/WORK_DONE_AND_REMAINING.md](docs/WORK_DONE_AND_REMAINING.md) for module-by-module detail.

## Local run (backend)

1. Create `backend/.env` with `DATABASE_URL=postgresql://user:pass@localhost:5432/materialmind`
2. Install dependencies: `pip install -r backend/requirements.txt`
3. Start API: `uvicorn app.main:app --reload` from `backend/` (adjust module path if needed)

## Team

Three-member division of remaining work: [docs/TEAM_WORK_DIVISION.md](docs/TEAM_WORK_DIVISION.md).
