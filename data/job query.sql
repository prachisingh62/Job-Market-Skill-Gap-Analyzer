SELECT COUNT(*) FROM jobs;
SELECT COUNT(*) FROM job_skills;
SELECT * FROM jobs LIMIT 5;

Top 10 skills:

SELECT skill, COUNT(*) AS demand
FROM job_skills
GROUP BY skill
ORDER BY demand DESC
LIMIT 10;

Highest paying job titles:

SELECT title, ROUND(AVG(avg_salary), 0) AS avg_pay
FROM jobs
GROUP BY title
ORDER BY avg_pay DESC
LIMIT 10;

City-wise job demand:

SELECT location, COUNT(*) AS total_jobs
FROM jobs
GROUP BY location
ORDER BY total_jobs DESC
LIMIT 10;

Skill vs average salary (kaunsi skill zyada paise deti hai):

SELECT skill, ROUND(AVG(avg_salary), 0) AS avg_pay, COUNT(*) AS demand
FROM job_skills
GROUP BY skill
ORDER BY avg_pay DESC
LIMIT 10;