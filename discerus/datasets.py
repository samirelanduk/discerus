import matplotlib.pyplot as plt
import numpy as np

def plot_dataset(dataframe, title="", output=False):
    # How many features are there to visualise?
    feature_count = len(dataframe.columns)
    if output: feature_count -= 1

    if feature_count == 1:
        # Just show distribution
        variables = dataframe_to_variables(dataframe, output)
        values = dataframe.iloc[:, 0].values
        bins = np.histogram(values, bins=len(values) // 4)[1]
        for var in variables:
            plt.hist(
             var.iloc[:, 0].values,
             label=var.values[0][-1],
             bins=bins,
             alpha=0.5 if len(variables) > 1 else 1
            )
        if len(variables) > 1: plt.legend()
        plt.xlabel(dataframe.columns[0])
        plt.title(dataframe.columns[0] + " Distribution")
        plt.show()
    elif feature_count == 2:
        # Plot two variables
        variables = dataframe_to_variables(dataframe, output)
        for var in variables:
            plt.scatter(
             var.iloc[:, 0].values,
             var.iloc[:, 1].values,
             label=var.values[0][-1]
            )
        if len(variables) > 1: plt.legend()
        plt.xlabel(dataframe.columns[0])
        plt.ylabel(dataframe.columns[1])
        plt.title(dataframe.columns[0] + " vs " + dataframe.columns[1])
        plt.show()


def dataframe_to_variables(dataframe, output=False):
    variables = []
    if output:
        for label in np.unique(dataframe.iloc[:, -1]):
            variables.append(dataframe[dataframe.iloc[:, -1] == label])
    else: variables = [dataframe]
    return variables
