# MaterialMind AI — Combined Milestone 1 & Milestone 2 Report

**Project title:** MaterialMind AI — AI-Powered Material Harmonization, Demand Forecasting & Procurement Intelligence Platform  

**Context:** Extension of SIH26099 — AI-driven standardization and harmonization of material codes across CPSEs  

**Team size:** 3 members  

**Report type:** Combined submission covering Milestone 1 (M1) and Milestone 2 (M2) evaluation criteria  

---

## Abstract

Large enterprises maintain material master data across ERP and procurement systems. Inconsistent descriptions, units, and duplicate codes inflate inventory, obscure true demand, and weaken supplier comparison. MaterialMind AI proposes an integrated pipeline: ingest and clean master and transactional data, understand materials via NLP, resolve duplicates with embeddings and specification-aware rules, standardize records with human approval, forecast demand and inventory using time-series models, and recommend procurement quantities with actionable alerts. This report identifies the problem domain (M1), reviews existing approaches and feasibility (M2), states objectives and methodology, justifies algorithm choices, and synchronizes the detailed design with current implementation status in the project repository.

---

## 1. Problem Domain Identification and Analysis (Milestone 1)

### 1.1 Problem statement

Organizations store materials under multiple codes for what is effectively the same item—for example, “SS Bolt M10 x 50,” “Stainless Steel Bolt 10mm 50mm,” and “SS M10/50 Bolt” may coexist as separate ERP records. Traditional systems keyed on material code treat these as distinct SKUs. The result is duplicate purchasing, excess stock, difficulty locating existing items, inconsistent units (PCS vs NOS vs Piece), fragmented history, and unreliable demand analytics.

A related problem appears after harmonization: even with a correct canonical material, planners need estimates of future consumption, stockout risk, and reorder timing. Siloed duplicate-detection or forecasting tools do not answer the combined question: *What material do we actually have, how much will we need, and what should we procure?*

### 1.2 Domain and stakeholders

| Stakeholder | Need |
|-------------|------|
| Procurement | Avoid duplicate orders; compare suppliers on standardized items |
| Stores / inventory | Accurate stock by canonical material; stockout warnings |
| Finance | Reduced carrying cost; better budget from demand forecasts |
| IT / ERP | Harmonized master data without unsafe automatic deletions |
| CPSE / large PSU context | Align material codes across units (SIH26099 theme) |

### 1.3 Problem characteristics

- **Unstructured text:** Descriptions are noisy, abbreviated, and non-standard.
- **Structured constraints:** Specifications (grade, standard) may differ despite high text similarity (304 vs 316 stainless).
- **Temporal data:** Consumption and purchase history drive forecasting.
- **Safety and governance:** Recommendations must not auto-place orders; human approval is mandatory.

### 1.4 Scope

**In scope:** CSV/Excel/API ingestion, NLP attribute extraction, similarity and entity resolution, canonical mapping with approval, demand/inventory/price forecasting where data exists, procurement recommendations, dashboard and alerts.

**Out of scope (initially):** Autonomous PO creation, full SAP live integration (demo uses file/API upload), enterprise SSO (planned later).

### 1.5 Success criteria

- Detect high-confidence duplicate and equivalent candidates with explainable scores.
- Flag specification conflicts when text similarity is high.
- Produce forecasts with measurable error metrics (MAE, RMSE, MAPE).
- Deliver reorder suggestions combining forecast, lead time, and safety stock.
- Demonstrate end-to-end flow on sample and scaled synthetic datasets.

---

## 2. Review of Existing Systems and Project Feasibility (Milestone 2)

### 2.1 Existing systems and practices

**ERP material masters (SAP MM, Oracle, etc.)**  
Centralized codes and descriptions but limited fuzzy matching across legacy imports. Duplicate creation often occurs at plant or company-code level. Harmonization is typically manual or batch MDM projects.

**Master Data Management (MDM) tools**  
Provide workflow, golden records, and matching rules. Strength: governance. Weakness: rule maintenance cost; semantic similarity across technical descriptions may be weak without ML.

**Dedicated deduplication / record linkage**  
Academic and commercial entity-resolution techniques (Fellegi-Sunter, learned matchers) apply to products and materials. Often batch-oriented, not tied to inventory and forecasting.

**Demand forecasting modules**  
ERP and specialized tools (statistical forecasting, supply-chain suites) forecast at SKU level. They assume a clean SKU master; they do not fix duplicate or ambiguous materials first.

**Gap MaterialMind addresses:** Closed loop from messy master → canonical material → historical demand → procurement recommendation, with specification-aware safety and human-in-the-loop merges.

### 2.2 Related literature and techniques (summary)

- **Material and product entity resolution:** String similarity, token-based metrics, embedding similarity, blocking for scale.
- **Industrial NLP:** Regex and gazetteers for dimensions, grades, standards (ISO, ASTM); optional NER models.
- **Vector retrieval:** Approximate nearest neighbors (pgvector, FAISS) for candidate generation before pairwise scoring.
- **Time-series forecasting:** Classical (MA, ETS, ARIMA/SARIMA), ML with lag features (XGBoost), deep sequence models for comparison.
- **Inventory policy:** Reorder point and order quantity using lead time and safety stock.

