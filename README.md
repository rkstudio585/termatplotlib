# termatplotlib

A lightweight and elegant Python library for rendering stunning ASCII plots directly in your terminal. Visualize your data with beautiful scatter, line, and bar charts, bringing the power of matplotlib to your command line.

## Features

*   **Terminal-based Visualization:** Generate plots directly in your terminal using ASCII characters.
*   **Multiple Chart Types:** Supports bar charts, scatter plots, line charts, pie charts, and histograms.
*   **Customization:** Options for titles, axis labels, colors, and markers.
*   **File Output:** Save your terminal plots to text files for sharing or later review.
*   **Easy to Use:** Simple API designed for quick and intuitive plotting.

## Installation

It is recommended to install `termatplotlib` using `pip` within a virtual environment.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
# .\venv\Scripts\activate

# Install termatplotlib
pip install termatplotlib
```

Alternatively, if you have cloned the repository, you can install it from the source:

```bash
pip install termatplotlib
```

## Usage

`termatplotlib` provides a simple API to create various types of plots.

### Bar Chart

```python
import termatplotlib as tpl

print("--- Example: Bar Chart ---")
labels = ["A", "B", "C", "D"]
values = [10, 20, 15, 5]
tpl.bar(labels, values, title="My Bar Chart", xlabel="Value", ylabel="Category", color="red")
```

### Scatter Plot

```python
import termatplotlib as tpl

print("--- Example: Scatter Plot ---")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 8, 9, 10, 8, 9]
data_scatter = [{'x': x, 'y': y, 'color': 'blue', 'marker': 'x'}]
tpl.scatter(data_scatter, title="My Scatter Plot", xlabel="X-Axis", ylabel="Y-Axis")
```

### Line Chart

```python
import termatplotlib as tpl

print("--- Example: Line Chart ---")
x_line = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_line = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
data_line = [{'x': x_line, 'y': y_line, 'color': 'green', 'marker': 'o'}]
tpl.line(data_line, title="My Line Chart", xlabel="X-Axis", ylabel="Y-Axis")
```

### Pie Chart

```python
import termatplotlib as tpl

print("--- Example: Pie Chart ---")
labels = ["A", "B", "C", "D"]
values = [10, 20, 15, 5]
tpl.pie(labels, values, title="My Pie Chart")
```

### Histogram

```python
import termatplotlib as tpl

print("--- Example: Histogram ---")
data_hist = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 7, 7, 7, 8, 9, 10]
tpl.hist(data_hist, bins=5, title="My Histogram", xlabel="Value Range", ylabel="Frequency", color="magenta")
```

### Saving to File

You can save any chart to a text file by providing the `output_file` argument (where supported).

```python
import termatplotlib as tpl

# Example: Bar chart saved to file
labels = ["E", "F", "G"]
values = [25, 10, 30]
tpl.bar(labels, values, title="Another Bar Chart", color="blue", output_file="bar_chart.txt")
```

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests on the [GitHub repository](https://github.com/rkstudio585/termatplotlib).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
