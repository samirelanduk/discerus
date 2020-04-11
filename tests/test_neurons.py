from unittest import TestCase
from discerus.neurons import *

class MCPNeuronTests(TestCase):

    def test(self):
        AND = MCPNeuron(2)
        self.assertTrue(AND([True, True]))
        self.assertFalse(AND([True, False]))
        self.assertFalse(AND([False, True]))
        self.assertFalse(AND([False, False]))

        OR = MCPNeuron(1)
        self.assertTrue(OR([True, True]))
        self.assertTrue(OR([True, False]))
        self.assertTrue(OR([False, True]))
        self.assertFalse(OR([False, False]))

        NOR = MCPNeuron(0, inhitors=[0, 1])
        self.assertFalse(NOR([True, True]))
        self.assertFalse(NOR([True, False]))
        self.assertFalse(NOR([False, True]))
        self.assertTrue(NOR([False, False]))



class PerceptronTests(TestCase):

    def test(self):
        perceptron = Perceptron([2, 5], 8)
        self.assertTrue(perceptron([-1, 2]))
        self.assertFalse(perceptron([-1, 1.99]))