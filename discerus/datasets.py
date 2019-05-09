import matplotlib.pyplot as plt
import numpy as np

def plot_dataset(dataframe, title="", output=False):
    # How many features are there to visualise?
    feature_count = len(dataframe.columns)
    if output: feature_count -= 1

    if feature_count == 1:
        # Just show distribution
        variables = []
        values = dataframe.iloc[:, 0].values
        bins = np.histogram(values, bins=len(values) // 4)[1]
        if output:
            for label in np.unique(dataframe.iloc[:, -1]):
                variables.append(dataframe[dataframe.iloc[:, -1] == label])
        else: variables = [dataframe]
        for var in variables:
            values = var.iloc[:, 0].values
            plt.hist(
             values,
             label=var.values[0][-1],
             bins=bins,
             alpha=0.5 if len(variables) > 1 else 1
            )
        if len(variables) > 1: plt.legend()
        plt.xlabel(dataframe.columns[0])
        plt.title(dataframe.columns[0] + " Distribution")
        plt.show()


    np.histogram(dataframe.iloc[:, 0].values)
