class MCPNeuron:

    def __init__(self, threshold, inhitors=None):
        self.inhibtors = inhitors or []
        self.threshold = threshold

    
    def __call__(self, inputs):
        if any(val == 1 and i in self.inhibtors for i, val in enumerate(inputs)):
            return False
        return sum(inputs) >= self.threshold