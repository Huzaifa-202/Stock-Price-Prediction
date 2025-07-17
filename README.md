📈 Stock Price Prediction Using Machine Learning

🔹 Overview

This project predicts stock price movement (up or down) using multiple supervised machine learning algorithms. It includes detailed Exploratory Data Analysis (EDA), technical indicator-based feature engineering, and a Streamlit web interface for interactive predictions and visualization.

🔹 Key Features

Data Preprocessing & Cleaning – Handling missing values, duplicates, and outliers

Technical Indicators – RSI, MACD, EMA, Bollinger Bands, Momentum

Machine Learning Models – K-Nearest Neighbors (KNN), Logistic Regression, Gaussian Naive Bayes

EDA & Visualization – Trend graphs, heatmaps, and feature relationships

Interactive Web UI – Built with Streamlit for real-time prediction and EDA

Jupyter Notebook Analysis – In-depth research and visualization

🔹 Tech Stack

Languages: Python
Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit
Models: KNN, Logistic Regression, Gaussian Naive Bayes
Visualization: Streamlit, Matplotlib, Seaborn
Tools: Jupyter Notebook, VS Code, Git

🔹 Project Structure

Stock_Prediction_Project
• README.md – Project documentation
• frontend.py – Streamlit UI for EDA & prediction
• model_backend.py – ML logic and prediction functions
• eda_stock_analysis.ipynb – Detailed EDA and data visualization
• cleaned_stock_data.csv – Cleaned dataset (optional)
• requirements.txt – Required Python libraries
• .gitignore – Ignore venv & cache
• stock-prediction/ – Virtual environment (ignored in Git)

🔹 Installation and Setup

1. Clone the Repository
Clone this repository to your local machine.

2. Create Virtual Environment (Optional but Recommended)
Create and activate a Python virtual environment.

3. Install Required Libraries
Install all dependencies listed in requirements.txt.

4. Run Streamlit App
Run the Streamlit application to explore EDA and make predictions.

🔹 Usage

Launch the Streamlit app.

Upload your stock CSV dataset (or use sample data).

Explore interactive EDA – trend graphs, heatmaps, volume analysis.

Select a Machine Learning model (KNN, Logistic Regression, or Naive Bayes) to predict stock movement.

View model accuracy and predicted trend.

🔹 Screenshots

<img width="431" height="392" alt="heatmap" src="https://github.com/user-attachments/assets/45d9fa11-03ca-46f0-a013-60b708136d5a" />

<img width="382" height="239" alt="scatterplot" src="https://github.com/user-attachments/assets/8e7440b7-36d6-4f6d-b04f-b10754e346d1" />


<img width="374" height="370" alt="scatter_plot91" src="https://github.com/user-attachments/assets/fc9dbbcb-3913-40d5-ba92-14a55006c3a7" />


<img width="736" height="390" alt="trend" src="https://github.com/user-attachments/assets/aeffbfc8-05a4-491a-a346-0c96326e982a" />

<img width="358" height="377" alt="pie_chart" src="https://github.com/user-attachments/assets/7e8bb150-2585-4d34-b07b-d02cb921d5e2" />


<img width="435" height="339" alt="pca" src="https://github.com/user-attachments/assets/01cf8346-96eb-4ee8-8544-35f8481fa5c2" />


🔹 Future Improvements

Add LSTM or Transformer-based models for time-series forecasting

Integrate real-time stock data (Yahoo Finance or Alpha Vantage API)

Deploy as a FastAPI backend with Streamlit frontend for production
