"""
Generate a realistic Student Performance dataset for the
"AI-Powered Student Performance Analytics" hackathon project.

Features realistic correlations, noise, missing values, and outliers
so that data-cleaning and EDA steps are meaningful.
"""

import numpy as np
import pandas as pd
import os

np.random.seed(42)

N = 1000

# ---------- helpers ----------
def clamp(arr, lo, hi):
    return np.clip(arr, lo, hi)

# ---------- independent / semi-independent features ----------
student_ids = [f"S{str(i).zfill(4)}" for i in range(1, N + 1)]

gender = np.random.choice(["Male", "Female", "Other"], N, p=[0.48, 0.48, 0.04])

age = np.random.choice(range(17, 26), N, p=[0.05, 0.15, 0.20, 0.25, 0.15, 0.10, 0.05, 0.03, 0.02])

departments = ["Computer Science", "Mechanical", "Electrical", "Civil",
               "Electronics", "MBA", "BBA"]
department = np.random.choice(departments, N)

year_of_study = np.random.choice([1, 2, 3, 4], N, p=[0.30, 0.28, 0.25, 0.17])

family_income = np.random.choice(["Low", "Medium", "High"], N, p=[0.35, 0.45, 0.20])

# Internet access correlates with income
internet_access = np.where(
    family_income == "High",
    np.random.choice(["Yes", "No"], N, p=[0.95, 0.05]),
    np.where(
        family_income == "Medium",
        np.random.choice(["Yes", "No"], N, p=[0.80, 0.20]),
        np.random.choice(["Yes", "No"], N, p=[0.55, 0.45]),
    ),
)

part_time_job = np.where(
    family_income == "Low",
    np.random.choice(["Yes", "No"], N, p=[0.45, 0.55]),
    np.where(
        family_income == "Medium",
        np.random.choice(["Yes", "No"], N, p=[0.25, 0.75]),
        np.random.choice(["Yes", "No"], N, p=[0.10, 0.90]),
    ),
)

distance_km = np.round(np.random.exponential(scale=10, size=N) + 1, 1)
distance_km = clamp(distance_km, 1, 50)

extracurricular = np.random.poisson(lam=1.5, size=N)
extracurricular = clamp(extracurricular, 0, 5).astype(int)

sleep_hours = np.round(np.random.normal(loc=6.5, scale=1.2, size=N), 1)
sleep_hours = clamp(sleep_hours, 3, 10)

mental_health = np.round(
    np.random.normal(loc=6.0, scale=1.8, size=N)
    + np.where(sleep_hours >= 7, 1.0, -0.5)
    + np.where(part_time_job == "Yes", -0.5, 0.3),
    1,
)
mental_health = clamp(mental_health, 1, 10)

online_resources = np.where(
    internet_access == "Yes",
    np.random.choice(["Yes", "No"], N, p=[0.75, 0.25]),
    np.random.choice(["Yes", "No"], N, p=[0.20, 0.80]),
)

# ---------- academic features (correlated) ----------
# Base academic ability (latent)
ability = np.random.normal(loc=0, scale=1, size=N)

# Previous CGPA driven by ability + noise
previous_cgpa = np.round(
    clamp(ability * 1.2 + 7.0 + np.random.normal(0, 0.5, N), 4.0, 10.0), 2
)

# Attendance driven by ability, mental health, distance
attendance = (
    ability * 5
    + 75
    + (mental_health - 5) * 1.5
    - (distance_km - 10) * 0.15
    + np.random.normal(0, 5, N)
)
attendance = np.round(clamp(attendance, 50, 100), 1)

# Study hours driven by ability, part-time job
study_hours = (
    ability * 1.0
    + 4.5
    + np.where(part_time_job == "Yes", -1.2, 0.4)
    + np.random.normal(0, 1.0, N)
)
study_hours = np.round(clamp(study_hours, 0, 10), 1)

# Inject ~15 outliers (students claiming 0-1 or 9-10 hours)
outlier_idx = np.random.choice(N, 15, replace=False)
study_hours[outlier_idx[:7]] = np.round(np.random.uniform(0, 0.5, 7), 1)
study_hours[outlier_idx[7:]] = np.round(np.random.uniform(9.5, 12, 8), 1)  # some > 10

