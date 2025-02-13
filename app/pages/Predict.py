# Import libraries
import streamlit as st
import pandas as pd
import requests
import urllib.parse
import zipfile


# Import from other py files
from display import plot_final_lstm, plot_final_lstm_global, plot_final_lstm_zoom

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
    test_df = pd.read_csv("data/csv_files/test_15percent.csv", index_col=None)
    st.dataframe(data = test_df.head())

# Get the predictions through API call
label_predict = "Predict excerpt values"
predict_button = st.button(label_predict)

if predict_button:
    # Define the path to your CSV file on disk
    csv_file_path = "data/csv_files/test_15percent.csv"  # Update with your actual file path

    # Read the CSV file from disk
    with open(csv_file_path, "r", encoding="utf-8") as f:
        csv_content = f.read()

    # URL-encode the CSV content so it can be safely transmitted as a query parameter
    encoded_csv = urllib.parse.quote(csv_content)

    # Define the API endpoint and parameters
    api_url = "https://co2levelsimage-scpwgaakrq-od.a.run.app/predict_csv"
    params = {"csv_data": encoded_csv}

    # Send the GET request
    response = requests.get(api_url, params=params)

    # *************************  Download ZIP file ****************************************
    # Check if the response contains a ZIP file
    if response.status_code == 200 and response.headers['Content-Type'] == 'application/zip':
        # Save the ZIP file
        with open("data/zip_files/API_response.zip", "wb") as file:
            file.write(response.content)
        print("ZIP file downloaded successfully!")
        st.write("Predictions computed successfully !")
    else:
        print("Failed to download the ZIP file or incorrect response.")
        st.write("Failed to download the ZIP file or incorrect response!")

    # ************************** Extract data from ZIP file ******************************
    # Open the ZIP file
    with zipfile.ZipFile("data/zip_files/API_response.zip", 'r') as zip_ref:
        # List all files within the ZIP
        file_list = zip_ref.namelist()
        print("Files in the ZIP:", file_list)

        # Extract all files to the current directory (optional)
        zip_ref.extractall('data/zip_files/extracted_data')
    # **************************************************************************

    # Display results
    # Retrieve train set
    csv_file_path = "data/csv_files/train_85percent.csv"  # Update with your actual file path
    train_df = pd.read_csv(csv_file_path, index_col=None)
    train_df['Year_Month'] = pd.to_datetime(train_df['Year_Month'])
    train_df= train_df.set_index('Year_Month')

    # Retrieve test set
    csv_file_path = "data/zip_files/extracted_data/y_test.csv"  # Update with your actual file path
    y_test = pd.read_csv(csv_file_path, index_col=None)
    y_test['Unnamed: 0'] = pd.to_datetime(y_test['Unnamed: 0'])
    y_test= y_test.set_index('Unnamed: 0')

    # Retrieve predictions
    csv_file_path = "data/zip_files/extracted_data/predictions.csv"  # Update with your actual file path
    predictions = pd.read_csv(csv_file_path, index_col=None)
    predictions['Unnamed: 0'] = pd.to_datetime(predictions['Unnamed: 0'])
    predictions= predictions.set_index('Unnamed: 0')

    # Display all the data (train, test and predictions)
    plot_final_lstm_global(train_df, "Carbon Dioxide (ppm)",
                            y_test, "test",
                            predictions, "predictions")

    # Display zoom of the data (train, test and predictions)
    plot_final_lstm_zoom(train_df, "Carbon Dioxide (ppm)",
                            y_test, "test",
                            predictions, "predictions")


    st.dataframe(data = y_test.tail())
    st.dataframe(data = predictions.tail())

    test_df = pd.read_csv("data/csv_files/test_15percent.csv", index_col=None)
    st.dataframe(data = test_df.tail())
