# Import libraries
import streamlit as st

# Load custom CSS
with open("app/css/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Explanation of the purpose of this app
st.markdown(
    """
    <h1>CO2 levels prediction </h1>
    <h2> Framing the problem </h2>
    <h3> What is the business objective?</h3>
    We need to help organizations meet emission standards and comply with regulations.

    The applications are: <br>
    - Forecast emissions trends to ensure compliance with future regulations.<br>
    - Generate reports for governments or stakeholders showcasing emission reduction efforts.<br>
    - Aid in carbon trading by quantifying emission reductions.<br>

    <h3> What is the type of learning?</h3>
    With the gathered information, we are ready to design our system.<br>
    This is a <b>time series forecasting</b> task.<br>
    With the gathered information, we are ready to design our system.<br>

    <h3> What is the current solution?</h3>
    Predicting carbon dioxide (CO₂) levels is a critical task for environmental monitoring and climate action.
    Based on the data at hand, which likely includes historical CO₂ emissions and time, several existing solutions and approaches can be applied to predict CO₂ levels.<br><br>
    Here’s an overview:

    <h4>Statistical and Classical Time Series Models</h4>
    These models are well-suited for datasets with clear temporal patterns and trends:
    <h4>Autoregressive Integrated Moving Average (ARIMA)</h4>
    • <b>Description</b>: A classical time series model used to predict CO₂ levels based on past values.<br>
    • <b>Use Case</b>: Suitable for linear trends and seasonality in CO₂ emissions.

    • <b>Advantages</b>:
    - Good for stationary data.
    - Provides interpretable coefficients.

    • <b>Challenges</b>:
    - May not handle complex patterns or external factors well.

    <h4>Deep Learning Models</h4>
    Deep learning methods are powerful for capturing complex patterns in large datasets.
    <h4>Long Short-Term Memory Networks (LSTMs)</h4>
    • <b>Description</b>: A type of recurrent neural network (RNN) designed for sequential data, ideal for time series forecasting.<br>
    • <b>Use Case</b>: Predicts future CO₂ levels by learning long-term dependencies in emission trends.<br>

    • <b>Advantages</b>:
    - Handles temporal dependencies well.
    - Works with non-linear trends.

    • <b>Challenges</b>:
    - Computationally intensive and requires large datasets.

    <h2> Selecting a performance measure </h2>
    The next step is to choose a performance measure:

    • <b>Short-term predictions</b>: Use MAE, RMSE, or MASE for clear and interpretable results.<br>
    • <b>Scale-independent metrics</b>: Use MAPE, sMAPE, or Theil’s U for datasets with varying scales or multiple regions.

    We'll focus on:
    <h3>Mean Absolute Error (MAE)</h3>

    • <b>Description</b>: The average of absolute differences between actual and predicted values.<br>
    • <b>Formula</b>:
    """,
    unsafe_allow_html=True
    )

st.latex(r'''
         MAE  = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|
         ''')
st.markdown(
    """
    • <b>Use Case</b>:
    - Easy to interpret as it represents the average error in the same unit as the data (e.g., metric tons of CO₂).
    - Sensitive to the scale of the data but not overly penalized by large errors.

    <h3>Mean Squared Error (MSE)</h3>
    • <b>Description</b>: The average of squared differences between actual and predicted values.<br>
    • <b>Formula</b>:
""",
    unsafe_allow_html=True
)

st.latex(r'''
        MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
         ''')

st.markdown(
    """
    • <b>Use Case</b>:
    - Penalizes large errors more heavily than MAE.
    - Useful for models where large prediction deviations are particularly undesirable.

    <h3>Root Mean Squared Error (RMSE)</h3>
    • <b>Description</b>: The square root of MSE, representing the error in the same units as the original data.<br>
    • <b>Formula</b>:
    """,
    unsafe_allow_html=True
)
st.latex(r'''
         RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
         ''')

st.markdown(
    """
    • <b>Use Case</b>:
    - Highlights significant prediction errors.
    - Popular in time series forecasting due to interpretability.


    <h3>Mean Absolute Percentage Error (MAPE)</h3>
    • <b>Description</b>: The average percentage error between actual and predicted values.<br>
    • <b>Formula</b>:
    """,
    unsafe_allow_html=True
)

st.latex(r'''
         MAPE=\frac{1}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right| \times 100
         ''')

st.markdown(
    """
    • <b>Use Case</b>:
    - Provides a percentage-based measure, making it scale-independent.
    - Becomes problematic when actual values are near zero (dividing by zero).
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h3>We are now ready to forecast emissions trends to ensure compliance with future regulations.</h3>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """ <h1> Let's go ! </h1>""",
    unsafe_allow_html=True
)
