# 📊 Job Market Skill-Gap Analyzer — India

An end-to-end data analytics project that scrapes real Data Analyst job postings across India, cleans and structures the data, analyzes it with SQL, and visualizes the findings in an interactive Power BI dashboard.

The goal: help job seekers and career switchers understand which skills are actually in demand, which ones pay the most, and where the jobs are — using real, current market data instead of guesswork.

---

## 🧭 Problem Statement

Aspiring data analysts often don't know which skill to prioritize learning first. This project answers that question with data: by pulling live job postings and analyzing what employers are actually asking for and paying for.

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Data Collection | Python, Adzuna Jobs API |
| Data Cleaning & Processing | Python (pandas) |
| Database | PostgreSQL |
| Analysis | SQL |
| Visualization | Power BI |
| Version Control | Git & GitHub |

---

## 🔄 Project Pipeline

1. **Data Collection** — Pulled 250+ live Data Analyst job postings across India using the Adzuna Jobs API.
2. **Data Cleaning** — Removed duplicates, handled missing values, standardized city names, and extracted mentioned skills from job descriptions.
3. **Database Design** — Loaded cleaned data into a normalized PostgreSQL database (`jobs` and `job_skills` tables).
4. **SQL Analysis** — Wrote queries to surface skill demand, salary trends, and city-wise hiring patterns.
5. **Dashboard** — Connected Power BI directly to PostgreSQL and built an interactive dashboard.

---

## 📈 Key Insights

- **SQL is the single most in-demand skill**, appearing in 55 of the analyzed postings — ahead of Excel (39) and Python (30).
- **Sr. Data Analyst roles command the highest average salary** (~₹13.5L), significantly above standard Data Analyst postings (~₹8.9L).
- **Bangalore and India-wide remote listings dominate hiring volume**, followed by Pune, Hyderabad, and Mumbai.
- **Demand and pay don't always align**: cloud skills like GCP and Azure command higher average salaries than SQL, despite far lower demand.

---

## 📊 Dashboard Preview

*(Insert your Power BI dashboard screenshot here — e.g. image/dashboard.png)*

---

## 📁 Repository Structure

```
Job_Market_Skill_Gap_Analyzer/
│
├── data/
│   ├── jobs_raw.csv
│   ├── jobs_cleaned.csv
│   └── job_skills_long.csv
│
├── src/
│   ├── get_job.py
│   └── clean_data.py
│
├── sql/
│   └── queries.sql
│
├── dashboard/
│   └── job_dashboard.pbix
│
├── image/
│   └── dashboard.png
│
└── README.md
```

---

## ▶️ How to Run This Project

1. Clone this repository
2. Get a free API key from Adzuna Developer
3. Add your APP_ID and APP_KEY in src/get_job.py
4. Run `python src/get_job.py`
5. Run `python src/clean_data.py`
6. Load cleaned CSVs into PostgreSQL
7. Open the dashboard in Power BI Desktop

---

## 🙋 About Me

Aspiring Data Analyst skilled in Python, SQL, and Power BI. This project reflects my ability to independently source real-world data, clean and model it, write meaningful SQL analysis, and communicate insights through a polished, interactive dashboard.