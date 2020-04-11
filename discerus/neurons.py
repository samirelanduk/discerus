class MCPNeuron:
    """A McCullock-Pitt neuron is a function of binary inputs, which returns a
    binary output.

    It sums the inputs, and if they are over some threshold, returns True.

    You can specify that some inputs are inhibitory - of they are True, the
    output will always be False."""

    def __init__(self, threshold, inhitors=None):
        self.inhibtors = inhitors or []
        self.threshold = threshold

    
    def __call__(self, inputs):
        if any(x == 1 and i in self.inhibtors for i, x in enumerate(inputs)):
            return False
        return sum(inputs) >= self.threshold



class Perceptron:

    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold
    

    def __call__(self, inputs):
        net_sum = sum(input * weight for input, weight in zip(inputs, self.weights))
        return net_sum >= self.threshold