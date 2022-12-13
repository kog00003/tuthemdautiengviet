

// encode_decode_match.py



function split_to_con_vow_fin(s) {
  pattern = /^(b|c|k|d|g|gh|h|l|m|n|p|q|r|s|t|v|x|ch|kh|ng|ngh|nh|ph|th|tr|gi){0,1}(a|e|i|o|u|y|ai|ao|au|ay|eo|eu|ia|ie|iu|oa|oe|oi|oo|ua|ui|uo|uy|uu|ieu|oai|oao|oay|oeo|uay|uoi|uya|uye|uyu|uoi|uou){1}(c|ch|ng|nh|m|n|p|t){0,1}$/i
  // m = re.match(pattern, s, flags=re.IGNORECASE)
  // return m if not m else [m.group(i) for i in (1, 2, 3)]
  m = s.match(pattern)
  if (m == null) return null
  return m.slice(1, 4)
}

// console.log(split_to_con_vow_fin('dnhanh'))


// na_con = 'b|c|k|d|g|gh|h|l|m|n|p|q|r|s|t|v|x|ch|kh|ng|ngh|nh|ph|th|tr|gi'.split(
//   '|')
// na_vow = 'a|e|i|o|u|y|ai|ao|au|ay|eo|eu|ia|ie|iu|oa|oe|oi|oo|ua|ui|uo|uy|uu|ieu|oai|oao|oay|oeo|uay|uoi|uya|uye|uyu|uoi|uou'.split(
//   '|')
// na_fin = 'c|ch|ng|nh|m|n|p|t'.split('|')
// na_con = {j: i+1 for i, j in enumerate(na_con)}
// na_vow = {j: i+1 for i, j in enumerate(na_vow)}
// na_fin = {j: i+1 for i, j in enumerate(na_fin)}
// na_cond = {i+1: j for i, j in enumerate(na_con)}
// na_vowd = {i+1: j for i, j in enumerate(na_vow)}
// na_find = {i+1: j for i, j in enumerate(na_fin)}

let na_con = {
  'b': 1,
  'c': 2,
  'k': 3,
  'd': 4,
  'g': 5,
  'gh': 6,
  'h': 7,
  'l': 8,
  'm': 9,
  'n': 10,
  'p': 11,
  'q': 12,
  'r': 13,
  's': 14,
  't': 15,
  'v': 16,
  'x': 17,
  'ch': 18,
  'kh': 19,
  'ng': 20,
  'ngh': 21,
  'nh': 22,
  'ph': 23,
  'th': 24,
  'tr': 25,
  'gi': 26
}
let na_vow = {
  'a': 1,
  'e': 2,
  'i': 3,
  'o': 4,
  'u': 5,
  'y': 6,
  'ai': 7,
  'ao': 8,
  'au': 9,
  'ay': 10,
  'eo': 11,
  'eu': 12,
  'ia': 13,
  'ie': 14,
  'iu': 15,
  'oa': 16,
  'oe': 17,
  'oi': 18,
  'oo': 19,
  'ua': 20,
  'ui': 21,
  'uo': 22,
  'uy': 23,
  'uu': 24,
  'ieu': 25,
  'oai': 26,
  'oao': 27,
  'oay': 28,
  'oeo': 29,
  'uay': 30,
  'uoi': 35,
  'uya': 32,
  'uye': 33,
  'uyu': 34,
  'uou': 36
}
let na_fin = { 'c': 1, 'ch': 2, 'ng': 3, 'nh': 4, 'm': 5, 'n': 6, 'p': 7, 't': 8 }

