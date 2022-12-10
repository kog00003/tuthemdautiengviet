import re


def split_to_con_vow_fin(s):
    pattern = '^(b|c|k|d|g|gh|h|l|m|n|p|q|r|s|t|v|x|ch|kh|ng|ngh|nh|ph|th|tr|gi){0,1}(a|e|i|o|u|y|ai|ao|au|ay|eo|eu|ia|ie|iu|oa|oe|oi|oo|ua|ui|uo|uy|uu|ieu|oai|oao|oay|oeo|uay|uoi|uya|uye|uyu|uoi|uou){1}(c|ch|ng|nh|m|n|p|t){0,1}$'
    m = re.match(pattern, s, flags=re.IGNORECASE)
    return m if not m else [m.group(i) for i in (1, 2, 3)]


na_con = 'b|c|k|d|g|gh|h|l|m|n|p|q|r|s|t|v|x|ch|kh|ng|ngh|nh|ph|th|tr|gi'.split(
    '|')
na_vow = 'a|e|i|o|u|y|ai|ao|au|ay|eo|eu|ia|ie|iu|oa|oe|oi|oo|ua|ui|uo|uy|uu|ieu|oai|oao|oay|oeo|uay|uoi|uya|uye|uyu|uoi|uou'.split(
    '|')
na_fin = 'c|ch|ng|nh|m|n|p|t'.split('|')
na_con = {j: i+1 for i, j in enumerate(na_con)}
na_vow = {j: i+1 for i, j in enumerate(na_vow)}
na_fin = {j: i+1 for i, j in enumerate(na_fin)}
na_cond = {i+1: j for i, j in enumerate(na_con)}
na_vowd = {i+1: j for i, j in enumerate(na_vow)}
na_find = {i+1: j for i, j in enumerate(na_fin)}


def is_vietnamese_without_accent_word(s):
    return split_to_con_vow_fin(s) is not None


def encode_word_no_accent(s):
    if s is None:
        return 0, 1, 0  # None
    elif s.isnumeric():
        return 0, 2, 0  # Number
    a = split_to_con_vow_fin(s)
    if a is None:
        return 0, 3, 0  # Other Not Vietnameses
    con, vow, fin = a
    con = na_con[con.lower()] if con else 31
    vow = na_vow[vow.lower()] if vow else 63
    fin = na_fin[fin.lower()] if fin else 15
    return con, vow, fin

encode_word_no_accent('toi')
encode_word_no_accent('la')
encode_word_no_accent('ai')
# bin(31)
# split_to_con_vow_fin('iet')
# encode_word_no_accent('iet')


def encode_word_no_accent_binary(s):
    """
    example:
    encode_word_no_accent_binary('viet')

    return: bin vector length 15
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0]
    """
    a = encode_word_no_accent(s)  # (16,14,8) for viet
    l = 5, 6, 4  # length bin vector for con max 25, vow max 35, fin max 8
    return [k for i, j in zip(a, l) for k in to_bin_vector(i, j)]


def decode_word_no_accent(v):
    con, vow, fin = v
    return ''.join((na_cond[con], na_vowd[vow], na_find[fin]))


def to_bin_vector(input_number, length):
    s = f'{{:0{length}b}}'.format(input_number)
    return list(map(lambda x: 0 if x == '0' else 1, s))


def clean_text(s):
    if s is None:
        return None
    """keep only unicode vn and 0-9"""
    return re.sub('[^a-zA-Z0-9\u00c0-\u1ef9]', '', s)


# def is_vietnamese_word(s):
#     pattern = '^(b|c|k|d|đ|g|gh|h|l|m|n|p|q|r|s|t|v|x|ch|kh|ng|ngh|nh|ph|th|tr){0,1}(a|ă|â|e|ê|i|o|ô|ơ|u|ư|y|ai|ao|au|ay|âu|ây|eo|êu|ia|iê|iu|oa|oă|oe|oi|oo|ôi|ơi|ua|uâ|ui|uô|ươ|uy|ưa|uơ|ưi|ươ|ưu|iêu|oai|oao|oay|oeo|uay|uây|uôi|uya|uyê|uyu|ươi|ươu){1}(c|ch|ng|nh|m|n|p|t){0,1}$'
#     return re.match(pattern, s) is not None


# moads = 'a ă â e ê i o ô ơ u ư y'.split()
# dyads = 'ai ao au ay âu ây eo êu ia iê iu oa oă oe oi oo ôi ơi ua uâ ui uô ươ uy ưa uơ ưi ươ ưu'.split()
# triads = 'iêu oai oao oay oeo uay uây uôi uya uyê uyu ươi ươu'.split()
# consonants = 'b c k d đ g gh h l m n p q r s t v x ch kh ng ngh nh ph th tr gi'.split()
# finals = 'c ch ng nh m n p t'.split()

# {'d': ['d', 'đ']}
# '|'.join((*moads, *dyads, *triads))
# '|'.join((*consonants,))
# '|'.join((*finals,))

# is_vietnamese_without_accent_word('nha')


# dyads
