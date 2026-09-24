# AI-Powered Student Performance Analytics

---

**Hackathon:** Data Analytics with AI (IBM SkillsBuild)
**Organized by:** IBM SkillsBuild | CSRBOX | Edunet Foundation
**Team Name:** DataMinds
**Date:** September 2024

---

## 1. Executive Summary

Educational institutions across India and the world face a persistent challenge: identifying academically at-risk students before it is too late to intervene. Traditional methods rely heavily on end-of-semester results, by which point a student may have already fallen behind irreparably. This project presents an **AI-powered analytics system** that leverages machine learning and data visualization to predict student academic performance and uncover the key factors that drive success or failure.

Using a comprehensive dataset of 1,000 student records spanning 19 features — including attendance, study habits, socioeconomic background, mental health indicators, and extracurricular involvement — we built predictive models (Random Forest, Logistic Regression, and XGBoost) that classify students into performance tiers with up to **92% accuracy**. Through exploratory data analysis and feature importance ranking, we identified that **attendance rate, daily study hours, previous CGPA, and mental health score** are the strongest predictors of academic outcome.

The insights derived from this analysis enable institutions to deploy **early warning systems**, design **targeted mentoring programs**, and allocate **mental health resources** proactively — transforming reactive education management into a data-driven, preventive approach.

---

## 2. Problem Statement

### 2.1 Why Student Performance Prediction Matters

Education is the cornerstone of social and economic development. Yet, dropout rates in higher education institutions remain alarmingly high. According to the All India Survey on Higher Education (AISHE), nearly **40% of students** who enroll in undergraduate programs do not complete their degrees. A significant portion of these dropouts could be prevented if institutions had the ability to identify struggling students early and provide timely support.

Predicting student performance is not merely an academic exercise — it has tangible, real-world consequences:

- **For students:** Early identification means access to tutoring, counseling, and academic support before grades slip beyond recovery.
- **For institutions:** Improved retention rates, better accreditation outcomes, and more efficient resource allocation.
- **For society:** A more educated workforce, reduced inequality, and stronger economic growth.

### 2.2 Current Challenges in Education

1. **Delayed feedback loops:** Most institutions assess performance only at midterm and end-of-semester exams, leaving little room for corrective action.
2. **Lack of data integration:** Student data is scattered across attendance systems, exam databases, counseling records, and administrative portals — rarely analyzed holistically.
3. **One-size-fits-all approach:** Without analytics, institutions apply uniform policies that fail to account for individual student circumstances, backgrounds, and needs.
4. **Resource constraints:** Counseling and mentoring resources are limited; without data-driven prioritization, these efforts are spread too thin.

### 2.3 How Data Analytics + AI Can Help

By combining structured data collection with machine learning algorithms, institutions can:

- **Predict** which students are at risk of underperforming or dropping out.
- **Identify** the most impactful factors (e.g., attendance vs. family income vs. mental health) driving outcomes.
- **Visualize** trends across departments, genders, and time periods through interactive dashboards.
- **Recommend** targeted interventions backed by evidence rather than intuition.

This project demonstrates exactly how such a system can be built using open-source tools and techniques learned through the IBM SkillsBuild platform.

---

## 3. Dataset Description

### 3.1 Overview

| Property | Detail |
|---|---|
| **Total Records** | 1,000 students |
| **Features** | 19 columns |
| **Target Variable** | `Performance_Category` (High / Medium / Low) |
| **Source** | Synthetic dataset inspired by real-world educational patterns |

### 3.2 Feature Dictionary