let bodau_rep = [['á', 'a'],
['à', 'a'],
['ạ', 'a'],
['ả', 'a'],
['ã', 'a'],
['â', 'a'],
['ấ', 'a'],
['ầ', 'a'],
['ậ', 'a'],
['ẩ', 'a'],
['ẫ', 'a'],
['ă', 'a'],
['ắ', 'a'],
['ằ', 'a'],
['ặ', 'a'],
['ẳ', 'a'],
['ẵ', 'a'],
['Á', 'A'],
['À', 'A'],
['Ạ', 'A'],
['Ả', 'A'],
['Ã', 'A'],
['Â', 'A'],
['Ấ', 'A'],
['Ầ', 'A'],
['Ậ', 'A'],
['Ẩ', 'A'],
['Ẫ', 'A'],
['Ă', 'A'],
['Ắ', 'A'],
['Ằ', 'A'],
['Ặ', 'A'],
['Ẳ', 'A'],
['Ẵ', 'A'],
['é', 'e'],
['è', 'e'],
['ẹ', 'e'],
['ẻ', 'e'],
['ẽ', 'e'],
['ê', 'e'],
['ế', 'e'],
['ề', 'e'],
['ệ', 'e'],
['ể', 'e'],
['ễ', 'e'],
['É', 'E'],
['È', 'E'],
['Ẹ', 'E'],
['Ẻ', 'E'],
['Ẽ', 'E'],
['Ê', 'E'],
['Ế', 'E'],
['Ề', 'E'],
['Ệ', 'E'],
['Ể', 'E'],
['Ễ', 'E'],
['ó', 'o'],
['ò', 'o'],
['ọ', 'o'],
['ỏ', 'o'],
['õ', 'o'],
['ô', 'o'],
['ố', 'o'],
['ồ', 'o'],
['ộ', 'o'],
['ổ', 'o'],
['ỗ', 'o'],
['ơ', 'o'],
['ớ', 'o'],
['ờ', 'o'],
['ợ', 'o'],
['ở', 'o'],
['ỡ', 'o'],
['Ó', 'O'],
['Ò', 'O'],
['Ọ', 'O'],
['Ỏ', 'O'],
['Õ', 'O'],
['Ô', 'O'],
['Ố', 'O'],
['Ồ', 'O'],
['Ộ', 'O'],
['Ổ', 'O'],
['Ỗ', 'O'],
['Ơ', 'O'],
['Ớ', 'O'],
['Ờ', 'O'],
['Ợ', 'O'],
['Ở', 'O'],
['Ỡ', 'O'],
['ú', 'u'],
['ù', 'u'],
['ụ', 'u'],
['ủ', 'u'],
['ũ', 'u'],
['ư', 'u'],
['ứ', 'u'],
['ừ', 'u'],
['ự', 'u'],
['ử', 'u'],
['ữ', 'u'],
['Ú', 'U'],
['Ù', 'U'],
['Ụ', 'U'],
['Ủ', 'U'],
['Ũ', 'U'],
['Ư', 'U'],
['Ứ', 'U'],
['Ừ', 'U'],
['Ự', 'U'],
['Ử', 'U'],
['Ữ', 'U'],
['í', 'i'],
['ì', 'i'],
['ị', 'i'],
['ỉ', 'i'],
['ĩ', 'i'],
['Í', 'I'],
['Ì', 'I'],
['Ị', 'I'],
['Ỉ', 'I'],
['Ĩ', 'I'],
['đ', 'd'],
['Đ', 'D'],
['ý', 'y'],
['ỳ', 'y'],
['ỵ', 'y'],
['ỷ', 'y'],
['ỹ', 'y'],
['Ý', 'Y'],
['Ỳ', 'Y'],
['Ỵ', 'Y'],
['Ỷ', 'Y'],
['Ỹ', 'Y']]
// # split_to_con_vow_fin('gioi')

function is_vietnamese_without_accent_word(s) {
  return (split_to_con_vow_fin(s) != null)
}

function isnumeric(s) {
  return !isNaN(s)
}

// console.log(isnumeric('a44244'))

function encode_word_no_accent(s) {
  if (s == null)
    return [0, 1, 0]
  else if (isnumeric(s))
    return [0, 2, 0]
  a = split_to_con_vow_fin(s)
  if (a == null)
    return [0, 3, 0]

  con = a[0]
  vow = a[1]
  fin = a[2]
  con = con ? na_con[con.toLowerCase()] : 31
  vow = vow ? na_vow[vow.toLowerCase()] : 63
  fin = fin ? na_fin[fin.toLowerCase()] : 15
  return [con, vow, fin]
}

// console.log(encode_word_no_accent('nhanh'));





