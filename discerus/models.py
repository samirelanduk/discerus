import numpy as np

def to_numpy(func):
    def new(self, l, *args, **kwargs):
        if isinstance(l, list):
            l = np.asarray(l)
        return func(self, l, *args, **kwargs)
    return new

class Perceptron:

    def __init__(self, training_data):
        self.training_data = training_data
        self.is_trained = False
        self.weights = np.ones(len(training_data.columns) - 1)
        self.threshold = 0


    def __repr__(self):
        return "<{}trained Perceptron (threshold={}, weights={})>".format(
         "" if self.is_trained else "un", self.threshold, self.weights
        )


    @to_numpy
    def net_activation(self, input):
        return input.dot(self.weights)


    @to_numpy
    def predict(self, input):
        return np.where(self.net_activation(input) >= self.threshold, 1, -1)