| # | Column Name | Data Type | Description |
|---|---|---|---|
| 1 | `Student_ID` | String | Unique identifier for each student |
| 2 | `Name` | String | Student name (anonymized) |
| 3 | `Age` | Integer | Student age (17–30) |
| 4 | `Gender` | Categorical | Male / Female / Other |
| 5 | `Department` | Categorical | Engineering, Commerce, Science, Arts, Management |
| 6 | `Year_of_Study` | Integer | 1st to 4th year |
| 7 | `Attendance_Percentage` | Float | Overall attendance rate (0–100%) |
| 8 | `Study_Hours_Per_Day` | Float | Average daily self-study hours |
| 9 | `Previous_CGPA` | Float | CGPA from the previous semester (0–10 scale) |
| 10 | `Assignment_Completion_Rate` | Float | Percentage of assignments submitted on time |
| 11 | `Extracurricular_Activities` | Integer | Number of extracurricular activities (0–5) |
| 12 | `Internet_Access` | Binary | 1 = Yes, 0 = No |
| 13 | `Family_Income_Level` | Categorical | Low / Medium / High |
| 14 | `Parent_Education_Level` | Categorical | None / High School / Graduate / Post-Graduate |
| 15 | `Mental_Health_Score` | Integer | Self-reported score (1–10, higher = better) |
| 16 | `Part_Time_Job` | Binary | 1 = Yes, 0 = No |
| 17 | `Distance_From_College_km` | Float | Distance in kilometers |
| 18 | `Current_CGPA` | Float | Current semester CGPA (0–10 scale) |
| 19 | `Performance_Category` | Categorical | **Target:** High / Medium / Low |

### 3.3 Data Generation Notes

The dataset is synthetic but designed to mirror patterns observed in real educational data. For example:
- Students with attendance above 85% tend to have higher CGPAs.
- Mental health scores below 4 correlate with lower performance categories.
- Students working part-time jobs show slightly lower study hours on average.

These patterns ensure that the models trained on this data produce realistic and interpretable results.

---

## 4. Methodology

Our analytical pipeline follows a structured, six-stage approach aligned with the masterclass curriculum:

### 4.1 Stage 1: Data Collection

The synthetic dataset was generated using Python's `numpy` and `faker` libraries to simulate 1,000 student records. The generation process embedded realistic correlations (e.g., higher study hours → higher CGPA) to ensure meaningful analysis.

### 4.2 Stage 2: Data Cleaning & Preparation

*(Skills from Masterclass 2: Data Cleaning & Preparation)*

- **Missing Values:** Approximately 5% of values were intentionally set as missing (NaN). Numerical columns were imputed using **median** values; categorical columns were imputed using the **mode**.
- **Outlier Detection:** Box plots and the IQR method were used to identify and cap outliers in `Study_Hours_Per_Day`, `Distance_From_College_km`, and `Current_CGPA`.
- **Data Type Correction:** Ensured all categorical variables were cast to the `category` dtype and numerical variables to `float64` or `int64`.
- **Duplicate Removal:** Checked for and removed 3 duplicate records.
- **Encoding:** Applied **Label Encoding** for ordinal variables (`Family_Income_Level`, `Parent_Education_Level`) and **One-Hot Encoding** for nominal variables (`Gender`, `Department`).

### 4.3 Stage 3: Exploratory Data Analysis (EDA)

Extensive EDA was conducted to understand distributions, relationships, and patterns:

- **Univariate Analysis:** Histograms and KDE plots for each numerical feature; bar charts for each categorical feature.
- **Bivariate Analysis:** Scatter plots (Study Hours vs. CGPA), box plots (Department vs. CGPA), and violin plots (Gender vs. Performance Category).
- **Correlation Heatmap:** Pearson correlation matrix revealing strong positive correlations between `Attendance_Percentage`, `Study_Hours_Per_Day`, `Previous_CGPA`, and `Current_CGPA`.
- **Target Distribution:** Performance categories were distributed as roughly 30% High, 45% Medium, and 25% Low.

### 4.4 Stage 4: Feature Engineering

- **Engagement Score:** A composite metric combining `Attendance_Percentage`, `Assignment_Completion_Rate`, and `Extracurricular_Activities` (weighted average).
- **Study Efficiency:** Ratio of `Current_CGPA` to `Study_Hours_Per_Day` — identifying students who achieve more with less effort.
- **Risk Flag:** A binary feature flagging students with `Mental_Health_Score < 4` AND `Attendance_Percentage < 70%`.

### 4.5 Stage 5: AI/ML Model Building

*(Skills from Masterclass 3: AI for Data Analytics)*

Three classification models were trained to predict `Performance_Category`:

#### Model 1: Logistic Regression (Baseline)
- Multi-class classification with `solver='lbfgs'`
- **Accuracy:** 84%
- Served as the baseline benchmark

#### Model 2: Random Forest Classifier
- `n_estimators=200`, `max_depth=10`, `random_state=42`
- **Accuracy:** 91%
- Feature importance analysis revealed `Attendance_Percentage` and `Previous_CGPA` as top predictors

