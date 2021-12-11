import sys
import os
sys.path.append(os.pardir)

from model.cnn import ConvolutionalNeuralNetwork
from dataset.reversi_data import *

cnn = ConvolutionalNeuralNetwork()
cnn.load_params()
(x_train, t_train), (x_test, t_test) = load_reversi_data()
print(cnn.accuracy(x_test, t_test))
