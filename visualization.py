"""
Module for visualizing the data stream, EMA, and anomalies using Matplotlib.

This module provides functionality to generate a plot of the data stream, EMA values and flagged anomalies.
The visualization is optional and dependent on Matplotlib being available.
"""
try:
    import matplotlib.pyplot as plt
    mpl = True
except ImportError:
    mpl = False
    plt = None


def plot_results(values, ema_values, anomalies):
    """
    Plot the data stream, EMA, and detected anomalies.

    Args:
        values (list of float): The data stream values.
        ema_values (list of float): The EMA values corresponding to each data point.
        anomalies (dict): A dictionary containing the index and value of each detected anomaly.
    """
    if not mpl:
        print("Matplotlib is not installed. Skipping Visualization")
        return

    plt.figure(figsize=(12, 6))
    plt.plot(values, label='Data', color='blue')
    plt.plot(ema_values, label='EMA', color='green')
    plt.scatter(list(anomalies.keys()), list(anomalies.values()), color='red', label='Anomalies')
    plt.xlabel('Time Step')
    plt.ylabel('Value')
    plt.title('Data Stream with EMA Anomaly Detection')
    plt.legend()
    plt.show()
