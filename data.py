"""
Provides a data stream that will be used for EMA anomaly detection.
"""

import math
import random
import time


def data_stream():
    """
    Simulates a data stream by generating values that incorporate regular patterns, seasonal elements, and random noise.
    The generated data values are based on a sine wave function for a regular pattern and seasonal value.
    Random noise and occasional anomalies are also added.


    Yields:
         float: the next value in data stream
    Exceptions:
        ValueError: If generated value is not within expected bounds
    """
    time_step = 0
    while True:
        try:
            # regular pattern is sine wave
            regular_value = 50 + 10 * math.sin(0.1 * time_step)

            # seasonal element is an additional sine wave
            seasonal_value = 5 * math.sin(0.05 * time_step)

            # random noise
            noise = random.uniform(-2, 2)
            # 5% chance to add larger noise
            if random.random() < 0.05:
                noise += random.uniform(-20, 20)

            value = regular_value + seasonal_value + noise

            # purposely introduce an anomaly
            if random.random() < 0.02:  # 2% chance of an anomaly
                # random spike or drop
                value += random.choice([random.uniform(20, 40), random.uniform(-40, -20)])

            # ensuring value is withing expected bounds
            if not (-100 <= value <= 200):
                raise ValueError(f"Generated value is out of expected bounds: {value}")

            # yield value to simulate streaming
            yield value

            time_step += 1

            # delay to simulate streaming
            time.sleep(0.1)

        except ValueError as ve:
            print(f"data validation failed: {ve}")
            # skip yielding this value

        except Exception as e:
            print(f"error: {e}")
            time_step += 1
            continue
