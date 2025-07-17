📈 Stock Price Prediction using Machine Learning
🔹 Overview
This project predicts stock price movement (up or down) using multiple Machine Learning algorithms:

K-Nearest Neighbors (KNN)

Logistic Regression

Gaussian Naive Bayes

It also includes Exploratory Data Analysis (EDA), technical indicator feature engineering (RSI, MACD, EMA, Bollinger Bands, Momentum, etc.), and an interactive Streamlit-based UI for predictions and visualization.

🔹 Features
✔ Data Cleaning & Preprocessing – Handling missing values, duplicates, and outliers.
✔ EDA & Visualization – Heatmaps, scatter plots, moving averages, and trend analysis.
✔ Technical Indicators – RSI, MACD, EMA, Bollinger Bands for better predictive performance.
✔ Model Comparison – KNN, Logistic Regression, Naive Bayes with accuracy scores.
✔ Interactive Streamlit UI – Upload CSV, explore EDA interactively, and predict stock trends.

🔹 Tech Stack
Programming Language: Python
Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
ML Models: KNN, Logistic Regression, Gaussian Naive Bayes
Visualization: Matplotlib, Seaborn
Frontend (UI): Streamlit
Development Tools: Jupyter Notebook, VS Code, Git

🔹 Project Structure
📂 Stock_Prediction_Project
│── .gitignore (Ignore virtual environment & cache)
│── requirements.txt (Required Python packages)
│── frontend.py (Streamlit app for EDA & predictions)
│── model_backend.py (ML model training & prediction logic)
│── eda_stock_analysis.ipynb (Detailed EDA in Jupyter)
│── cleaned_stock_data.csv (Cleaned/preprocessed data - optional)
│── README.md (Project documentation)
│── stock-prediction/ (Virtual environment - ignored in Git)

🔹 Installation & Setup
Clone the Repository
git clone https://github.com/your-username/stock-price-prediction.git
cd stock-price-prediction

Create Virtual Environment (Optional but Recommended)
Windows:
python -m venv stock-prediction
stock-prediction\Scripts\activate

Mac/Linux:
python3 -m venv stock-prediction
source stock-prediction/bin/activate

Install Required Libraries
If you have a requirements.txt:
pip install -r requirements.txt

If not:
pip install pandas numpy scikit-learn matplotlib seaborn streamlit

Run Streamlit App
streamlit run frontend.py

🔹 Usage
Launch the Streamlit app using the above command.

Upload your stock CSV dataset (or use sample data).

Explore interactive EDA (trend graphs, heatmaps, volume analysis).

Select the ML model (KNN, Logistic Regression, or Naive Bayes) to predict stock movement.

View model accuracy & predicted trend.

🔹 Screenshots of EDA

<img width="360" height="324" alt="heatmap" src="https://github.com/user-attachments/assets/bf84f6ea-a834-4158-933f-1993bb1af445" />
<img width="382" height="239" alt="scatterplot" src="https://github.com/user-attachments/assets/2c5a3295-c36c-4572-9b95-9301303fa144" />
<img width="374" height="370" alt="scatter_plot91" src="https://github.com/user-attachments/assets/aa3d4387-1daa-4ff5-bf71-c8698177055e" />
<img width="736" height="390" alt="trend" src="https://github.com/user-attachments/assets/a1ee0458-4e4f-4168-8952-14d79c491f39" />
<img width="358" height="377" alt="pie_chart" src="https://github.com/user-attachments/assets/fb8e5779-57c6-4ab8-b8d4-87e176a4bb15" />
<img width="738" height="384" alt="MA VALUES" src="https://github.com/user-attachments/assets/d5e207f1-1896-4b7a-9ab0-c8d1391d49ba" />

🔹 Future Improvements
Add LSTM or Transformer-based models for better time-series forecasting.

Integrate real-time stock data (Yahoo Finance / Alpha Vantage API).

Deploy as a FastAPI backend + Streamlit frontend for production.

🔹 Author
👤 Huzaifa Asad
AI/ML Engineer | Data Scientist
📧 huzaifaasad4838@gmail.com
GitHub: https://github.com/huzaifa-asad
LinkedIn: https://www.linkedin.com/in/huzaifa-asad-742988288/
