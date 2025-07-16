
import math

COLORS = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'reset': '\033[0m'
}

def bar(labels, values, max_width=80, title=None, xlabel=None, ylabel=None, color=None, output_file=None):
    """
    Displays a horizontal bar chart in the terminal.
    """
    output = []
    if title:
        output.append(f"\n{title.center(max_width)}\n")

    if not labels or not values or len(labels) != len(values):
        if output_file:
            with open(output_file, 'w') as f:
                f.write("Error: Invalid input. Labels and values must be non-empty and of the same length.\n")
        else:
            print("Error: Invalid input. Labels and values must be non-empty and of the same length.")
        return

    max_label_len = max(len(str(label)) for label in labels)
    max_value = max(values)
    scale = (max_width - max_label_len - 5) / max_value

    color_code = COLORS.get(color, '')
    reset_code = COLORS['reset'] if color_code else ''

    if ylabel:
        output.append(f"{ylabel.rjust(max_label_len)}")

    for i, (label, value) in enumerate(zip(labels, values)):
        bar_len = int(value * scale)
        bar = '█' * bar_len
        output.append(f"{str(label):<{max_label_len}} | {color_code}{bar}{reset_code} {value}")

    if xlabel:
        output.append(f"\n{xlabel.center(max_width)}")

    if output_file:
        with open(output_file, 'w') as f:
            f.write("\n".join(output) + "\n")
    else:
        print("\n".join(output))


