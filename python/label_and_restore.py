# from bo_dau_tieng_viet import bodau


# tone_rank = list('ÂâĂăÊêÔôƠơƯưEAOYUIeaoyuiĐđ')
# tone_rank = dict(((j, i) for i, j in enumerate(tone_rank)))

# df = df.sort_values('koDauT', key=lambda x: [tone_rank[i] for i in x])



# dau = ['GRAVE', 'ACUTE', 'HOOK ABOVE', 'TILDE', 'DOT BELOW']

# spec = ['CIRCUMFLEX', 'HORN', 'BREVE', 'STROKE']

# restore_tones = [df[df.tone == i].loc[:,
#                                       ('koDauT', 'vi')].values.tolist() for i in dau]

# restore_specs = [df[df.spec == i].loc[:,
#                                       ('koDau', 'koDauT')].values.tolist() for i in spec]


# dict_vi2viqr = dict(zip(df.vi, df.viqr))



dict_vi2viqr = {'À': 'A`',
                'Á': "A'",
                'Â': 'A^',
                'Ã': 'A~',
                'È': 'E`',
                'É': "E'",
                'Ê': 'E^',
                'Ì': 'I`',
                'Í': "I'",
                'Ò': 'O`',
                'Ó': "O'",
                'Ô': 'O^',
                'Õ': 'O~',
                'Ù': 'U`',
                'Ú': "U'",
                'Ý': "Y'",
                'à': 'a`',
                'á': "a'",
                'â': 'a^',
                'ã': 'a~',
                'è': 'e`',
                'é': "e'",
                'ê': 'e^',
                'ì': 'i`',
                'í': "i'",
                'ò': 'o`',
                'ó': "o'",
                'ô': 'o^',
                'õ': 'o~',
                'ù': 'u`',
                'ú': "u'",
                'ý': "y'",
                'Ă': 'A(',
                'ă': 'a(',
                'Đ': 'DD',
                'đ': 'dd',
                'Ĩ': 'I~',
                'ĩ': 'i~',
                'Ũ': 'U~',
                'ũ': 'u~',
                'Ơ': 'O+',
                'ơ': 'o+',
                'Ư': 'U+',
                'ư': 'u+',
                'Ạ': 'A.',
                'ạ': 'a.',
                'Ả': 'A?',
                'ả': 'a?',
                'Ấ': "A^'",
                'ấ': "a^'",
                'Ầ': 'A^`',
                'ầ': 'a^`',
                'Ẩ': 'A^?',
                'ẩ': 'a^?',
                'Ẫ': 'A^~',
                'ẫ': 'a^~',
                'Ậ': 'A^.',
                'ậ': 'a^.',
                'Ắ': "A('",
                'ắ': "a('",
                'Ằ': 'A(`',
                'ằ': 'a(`',
                'Ẳ': 'A(?',
                'ẳ': 'a(?',
                'Ẵ': 'A(~',
                'ẵ': 'a(~',
                'Ặ': 'A(.',
                'ặ': 'a(.',
                'Ẹ': 'E.',
                'ẹ': 'e.',
                'Ẻ': 'E?',
                'ẻ': 'e?',
                'Ẽ': 'E~',
                'ẽ': 'e~',
                'Ế': "E^'",
                'ế': "e^'",
                'Ề': 'E^`',
                'ề': 'e^`',
                'Ể': 'E^?',
                'ể': 'e^?',
                'Ễ': 'E^~',
                'ễ': 'e^~',
                'Ệ': 'E^.',
                'ệ': 'e^.',
                'Ỉ': 'I?',
                'ỉ': 'i?',
                'Ị': 'I.',
                'ị': 'i.',
                'Ọ': 'O.',
                'ọ': 'o.',
                'Ỏ': 'O?',
                'ỏ': 'o?',
                'Ố': "O^'",
                'ố': "o^'",
                'Ồ': 'O^`',
                'ồ': 'o^`',
                'Ổ': 'O^?',
                'ổ': 'o^?',
                'Ỗ': 'O^~',
                'ỗ': 'o^~',
                'Ộ': 'O^.',
                'ộ': 'o^.',
                'Ớ': "O+'",
                'ớ': "o+'",
                'Ờ': 'O+`',
                'ờ': 'o+`',
                'Ở': 'O+?',
                'ở': 'o+?',
                'Ỡ': 'O+~',
                'ỡ': 'o+~',
                'Ợ': 'O+.',
                'ợ': 'o+.',
                'Ụ': 'U.',
                'ụ': 'u.',
                'Ủ': 'U?',
                'ủ': 'u?',
                'Ứ': "U+'",
                'ứ': "u+'",
                'Ừ': 'U+`',
                'ừ': 'u+`',
                'Ử': 'U+?',
                'ử': 'u+?',
                'Ữ': 'U+~',
                'ữ': 'u+~',
                'Ự': 'U+.',
                'ự': 'u+.',
                'Ỳ': 'Y`',
                'ỳ': 'y`',
                'Ỵ': 'Y.',
                'ỵ': 'y.',
                'Ỷ': 'Y?',
                'ỷ': 'y?',
                'Ỹ': 'Y~',
                'ỹ': 'y~'}

