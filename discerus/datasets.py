import matplotlib.pyplot as plt
import numpy as np

def plot_dataset(dataframe, title="", output=False, color=None):
    # How many features are there to visualise?
    feature_count = len(dataframe.columns)
    if output: feature_count -= 1

    if feature_count == 1:
        # Just show distribution
        render_distribution(plt, dataframe, output)
        plt.show()
    elif feature_count == 2:
        # Plot two variables
        render_relation(plt, dataframe, output, color=color)
        plt.show()
    elif feature_count > 2:
        # Plot grid
        fig = plt.figure()
        fig.subplots_adjust(hspace=0.5, wspace=0.5)
        for row in range(1, feature_count + 1):
            for col in range(1, feature_count + 1):
                ax = fig.add_subplot(
                 feature_count, feature_count, ((row - 1) * feature_count + col)
                )
                if row == col:
                    df = dataframe.iloc[:, [row - 1, -1] if output else [row - 1]]
                    render_distribution(ax, df, output, legend=row == 1)
                elif row > col:
                    df = dataframe.iloc[:, [row - 1, col - 1, -1] if output else [row - 1, col - 1]]
                    render_relation(ax, df, output, legend=False)
                else:
                    ax.set_visible(False)
        if output: fig.legend()


def dataframe_to_variables(dataframe, output=False):
    variables = []
    if output:
        for label in np.unique(dataframe.iloc[:, -1]):
            variables.append(dataframe[dataframe.iloc[:, -1] == label])
    else: variables = [dataframe]
    return variables


def render_distribution(axes, dataframe, output=False, legend=True):
    variables = dataframe_to_variables(dataframe, output)
    values = dataframe.iloc[:, 0].values
    bins = np.histogram(values, bins=len(values) // 5)[1]
    for var in variables:
        axes.hist(
         var.iloc[:, 0].values,
         label=var.values[0][-1] if legend else None,
         bins=bins,
         alpha=0.5 if len(variables) > 1 else 1
        )
    try:
        axes.xlabel(dataframe.columns[0])
        axes.title(dataframe.columns[0] + " Distribution")
        if len(variables) > 1 and legend: plt.legend()
    except AttributeError:
        axes.set_xlabel(dataframe.columns[0])
        axes.set_title(dataframe.columns[0] + " Distribution")


def render_relation(axes, dataframe, output=False, legend=True, color=None):
    variables = dataframe_to_variables(dataframe, output)
    for var in variables:
        plt.scatter(
         var.iloc[:, 0].values,
         var.iloc[:, 1].values,
         s=10,
         label=var.values[0][-1] if legend else None
        )
    if color:
        x_limits, y_limits = axes.xlim(), axes.ylim()
        grid = []
        for range_ in (x_limits, y_limits):
            diff = range_[1] - range_[0]
            resolution = diff / 100
            points = [range_[0] - resolution]
            while points[-1] <= range_[1] + resolution:
                points.append(points[-1] + resolution)
            grid.append(points)
        results = []
        for r in grid[1]:
            row = []
            for c in grid[0]:
                row.append(color([r, c]))
            results.append(row)
        axes.imshow(results, interpolation='nearest', origin='low', extent=axes.xlim() + axes.ylim(), alpha=0.7)
        axes.colorbar()
    try:
        axes.xlabel(dataframe.columns[0])
        axes.ylabel(dataframe.columns[1])
        axes.title(dataframe.columns[0] + " vs " + dataframe.columns[1])
        if len(variables) > 1 and legend: plt.legend()
    except AttributeError:
        axes.set_xlabel(dataframe.columns[0])
        axes.set_ylabel(dataframe.columns[1])
        axes.set_title(dataframe.columns[0] + " vs " + dataframe.columns[1])