assignment_rate = (
    ability * 8
    + 65
    + np.where(online_resources == "Yes", 5, -3)
    + np.random.normal(0, 7, N)
)
assignment_rate = np.round(clamp(assignment_rate, 30, 100), 1)

# ---------- target: Performance Score (0-100) ----------
performance_score = (
    0.25 * attendance
    + 0.20 * study_hours * 5          # scale study_hours contribution
    + 0.15 * previous_cgpa * 5        # scale CGPA contribution
    + 0.10 * assignment_rate * 0.5
    + 0.08 * mental_health * 3
    + 0.05 * np.where(online_resources == "Yes", 10, 0)
    + 0.05 * np.where(internet_access == "Yes", 5, 0)
    - 0.02 * distance_km
    + np.random.normal(0, 4, N)       # noise
)
# Normalise to 0-100 with a shifted mean (~55) for realistic grade spread
performance_score = (performance_score - performance_score.min()) / (
    performance_score.max() - performance_score.min()
) * 80 + 10  # range ~10-90 with fat middle
performance_score = np.round(clamp(performance_score + np.random.normal(0, 3, N), 0, 100), 1)

# ---------- target: Final Grade (categorical) ----------
def score_to_grade(s):
    if s >= 75:
        return "A"
    elif s >= 60:
        return "B"
    elif s >= 45:
        return "C"
    elif s >= 30:
        return "D"
    else:
        return "F"

final_grade = np.array([score_to_grade(s) for s in performance_score])

# ---------- assemble dataframe ----------
df = pd.DataFrame(
    {
        "Student_ID": student_ids,
        "Gender": gender,
        "Age": age,
        "Department": department,
        "Year_of_Study": year_of_study,
        "Attendance_Percentage": attendance,
        "Study_Hours_Per_Day": study_hours,
        "Previous_CGPA": previous_cgpa,
        "Assignment_Completion_Rate": assignment_rate,
        "Online_Resources_Used": online_resources,
        "Extracurricular_Activities": extracurricular,
        "Sleep_Hours": sleep_hours,
        "Family_Income_Category": family_income,
        "Internet_Access": internet_access,
        "Mental_Health_Score": mental_health,
        "Part_Time_Job": part_time_job,
        "Distance_From_College_KM": distance_km,
        "Final_Grade": final_grade,
        "Performance_Score": performance_score,
    }
)

# ---------- inject missing values ----------
# ~5 % missing in Attendance
mask = np.random.rand(N) < 0.05
df.loc[mask, "Attendance_Percentage"] = np.nan

# ~4 % missing in Study_Hours_Per_Day
mask = np.random.rand(N) < 0.04
df.loc[mask, "Study_Hours_Per_Day"] = np.nan

# ~3 % missing in Mental_Health_Score
mask = np.random.rand(N) < 0.03
df.loc[mask, "Mental_Health_Score"] = np.nan

# ~3 % missing in Previous_CGPA
mask = np.random.rand(N) < 0.03
df.loc[mask, "Previous_CGPA"] = np.nan

# ~2 % missing in Assignment_Completion_Rate
mask = np.random.rand(N) < 0.02
df.loc[mask, "Assignment_Completion_Rate"] = np.nan

# ---------- inject a few duplicate rows ----------
dup_idx = np.random.choice(N, 8, replace=False)
duplicates = df.iloc[dup_idx].copy()
df = pd.concat([df, duplicates], ignore_index=True)

# ---------- save ----------
out_path = os.path.join("E:/Projects/hackathon/data", "student_performance_raw.csv")
df.to_csv(out_path, index=False)

print(f"Dataset saved to {out_path}")
print(f"Shape: {df.shape}")
print(f"\nMissing values:\n{df.isnull().sum()[df.isnull().sum() > 0]}")
print(f"\nGrade distribution:\n{df['Final_Grade'].value_counts().sort_index()}")
print(f"\nPerformance Score stats:\n{df['Performance_Score'].describe()}")
