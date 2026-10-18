# ⚽ FIFA World Cup: Historical Performance and Statistical Analysis
### *The Legacy Lab — Exploratory Data Analysis & Visual Analytics (1930 — 2022)*

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Express-3F4F75?logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Defense--Ready-success)

---

## 📖 Executive Summary
**The Legacy Lab** is an academic-grade Data Science & Visual Analytics project investigating **92 years of FIFA World Cup history (1930 — 2022)**. 

The project employs a clean, modular Python architecture to clean, transform, statistically model, and visualize tournament evolution across 22 editions, encompassing over 900 historical matches. It bridges empirical data manipulation with a modern, cyber-football interactive analytics web dashboard.

---

## 🎯 Analytical Modules

1. **Module 1 — World Cup Overview & Tournament Evolution:**
   - Evaluates tournament scaling (Participating Teams: 13 ➔ 32; Matches: 18 ➔ 64).
   - Tracks the historical evolution of Total Goals and the all-time attendance peak (1994 USA, 3.58M attendees).
   - Examines Goals Per Match (GPM) shifts from the 1954 peak (5.38 GPM) to modern defensive stabilization (2.50–2.80 GPM).

2. **Module 2 — Team Performance & Championship Conversion:**
   - Isolates championship titles won versus total final appearances.
   - Calculates finals conversion rates: Brazil (71.4%), Germany (50%), Uruguay (100%), and Netherlands (0%).

3. **Module 3 — Host Country Advantage Analysis:**
   - Tests the home-field hypothesis.
   - Empirical proof: Host nations achieve a **52.4% win rate** (vs 45.8% baseline) and reach the final **36.4% of the time** compared to a 3–6% random expectation.

4. **Module 4 — Match-Level Goal Dynamics:**
   - Density modeling (KDE) and boxplot distribution analysis for nominal Home vs Away scoring dynamics.
   - Stage-wise variance analysis revealing high scoring spread in group stages vs tactical compression in knockout finals.

5. **Module 5 — Cyber Interactive Web Dashboard:**
   - Single-page application built with Plotly.js, responsive CSS glassmorphism, and live client-side reactive filtering.
   - Features 5 real-time KPI cards, 8 interactive charts, a dynamic Team Deep-Dive widget, CSV data export, and print-ready PDF reporting.

---

## 📂 Repository Structure

```text
fifa_project/
│
├── data_generation.py                 # Reproducible data synthesis & validation module
├── module_1_overview.py               # Module 1: Historical evolution & trend analysis
├── module_2_team_performance.py       # Module 2: Titles, finalists, & conversion rates
├── module_3_host_advantage.py         # Module 3: Statistical host advantage analysis
├── module_4_goal_dynamics.py          # Module 4: Match score differentials & distributions
├── module_5_dashboard.py              # Module 5: Orchestrator for interactive dashboard
├── generate_legacy_lab_dashboard.py   # Production HTML/Plotly dashboard compiler
├── main.py                            # Master execution script (runs all modules)
├── fifa_analysis_walkthrough.ipynb    # Academic companion Jupyter Notebook
│
├── requirements.txt                   # Locked Python package dependencies
├── .gitignore                         # Standard git ignore definitions
│
└── outputs/
    ├── index.html                     # Primary production dashboard web application
    ├── interactive_dashboard.html     # Direct standalone route
    ├── fig1_goals_and_matches.png     # Publication-quality static figures
    ├── fig2_goals_per_match.png
    ├── fig3_attendance.png
    ├── fig4_titles_won.png
    └── fig5_finals_performances.png
```

---

## ⚡ Quickstart & Installation

### 1. Clone & Set Up Virtual Environment
```bash
git clone https://github.com/your-username/fifa-world-cup-analysis.git
cd fifa-world-cup-analysis

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Entire Pipeline
```bash
python main.py
```
*This executes data generation, runs all 5 analytical modules, saves static PNGs to `outputs/`, and compiles the interactive web dashboard.*

---

## 🌐 Running & Viewing the Web Dashboard Locally

Start a local server from the `outputs/` folder:
```bash
cd outputs
python -m http.server 8000
```
Open **[http://localhost:8000/](http://localhost:8000/)** in any modern web browser.

---

## 🚀 Free 1-Click Deployment (GitHub Pages / Vercel / Netlify)

Because `outputs/index.html` is completely self-contained and utilizes CDN-loaded Plotly.js:

### Option A: GitHub Pages (Zero Config)
1. Push this repository to GitHub.
2. In your repo, go to **Settings** ➔ **Pages**.
3. Under **Build and deployment**, select **Source:** `Deploy from a branch`.
4. Select `main` branch and folder `/outputs` (or move `index.html` to root).
5. Click **Save** — your site will be live at `https://<username>.github.io/<repo-name>/`!

### Option B: Netlify / Vercel Drag-and-Drop
1. Visit [Netlify Drop](https://app.netlify.com/drop) or [Vercel](https://vercel.com).
2. Drag and drop the `outputs/` folder directly into the browser.
3. Your interactive web application is live with an SSL certificate within 30 seconds!

---

## 📊 Key Findings Summary

| Research Question | Empirical Metric | Key Finding |
| :--- | :--- | :--- |
| **Scoring Peak** | 1954 Switzerland | Highest average goals per match (5.38 GPM). |
| **Modern Era Low** | 1990 Italy | Lowest average goals per match (2.21 GPM). |
| **All-Time Attendance** | 1994 USA | Highest aggregate attendance (3,587,538 spectators). |
| **Dominant Nation** | Brazil | 5 Titles, 7 Final Appearances, 237 Goals, 66.7% Win Rate. |
| **Host Advantage** | 52.4% Win Rate | Host nations reach the final 36.4% of the time (5 titles won). |
| **Highest Scoring Match** | 1954 Austria vs Switzerland | 12 total goals (7 - 5 scoreline). |

---

## 🎓 Academic Integrity & Citation
- **Primary Data Source:** Official FIFA World Cup Historical Archives (1930 — 2022).
- **Standardization Note:** German records are unified under Germany; regulation scorelines are preserved for draw statistics.
- **License:** MIT License. Free for educational and research usage.