restore_tones = [[['Â', 'Ầ'],
  ['â', 'ầ'],
  ['Ă', 'Ằ'],
  ['ă', 'ằ'],
  ['Ê', 'Ề'],
  ['ê', 'ề'],
  ['Ô', 'Ồ'],
  ['ô', 'ồ'],
  ['Ơ', 'Ờ'],
  ['ơ', 'ờ'],
  ['Ư', 'Ừ'],
  ['ư', 'ừ'],
  ['E', 'È'],
  ['A', 'À'],
  ['O', 'Ò'],
  ['Y', 'Ỳ'],
  ['U', 'Ù'],
  ['I', 'Ì'],
  ['e', 'è'],
  ['a', 'à'],
  ['o', 'ò'],
  ['y', 'ỳ'],
  ['u', 'ù'],
  ['i', 'ì']],
 [['Â', 'Ấ'],
  ['â', 'ấ'],
  ['Ă', 'Ắ'],
  ['ă', 'ắ'],
  ['Ê', 'Ế'],
  ['ê', 'ế'],
  ['Ô', 'Ố'],
  ['ô', 'ố'],
  ['Ơ', 'Ớ'],
  ['ơ', 'ớ'],
  ['Ư', 'Ứ'],
  ['ư', 'ứ'],
  ['E', 'É'],
  ['A', 'Á'],
  ['O', 'Ó'],
  ['Y', 'Ý'],
  ['U', 'Ú'],
  ['I', 'Í'],
  ['e', 'é'],
  ['a', 'á'],
  ['o', 'ó'],
  ['y', 'ý'],
  ['u', 'ú'],
  ['i', 'í']],
 [['Â', 'Ẩ'],
  ['â', 'ẩ'],
  ['Ă', 'Ẳ'],
  ['ă', 'ẳ'],
  ['Ê', 'Ể'],
  ['ê', 'ể'],
  ['Ô', 'Ổ'],
  ['ô', 'ổ'],
  ['Ơ', 'Ở'],
  ['ơ', 'ở'],
  ['Ư', 'Ử'],
  ['ư', 'ử'],
  ['E', 'Ẻ'],
  ['A', 'Ả'],
  ['O', 'Ỏ'],
  ['Y', 'Ỷ'],
  ['U', 'Ủ'],
  ['I', 'Ỉ'],
  ['e', 'ẻ'],
  ['a', 'ả'],
  ['o', 'ỏ'],
  ['y', 'ỷ'],
  ['u', 'ủ'],
  ['i', 'ỉ']],
 [['Â', 'Ẫ'],
  ['â', 'ẫ'],
  ['Ă', 'Ẵ'],
  ['ă', 'ẵ'],
  ['Ê', 'Ễ'],
  ['ê', 'ễ'],
  ['Ô', 'Ỗ'],
  ['ô', 'ỗ'],
  ['Ơ', 'Ỡ'],
  ['ơ', 'ỡ'],
  ['Ư', 'Ữ'],
  ['ư', 'ữ'],
  ['E', 'Ẽ'],
  ['A', 'Ã'],
  ['O', 'Õ'],
  ['Y', 'Ỹ'],
  ['U', 'Ũ'],
  ['I', 'Ĩ'],
  ['e', 'ẽ'],
  ['a', 'ã'],
  ['o', 'õ'],
  ['y', 'ỹ'],
  ['u', 'ũ'],
  ['i', 'ĩ']],
 [['Â', 'Ậ'],
  ['â', 'ậ'],
  ['Ă', 'Ặ'],
  ['ă', 'ặ'],
  ['Ê', 'Ệ'],
  ['ê', 'ệ'],
  ['Ô', 'Ộ'],
  ['ô', 'ộ'],
  ['Ơ', 'Ợ'],
  ['ơ', 'ợ'],
  ['Ư', 'Ự'],
  ['ư', 'ự'],
  ['E', 'Ẹ'],
  ['A', 'Ạ'],
  ['O', 'Ọ'],
  ['Y', 'Ỵ'],
  ['U', 'Ụ'],
  ['I', 'Ị'],
  ['e', 'ẹ'],
  ['a', 'ạ'],
  ['o', 'ọ'],
  ['y', 'ỵ'],
  ['u', 'ụ'],
  ['i', 'ị']]]

