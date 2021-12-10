import sys
import os
sys.path.append(os.pardir)

import unittest
from model.cnn import ConvolutionalNeuralNetwork
from model.deep_cnn import DeepConvNet
from dataset.reversi_data import *


class TestConvolutionalNeuralNetwork(unittest.TestCase):
    def test_accuracy(self):
        cnn = DeepConvNet()
        cnn.load_params()
        (x_train, t_train), (x_test, t_test) = load_reversi_data()
        print(cnn.accuracy(x_test, t_test))


if __name__ == '__main__':
    unittest.main()
