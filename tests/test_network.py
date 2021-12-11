import sys
import os
sys.path.append(os.pardir)

import unittest
from model.cnn import ConvolutionalNeuralNetwork
from dataset.reversi_data import *


class TestConvolutionalNeuralNetwork(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
