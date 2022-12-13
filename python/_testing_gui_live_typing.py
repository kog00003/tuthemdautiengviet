import json
import tkinter as tk
import more_itertools
# import tqdm
from input_and_sample import array_split_by_position
from label_and_restore import restore_tone_with_status
from encode_decode_match import encode_word_no_accent_binary, is_vietnamese_without_accent_word, clean_text
import simpletorch
import torch
from bo_dau import bodau
import torch.nn as nn
from simpletorch import LinearNormRelu, toTensorF, toTensorL
import numpy as np
import re

model = torch.nn.Sequential(LinearNormRelu(45, 128),
                            LinearNormRelu(128, 128),
                            LinearNormRelu(128, 128),
                            LinearNormRelu(128, 128),
                            LinearNormRelu(128, 128),
                            LinearNormRelu(128, 128),
                            LinearNormRelu(128, 128),
                            LinearNormRelu(128, 128),
                            LinearNormRelu(128, 128),
                            nn.Linear(128, 11))


model = simpletorch.loadModel(model, 'data/model')
print('n_params', sum(p.numel() for p in model.parameters()))


class RNNX(nn.Module):
    """
    RNN only output for nn.Sequential
    output flatten, and stack with x
    """

    def __init__(self, hidden_size=32, num_layers=1):
        super().__init__()
        self.rnn = nn.RNN(15, hidden_size, num_layers=num_layers, nonlinearity='relu',
                          batch_first=True)

    def forward(self, x):
        n = len(x)
        return torch.hstack((self.rnn(x.reshape(n, 3, 15))[0].flatten(1), x))


model_rnn = nn.Sequential(RNNX(hidden_size=128, num_layers=2),
                          LinearNormRelu(429, 128),
                          LinearNormRelu(128, 128),
                          LinearNormRelu(128, 128),
                          LinearNormRelu(128, 128),
                          nn.Linear(128, 11))

model_rnn = simpletorch.loadModel(model_rnn, 'data/model_rnn')
# restore_with_model(model,'toi','la','ai')
print('n_params', sum(p.numel() for p in model_rnn.parameters()))


model_rnn_simple = nn.Sequential(RNNX(hidden_size=128, num_layers=1),
                                 LinearNormRelu(429, 128),
                                 nn.Linear(128, 11))

model_rnn_simple = simpletorch.loadModel(
    model_rnn_simple, 'data/model_rnn_simple')
# restore_with_model(model_rnn_simple,'toi','la','ai')
print('n_params', sum(p.numel() for p in model_rnn_simple.parameters()))

models = (model, model_rnn, model_rnn_simple)
end_segment_chars = ('.', ',', ':', '!')


def restore_with_model(model, prevW, currW, nextW):
    if not is_vietnamese_without_accent_word(clean_text(currW)):
        return currW
    multi_positions = [[0, 2], [2, 5], [5, 11]]
    words = [bodau(clean_text(x)).lower() if x else None
             for x in (prevW, currW, nextW)]
    # print(words)
    x = [i for w in words for i in encode_word_no_accent_binary(w)]
    status = simpletorch.predictMulitTarget(model, toTensorF(
        x).unsqueeze(0), multi_positions=multi_positions)[0]
    return restore_tone_with_status(currW, status)


skip_last_word = False


def them_dau_with_model(model, s, onlyLast=False):
    global skip_last_word
    ss = s.split()
    samples = []
    split_positions = [pos+1 for pos,
                       i in enumerate(ss) if i[-1] in end_segment_chars]
    if split_positions:
        ss = array_split_by_position(ss, split_positions)
    else:
        ss = [ss, ]
    for arr in ss:
        arr.insert(0, None)
        arr.append(None)
        samples.extend(list(more_itertools.sliding_window(arr, 3)))
    samples = [list(i) for i in samples]

    if len(samples) == 0:
        return s

    if onlyLast:

        prefix = ' '.join([j for _, j, _ in samples[:len(samples)-2]])

        # use only last two samples

        samples = samples[-2:]

        if len(samples) == 2:
            if not skip_last_word:
                # reset word near last
                samples[0][1] = bodau(samples[0][1])

        # if user already add accent to word, change value skip_last_word to true so next time dont reset / predict accent

        skip_last_word = not is_vietnamese_without_accent_word(samples[-1][1])

        ns = ' '.join([restore_with_model(model, *i)
                       for i in samples])

    else:
        prefix = ''
        ns = ' '.join([restore_with_model(model, *i)
                       for i in samples])

    return f'{prefix} {ns}' if prefix else ns


options = [
    "Linear 150K",
    "RNN 150K",
    "RNN_Simple 75K"
]


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.clicked = tk.StringVar()
        self.clicked.set(options[1])
        self.model = models[1]
        self.dropdown = tk.OptionMenu(
            None, self.clicked, *options, command=self.option_change)
        self.dropdown.pack()
        self.entrythingy = tk.Entry(width=40, font=32)
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<KeyPress>',
                              self.print_contents)

    def option_change(self, event):
        # print('option change', options.index(event))
        self.model = models[options.index(event)]
        self.reset_and_them_dau()

    def reset_and_them_dau(self):
        self.contents.set(them_dau_with_model(
            self.model, bodau(self.contents.get()), onlyLast=False))

    def them_dau(self):
        s = them_dau_with_model(
            self.model, self.contents.get(), onlyLast=True)
        self.contents.set(s)

    def print_contents(self, event):
        # print(event.char)
        if event.char == ' ' or event.char in end_segment_chars:
            self.them_dau()
            # print(self.contents.get())


root = tk.Tk()
root.geometry('400x80')
myapp = App(root)
myapp.master.title("github.com/kog00003/tuthemdautiengviet/")
myapp.mainloop()




# str([i for w in 'toi la ai'.split()
#          for i in encode_word_no_accent_binary(w)])
