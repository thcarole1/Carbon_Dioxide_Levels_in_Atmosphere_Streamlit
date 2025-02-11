# Import libraries
import streamlit as st
import pandas as pd
import requests
import urllib.parse

# Load custom CSS
with open("app/css/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
"""
    <h1>CO2 levels prediction </h1>
    <h2> Predictions </h2>
    Let's predict the co2 levels based on unseen values !<br><br>
    """,
    unsafe_allow_html=True
)

# Loading excerpt dataset of test values
label ="Load dataset excerpt"
load_button = st.button(label)

if load_button:
    st.write("We only show the first rows of our excerpt.")
    test_df = pd.read_csv("data/test_15percent.csv", index_col=None)
    st.dataframe(data = test_df.head(), hide_index=True)


# Get the predictions through API call
label_predict = "Predict excerpt values"
predict_button = st.button(label_predict)

if predict_button:
    # Define the path to your CSV file on disk
    csv_file_path = "data/test_15percent.csv"  # Update with your actual file path

    # Read the CSV file from disk
    with open(csv_file_path, "r", encoding="utf-8") as f:
        csv_content = f.read()

    # URL-encode the CSV content so it can be safely transmitted as a query parameter
    encoded_csv = urllib.parse.quote(csv_content)

    # Define the API endpoint and parameters
    api_url = "https://co2levelsimage-scpwgaakrq-od.a.run.app/predict"
    params = {"csv_data": encoded_csv}

    # Send the GET request
    response = requests.get(api_url, params=params)

    # Check and display the response
    if response.ok:
        st.success("CSV file sent successfully!")
        st.write(response.json())
    else:
        st.error("Failed to send CSV file")
        st.write("Status code:", response.status_code)
        st.write(response.text)
