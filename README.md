🩺 Diabetes Prediction using Machine Learning

💡 Project Overview:

This project aims to build a machine learning model to predict the likelihood of diabetes in individuals based on medical features. It covers the full data analysis pipeline, including data cleaning, visualization, model training, evaluation, and finally deployment through a simple web interface where users can input data and receive predictions.


---

📊 Steps:

1. Data Collection

Dataset used: Pima Indians Diabetes Dataset (Kaggle)



2. Data Cleaning & Preprocessing

Handled missing values and zeros in critical columns such as Glucose, BMI, Blood Pressure.

Converted data types and ensured consistency.



3. Exploratory Data Analysis (EDA)

Used pandas, matplotlib, and seaborn to:

Understand feature distributions.

Check correlations with diabetes outcomes.

Create clear visualizations (heatmaps, pairplots, histograms).




4. Model Building

Trained multiple models: Logistic Regression, Random Forest, Decision Tree.

Performed train-test split and cross-validation.

Evaluated models using accuracy, precision, recall, F1-score.



5. Deployment

Built an interactive app using Streamlit.

Users can input their medical info and receive real-time prediction results.





---

🌐 Live App

Try the web app here:
🔗  (http://localhost:8501/)


---

⚙️ Tools & Technologies:

Python

pandas, numpy, scikit-learn

matplotlib, seaborn

Streamlit (for web deployment)



---

📌 Key Insights:

The most influential factors in predicting diabetes were Glucose, BMI, and Age.

The model reached an accuracy of ~80%, making it a useful assistant in early detection.