restore_vowels = [[['A', 'Â'],
  ['A', 'Â'],
  ['A', 'Â'],
  ['A', 'Â'],
  ['A', 'Â'],
  ['A', 'Â'],
  ['a', 'â'],
  ['a', 'â'],
  ['a', 'â'],
  ['a', 'â'],
  ['a', 'â'],
  ['a', 'â'],
  ['E', 'Ê'],
  ['E', 'Ê'],
  ['E', 'Ê'],
  ['E', 'Ê'],
  ['E', 'Ê'],
  ['E', 'Ê'],
  ['e', 'ê'],
  ['e', 'ê'],
  ['e', 'ê'],
  ['e', 'ê'],
  ['e', 'ê'],
  ['e', 'ê'],
  ['O', 'Ô'],
  ['O', 'Ô'],
  ['O', 'Ô'],
  ['O', 'Ô'],
  ['O', 'Ô'],
  ['O', 'Ô'],
  ['o', 'ô'],
  ['o', 'ô'],
  ['o', 'ô'],
  ['o', 'ô'],
  ['o', 'ô'],
  ['o', 'ô']],
 [['O', 'Ơ'],
  ['O', 'Ơ'],
  ['O', 'Ơ'],
  ['O', 'Ơ'],
  ['O', 'Ơ'],
  ['O', 'Ơ'],
  ['o', 'ơ'],
  ['o', 'ơ'],
  ['o', 'ơ'],
  ['o', 'ơ'],
  ['o', 'ơ'],
  ['o', 'ơ'],
  ['U', 'Ư'],
  ['U', 'Ư'],
  ['U', 'Ư'],
  ['U', 'Ư'],
  ['U', 'Ư'],
  ['U', 'Ư'],
  ['u', 'ư'],
  ['u', 'ư'],
  ['u', 'ư'],
  ['u', 'ư'],
  ['u', 'ư'],
  ['u', 'ư']],
 [['A', 'Ă'],
  ['A', 'Ă'],
  ['A', 'Ă'],
  ['A', 'Ă'],
  ['A', 'Ă'],
  ['A', 'Ă'],
  ['a', 'ă'],
  ['a', 'ă'],
  ['a', 'ă'],
  ['a', 'ă'],
  ['a', 'ă'],
  ['a', 'ă']],
 [['D', 'Đ'], ['d', 'đ']]]

fix_vowel = [('ơă', 'oă'), ('ưă', 'ưa'),
             ('ưư', 'ưu'), ('ươư', 'ươu')]

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
    vowel status: 0 a,o,u, 1 â,ô, 2 ă,ơ,ư,
    tone status: 0 a, 1 à, 2 á, 3 ả, 4 ã, 5 ạ
    """
    s = s.lower()
    s = toviqr(s)
    d_status = 'dd' in s
    # vowel_status = 'dd' in s

    vowel_status = [i for i, v in vowel_spec_chars if v in s]
    tone_status = [i for i, v in tone_spec_chars if v in s]

    vowel_status = 0 if len(vowel_status) == 0 else (
        1 if vowel_status[0] == 1 else 2)
    tone_status = 0 if not tone_status else tone_status[0]+1
    return int(d_status), vowel_status, tone_status
    # tone_status=

def str_multi_replace(s, replaces):
    """
    Args:
    s: source string
    replaces: ((old1,new1),(old2,new2)...)
    """
    for i, j in replaces:
        s = s.replace(i, j)
    return s


def str_multi_replace_one(s, replaces):
    """
    Args:
    s: source string
    replaces: ((old1,new1),(old2,new2)...)
    stop when replace match
    """
    if s is None:
        return s
    for i, j in replaces:
        if i in s:
            return s.replace(i, j)
    return s


def restore_tone_with_status(s, status):
    d_status, vowel_status, tone_status = status

    if d_status:
        s = str_multi_replace_one(s, restore_vowels[3])

    if vowel_status:
        s = str_multi_replace(s, restore_vowels[vowel_status-1])
        if vowel_status == 2:
            s = str_multi_replace(s, restore_vowels[2])
        s = str_multi_replace(s, fix_vowel)

    if tone_status:
        s = str_multi_replace_one(s, restore_tones[tone_status-1])
    return s


# s = 'Đửa'
# restore_tone_with_status(bodau(s), get_status(s))
