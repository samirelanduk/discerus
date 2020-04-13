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

    def __init__(self, size):
        self.size = size
        self.weights = [0] * size
        self.threshold = 0
    

    def __call__(self, input):
        net_input = self.net_input(input)
        return self.activation(net_input)
    

    def net_input(self, input):
        return sum(input * weight for input, weight in zip(input, self.weights))
    

    def activation(self, net_input):
        return net_input >= self.threshold