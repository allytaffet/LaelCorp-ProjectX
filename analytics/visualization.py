import matplotlib.pyplot as plt

def plot_histogram(data):
    """
    Create and display a histogram of the processed data.
    """
    # Implementation to create a histogram using matplotlib
    plt.hist(data, bins=10, color='blue', alpha=0.7)
    plt.title("Data Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

def plot_line_chart(data):
    """
    Create and display a line chart of the processed data over time.
    """
    # Implementation to create a line chart using matplotlib
    plt.plot(range(len(data)), data, marker='o', color='green')
    plt.title("Data Line Chart")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.show()
