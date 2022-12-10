import more_itertools
from label_and_restore import restore_tone_with_status
from encode_decode_match import encode_word_no_accent_binary, is_vietnamese_without_accent_word
from input_and_sample import generate_data_from_text_file
import simpletorch
from matplotlib import pyplot as plt
import torch
from simpletorch import LinearReLU, LinearReLUStackX, crossEntropyLossMultiTarget
import torch.nn as nn
from simpletorch import toTensorF, toTensorL, get_num_params
import numpy as np
data, label = generate_data_from_text_file(endLine=200000)
# len(data)
# len(label)
data = toTensorF(data)
label = toTensorL(label)
torch.save(data.type(torch.int8), 'data/x')
torch.save(label.type(torch.int8), 'data/y')