### 2.3 Feasibility analysis

| Factor | Assessment |
|--------|------------|
| **Technical** | Mature open-source stack: FastAPI, PostgreSQL, pgvector, React, scikit-learn, statsmodels, sentence-transformers |
| **Data** | Demo feasible with CSV samples; no mandatory live CPSE database |
| **Team skill** | Aligns with AI/DS curriculum: NLP, ML, time series, full-stack API |
| **Timeline** | Modular delivery: ingestion → matching → forecast → UI enables partial demos at M2 |
| **Compute** | Training feasible on CPU for baselines; GPU optional for deep models |

### 2.4 Risks and mitigations

| Risk | Mitigation |
|------|------------|
| False merge of distinct grades | Specification conflict rules; SIMILAR vs SAME; human approval |
| Poor forecast with sparse history | Pattern classification; fallback to moving average; confidence flags |
| Scale (50k materials) | Embedding index + blocking; batch jobs |
| Over-reliance on LLM | Deterministic extraction first; LLM for assistive parsing only |

**Conclusion:** The project is feasible as a modular portfolio-grade system with incremental demos.

---

## 3. Objectives and Methodology of the Proposed Work (Milestone 2)

### 3.1 Objectives

**Primary**

1. Ingest and validate material, inventory, and purchase data from files/API.  
2. Extract structured attributes from descriptions and detect duplicate/near-duplicate materials.  
3. Create canonical material records with user approval and legacy code mapping.  
4. Forecast demand (and where applicable inventory trajectory and price trends).  
5. Recommend procurement quantities and surface operational alerts.

**Secondary**

- Build a knowledge graph of categories, specs, suppliers, and equivalences.  
- Compare forecasting models per material demand pattern.  
- Provide natural-language explanations for recommendations (optional LLM).

### 3.2 Methodology

**Phase A — Data foundation**  
Validate schemas; clean text; normalize units; persist to PostgreSQL.

**Phase B — Understanding and resolution**  
Parse attributes; embed descriptions; retrieve neighbors; compute multi-field confidence; classify SAME/SIMILAR/EQUIVALENT/DIFFERENT; detect spec conflicts.

**Phase C — Standardization**  
Propose canonical IDs and names; present approval UI; log decisions.

**Phase D — Time series**  
Align consumption by canonical material; detect demand pattern; train/select models; output multi-horizon forecasts and stockout dates.

**Phase E — Procurement intelligence**  
Combine forecast, on-hand stock, lead time, safety stock; generate alerts (stockout, duplicate risk, spikes, price).

**Phase F — Integration & evaluation**  
Dashboard; API documentation; metrics on holdout periods; user demo script.

### 3.3 Data methodology

- **Sources:** Uploaded CSV/Excel; REST ingestion for demo.  
- **Sample set:** `backend/data/sample/materials.csv` for master data; extended synthetic inventory/purchase files (planned).  
- **Split for forecasting:** Chronological train/validation/test to avoid leakage.  
- **Metrics:** MAE, RMSE, MAPE/sMAPE for forecasts; precision/recall @ k for duplicate suggestions (manual labeling on sample).

### 3.4 Development methodology

Agile sprints per module; API-first backend; Swagger for evaluators; three-member parallel tracks (see Team Work Division document).

---

## 4. Relevance of Algorithms and Techniques (Milestone 2)

| Component | Technique | Relevance |
|-----------|-----------|-----------|
| Cleaning & units | Rule-based normalization, pandas pipelines | Reliable baseline before ML |
| Attribute extraction | Regex, domain dictionaries, spaCy NER | Interpretable fields for matching |
| Semantic similarity | Sentence Transformers → embeddings | Captures paraphrase across descriptions |
| Candidate retrieval | pgvector ANN | Scales to large catalogs |
| Entity resolution | Weighted score fusion + thresholds | Industry-standard duplicate/conflict workflow |
| Spec safety | Attribute inequality rules (grade, standard) | Prevents dangerous “same” merges |
| Forecasting baselines | Moving average, exponential smoothing | Stable demand, few data points |
| Forecasting classical | ARIMA/SARIMA | Seasonal industrial consumption |
| Forecasting ML | XGBoost/LightGBM with lags, rolling stats | Nonlinear patterns |
| Model selection | Backtest MAE/RMSE/MAPE | Per-material best model |
| Pattern routing | Cluster/intermittent demand tests | Avoid one-model-fits-all |
| Procurement | (Forecast + lead time demand + safety stock) − on hand | Standard inventory policy, explainable |
| Optional advanced | LSTM/TFT, Neo4j graph | Stretch goals for comparison |
| LLM | Optional extraction/explanation | Not sole decision engine |

Techniques are chosen for **interpretability**, **enterprise safety**, and **demonstrable evaluation**, not black-box automation of purchasing.

