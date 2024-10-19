import numpy as np
import time

def generate_data_point(t):
    
    seasonal_component = 10 * np.sin(2 * np.pi * t / 50)  # Periodic wave
    noise = np.random.normal(0, 2)  # Random noise
    trend = 0.05 * t  # increasing trend
    return seasonal_component + noise + trend

def data_stream():
    """Simulate a continuous data stream."""
    t = 0
    while True:
        yield generate_data_point(t)
        t += 1
        time.sleep(1)  # Mimic real-time streaming