function to_bin_vector(input_number, length) {
  // s = f'{{:0{length}b}}'.format(input_number)
  // return list(map(lambda x: 0 if x == '0' else 1, s))
  s = (input_number >>> 0).toString(2)
  prefix = '0'.repeat(length - s.length)
  return Array.from(prefix + s).map((x) => parseInt(x) || 0)
}

// console.log(to_bin_vector(125,10))

function encode_word_no_accent_binary(s) {
  // """
  // example:
  // encode_word_no_accent_binary('viet')

  // return: bin vector length 15
  // [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0]
  // """
  a = encode_word_no_accent(s)
  // # (16,14,8) for viet
  l = [5, 6, 4]
  // # length bin vector for con max 25, vow max 35, fin max 8
  arr = []
  for (k in a) {
    i = a[k]
    j = l[k]
    for (k of to_bin_vector(i, j)) arr.push(k)
  }
  return arr
  // return [k for i, j in zip(a, l) for k in to_bin_vector(i, j)]

}

// console.log(encode_word_no_accent_binary('viet'));


function decode_word_no_accent(v) {
  con = v[0]
  vow = v[1]
  fin = v[2]
  return [na_cond[con], na_vowd[vow], na_find[fin]].join('')
}

function clean_text(s) {
  // if s is None:
  //     return None
  // """keep only unicode vn and 0-9"""
  return s.replaceAll(/[^a-zA-Z0-9\u00c0-\u1ef9]/g, '')
}

// console.log(clean_text('Nhafdaf78473*&*(^9743'));
// label_and_restore.py