def scatter(data, width=50, height=20, title=None, xlabel=None, ylabel=None, output_file=None, color=None):
    """
    Displays a scatter plot in the terminal with multiple series.
    data: A list of dictionaries, where each dictionary represents a series
          and contains 'x', 'y', 'color', and 'marker' keys.
    """
    output = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    all_x = [val for series in data for val in series['x']]
    all_y = [val for series in data for val in series['y']]

    if not all_x or not all_y:
        if output_file:
            with open(output_file, 'w') as f:
                f.write("Error: Input data cannot be empty.\n")
        else:
            print("Error: Input data cannot be empty.")
        return

    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)

    x_range = max_x - min_x
    y_range = max_y - min_y

    grid = [[' ' for _ in range(width)] for _ in range(height)]

    for series in data:
        x = series['x']
        y = series['y']
        color = series.get('color')
        marker = series.get('marker', '*')

        color_code = COLORS.get(color, '')
        reset_code = COLORS['reset'] if color_code else ''

        for i in range(len(x)):
            x_scaled = int(((x[i] - min_x) / x_range) * (width - 1)) if x_range != 0 else 0
            y_scaled = int(((y[i] - min_y) / y_range) * (height - 1)) if y_range != 0 else 0
            grid[height - 1 - y_scaled][x_scaled] = color_code + marker + reset_code

    # Add y-axis labels
    y_label_width = len(f"{max_y:.1f}") + 2  # Max width for y-axis labels, assuming one decimal place

    # Create a new grid that includes space for y-axis labels
    display_grid = [[' ' for _ in range(width + y_label_width)] for _ in range(height)]

    for r in range(height):
        y_val = min_y + (height - 1 - r) * (y_range / (height - 1) if height > 1 else 1)
        if r % (height // 5 if height >= 5 else 1) == 0 or r == 0 or r == height - 1:  # Print ~5 ticks and ends
            label = f"{y_val:.1f}"
            for i, char in enumerate(label):
                if i < y_label_width:
                    display_grid[r][i] = char
        
        # Copy the plot content to the display grid
        for c in range(width):
            display_grid[r][c + y_label_width] = grid[r][c]

    output.append('+' + '-' * (width + y_label_width) + '+')
    for row in display_grid:
        output.append('|' + ''.join(row) + '|')
    output.append('+' + '-' * (width + y_label_width) + '+')

    # Add x-axis labels
    x_tick_interval = x_range / (width - 1) if width > 1 else 1
    x_labels_line = [" "] * (width + y_label_width)
    for c in range(width):
        x_val = min_x + c * x_tick_interval
        if c % (width // 5 if width >= 5 else 1) == 0 or c == 0 or c == width - 1: # Print ~5 ticks and ends
            label = f"{x_val:.1f}"
            # Ensure label fits and doesn't overwrite other labels
            if c + y_label_width + len(label) < len(x_labels_line):
                for i, char in enumerate(label):
                    x_labels_line[c + y_label_width + i] = char
    output.append(''.join(x_labels_line))

    if xlabel:
        output.append(f"\n{xlabel.center(width + y_label_width)}")
    output.append("\n")

    if output_file:
        with open(output_file, 'w') as f:
            f.write("\n".join(output) + "\n")
    else:
        print("\n".join(output))


def line(data, width=50, height=20, title=None, xlabel=None, ylabel=None, output_file=None, color=None):
    """
    Displays a line chart in the terminal with multiple series.
    data: A list of dictionaries, where each dictionary represents a series
          and contains 'x', 'y', 'color', and 'marker' keys.
    """
    output = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    all_x = [val for series in data for val in series['x']]
    all_y = [val for series in data for val in series['y']]

    if not all_x or not all_y:
        if output_file:
            with open(output_file, 'w') as f:
                f.write("Error: Input data cannot be empty.\n")
        else:
            print("Error: Input data cannot be empty.")
        return

    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)

    x_range = max_x - min_x
    y_range = max_y - min_y

    grid = [[' ' for _ in range(width)] for _ in range(height)]

    for series in data:
        x = series['x']
        y = series['y']
        color = series.get('color')
        marker = series.get('marker', '*')

        color_code = COLORS.get(color, '')
        reset_code = COLORS['reset'] if color_code else ''

        def plot_line(x0, y0, x1, y1):
            dx = abs(x1 - x0)
            dy = -abs(y1 - y0)
            sx = 1 if x0 < x1 else -1
            sy = 1 if y0 < y1 else -1
            err = dx + dy

            while True:
                if 0 <= y0 < height and 0 <= x0 < width:
                    grid[y0][x0] = color_code + marker + reset_code
                if x0 == x1 and y0 == y1:
                    break
                e2 = 2 * err
                if e2 >= dy:
                    err += dy
                    x0 += sx
                if e2 <= dx:
                    err += dx
                    y0 += sy

        scaled_points = []
        for i in range(len(x)):
            x_scaled = int(((x[i] - min_x) / x_range) * (width - 1)) if x_range != 0 else 0
            y_scaled = int(((y[i] - min_y) / y_range) * (height - 1)) if y_range != 0 else 0
            scaled_points.append((x_scaled, height - 1 - y_scaled))

        for i in range(len(scaled_points) - 1):
            plot_line(scaled_points[i][0], scaled_points[i][1], scaled_points[i+1][0], scaled_points[i+1][1])

    # Add y-axis labels
    y_label_width = len(f"{max_y:.1f}") + 2  # Max width for y-axis labels, assuming one decimal place

    # Create a new grid that includes space for y-axis labels
    display_grid = [[' ' for _ in range(width + y_label_width)] for _ in range(height)]

    for r in range(height):
        y_val = min_y + (height - 1 - r) * (y_range / (height - 1) if height > 1 else 1)
        if r % (height // 5 if height >= 5 else 1) == 0 or r == 0 or r == height - 1:  # Print ~5 ticks and ends
            label = f"{y_val:.1f}"
            for i, char in enumerate(label):
                if i < y_label_width:
                    display_grid[r][i] = char
        
        # Copy the plot content to the display grid
        for c in range(width):
            display_grid[r][c + y_label_width] = grid[r][c]

    output.append('+' + '-' * (width + y_label_width) + '+')
    for row in display_grid:
        output.append('|' + ''.join(row) + '|')
    output.append('+' + '-' * (width + y_label_width) + '+')

    # Add x-axis labels
    x_tick_interval = x_range / (width - 1) if width > 1 else 1
    x_labels_line = [" "] * (width + y_label_width)
    for c in range(width):
        x_val = min_x + c * x_tick_interval
        if c % (width // 5 if width >= 5 else 1) == 0 or c == 0 or c == width - 1: # Print ~5 ticks and ends
            label = f"{x_val:.1f}"
            # Ensure label fits and doesn't overwrite other labels
            if c + y_label_width + len(label) < len(x_labels_line):
                for i, char in enumerate(label):
                    x_labels_line[c + y_label_width + i] = char
    output.append(''.join(x_labels_line))

    if xlabel:
        output.append(f"\n{xlabel.center(width + y_label_width)}")
    output.append("\n")

    if output_file:
        with open(output_file, 'w') as f:
            f.write("\n".join(output) + "\n")
    else:
        print("\n".join(output))

def pie(labels, values, radius=10, title=None, legend=True):
    """
    Displays a pie chart in the terminal.
    """
    if title:
        print(f"\n{title.center(radius * 2)}\n")

    if not labels or not values or len(labels) != len(values):
        print("Error: Invalid input. Labels and values must be non-empty and of the same length.")
        return

    total = sum(values)
    proportions = [v / total for v in values]
    colors = list(COLORS.keys())[:-1]  # Exclude 'reset'

    grid = [[' ' for _ in range(radius * 2)] for _ in range(radius * 2)]
    center_x, center_y = radius, radius

    start_angle = 0
    for i, prop in enumerate(proportions):
        end_angle = start_angle + prop * 2 * math.pi
        color = COLORS[colors[i % len(colors)]]

        for y in range(radius * 2):
            for x in range(radius * 2):
                dx, dy = x - center_x, y - center_y
                angle = math.atan2(dy, dx)
                if angle < 0:
                    angle += 2 * math.pi

                if dx**2 + dy**2 <= radius**2:
                    if start_angle <= angle < end_angle:
                        grid[y][x] = color + '█' + COLORS['reset']

        start_angle = end_angle

    for row in grid:
        print(''.join(row))

    if legend:
        print("\nLegend:")
        for i, label in enumerate(labels):
            color = COLORS[colors[i % len(colors)]]
            print(f"{color}█{COLORS['reset']} {label}: {values[i]} ({proportions[i]:.1%})")
    print("\n")


def hist(data, bins=10, width=80, height=10, title=None, xlabel=None, ylabel=None, color=None, char='█'):
    """
    Displays a histogram in the terminal.
    """
    if title:
        print(f"\n{title.center(width)}\n")

    if not data:
        print("Error: Input data cannot be empty.")
        return

    min_val, max_val = min(data), max(data)
    if min_val == max_val:
        print("Error: All data points are the same, cannot create meaningful bins.")
        return

    bin_range = (max_val - min_val) / bins
    counts = [0] * bins
    bin_edges = [min_val + i * bin_range for i in range(bins + 1)]

    for x in data:
        if x == max_val:  # Include max_val in the last bin
            counts[bins - 1] += 1
        else:
            for i in range(bins):
                if bin_edges[i] <= x < bin_edges[i+1]:
                    counts[i] += 1
                    break

    max_count = max(counts)
    if max_count == 0:
        print("No data points fell into any bin.")
        return

    scale = height / max_count

    color_code = COLORS.get(color, '')
    reset_code = COLORS['reset'] if color_code else ''

    # Print the histogram bars
    for h in range(height - 1, -1, -1):
        row_str = ""
        for i in range(bins):
            if counts[i] * scale > h:
                row_str += color_code + char + reset_code + " " * (width // bins - 1)
            else:
                row_str += " " * (width // bins)
        print(row_str)

    # Print x-axis labels (bin edges)
    print("-" * width)
    bin_labels = [f"{edge:.1f}" for edge in bin_edges]
    label_spacing = width // bins
    label_line = ""
    for i in range(bins):
        label = bin_labels[i]
        label_line += label.ljust(label_spacing)[:label_spacing]
    print(label_line)

    if xlabel:
        print(f"\n{xlabel.center(width)}")
    if ylabel:
        print(f"{ylabel.rjust(10)} (count)")
    print("\n")
