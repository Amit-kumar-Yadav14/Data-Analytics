# AI-Powered Student Performance Analytics

## AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026 | BharatCares

---

## 📋 Project Overview

This project implements an **AI-powered predictive analytics system** to identify at-risk students and provide actionable insights for educational institutions. It demonstrates the complete data science pipeline from data cleaning to machine learning model deployment.

**Target Problem**: Early identification of students at-risk of academic failure to enable timely intervention.

**Solution**: Machine learning models (Linear Regression, Random Forest, Gradient Boosting, XGBoost) trained to predict student performance scores based on 19 features covering academic, socioeconomic, and behavioral indicators.

---

## 📊 Dataset

**Link**: The dataset (`student_performance_raw.csv`) is included in the `data/` directory of this repository. It is a synthetic dataset designed with realistic correlations to simulate real-world educational patterns.

- **Total Records**: 1,000+ students
- **Features**: 19 columns
- **Target Variable**: `Performance_Score` (continuous, 0-100 scale)

### Features Include:
- **Academic**: Attendance Percentage, Study Hours/Day, Previous CGPA, Assignment Completion Rate
- **Personal**: Age, Gender, Sleep Hours, Mental Health Score, Extracurricular Activities
- **Socioeconomic**: Family Income Category, Internet Access, Part-Time Job, Distance from College
- **Target**: Performance Score (0-100), Final Grade (A/B/C/D/F)

---

## 🛠️ Technologies Used

| Category | Tools |
|----------|-------|
| **Language** | Python 3.9+ |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn, XGBoost |
| **Visualization** | Matplotlib, Seaborn |
| **Statistical Analysis** | SciPy |
| **Environment** | Jupyter Notebook |
| **Learning Platform** | IBM SkillsBuild |

---

## 🚀 Setup / Run Instructions

### Prerequisites
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### Running the Project

**Step 1**: Clone or download this repository
```bash
git clone <repository-url>
cd CSRBOX
```

**Step 2**: Install dependencies
```bash
pip install -r requirements.txt
```

**Step 3**: Open and run the Jupyter Notebook
```bash
jupyter notebook AmitKumar_StudentPerformanceAnalytics.ipynb
```

**Step 4**: Execute all cells sequentially (Shift + Enter) or use **Cell → Run All**

The notebook will:
- Load the raw dataset from `data/student_performance_raw.csv`
- Perform data cleaning (missing values, outliers, validation)
- Generate 8 visualization outputs in the `outputs/` folder
- Train 4 ML models and compare performance
- Create a comprehensive 9-panel dashboard
- Generate business insights and recommendations

### Output Files
After running:
- `outputs/` — 8 PNG visualization files + model results CSV
- `data/student_performance_cleaned.csv` — Cleaned dataset

---

## 📁 Project Structure

```
CSRBOX/
├── AmitKumar_StudentPerformanceAnalytics.ipynb   # Main Code File (.ipynb)
├── requirements.txt                               # Python Dependencies
├── AmitKumar_ProjectReport.docx                   # Project Report (.docx)
├── README.md                                      # This file
├── data/
│   ├── student_performance_raw.csv                # Raw dataset
│   └── student_performance_cleaned.csv            # Cleaned dataset (generated)
├── outputs/
│   ├── 01_missing_values.png
│   ├── 02_distributions.png
│   ├── 03_correlation_matrix.png
│   ├── 04_categorical_analysis.png
│   ├── 05_model_comparison.png
│   ├── 06_feature_importance.png
│   ├── 07_actual_vs_predicted.png
│   ├── 08_comprehensive_dashboard.png
│   └── model_results_summary.csv
├── presentation/
│   └── AI_Student_Performance_Analytics_Presentation.pptx
├── generate_dataset.py                            # Dataset generation script
└── create_presentation.py                         # Presentation generation script
```

---

## 🤖 Machine Learning Models & Results

### Models Trained
1. **Linear Regression** — Baseline model
2. **Random Forest Regressor** ⭐ Best Model
3. **Gradient Boosting Regressor**
4. **XGBoost Regressor**

### Performance Comparison

| Model | RMSE | MAE | R² Score |
|-------|------|-----|----------|
| Linear Regression | 8.93 | 7.22 | 0.490 |
| **Random Forest** | **8.89** | **7.11** | **0.495** |
| Gradient Boosting | 9.03 | 7.13 | 0.478 |
| XGBoost | 9.74 | 7.66 | 0.394 |

**Best Model**: Random Forest Regressor (lowest RMSE, highest R²)

---

## 📈 Key Insights

### Top Performance Drivers
1. **Attendance Percentage** — Strongest predictor
2. **Previous CGPA** — Strong academic indicator
3. **Study Hours/Day** — Direct positive correlation
4. **Mental Health Score** — Significant impact
5. **Assignment Completion Rate** — Measures engagement

### Student Risk Segmentation
- **At-Risk** (Score < 60): Students needing immediate intervention
- **Average** (Score 60-80): Performing adequately
- **High Performers** (Score ≥ 80): Excelling academically

### Key Finding
Academic engagement factors (attendance, study hours) dominate over socioeconomic factors — behavioral interventions can have greater impact than financial aid alone.

---

## 💡 Strategic Recommendations

1. **Early Warning System** — Deploy automated alerts for at-risk students
2. **Attendance Optimization** — Minimum target: 75% attendance
3. **Study Hour Targets** — Recommended: 4-6 hours/day
4. **Mental Health Support** — Strengthen counseling services
5. **Digital Infrastructure** — Expand WiFi, provide offline resources
6. **Department-Specific Initiatives** — Targeted mentoring for struggling departments

---

## 📊 Visualizations Generated

1. Missing Data Distribution
2. Feature Distributions (9 numerical columns)
3. Correlation Matrix Heatmap
4. Categorical Analysis (Department, Gender, Year, Internet)
5. Model Performance Comparison (RMSE, MAE, R²)
6. Feature Importance (Top 10)
7. Actual vs Predicted Performance
8. Comprehensive 9-Panel Dashboard

---

## 🎓 Alignment with IBM SkillsBuild Masterclass

| Masterclass | Coverage |
|-------------|----------|
| Data Fundamentals | ✅ Data types, statistics, distributions |
| Data Cleaning & Preparation | ✅ Missing values, outliers, validation |
| AI for Data Analytics | ✅ 4 ML models, feature importance, predictions |
| Business Solutions | ✅ Dashboard, KPIs, recommendations |

---

## 📄 Submission Files

| # | File | Format | Description |
|---|------|--------|-------------|
| 1 | `AmitKumar_StudentPerformanceAnalytics.ipynb` | .ipynb | Complete project code |
| 2 | `requirements.txt` | .txt | Python dependencies |
| 3 | `AmitKumar_ProjectReport.docx` | .docx | Project documentation |
| 4 | `README.md` | .md | Project overview (this file) |

---

## 👤 Author

**Name**: Amit Kumar  
**Email**: amityadav987000@gmail.com  
**Program**: IBM SkillsBuild Data Analytics with AI Academic Internship 2026  
**Conducted By**: BharatCares in association with AICTE

---

**Last Updated**: September 23, 2026  
**Status**: ✅ Complete & Ready for Submission
