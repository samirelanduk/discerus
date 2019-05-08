import matplotlib.pyplot as plt
import numpy as np

def plot_dataset(dataframe, title=""):
    column_names = dataframe.columns
    for label in np.unique(dataframe[column_names[-1]]):
        df = dataframe[dataframe[column_names[-1]] == label]
        plt.scatter(df[column_names[0]], df[column_names[1]], label=label)
    plt.xlabel(column_names[0])
    plt.ylabel(column_names[1])
    plt.title(title)
    plt.legend()
    plt.show()