let restore_tones = [[['Â', 'Ầ'],
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

let restore_vowels = [[['A', 'Â'],
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

let fix_vowel = [('ơă', 'oă'), ('ưă', 'ưa'),
('ưư', 'ưu'), ('ươư', 'ươu')]


function str_multi_replace(s, replaces) {
  for (k of replaces) {
    i = k[0]
    j = k[1]
    s = s.replaceAll(i, j)
  }
  return s
}



// console.log(str_multi_replace('viet',[['v','x'],['i','j']]));


function str_multi_replace_one(s, replaces) {
  if (s == null) return s
  for (k of replaces) {
    i = k[0]
    j = k[1]
    if (s.includes(i)) {
      return s.replaceAll(i, j)
    }
  }
  return s
}

// console.log(str_multi_replace_one('viet',[['v','x'],['i','j']]));

function restore_tone_with_status(s, status) {
  d_status = status[0]
  vowel_status = status[1]
  tone_status = status[2]

  if (d_status)
    s = str_multi_replace_one(s, restore_vowels[3])

  if (vowel_status) {
    s = str_multi_replace(s, restore_vowels[vowel_status - 1])
    if (vowel_status == 2)
      s = str_multi_replace(s, restore_vowels[2])
    s = str_multi_replace(s, fix_vowel)
  }
  if (tone_status)
    s = str_multi_replace_one(s, restore_tones[tone_status - 1])
  return s
}



// console.log(restore_tone_with_status('viet', [0, 1, 6]));





// var m1 = [[1, 2], [3, 4]]
// var m2 = [[5, 6], [7, 8]]

// var mResult = multiplyMatrices(m1, m2)


// console.table(mResult) /* it shows the matrix in a table */



function sliding_window(inputArray, size) {
  //to do
  return Array.from(
    { length: inputArray.length - (size - 1) }, //get the appropriate length
    (_, index) => inputArray.slice(index, index + size) //create the windows
  )
}


// console.log(sliding_window([1, 2, 3, 4, 5, 6], 2));
// [ [ 1, 2 ], [ 2, 3 ], [ 3, 4 ], [ 4, 5 ], [ 5, 6 ] ]


function array_split_by_position(arr, positions) {

  // arr = [1, 2, 3, 4, 5, 6, 7, 8]
  // positions = [2, 5]
  if (positions[0] > 0)
    positions.unshift(0)
  if (positions.slice(-1)[0] < arr.length)
    positions.push(arr.length)
  // console.log((positions));
  s = sliding_window(positions, 2).map((x) => {
    // console.log(x);
    return arr.slice(x[0], x[1])
  })
  // console.log(s);
  return s
  // return [arr[i:j] for i, j in more_itertools.sliding_window(positions, 2)]
}

// [2, 6].length
// console.log([2, 6].slice(-1)[0] < 5);
// console.log(array_split_by_position([1, 2, 3, 4, 5, 6], [2, 6]));




function bodau(x) {
  return str_multi_replace(x, bodau_rep)
}

// console.log(bodau('Giá xăng về sát'));

function restore_with_model(words) {

  prevW = words[0]
  currW = words[1]
  nextW = words[2]
  // return currW
  if (!is_vietnamese_without_accent_word(clean_text(currW)))
    return currW
  // multi_positions = [[0, 2], [2, 5], [5, 11]]
  words = [prevW ? bodau(clean_text(prevW)) : null, currW ? bodau(clean_text(currW)) : null, nextW ? bodau(clean_text(nextW)) : null]

  x = []
  for (w of words) {
    for (i of encode_word_no_accent_binary(w)) {
      x.push(i)
    }
  }
  stat = predict(x)
  return restore_tone_with_status(currW, stat)
}

// console.log(restore_with_model(['toi', 'la', 'ai']));

let end_segment_chars = ['.', ',', ':', '!']

function them_dau_with_model(s) {
  // ss = s.split()
  // samples = []
  // split_positions = [pos+1 for pos,
  //                    i in enumerate(ss) if i[-1] in end_segment_chars]
  // if split_positions:
  //     ss = array_split_by_position(ss, split_positions)
  // else:
  //     ss = [ss, ]
  // for arr in ss:
  //     arr.insert(0, None)
  //     arr.append(None)
  //     samples.extend(list(more_itertools.sliding_window(arr, 3)))
  // # print(samples)
  // return ' '.join([restore_with_model(model, *i)
  //                  for i in samples])
  ss = s.split(' ')

  samples = []
  split_positions = []

  for (pos in ss) {
    i = ss[pos]
    if (end_segment_chars.includes(i.slice(-1)[0]))
      split_positions.push(pos + 1)
  }
  if (split_positions.length > 0)
    ss = array_split_by_position(ss, split_positions)
  else
    ss = [ss,]
  // console.log(ss);
  for (arr of ss) {
    arr.unshift(null)
    arr.push(null)
    // samples = samples.concat(sliding_window(arr, 3))
    samples.push(...sliding_window(arr, 3))
    // console.log(sliding_window(arr, 3));
  }
  // console.log(samples);
  return samples.map((i) => { return restore_with_model(i) }).join(' ')
}
// s = 'ddd adfad '.split(' ')
// s = them_dau_with_model('hom nay la thu hai, mai la thu ba')
// console.log(s);



function addArray(x, y) {
  return x.map((v, i) => v + y[i])
}

function minusArray(x, y) {
  return x.map((v, i) => v - y[i])
}

function multiplyArray(x, y) {
  return x.map((v, i) => v * y[i])
}
function divideArray(x, y) {
  return x.map((v, i) => v / y[i])
}

// s = addArray([1, 2, 3], [4, 5, 6])
// console.log(s);

function sqrtArray(x) {
  return x.map((v) => Math.sqrt(v))
}
// s = sqrtArray([1, 2, 3])
// console.log(s);

function addArrayWithNumber(arr_x, y) {
  return arr_x.map((v) => v + y)
}

// s = addArrayWithNumber([1, 2, 3], 2)
// console.log(s);

function addMatix(x, y) {
  return x.map((v, i) => addArray(v, y[i]))
}


function transpose(array) {
  return array[0].map((_, colIndex) => array.map(row => row[colIndex]));
}

// console.log(transpose([[1, 2], [3, 4]]));
// 1 3 2 4

// function multiplyMatrices(m1, m2) {
//   var result = [];
//   for (var i = 0; i < m1.length; i++) {
//     result[i] = [];
//     for (var j = 0; j < m2[0].length; j++) {
//       var sum = 0;
//       for (var k = 0; k < m1[0].length; k++) {
//         sum += m1[i][k] * m2[k][j];
//       }
//       result[i][j] = sum;
//     }
//   }
//   return result;
// }



// s = addMatix([[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [4, 5, 6]])
// console.log(s);

function nn_linear(x, weight, bias) {
  // return torch.matmul(x, weight.T + bias)
  x = multiplyMatrices(x, transpose(weight))
  return matrixAddArray(x, bias)
}

function nn_relu(x) {
  // x matrix
  // x[x < 0] = 0
  // return x
  return x.map((v) => { return v.map((z) => z < 0 ? 0 : z) })
}

function matrixMinusArray(x, y) {
  return x.map((v) => minusArray(v, y))
}

function matrixMultiplyArray(x, y) {
  return x.map((v) => multiplyArray(v, y))
}


function matrixAddArray(x, y) {
  return x.map((v) => addArray(v, y))
}

function matrixDivideArray(x, y) {
  return x.map((v) => divideArray(v, y))
}

// s = nn_relu([1, -4, 3, 4, -1, 6])
// console.log(s);

function nn_norm(x, weight, bias, mean, variant) {
  // return ((x-mean) / torch.sqrt(var + 1e-5)) * weight + bias
  x = matrixMinusArray(x, mean)
  // console.log(x.length);
  x = matrixDivideArray(x, sqrtArray(addArrayWithNumber(variant, 0)))
  x = matrixMultiplyArray(x, weight)
  x = matrixAddArray(x, bias)
  return x
}


function sumArray(x) {
  return x.reduce((partialSum, a) => partialSum + a, 0)
}
// s = sumArray([1, 2, 3])
// console.log(s);

function getColumn(x, col_index) {
  return x.map((v) => v[col_index])
}

// s = getColumn([[1, 2, 3], [1, 2, 3]], 1)
// console.log(s);
// function multiplyMatrices(m1, m2) {
//   var result = [];
//   for (var i = 0; i < m1.length; i++) {
//     result[i] = [];
//     for (var j = 0; j < m2[0].length; j++) {
//       var sum = 0;
//       for (var k = 0; k < m1[0].length; k++) {
//         sum += m1[i][k] * m2[k][j];
//       }
//       result[i][j] = sum;
//     }
//   }
//   return result;
// }

function multiplyMatrices(x, y) {
  return x.map((v) => {
    return transpose(y).map((z) => sumArray(multiplyArray(v, z)))
  })
}



// var model = require("model.json");
var model = null

fetch('model.json')
  .then((response) => response.json())
  .then((json) => { console.log(json.length); model = json });


// x = [[0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]]


// console.log(model[0][0]);
// for 
// weight = model[0][1][0]
// bias = model[0][1][1]

// nweight = model[1][1][0]
// nbias = model[1][1][1]
// nmean = model[1][1][2]
// nvar = model[1][1][3]

// addArrayWithNumber(nvar, 1)
// console.log(nmean);
// console.log(weight.length);
// console.log(bias.length);
function applyLayer(x, layerData) {
  i = layerData
  // console.log(i[0]);
  if (i[0] == 'linear') x = nn_linear(x, ...i[1])
  else if (i[0] == 'norm') x = nn_norm(x, ...(i[1].slice(0, 4)))
  else if (i[0] == 'relu') x = nn_relu(x)
  return x
}



function argMax(array) {
  return array.map((x, i) => [x, i]).reduce((r, a) => (a[0] > r[0] ? a : r))[1];
}

// console.log(model[1][1].slice(0, 4).length)

// x = applyLayer(x, model[0])
// x = applyLayer(x, model[1])
// x = applyLayer(x, model[2])
// x = nn_norm(x, ...(model[1][1].slice(0, 4)))
// x = nn_norm(x, nweight, nbias, nmean, nvar)
// console.log(x[0]);

// y = array_split_by_position(x[0], [2, 5])
// y = y.map((v) => argMax(v))
// console.log(y);


function predict(x) {
  x = [x]
  for (i of model) {
    x = applyLayer(x, i)
  }
  y = array_split_by_position(x[0], [2, 5])
  y = y.map((v) => argMax(v))
  return y
}

// s = them_dau_with_model('vi sao anh khong den ben toi')
// console.log(s);
