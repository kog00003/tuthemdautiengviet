from create_sample import generate_data_from_text_file
import simpletorch
from matplotlib import pyplot as plt
import torch
from simpletorch import crossEntropyLossMultiTarget
import torch.nn as nn
from simpletorch import toTensorF, toTensorL


# data, label = generate_data_from_text_file(endLine=100000)
# # len(data)
# # len(label)
# data = toTensorF(data)
# label = toTensorL(label)
# torch.save(data, 'x')
# torch.save(label, 'y')


data = torch.load('x')
label = torch.load('y')


xtn, ytn, xtt, ytt = simpletorch.chooseTrainTest(data, label)

model = torch.nn.Sequential(nn.Linear(45, 32),
                            nn.ReLU(),
                            nn.Linear(32, 11))


lossUse = crossEntropyLossMultiTarget([[0, 2], [2, 5], [5, 11]])


l = simpletorch.training(model, xtn, ytn,
                         lossUse=lossUse, learningRate=.1, numSteps=20, numStepsPerBatch=2)

print('train loss', l[-1], 'mean', simpletorch.mean(l))
print('test loss', lossUse(model(xtt), ytt))
plt.plot(l)
