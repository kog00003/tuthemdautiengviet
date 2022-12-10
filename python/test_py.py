import pandas as pd
from gzip import open as openGz
import json
import re
import tqdm
import numpy as np
import more_itertools
import clipboard
from pathlib import Path

with openGz('D:/Data/Notebook/vinlp/corpus-full.txt.gz', 'r') as f:
    a = [f.readline().decode('utf8') for _ in range(10000)]

from bo_dau import bodau
from encode_decode_match import is_vietnamese_without_accent_word
# json.loads(a)['content']
# with open('D:/Data/Notebook/vinlp/corpus-full.txt', 'r', encoding='utf8') as f:
#     a = f.readline()

# a.decode('utf8')


def array_split_by_position(arr, positions):
    if positions[0] > 0:
        positions.insert(0, 0)
    if positions[-1] < len(arr):
        positions.append(len(arr))
    return [arr[i:j] for i, j in more_itertools.sliding_window(positions, 2)]


s = a[1]

samples = []
for s in a:
    ss = s.split()
    # split to segments by .,!
    split_positions = [pos+1 for pos,
                       i in enumerate(ss) if i[-1] in ('.', ',', ':', '!')]

    if split_positions:
        ss = array_split_by_position(ss, split_positions)
    else:
        ss = [ss, ]
    for arr in ss:
        arr.insert(0, None)
        arr.append(None)
        samples.extend(list(more_itertools.sliding_window(arr, 3)))
# len(samples)

df = pd.DataFrame(samples, columns=['w1', 'w2', 'w3'])

df = df.assign(w1wa=df['w1'].apply(bodau),
               w2wa=df['w2'].apply(bodau),
               w3wa=df['w3'].apply(bodau))

df.firstWord[:100].apply(bodau)

'99'.isnumeric()

'sss'.lower()

df = df[df.w2wa.apply(lambda x: is_vietnamese_without_accent_word(x.lower()))]

Path('vi-vocal-notone.txt').write_text(
    '\n'.join(df.w2wa.str.lower().value_counts().index), 'utf8')


vocals = list(df.w2wa.str.lower().value_counts().index)

vocals_dict = dict((v, i+4) for i, v in enumerate(vocals))

# ''.join(df.vi)

u'\u00C0'



# # clean_text('Điện.,')

# def tokenize(w):
#     """
#     1 number
#     2 unknown/not in dict
#     3 none
#     >3 dict value
#     """
#     if w is None or w.isspace():
#         return 3
#     w = w.lower()
#     if w in vocals_dict:
#         return vocals_dict[w]
#     elif w.isnumeric():
#         return 1
#     else:
#         return 2


# # tokenize('8844aa')

df.w2wa.apply(tokenize)
df.w1wa.apply(tokenize)
# vocals_dict[w]
df.w3wa.apply(tokenize)


s = 'Đảnh'
s = s.lower()


# df = pd.read_html(clipboard.paste())[0]
# df.columns = df.iloc[0, :]
# df = df[1:]
# df.to_csv('vietnamese_table.csv')

df = pd.read_csv('vietnamese_table.csv', index_col='Unnamed: 0')


df.columns

# df[df['English Name'].str.contains('GRAVE')]

# huyen sac hoi nga nang

# dau = ['GRAVE', 'ACUTE', 'ABOVE', 'TILDE', 'DOT BELOW']
# for i in dau:
#     df['Viet'][df['English Name'].str.contains(i)]

dict(df.Viet, df.VIQR.apply(lambda x: x[1:]))


dict_vi2viqr = dict(zip(df.Viet, df.VIQR))
# list(zip(df.Viet, df.VIQR))
# df.Viet.values
# df.VIQR.values

# with open('vi_to_viqr.json','w') as f:
#     json.dump(dict(zip(df.Viet, df.VIQR)), f)


def toviqr(s):

    for k, v in dict_vi2viqr.items():
        s = s.replace(k, v)
    return s


vowel_spec_chars = list(enumerate(list('(^+')))
tone_spec_chars = list(enumerate(list('`\'?~.')))


def get_status(s):
    """
    return tuple(d_status,vowel_status,tone_status)
    d_status: 0 d, 1 đ
    vowel status: 0 a,o,u, 1 ă,ơ,ư, 2 â,ô,
    tone status: 0 a, 1 à, 2 á, 3 ả, 4 ã, 5 ạ
    """
    s = s.lower()
    s = toviqr(s)
    d_status = 'dd' in s
    # vowel_status = 'dd' in s

    vowel_status = [i for i, v in vowel_spec_chars if v in s]
    tone_status = [i for i, v in tone_spec_chars if v in s]

    vowel_status = 0 if len(vowel_status) == 0 else (
        2 if vowel_status[0] == 1 else 1)
    tone_status = 0 if not tone_status else tone_status[0]+1
    return int(d_status), vowel_status, tone_status
    # tone_status=


def restore_tone_with_status(s, status):
    d_status, vowel_status, tone_status = status
    #


s = 'Đảnh'
get_status(s)
