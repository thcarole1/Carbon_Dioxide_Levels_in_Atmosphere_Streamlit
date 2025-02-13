import streamlit as st
import matplotlib.dates as mdates

# Visualization
import matplotlib.pyplot as plt


def plot_final_lstm(train, train_label,
                   test, test_label,
                   forecast_recons, forecast_recons_label):
    '''
    Plots the training data, the test data and the predictions from LSTM model.
    Outputs : All the data on left side, a zoomed plot on latest data on the right side.
    '''

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    axs[0].plot(train, label=train_label)
    axs[0].plot(test, label=test_label)
    axs[0].plot(forecast_recons, label=forecast_recons_label)
    axs[0].legend()
    axs[0].set_title('Train data, test data and predictions')
    axs[0].set_xlabel('Date')
    axs[0].set_ylabel('Co2 level (ppm)')

    n_last =100
    axs[1].plot(train[-n_last:], label=train_label)
    axs[1].plot(test, label=test_label)
    axs[1].plot(forecast_recons, label=forecast_recons_label)
    axs[1].legend()
    axs[1].set_title('ZOOM on train data, test data and predictions')
    axs[1].set_xlabel('Date')
    axs[1].set_ylabel('Co2 level (ppm)')

    # Set major ticks to show months and years only
    interval = 40
    axs[0].xaxis.set_major_locator(mdates.MonthLocator(interval=interval))  # Show every 2nd month
    axs[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format to show Year-Month
    axs[1].xaxis.set_major_locator(mdates.MonthLocator(interval=interval))  # Show every 2nd month
    axs[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format to show Year-Month

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(plt)



def plot_final_lstm_global(train, train_label,
                   test, test_label,
                   forecast_recons, forecast_recons_label):
    '''
    Plots the training data, the test data and the predictions from LSTM model.
    Outputs : All the data on left side, a zoomed plot on latest data on the right side.
    '''

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(train, label=train_label)
    ax.plot(test, label=test_label)
    ax.plot(forecast_recons, label=forecast_recons_label)
    ax.legend()
    ax.set_title('Train data, test data and predictions')
    ax.set_xlabel('Date')
    ax.set_ylabel('Co2 level (ppm)')

    # Set major ticks to show months and years only
    interval = 40
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=interval))  # Show every 2nd month
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format to show Year-Month

    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

def plot_final_lstm_zoom(train, train_label,
                   test, test_label,
                   forecast_recons, forecast_recons_label):
    '''
    Plots the training data, the test data and the predictions from LSTM model.
    Outputs : All the data on left side, a zoomed plot on latest data on the right side.
    '''

    fig, ax = plt.subplots(figsize=(10, 5))
    n_last =100
    ax.plot(train[-n_last:], label=train_label)
    ax.plot(test, label=test_label)
    ax.plot(forecast_recons, label=forecast_recons_label)
    ax.legend()
    ax.set_title('ZOOM on train data, test data and predictions')
    ax.set_xlabel('Date')
    ax.set_ylabel('Co2 level (ppm)')

    # Set major ticks to show months and years only
    interval = 40
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=interval))  # Show every 2nd month
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format to show Year-Month

    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
