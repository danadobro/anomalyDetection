"""
Implements the Exponential Moving Average (EMA) based anomaly detection
"""


class EMA:

    # EMA stands for Exponential Moving Average
    def __init__(self, alpha=0.1, threshold=15, warmup_period=5):
        """
        Initialize the EMA anomaly detector.

        Args:
            alpha (float): Smoothing factor for EMA, must be between 0 and 1.
            threshold (float): Value deviation from EMA considered an anomaly.
            warmup_period (int): The amount of initial values used to calculate the initial EMA.

        Raises:
            ValueError: If alpha is not between 0 and 1, or if threshold is not positive.
        """

        if not (0 < alpha <= 1):
            raise ValueError("Alpha should be between 0 and 1")

        if threshold <= 0:
            raise ValueError("Threshold must be positive")

        self.alpha = alpha
        self.threshold = threshold
        self.ema = None
        self.warmup_period = warmup_period
        self.warmup_values = []

    def update(self, new_value):
        """
        Update the EMA with a new value and check if it's an anomaly

        Args:
            new_value (float): The latest value from the data stream

        Returns:
            tuple: (is_anomaly (bool), ema (float)) indicating whether the new value is an anomaly and the updated EMA
        """
        try:
            if not isinstance(new_value, (int, float)):
                # validate that input is a number
                raise TypeError(f"Invalid value type: {type(new_value)}")

            self.warmup_values.append(new_value)

            if len(self.warmup_values) <= self.warmup_period:
                # calculate the initial EMA using SMA of the first few values
                self.ema = sum(self.warmup_values) / len(self.warmup_values)
                return False, self.ema

            # update EMA after the warmup period
            self.ema = self.alpha * new_value + (1 - self.alpha) * self.ema

            # calculate if new value deviates significantly from the EMA
            deviation = abs(new_value - self.ema)
            is_anomaly = deviation > self.threshold
            return is_anomaly, self.ema

        except TypeError as te:
            print(f"error: {te}")
            # treat invalid values as not anomaly to continue
            return False, self.ema

        except Exception as e:
            print(f"error: {e}")
            return False, self.ema
