import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from model_backend import preprocess_data, train_and_predict

st.title("📈 Stock Price Prediction")

# Upload file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    data = preprocess_data(data)

    st.subheader("Cleaned Data Sample")
    st.write(data.head())

    # Heatmap
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(data.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # Model selection
    model_name = st.selectbox("Select Model", ["KNN", "Logistic Regression", "Naive Bayes"])
    if st.button("Run Model"):
        predictions, accuracy = train_and_predict(data, model_name)
        st.success(f"Model Accuracy: {accuracy*100:.2f}%")
        st.write(pd.DataFrame({"Actual": data['Label'][:20], "Predicted": predictions[:20]}))
else:
    st.info("Please upload a CSV file to continue.")