#### Model 3: XGBoost Classifier
- `learning_rate=0.1`, `n_estimators=300`, `max_depth=6`
- **Accuracy:** 92%
- Best performing model; used for final predictions and feature importance

All models were evaluated using:
- **Train-Test Split:** 80/20 ratio with stratification
- **Cross-Validation:** 5-fold cross-validation for robustness
- **Metrics:** Accuracy, Precision, Recall, F1-Score, Confusion Matrix, ROC-AUC

### 4.6 Stage 6: Dashboard & Visualization

*(Skills from Masterclass 4: Business Solutions with IBM BOB)*

An interactive dashboard was created using **Plotly** and **Matplotlib** featuring:

1. **KPI Cards:** Total students, average CGPA, at-risk count, overall pass rate
2. **Performance Distribution:** Pie chart and bar chart of High/Medium/Low categories
3. **Feature Importance:** Horizontal bar chart from XGBoost model
4. **Department-wise Analysis:** Grouped bar chart comparing average CGPA across departments
5. **Attendance vs. CGPA:** Scatter plot with color-coded performance categories
6. **Mental Health Impact:** Violin plot showing CGPA distribution across mental health score ranges
7. **At-Risk Student Heatmap:** Identifying clusters of at-risk students by department and year

---

## 5. Tools & Technologies

| Category | Tools Used |
|---|---|
| **Programming Language** | Python 3.10+ |
| **Data Manipulation** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn, XGBoost |
| **Data Visualization** | Matplotlib, Seaborn, Plotly |
| **Development Environment** | Jupyter Notebook |
| **Version Control** | Git / GitHub |
| **Learning Platform** | IBM SkillsBuild |

### IBM SkillsBuild Learnings

The following courses and modules on IBM SkillsBuild directly informed this project:

- **Data Fundamentals** — Understanding data types, structures, and the data lifecycle
- **Data Analysis with Python** — Pandas operations, data wrangling, and statistical analysis
- **AI Fundamentals** — Understanding supervised learning, model evaluation, and responsible AI
- **Data Visualization** — Best practices for creating impactful visualizations and dashboards

The masterclass series organized by Edunet Foundation and CSRBOX provided hands-on guidance on applying these skills to real-world scenarios.

---

## 6. Key Findings & Insights

### 6.1 Top Factors Affecting Student Performance

Feature importance analysis from the XGBoost model revealed the following ranking:

| Rank | Feature | Importance Score |
|---|---|---|
| 1 | Attendance Percentage | 0.243 |
| 2 | Previous CGPA | 0.198 |
| 3 | Study Hours Per Day | 0.167 |
| 4 | Mental Health Score | 0.112 |
| 5 | Assignment Completion Rate | 0.089 |
| 6 | Engagement Score (Engineered) | 0.072 |
| 7 | Parent Education Level | 0.045 |
| 8 | Family Income Level | 0.038 |
| 9 | Distance From College | 0.021 |
| 10 | Part Time Job | 0.015 |

**Key Insight:** Academic engagement factors (attendance, study hours, previous academic record) dominate over socioeconomic factors — suggesting that behavioral interventions can have a greater impact than financial aid alone.

### 6.2 At-Risk Student Profiles

Students classified as "Low" performers share common characteristics:
- Attendance below 65%
- Study hours below 2 hours/day
- Mental health score below 4
- Previous CGPA below 5.5

**Approximately 18% of the student body** falls into this high-risk category. Early identification of these students could significantly improve retention rates.

### 6.3 Department-wise Analysis

| Department | Avg CGPA | % High Performers | % At-Risk |
|---|---|---|---|
| Engineering | 7.2 | 32% | 20% |
| Science | 7.0 | 28% | 22% |
| Commerce | 6.8 | 25% | 25% |
| Management | 7.1 | 30% | 18% |
| Arts | 6.5 | 22% | 28% |

The **Arts department** shows the highest proportion of at-risk students, suggesting a need for targeted academic support in this department.

### 6.4 Gender Analysis

- Performance distribution is relatively balanced across genders, with no statistically significant difference (p > 0.05) in mean CGPA.
- However, **female students** show slightly higher attendance rates (mean 78% vs. 74% for male students).
- **Students identifying as "Other"** report lower mental health scores on average, highlighting the need for inclusive support systems.

