import re


def is_vietnamese_without_accent_word(s):
    pattern = '^(b|c|k|d|g|gh|h|l|m|n|p|q|r|s|t|v|x|ch|kh|ng|ngh|nh|ph|th|tr){0,1}(a|e|i|o|u|y|ai|ao|au|ay|eo|eu|ia|ie|iu|oa|oe|oi|oo|ua|ui|uo|uy|uu|ieu|oai|oao|oay|oeo|uay|uoi|uya|uye|uyu|uoi|uou){1}(c|ch|ng|nh|m|n|p|t){0,1}$'
    return re.match(pattern, s) is not None


def is_vietnamese_word(s):
    pattern = '^(b|c|k|d|đ|g|gh|h|l|m|n|p|q|r|s|t|v|x|ch|kh|ng|ngh|nh|ph|th|tr){0,1}(a|ă|â|e|ê|i|o|ô|ơ|u|ư|y|ai|ao|au|ay|âu|ây|eo|êu|ia|iê|iu|oa|oă|oe|oi|oo|ôi|ơi|ua|uâ|ui|uô|ươ|uy|ưa|uơ|ưi|ươ|ưu|iêu|oai|oao|oay|oeo|uay|uây|uôi|uya|uyê|uyu|ươi|ươu){1}(c|ch|ng|nh|m|n|p|t){0,1}$'
    return re.match(pattern, s) is not None


moads = 'a ă â e ê i o ô ơ u ư y'.split()
dyads = 'ai ao au ay âu ây eo êu ia iê iu oa oă oe oi oo ôi ơi ua uâ ui uô ươ uy ưa uơ ưi ươ ưu'.split()
triads = 'iêu oai oao oay oeo uay uây uôi uya uyê uyu ươi ươu'.split()
consonants = 'b c k d đ g gh h l m n p q r s t v x ch kh ng ngh nh ph th tr'.split()
finals = 'c ch ng nh m n p t'.split()

# '|'.join((*moads, *dyads, *triads))
# '|'.join((*consonants,))
# '|'.join((*finals,))

# is_vietnamese_without_accent_word('nha')
