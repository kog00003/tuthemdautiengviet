import tkinter as tk
import more_itertools
# import tqdm
from create_sample import array_split_by_position
from label_and_restore import restore_tone_with_status
from vi_match_encode_decode import encode_word_no_accent_binary, is_vietnamese_without_accent_word, clean_text
import simpletorch
import torch
from bo_dau_tieng_viet import bodau
import torch.nn as nn
from simpletorch import toTensorF, toTensorL
import numpy as np
model = torch.nn.Sequential(nn.Linear(45, 128),
                            nn.ReLU(),
                            nn.BatchNorm1d(128),
                            nn.Linear(128, 128),
                            nn.ReLU(),
                            nn.BatchNorm1d(128),
                            nn.Linear(128, 128),
                            nn.ReLU(),
                            nn.BatchNorm1d(128),
                            nn.Linear(128, 128),
                            nn.ReLU(),
                            nn.BatchNorm1d(128),
                            nn.Linear(128, 128),
                            nn.ReLU(),
                            nn.BatchNorm1d(128),
                            nn.Linear(128, 128),
                            nn.ReLU(),
                            nn.BatchNorm1d(128),
                            nn.Linear(128, 128),
                            nn.ReLU(),
                            nn.BatchNorm1d(128),
                            nn.Linear(128, 128),
                            nn.ReLU(),
                            nn.BatchNorm1d(128),
                            nn.Linear(128, 128),
                            nn.ReLU(),
                            nn.Linear(128, 11))

model = simpletorch.loadModel(model, 'model')
print('n_params', sum(p.numel() for p in model.parameters()))

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


def them_dau_with_model(model, s):
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
    # print(samples)
    return ' '.join([restore_with_model(model, *i)
                     for i in samples])

# restore_with_model(model,'','BaT','dau')
# data = torch.load('x').type(torch.float)
# label = torch.load('y').type(torch.long)
# simpletorch.testingWithCrossEntropyLossMultiTarget(
#     model, data, label, [[0, 2], [2, 5], [5, 11]])


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

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

    def print_contents(self, event):
        # print(event.char)
        if event.char == ' ' or event.char in end_segment_chars:
            s = them_dau_with_model(model, bodau(self.contents.get()))
            self.contents.set(s)
            # print(self.contents.get())


root = tk.Tk()
root.geometry('400x50')
myapp = App(root)
myapp.master.title("test them dau tv")
myapp.mainloop()
