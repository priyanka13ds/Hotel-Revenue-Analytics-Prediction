# 🏨 Hotel Revenue Analytics & Forecasting Dashboard

## 📌 Project Overview
This project delivers an **end-to-end data science solution** for analyzing hotel booking data and predicting revenue using machine learning.  
It combines **data analysis, predictive modeling, and interactive visualization** to support **data-driven pricing and revenue optimization decisions**.

The project follows a **real-world data science workflow**, from data preparation to deployment via a **Streamlit dashboard**.

---

## 🎯 Business Objective
- Identify **key drivers of hotel revenue**
- Analyze **room demand vs revenue contribution**
- Understand **seasonal and booking behavior trends**
- Build predictive models to **forecast total booking revenue**
- Provide insights through an **interactive, user-friendly dashboard**

---

## 🔄 Project Workflow

### 1️⃣ Data Generation
- Simulated hotel booking data to reflect real-world booking patterns
- Included features such as:
  - Room types  
  - Stay duration  
  - Pricing details  
  - Booking dates  
  - Room service costs  
  - Total revenue  

---

### 2️⃣ Data Manipulation
- Performed initial transformations using **Pandas**:
  - Column selection and renaming  
  - Feature creation  
  - Aggregations for analysis  
- Structured datasets for efficient analysis and modeling

---

### 3️⃣ Data Cleaning
- Handled missing values and inconsistencies  
- Corrected data types for dates and numeric fields  
- Ensured high data quality and consistency for downstream tasks

---

### 4️⃣ Exploratory Data Analysis (EDA)
- Analyzed:
  - Revenue distribution by room type  
  - Demand vs revenue contribution  
  - Monthly and seasonal booking trends  
- Visualized insights with **business-focused interpretations**, not just plots  
- Highlighted patterns relevant for pricing and inventory decisions

---

### 5️⃣ Feature Engineering
- Created machine-learning-ready features:
  - Date-based attributes (month, day of week, weekend indicator)  
  - Pricing metrics  
  - Encoded categorical variables (room types)  
- Designed features aligned with real-world revenue drivers

---

### 6️⃣ Modeling & Evaluation
- Built and compared multiple regression models:
  - **Linear Regression** for interpretability  
  - **Random Forest Regressor** for capturing non-linear relationships  
- Evaluated models using:
  - Mean Absolute Error (MAE)  
  - Root Mean Squared Error (RMSE)  
  - R² Score  
- Selected the best-performing model for deployment

---

### 7️⃣ Interactive Streamlit Dashboard 🚀
Developed a **portfolio-ready Streamlit dashboard** featuring:

#### 🔹 Executive Overview
- High-level KPIs:
  - Total revenue  
  - Average revenue per booking  
  - Total bookings  
- Revenue trends and room-wise performance  
- Clean, expandable dataset preview

#### 🔹 Revenue & Demand Insights
- Interactive filters:
  - Room type  
  - Weekend vs weekday stays  
- Dynamic KPIs and visual analytics  
- Revenue contribution and seasonal trends

#### 🔹 Revenue Forecasting
- ML-based revenue prediction using booking inputs  
- Scenario analysis:
  - Weekday vs weekend revenue impact  
- Confidence range visualization (conservative to optimistic)  
- Comparison with base (non-ML) revenue estimates

---

## 🛠️ Tools & Technologies
- **Programming Language:** Python  
- **Data Analysis:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn, Altair  
- **Machine Learning:** Scikit-learn  
- **Dashboard:** Streamlit  
- **Model Persistence:** Joblib  
- **Development:** Jupyter Notebook, GitHub Codespaces  

---

## 📊 Key Insights
- **Stay duration** is the strongest driver of revenue  
- **Dynamic pricing per day** has a greater impact than base room price alone  
- Premium room categories (Executive, Suite) contribute higher revenue but lower demand  
- Weekend stays show higher revenue potential compared to weekdays  
- Seasonal patterns influence bookings but are secondary to pricing and stay length  

---

## 🚀 Deployment
- The Streamlit dashboard is deployed on **Streamlit Community Cloud**
- Provides a **public, shareable URL** suitable for resumes and portfolios

🔗 **Live Dashboard:** *(URL:https://hotel-revenue-analytics-prediction-zlqmiyzrsqefaz3dxgyyfz.streamlit.app/)*

---

## 🔮 Future Enhancements
- Integrate real-world hotel booking datasets  
- Perform hyperparameter tuning for improved model accuracy  
- Add advanced forecasting techniques  
- Implement user authentication for role-based access  
- Extend deployment using **FastAPI + Streamlit** architecture

---

## 👩‍💻 Author
**Priyanka Pandiyan**  
*Data Scientist | NLP & Generative AI Enthusiast*


