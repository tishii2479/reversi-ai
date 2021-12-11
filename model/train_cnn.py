import sys
import os
sys.path.append(os.pardir)

import numpy as np
import matplotlib.pyplot as plt
from model.cnn import ConvolutionalNeuralNetwork
from common.trainer import Trainer
from dataset.reversi_data import load_reversi_data

(x_train, t_train), (x_test, t_test) = load_reversi_data()

max_epochs = 50

network = ConvolutionalNeuralNetwork()

trainer = Trainer(network, x_train, t_train, x_test, t_test,
                  epochs=max_epochs, mini_batch_size=50,
                  optimizer='Adam', optimizer_param={'lr': 0.001},
                  evaluate_sample_num_per_epoch=None)
trainer.train()

# パラメータの保存
network.save_params("params.pkl")
print("Saved Network Parameters!")

# グラフの描画
markers = {'train': 'o', 'test': 's'}
x = np.arange(max_epochs)
plt.plot(x, trainer.train_acc_list, marker='o', label='train', markevery=2)
plt.plot(x, trainer.test_acc_list, marker='s', label='test', markevery=2)
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()
