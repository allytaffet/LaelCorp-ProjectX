import analytics.data_processing as dp
import analytics.visualization as vis
import analytics.reporting as rpt

def main():
    # Load and process data
    data = dp.load_data("data.csv")
    processed_data = dp.process_data(data)

    # Create visualizations
    vis.plot_histogram(processed_data)
    vis.plot_line_chart(processed_data)

    # Generate a report
    report = rpt.generate_report(processed_data)
    rpt.save_report(report, "data_report.pdf")

if __name__ == "__main__":
    main()
