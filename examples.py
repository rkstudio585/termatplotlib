import termatplotlib as tpl

# Example 1: Simple bar chart with title, labels, and color
print("--- Example 1: Enhanced Bar Chart ---")
labels1 = ["A", "B", "C", "D"]
values1 = [10, 20, 15, 5]
tpl.bar(labels1, values1, title="My Bar Chart", xlabel="Value", ylabel="Category", color="red")

# Example 2: Scatter plot with title, labels, color, and custom marker
print("--- Example 2: Enhanced Scatter Plot ---")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 8, 9, 10, 8, 9]
data_scatter = [{'x': x, 'y': y, 'color': 'blue', 'marker': 'x'}]
tpl.scatter(data_scatter, title="My Scatter Plot", xlabel="X-Axis", ylabel="Y-Axis")

# Example 3: Line chart with title, labels, color, and custom marker
print("--- Example 3: Enhanced Line Chart ---")
x_line = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_line = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
data_line = [{'x': x_line, 'y': y_line, 'color': 'green', 'marker': 'o'}]
tpl.line(data_line, title="My Line Chart", xlabel="X-Axis", ylabel="Y-Axis")

# Example 4: Pie chart
print("--- Example 4: Pie Chart ---")
labels4 = ["A", "B", "C", "D"]
values4 = [10, 20, 15, 5]
tpl.pie(labels4, values4, title="My Pie Chart")

# Example 5: Histogram
print("--- Example 5: Histogram ---")
data_hist = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 7, 7, 7, 8, 9, 10]
tpl.hist(data_hist, bins=5, title="My Histogram", xlabel="Value Range", ylabel="Frequency", color="magenta")

# Example 6: Scatter plot with numerical axis ticks and saving to file
print("--- Example 6: Scatter Plot with Numerical Axis Ticks (saved to file) ---")
x_ticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_ticks = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
data_scatter_file = [{'x': x_ticks, 'y': y_ticks, 'color': 'cyan', 'marker': '+'}]
tpl.scatter(data_scatter_file, title="Scatter Plot with Ticks", xlabel="X-Values", ylabel="Y-Values", output_file="scatter_plot.txt")

# Example 7: Line chart with numerical axis ticks and saving to file
print("--- Example 7: Line Chart with Numerical Axis Ticks (saved to file) ---")
x_line_file = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_line_file = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
data_line_file = [{'x': x_line_file, 'y': y_line_file, 'color': 'yellow', 'marker': '*'}]
tpl.line(data_line_file, title="Line Chart with Ticks", xlabel="X-Values", ylabel="Y-Values", output_file="line_plot.txt")

# Example 8: Bar chart saved to file
print("--- Example 8: Bar Chart (saved to file) ---")
labels8 = ["E", "F", "G"]
values8 = [25, 10, 30]
tpl.bar(labels8, values8, title="Another Bar Chart", color="blue", output_file="bar_chart.txt")

# Example 9: Pie chart saved to file
print("--- Example 9: Pie Chart (saved to file) ---")
labels9 = ["X", "Y", "Z"]
values9 = [40, 30, 30]
tpl.pie(labels9, values9, title="Another Pie Chart")

# Example 10: Histogram saved to file
print("--- Example 10: Histogram (saved to file) ---")
data_hist_file = [10, 12, 12, 15, 15, 15, 18, 20, 20, 22, 25]
tpl.hist(data_hist_file, bins=4, title="Another Histogram", color="green")
