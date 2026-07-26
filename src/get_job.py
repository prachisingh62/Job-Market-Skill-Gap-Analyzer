import requests
import pandas as pd
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = BASE_DIR
while os.path.basename(PROJECT_ROOT) != "Job_Market_Skill_Gap_Analyzer" and os.path.dirname(PROJECT_ROOT) != PROJECT_ROOT:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
os.makedirs(DATA_DIR, exist_ok=True)

APP_ID = "2a2fc15f"
APP_KEY = "6db1741a6b4f84d7683f1de851c26742"
COUNTRY = "in"


def fetch_jobs(keyword="data analyst", pages=5):
    all_jobs = []
    for page in range(1, pages + 1):
        url = f"https://api.adzuna.com/v1/api/jobs/{COUNTRY}/search/{page}"
        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "results_per_page": 50,
            "what": keyword,
            "content-type": "application/json"
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Page {page} par error: {response.status_code}")
            break
        data = response.json()
        results = data.get("results", [])
        if not results:
            break
        for job in results:
            all_jobs.append({
                "title": job.get("title"),
                "company": job.get("company", {}).get("display_name"),
                "location": job.get("location", {}).get("display_name"),
                "salary_min": job.get("salary_min"),
                "salary_max": job.get("salary_max"),
                "description": job.get("description"),
                "created": job.get("created"),
                "category": job.get("category", {}).get("label")
            })
        print(f"Page {page} se {len(results)} jobs mile.")
        time.sleep(1)
    return pd.DataFrame(all_jobs)


if __name__ == "__main__":
    df = fetch_jobs(keyword="data analyst", pages=5)
    if len(df) == 0:
        print("Koi data nahi mila.")
    else:
        save_path = os.path.join(DATA_DIR, "jobs_raw.csv")
        df.to_csv(save_path, index=False)
        print(f"\nTotal {len(df)} jobs collect ho gaye.")
        print(f"File save ho gayi: {save_path}")