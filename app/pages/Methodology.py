# Import libraries
import streamlit as st
import pandas as pd

# Load custom CSS
with open("app/css/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
"""
    <h1>CO2 levels prediction </h1>
    <h2> Specific issues and objectives </h2>

    <h3> Nature of the problem </h3>
    We want to forecast the CO2 levels in the atmosphere based on a times series dataset.<br>

    <h2> Data analysis </h2>
    Let's look at the data at hand: <br>
    """,
    unsafe_allow_html=True
)

st.image("data/figures/co2_levels_raw.png", caption="co2 levels dataset", output_format='PNG')

st.markdown(
"""
    Let's look at some statistic relevant info: <br>
    """,
    unsafe_allow_html=True
)

st.image("data/figures/co2_levels_visuals.png", caption="co2 levels statistics", output_format='PNG')

st.markdown(
"""
    After some data preprocessing, we will comparer the performance of an **ARIMA model** and a **LSTM model**.
    <h2> Model Comparison </h2>
    <h2> Cross validation of ARIMA model (CV = 5)</h2>
    """,
    unsafe_allow_html=True
)
st.image("data/figures/cross_arima_1.png", caption="Cross validation on ARIMA model (CV :1)", output_format='PNG')
st.image("data/figures/cross_arima_2.png", caption="Cross validation on ARIMA model (CV :2)", output_format='PNG')
st.image("data/figures/cross_arima_3.png", caption="Cross validation on ARIMA model (CV :3)", output_format='PNG')
st.image("data/figures/cross_arima_4.png", caption="Cross validation on ARIMA model (CV :4)", output_format='PNG')
st.image("data/figures/cross_arima_5.png", caption="Cross validation on ARIMA model (CV :5)", output_format='PNG')


st.markdown(
"""
    <h2> Cross validation of LSTM model (CV = 5)</h2>
    """,
    unsafe_allow_html=True
)
st.image("data/figures/cross_lstm_1.png", caption="Cross validation on LSTM model (CV :1)", output_format='PNG')
st.image("data/figures/cross_lstm_2.png", caption="Cross validation on LSTM model (CV :2)", output_format='PNG')
st.image("data/figures/cross_lstm_3.png", caption="Cross validation on LSTM model (CV :3)", output_format='PNG')
st.image("data/figures/cross_lstm_4.png", caption="Cross validation on LSTM model (CV :4)", output_format='PNG')
st.image("data/figures/cross_lstm_5.png", caption="Cross validation on LSTM model (CV :5)", output_format='PNG')

st.markdown(
"""
    <h2> Cross validation results</h2>
    Let's compute different metrics for each model AFTER CROSS VALIDATION (cv=5) : <br><br>
    """,
    unsafe_allow_html=True
)

compare_metrics = pd.read_csv("data/csv_files/metrics_df.csv", index_col=None)
st.dataframe(data = compare_metrics)

st.markdown(
"""
    The **LSTM model** has the **lowest mean MAPE**, as well as for the other metrics.<br>
    Let's use the **LSTM model** for our application.

    Let's manipulate our final LSTM model in the prediction pages.
""",
    unsafe_allow_html=True
)


# from pathlib import Path
# file_path = Path("data/piechart_Personal_Loan.png").resolve()
# st.write(f"Resolved path: {file_path}")
# st.image(file_path, caption="Target (i.e Personal_Loan) imbalance", output_format='PNG')
# st.image("data/piechart_Personal_Loan.png", caption="Target (i.e Personal_Loan) imbalance", output_format='PNG')

# st.markdown(
# """
# Models must be robust to this or require rebalancing techniques (e.g., <b>SMOTE</b>, class weighting). <br><br>
# In our particular case, before traininga any model, we will : <br>
# - Stratify our train set and our test set,
# - Oversample the minority label with **SMOTE**, **ONLY** on the train set.
#     """,
#     unsafe_allow_html=True
# )

# st.markdown(
# """
#     <h3> Features </h3>
#     - Categorical features (e.g., Family size, Education level).<br><br>
#     """,
#     unsafe_allow_html=True
# )

# st.image("data/count_plots_Categorical.png", caption="Examples of categorical features")

# st.markdown(
# """
#     - Numerical features (e.g., income, average credit card spending).<br><br>
#     """,
#     unsafe_allow_html=True
# )
# st.image("data/hist_plots_Numerical.png", caption="Examples of numerical features")

# st.markdown(
# """
#     <h3> Correlation between features </h3>
#     """,
#     unsafe_allow_html=True
# )
# st.image("data/correlation_numerical.png", caption="Correlation between numerical features")


# st.markdown(
# """
#     <h2> Model comparison </h2>

#     <h3> Confusion matrix </h3>
#     Let's plot the confusion matrix for each classification model we want to train : <br><br>
#     """,
#     unsafe_allow_html=True
# )
# st.image("data/confusion_matrixes.png", caption="Confusion matrix for each selected classification model")

# st.markdown(
# """
#     <h3> Cross validation </h3>
#     Let's plot different metrics for each classification model we want to train <b>AFTER CROSS VALIDATION</b> (cv = 20) : <br><br>
#     """,
#     unsafe_allow_html=True
# )

# compare_metrics = pd.read_csv("data/compare_metrics.csv")
# st.dataframe(data = compare_metrics, hide_index=True)

# st.markdown(
# """
#     **XGBClassifier** has the **best recall**, **best precision**  and **best F1 score**.
#     """,
#     unsafe_allow_html=True
# )

# st.markdown(
# """
#     <h2> Explainability of the model</h2>
#     After fine-tuning our <b>XGBClassifier</b> through <b>Random Grid Search</b>, we perform <b>feature permutation importance</b> technique to evaluate the importance of individual features (or predictors) in a predictive model. It provides a measure of how much
#     a model's performance is affected when the values of a particular feature are randomly shuffled, effectively breaking any
#     relationship between that feature and the target variable.<br><br>
#     """,
#     unsafe_allow_html=True
# )
# st.image("data/feature_permutation_importance.png", caption="Feature permutation importance based on F1 score")

# st.markdown(
# """
#     <h2> Final validation </h2>
#     Let's check the model performance on a test set not used during training.<br><br>
#     """,
#     unsafe_allow_html=True
# )
# st.image("data/confusion_matrix_final_model.png", caption="Final validation with test set")

# st.markdown(
# """
#     With this model, we can achieve (<b>on class 1</b>):
#     - <b>96%</b> recall
#     - <b>80%</b> precision .
#     - <b>87%</b> for F1 score. <br><br>
#     """,
#     unsafe_allow_html=True
# )
