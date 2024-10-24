"""
Main script for detecting anomalies using the EMA (Exponential Moving Average) algorithm.

This script processes a data stream and detects anomalies based on deviation from the calculated EMA.
It also includes optional visualization functionality if matplotlib is installed.
"""
from data import data_stream
from anomaly_detection import EMA

# Attempt to import plot_results from visualization.py
try:
    from visualization import plot_results
    visualization_available = True
except ImportError:
    visualization_available = False
    plot_results = None

plot_enabled = False
if visualization_available:
    plot_enabled = True

# Initializing the EMA anomaly detector
alpha = 0.1
threshold = 15
detector = EMA(alpha=alpha, threshold=threshold, warmup_period=5)

data = data_stream()

# these are for visualization
values = []
ema_values = []
anomalies = {}

# detect anomalies in the data stream
for _ in range(200):
    """
    Iterates over the data stream to detect anomalies using EMA.

    For each value in the data stream, the EMA is updated, and if the difference between the
    current value and the EMA exceeds a set threshold, it is flagged as an anomaly.
    """
    try:
        value = next(data)
        is_anomaly, ema = detector.update(value)

        # append value for visualization
        values.append(value)

        if is_anomaly:
            anomalies[_] = value
            print(f"Value {_}: {value:.2f} (Anomaly Detected)")
        else:
            ema_values.append(ema)
            print(f"Value {_}: {value:.2f} (EMA:{ema:.2f})")

    except Exception as e:
        print(f"error in main: {e}")
        continue

# Plot the results if the visualization is available
if plot_enabled:
    """
    Plots the results of the data stream, EMA, and anomalies if visualization
    is available and the plot flag is set to True.
    """
    plot_results(values, ema_values, anomalies)
