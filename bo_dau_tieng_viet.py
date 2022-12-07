from re import sub
# import tokenizer
new_values = list("aAeEoOuUiIdDyY")
old_values = ["áàạảãâấầậẩẫăắằặẳẵ",
              "ÁÀẠẢÃÂẤẦẬẨẪĂẮẰẶẲẴ",
              "éèẹẻẽêếềệểễ",
              "ÉÈẸẺẼÊẾỀỆỂỄ",
              "óòọỏõôốồộổỗơớờợởỡ",
              "ÓÒỌỎÕÔỐỒỘỔỖƠỚỜỢỞỠ",
              "úùụủũưứừựửữ",
              "ÚÙỤỦŨƯỨỪỰỬỮ",
              "íìịỉĩ",
              "ÍÌỊỈĨ",
              "đ",
              "Đ",
              "ýỳỵỷỹ",
              "ÝỲỴỶỸ"]

zip_values = [(k, new_values[i])
              for i, j in enumerate(old_values) for k in j]
old_values_regex = ['|'.join(j for j in i) for i in old_values]

old_values_flat = [i for i, j in zip_values]
new_values_flat = [j for i, j in zip_values]

translate_table = str.maketrans(
    ''.join(old_values_flat), ''.join(new_values_flat))


def bodau_re_sub(a):
    """use re.sub"""
    for re_str, re_rep in zip(old_values_regex, new_values):
        a = sub(re_str, re_rep, a)
    return a


def bodau_str_translate(x): return x.translate(translate_table)


def bodau_str_replace(a):
    """use str.replace"""
    for i, j in zip_values:
        a = a.replace(i, j)
    return a


# str replace vs str translate, sometime faster, sometime slower

# bodau_str_translate with none check
def bodau(x): return bodau_str_translate(x) if x else x


# test_text = 'Giải bóng đá Ngoại hạng Anh là hạng đấu cao nhất của hệ thống các giải bóng đá ở Anh. Gồm 20 câu lạc bộ, giải đấu sử dụng hệ thống thăng hạng và xuống hạng với English Football League (EFL). Mùa giải kéo dài từ tháng 8 đến tháng 5 với mỗi đội chơi 38 trận đấu (đấu với 19 đội khác trên sân nhà và sân khách). Đa số các trận đấu được diễn ra vào chiều Thứ Bảy và Chủ Nhật.'
# import tqdm

# 100%|██████████| 100000/100000 [00:03<00:00, 30441.57it/s]
# for _ in tqdm.trange(100000):
#     s = bodau_str_translate(test_text)

# 100%|██████████| 100000/100000 [00:02<00:00, 33770.32it/s]
# for _ in tqdm.trange(100000):
#     s = bodau_str_replace(test_text)

# 100%|██████████| 100000/100000 [00:07<00:00, 13675.33it/s]
# for _ in tqdm.trange(100000):
#     s = bodau_re_sub(test_text)
