# Visualization
import matplotlib.pyplot as plt
import seaborn as sns


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
    axs[0].set_ylabel('Co2 level')

    n_last =100
    axs[1].plot(train[-n_last:], label=train_label)
    axs[1].plot(test, label=test_label)
    axs[1].plot(forecast_recons, label=forecast_recons_label)
    axs[1].legend()
    axs[1].set_title('ZOOM on train data, test data and predictions')
    axs[1].set_xlabel('Date')
    axs[1].set_ylabel('Co2 level')
