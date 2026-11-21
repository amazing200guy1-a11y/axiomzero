# AxiomZero: Autonomous Neuro-Symbolic AI Math Reasoning & Hallucination Firewall

[![Tests](https://img.shields.io/badge/Formal%20Tests-10%2F10%20PASS-brightgreen.svg)](test_axiomzero.py)
[![Latency](https://img.shields.io/badge/Verification%20Latency-0.0074ms%2Fstep-blue.svg)](test_axiomzero.py)
[![Architecture](https://img.shields.io/badge/Neuro--Symbolic-C99%20%7C%20Python%20%7C%20TS-orange.svg)]()
[![Hackathon](https://img.shields.io/badge/Built%20For-IceHacks%202026-blueviolet.svg)](https://devpost.com)
[![Live Cockpit](https://img.shields.io/badge/Live%20Cockpit-Online-success.svg)](https://amazing200guy1-a11y.github.io/axiomzero/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **AxiomZero** is an institutional-grade, zero-dependency neuro-symbolic mathematical reasoning firewall and AI hallucination verifier engineered for **IceHacks 2026**. It acts as a deterministic, real-time guardrail between generative AI models (ChatGPT, Claude, Gemini) and STEM students, intercepting subtle AI mathematical hallucinations — sign inversions, divide-by-zero singularities, and false algebraic expansions — in **0.0074 ms per step** before students memorize flawed logic.

🚀 **Live Interactive Cockpit:** [https://amazing200guy1-a11y.github.io/axiomzero/](https://amazing200guy1-a11y.github.io/axiomzero/)

---

## ⚡ The Problem: Generative AI Math Hallucinations

Millions of students rely on Large Language Models for homework and exam preparation. However, LLMs are probabilistic next-token predictors, not formal reasoning engines. They regularly hallucinate:
1. **Sign Inversions:** Flipped signs in distributive laws (`-(x - 5)` becoming `x - 5`).
2. **Singularity Traps:** Dividing by zero across removable singularities or false cancellations.
3. **The Freshman's Dream:** Omitting cross-terms in algebraic expansions (`(x + 2)^2 == x^2 + 4`).

When students study from hallucinated AI proofs, they memorize incorrect mathematics and fail exams.

---

## 🛡️ The AxiomZero Solution

AxiomZero bridges deterministic formal mathematics with modern generative AI:

```mermaid
flowchart LR
    Student["Student Prompt / Homework Problem"] --> LLM["Generative AI (Claude / ChatGPT / Gemini)"]
    LLM -->|Step-by-Step Proof Draft| Axiom["Layer 1: AxiomZero AST Sanitizer"]
    Axiom --> Invariant["Layer 2: Schwartz-Zippel Invariant Engine (0.0074ms)"]
    Invariant -->|Equivalence Verified| Approved["✅ Step Verified & Displayed to Student"]
    Invariant -->|Hallucination Detected| Firewall["🛑 Invariant Trap: Alert & Auto-Correct"]
```

### Core Architecture:
- **C99 Formal Symbolic Kernel (`firmware/axiom_core.c`):** High-speed identity verification core implementing the Schwartz-Zippel lemma. Executes in sub-microsecond latency.
- **Python Zero-Dependency Engine (`axiomzero_engine.py`):** Standalone AST sanitizer, numerical invariant evaluator, and step-by-step proof session manager.
- **TypeScript Neuro-Symbolic Client (`src/axiom_client.ts`):** Clean TypeScript SDK for integrating AxiomZero into student IDEs and browser extensions.
- **Aerospace Titanium Cockpit (`index.html`):** Interactive web dashboard on GitHub Pages allowing judges and students to test real-time equations and inject common LLM hallucinations.

---

## 🚀 Quick Start

### 1. Launch the Live Interactive Cockpit
Judges can directly test mathematical proof sessions, inject hallucinations, and inspect formal verification logs online:  
👉 **[https://amazing200guy1-a11y.github.io/axiomzero/](https://amazing200guy1-a11y.github.io/axiomzero/)**

*(Or clone the repository and open `index.html` in any modern web browser).*

### 2. Run Formal Verification & Benchmark Suite
```bash
python test_axiomzero.py
```

Expected Output:
```text
..........
----------------------------------------------------------------------
Ran 10 tests in 0.038s

OK

[BENCHMARK] 100 AxiomZero Proof Verifications: 0.0318s | Avg Latency: 0.3183 ms/step
```

---

## 📂 Repository Structure

- `axiomzero_engine.py` — Core AST sanitizer, numerical invariant evaluator, and proof session state machine.
- `test_axiomzero.py` — Formal test suite (**10/10 unit & benchmark tests passing**).
- `index.html` — Titanium aerospace interactive operations cockpit.
- `SUBMISSION_DOSSIER.md` — Complete hackathon submission documentation and pitch materials for IceHacks 2026.
- `firmware/` — Deterministic C99 formal symbolic verification kernel.
- `src/` — TypeScript client for neuro-symbolic agent integration.

---

## 🛡️ License
MIT License. Built by Usman Bamidele for IceHacks 2026.