---

## 5. Synchronization of Project Design and Implementation (Milestone 2)

### 5.1 Intended architecture (design)

```
User → Upload (CSV/Excel/API) → Validation → Clean/Normalize → DB
     → NLP / Attributes → Embeddings → Similarity → Entity Resolution
     → Human Approval → Canonical Material
     → Time-Series Engine → Procurement Engine → Dashboard / Alerts
```

Layers: React frontend, FastAPI backend, PostgreSQL (+ pgvector), ML services for NLP and forecasting.

Full detail: repository file `prompt.text`.

### 5.2 Current implementation status (repository snapshot)

| Design module | Planned capability | Implementation status |
|---------------|-------------------|-------------------------|
| FastAPI backend | REST API | **Done** — app shell, OpenAPI |
| PostgreSQL | Persistent store | **Done** — SQLAlchemy, Material table |
| Material CSV ingest | Upload master | **Partial** — CSV only, required columns, basic fillna |
| Unit normalization | Canonical units | **Not started** |
| Inventory / purchase ingest | Transactional data | **Not started** |
| NLP / NER | Attribute extraction | **Not started** |
| Embeddings / pgvector | Similarity search | **Not started** |
| Entity resolution | SAME/SIMILAR/… | **Not started** |
| Standardization + approval | Canonical + HITL | **Not started** |
| Forecasting | Demand/stock/price | **Not started** |
| Procurement + alerts | Recommendations | **Not started** |
| Knowledge graph | Relationships | **Not started** |
| React dashboard | Full UX | **Not started** (Vite template only) |
| Docker / CI | Deployment | **Not started** |

**Estimated overall completion:** ~10–12% of full design.

### 5.3 Traceability matrix (design → code → UI)

| Feature | API (planned) | Backend today | Frontend (planned) |
|---------|---------------|---------------|-------------------|
| Upload materials | `POST /api/ingestion/materials` | Implemented | Upload page — pending |
| List/search materials | `GET /materials`, `/search` | Pending | Material list — pending |
| Match duplicates | `POST /match` | Pending | Duplicate review — pending |
| Standardize | `POST /standardize` | Pending | Approve/Reject — pending |
| Forecast | `GET /forecast/{id}` | Pending | Charts — pending |
| Procurement | `GET /procurement/{id}` | Pending | Detail page — pending |
| Alerts | `GET /alerts` | Pending | Dashboard widgets — pending |

### 5.4 Alignment statement

The **design** in `prompt.text` defines the target system for final evaluation and SIH-style demo. The **implementation** intentionally began with the ingestion layer and database model to support a **partial demo** (CSV upload and persistence) required by milestone instructions. Subsequent sprints will align APIs and UI rows in §5.3 with the architecture diagram. No design module has been discarded; priority order follows the critical path in `docs/WORK_DONE_AND_REMAINING.md`.

### 5.5 Evidence for evaluators

- **Code:** `backend/app/main.py`, `backend/api/ingestion.py`, `backend/models/material.py`  
- **Sample data:** `backend/data/sample/materials.csv`  
- **Status doc:** `docs/WORK_DONE_AND_REMAINING.md`

---

## 6. Conclusion and Next Steps

MaterialMind AI targets a well-defined enterprise pain point: inconsistent material masters and disconnected forecasting. Milestone 1 analysis establishes domain, stakeholders, and scoped objectives. Milestone 2 sections show that existing ERP/MDM approaches leave an integration gap, that the proposed methodology is feasible with open tools, that selected algorithms match each sub-problem, and that current code implements the first slice of the design (material ingestion) while the remainder follows a documented module plan.

**Immediate next steps (post M2 submission)**

1. Material list API and frontend upload screen.  
2. Attribute extraction and embedding pipeline with pgvector.  
3. Duplicate candidate API with spec-conflict warnings.  
4. Synthetic inventory history and baseline forecast endpoint.  
5. Docker Compose for one-command demo.

---

## 7. References (indicative)

1. Fellegi, I. P., & Sunter, A. B. (1969). A theory for record linkage. *Journal of the American Statistical Association*.  
2. Hyndman, R. J., & Athanasopoulos, G. *Forecasting: Principles and Practice* (online text).  
3. Reimers, N., & Gurevych, I. Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks.  
4. SIH Problem Statement SIH26099 — AI-driven standardization and harmonization of material codes across CPSEs.  
5. Project internal specification: `prompt.text`, MaterialMind AI Complete System Design.

---

## Appendix A — Team contributions (summary)

Detailed task ownership: see `docs/TEAM_WORK_DIVISION.md`. Each member should be prepared to explain their module in viva per institute guidelines.

## Appendix B — Submission checklist

- [ ] PDF generated from this report with institute cover page  
- [ ] Single team member submits once  
- [ ] Partial demo: FastAPI + CSV ingest rehearsed  
- [ ] All members review §1–§5 for viva questions  

---

*Document version: 1.0 — aligned with repository state at Milestone 2 preparation.*