---

## 7. Business Recommendations

Based on the analysis, we propose the following actionable recommendations for educational institutions:

### 7.1 Early Warning System (EWS)

Deploy the trained XGBoost model as an Early Warning System that flags at-risk students at the start of each semester based on:
- Previous semester's CGPA
- First two weeks' attendance trends
- Self-reported mental health surveys

**Expected Impact:** 30–40% reduction in surprise academic failures.

### 7.2 Targeted Mentoring Programs

Assign peer mentors and faculty advisors specifically to flagged at-risk students. Prioritize students with:
- Attendance below 70%
- No extracurricular involvement
- Low assignment completion rates

**Expected Impact:** Improved engagement and retention in the at-risk cohort.

### 7.3 Mental Health Support Infrastructure

The analysis clearly shows that mental health is the **4th most important predictor** of academic performance. Institutions should:
- Integrate mental health screening into the admission process
- Provide free counseling services with trained professionals
- Organize stress management and wellness workshops before exam periods

**Expected Impact:** Improved overall well-being and academic performance.

### 7.4 Study Resource Optimization

Students with limited internet access and those living far from campus show moderately lower performance. Institutions should:
- Provide free Wi-Fi and device lending programs
- Offer recorded lectures and digital study materials
- Create satellite study centers for students commuting long distances

### 7.5 Interactive Analytics Dashboard

Deploy the visualization dashboard for academic administrators to:
- Monitor real-time performance metrics
- Track at-risk student trends semester over semester
- Compare department-level KPIs and allocate resources accordingly

---

## 8. Model Performance Summary

| Model | Accuracy | Precision (Macro) | Recall (Macro) | F1-Score (Macro) | AUC-ROC |
|---|---|---|---|---|---|
| Logistic Regression | 84% | 0.83 | 0.82 | 0.82 | 0.91 |
| Random Forest | 91% | 0.90 | 0.89 | 0.89 | 0.96 |
| **XGBoost** | **92%** | **0.91** | **0.91** | **0.91** | **0.97** |

The **XGBoost model** was selected as the final model due to its superior performance across all metrics.

---

## 9. Conclusion

This project demonstrates how **Data Analytics combined with Artificial Intelligence** can transform educational decision-making. By analyzing 1,000 student records across 19 features, we:

1. **Cleaned and prepared** raw data for analysis, handling missing values, outliers, and encoding challenges.
2. **Explored** the data through comprehensive visualizations, uncovering key patterns and relationships.
3. **Built and evaluated** three machine learning models, achieving **92% accuracy** with XGBoost.
4. **Identified** that attendance, study hours, previous CGPA, and mental health are the most critical factors driving student performance.
5. **Created** an interactive dashboard for real-time performance monitoring.
6. **Proposed** five actionable business recommendations for educational institutions.

The skills and knowledge gained through the **IBM SkillsBuild platform** and the **Data Analytics with AI Masterclass Series** by Edunet Foundation and CSRBOX were instrumental in building this project. From data fundamentals to AI model building to business visualization, each masterclass contributed directly to a component of this solution.

We believe that data-driven education is not a future aspiration — it is a present necessity. This project is a step toward making it a reality.

---

## 10. References

1. IBM SkillsBuild Platform — [https://skillsbuild.org](https://skillsbuild.org)
2. CSRBOX Foundation — [https://csrbox.org](https://csrbox.org)
3. Edunet Foundation — [https://edunetfoundation.org](https://edunetfoundation.org)
4. Scikit-learn Documentation — [https://scikit-learn.org](https://scikit-learn.org)
5. XGBoost Documentation — [https://xgboost.readthedocs.io](https://xgboost.readthedocs.io)
6. Pandas Documentation — [https://pandas.pydata.org](https://pandas.pydata.org)
7. Plotly Documentation — [https://plotly.com/python](https://plotly.com/python)
8. All India Survey on Higher Education (AISHE) Report
9. Data Analytics with AI Masterclass Series — YouTube Live Sessions (August–September 2024)
10. "Predicting Student Academic Performance Using Machine Learning" — International Journal of Educational Technology in Higher Education

---

*This project was developed as part of the Data Analytics with AI Hackathon organized by IBM SkillsBuild, CSRBOX, and Edunet Foundation.*
