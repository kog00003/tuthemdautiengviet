import more_itertools
from label_and_restore import restore_tone_with_status
from vi_match_encode_decode import encode_word_no_accent_binary, is_vietnamese_without_accent_word
import simpletorch
import torch
import torch.nn as nn
from simpletorch import toTensorF, toTensorL
import numpy as np
model = torch.nn.Sequential(nn.Linear(45, 128),
                            nn.ReLU(),
                            nn.Linear(128, 128),
                            nn.ReLU(),
                            nn.Linear(128, 128),
                            nn.ReLU(),
                            nn.Linear(128, 128),
                            nn.ReLU(),
                            nn.Linear(128, 128),
                            nn.ReLU(),
                            nn.Linear(128, 128),
                            nn.ReLU(),
                            nn.Linear(128, 128),
                            nn.ReLU(),
                            nn.Linear(128, 11))

model = simpletorch.loadModel(model, 'model')
print('n_params', sum(p.numel() for p in model.parameters()))


def restore_with_model(model, prevW, currW, nextW):
    if not is_vietnamese_without_accent_word(currW):
        return currW
    multi_positions = [[0, 2], [2, 5], [5, 11]]
    words = [prevW, currW, nextW]
    x = [i for w in words for i in encode_word_no_accent_binary(w)]
    status = simpletorch.predictMulitTarget(model, toTensorF(
        x).unsqueeze(0), multi_positions=multi_positions)[0]
    return restore_tone_with_status(words[1], status)


def them_dau_with_model(model, s):
    s = s.split()
    s.insert(0, None)
    s.append(None)
    return ' '.join([restore_with_model(model, *i)
                     for i in list(more_itertools.sliding_window(s, 3))])


# data = torch.load('x')
# label = torch.load('y')
# simpletorch.testingWithCrossEntropyLossMultiTarget(
#     model, data, label, [[0, 2], [2, 5], [5, 11]])

s = 'ngay 9 thang 12 nam 2022 dat toi ket qua chinh xac 87% voi 106379 params'
them_dau_with_model(model, s)


