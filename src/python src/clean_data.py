import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = BASE_DIR
while os.path.basename(PROJECT_ROOT) != "Job_Market_Skill_Gap_Analyzer" and os.path.dirname(PROJECT_ROOT) != PROJECT_ROOT:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
os.makedirs(DATA_DIR, exist_ok=True)

df = pd.read_csv(os.path.join(DATA_DIR, "jobs_raw.csv"))
print(f"Shuruaati total rows: {len(df)}")

df = df.drop_duplicates(subset=["title", "company", "location"])
print(f"Duplicates hatane ke baad: {len(df)}")

df["company"] = df["company"].fillna("Not Specified")
df["location"] = df["location"].fillna("Not Specified")
df["salary_min"] = df["salary_min"].fillna(df["salary_min"].median())
df["salary_max"] = df["salary_max"].fillna(df["salary_max"].median())
df["avg_salary"] = (df["salary_min"] + df["salary_max"]) / 2

location_map = {
    "bengaluru": "bangalore",
    "gurugram": "gurgaon",
    "delhi ncr": "delhi",
    "new delhi": "delhi"
}
df["location"] = df["location"].astype(str).str.lower().str.strip()
df["location"] = df["location"].replace(location_map)

SKILL_KEYWORDS = [
    "python", "sql", "excel", "tableau", "power bi", "r programming",
    "machine learning", "statistics", "pandas", "numpy", "aws",
    "spark", "hadoop", "google sheets", "looker", "sas", "vba",
    "azure", "gcp", "etl", "data visualization", "communication"
]

def extract_skills(description):
    if pd.isna(description):
        return []
    text = str(description).lower()
    return [skill for skill in SKILL_KEYWORDS if skill in text]

df["skills"] = df["description"].apply(extract_skills)
df["skill_count"] = df["skills"].apply(len)

df_final = df[["title", "company", "location", "salary_min", "salary_max",
               "avg_salary", "description", "created", "category", "skill_count"]]
df_final.to_csv(os.path.join(DATA_DIR, "jobs_cleaned.csv"), index=False)
print(f"Cleaned data save ho gaya: {DATA_DIR}\\jobs_cleaned.csv")
print(f"Final total rows: {len(df_final)}")

df_skills = df.explode("skills")[["title", "company", "location", "avg_salary", "skills"]]
df_skills = df_skills.dropna(subset=["skills"])
df_skills = df_skills.rename(columns={"skills": "skill"})
df_skills.to_csv(os.path.join(DATA_DIR, "job_skills_long.csv"), index=False)
print(f"Skills (long format) save ho gaya: {DATA_DIR}\\job_skills_long.csv")

print("\nTop 10 sabse zyada demand wali skills:")
print(df_skills["skill"].value_counts().head(10))