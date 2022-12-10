
from gzip import open as openGz
import more_itertools
from bo_dau import bodau
from label_and_restore import get_status, restore_tone_with_status
import tqdm
from encode_decode_match import encode_word_no_accent, is_vietnamese_without_accent_word, clean_text, encode_word_no_accent_binary
import numpy as np


def array_split_by_position(arr, positions):
    if positions[0] > 0:
        positions.insert(0, 0)
    if positions[-1] < len(arr):
        positions.append(len(arr))
    return [arr[i:j] for i, j in more_itertools.sliding_window(positions, 2)]


def create_samples(s):
    """
    s: sentence...
    Return:
    [sample,sample...]
    sample: ((prev word, current word, next word),status)
    status: (d_status,vowel_status,tone_status)
    """
    s = s.lower()
    samples = []
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

    samples = [(clean_text(i), clean_text(j), clean_text(k))
               for i, j, k in samples]

    samples = [((bodau(i), bodau(j), bodau(k)), get_status(j))
               for i, j, k in samples if is_vietnamese_without_accent_word(bodau(j))]

    return samples


def samples_to_data_label(samples):
    """
    return data,label
    """
    data = []
    label = []
    for i, j in samples:
        sample = [b for k in i for b in encode_word_no_accent(k)]
        data.append(sample)
        label.append(j)

    return np.array(data), np.array(label)


def samples_to_data_label_binary(samples):
    """
    return data,label: nparray data in binary
    """
    data = []
    label = []
    for i, j in samples:
        sample = [b for k in i for b in encode_word_no_accent_binary(k)]
        data.append(sample)
        label.append(j)

    return np.array(data), np.array(label)


# samples = create_samples(
#     'chiến thuật hiện đại, theo Phó chủ nhiệm Tổng cục Công nghiệp quốc phòng Dương Văn Yên.')
# samples_to_data_label(samples)
# samples_to_data_label_binary(samples)


def generate_data_from_text_file(filePath='corpus-full.txt.gz', endLine=100, gz=True):
    # filePath = 'D:/Data/Notebook/vinlp/corpus-full.txt.gz'
    a = []
    if gz:
        with openGz(filePath, 'r') as f:
            for _ in tqdm.trange(endLine, desc='reading line'):
                s = f.readline().decode('utf8')
                if not s:
                    break
                a.append(s)
    else:
        with open(filePath, 'r') as f:
            for _ in tqdm.trange(endLine, desc='reading file'):
                s = f.readline()
                if not s:
                    break
                a.append(s)
    data = []
    label = []
    for sample in tqdm.tqdm(a, desc='creating sample'):
        d, l = samples_to_data_label_binary(create_samples(sample))
        data.extend(d)
        label.extend(l)
    return np.array(data), np.array(label)


# data, label = generate_data_from_text_file(
#     'D:/Data/Notebook/vinlp/corpus-full.txt.gz', endLine=100, gz=True)
