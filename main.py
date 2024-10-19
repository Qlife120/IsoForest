import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
from detector import IsolationForestDetector
from data_stream import data_stream

def real_time_plot():
    plt.ion() 
    fig, ax = plt.subplots()
    line, = ax.plot([], [], 'b-', label='Data Stream')
    anomaly_points, = ax.plot([], [], 'ro', label='Anomalies')
    ax.legend()
    return fig, ax, line, anomaly_points

def update_plot(line, anomaly_points, x_data, y_data, anomalies):
    line.set_data(x_data, y_data)
    anomaly_points.set_data([x_data[i] for i in anomalies], [y_data[i] for i in anomalies])
    plt.xlim(max(0, x_data[-1] - 100), x_data[-1] + 10)
    plt.ylim(min(y_data) - 5, max(y_data) + 5)
    plt.pause(0.01)  

def main():
    detector = IsolationForestDetector(contamination=0.01, window_size=50)
    fig, ax, line, anomaly_points = real_time_plot()
    x_data, y_data, anomalies = [], [], []

    try:
        for t, value in enumerate(data_stream()):
            if detector.detect(value):
                anomalies.append(t)
            x_data.append(t)
            y_data.append(value)
            update_plot(line, anomaly_points, x_data, y_data, anomalies)
            fig.canvas.flush_events()
    except KeyboardInterrupt:
        print("Stream stopped by user.")

    plt.ioff()  
    plt.show()  

if __name__ == "__main__":
    main()
