
from sklearn.ensemble import IsolationForest
import numpy as np

## adapt isolation forest for continuous datastream 

class IsolationForestDetector:
    def __init__(self, contamination=0.01, window_size=50):
        """Initialize the Isolation Forest detector."""
        self.contamination = contamination  # Expected anomaly proportion
        self.window_size = window_size  # Number of recent points to consider
        self.model = IsolationForest(contamination=self.contamination, n_estimators=100)
        self.data = []

    def detect(self, value):
        """Detect anomalies using Isolation Forest."""
        self.data.append(value)

        # data not enough for anomaly prediction based on window size     
        if len(self.data) < self.window_size:
            return False  

        # Use the recent window of data points for model fitting
        window = np.array(self.data[-self.window_size:]).reshape(-1, 1)

        # predict if the last value is anomaly 
        self.model.fit(window)
        prediction = self.model.predict(window[-1].reshape(1, -1))

        return prediction[0] == -1  
