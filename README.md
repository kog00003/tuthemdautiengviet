# vinlp-themdautiengviet

training model tự thêm dấu

on processing...

không dùng vocal/dictionary encode như thông thường nlp

data in:

không dùng cả câu chỉ dùng 3 chữ (chữ trước, chữ hiện tãi(cần thêm dấu), chữ tiếp theo)

encode chữ: 

tách chữ thành: (phụ âm - nguyên âm - phụ âm cuối), đánh số cho từng giá trị.

?Tại sao: chữ có cùng nguyên/phụ âm có thể dấu cũng tương tự, không cần vocal file.

ex: toi la ai -> (15, 18, 15) (8, 1, 15) (31, 7, 15)

chuyển tất cả số sang binary (0,1,0...)

label:

Predict phụ âm (d/đ), nguyên âm (a,ă,â), dấu riêng rẽ: dùng score-softmax(CrossEntropy)
 
2 out cho d/đ

3 out cho a,ă,â..

6 out cho dấu


model:

simple chỉ linear+relu: đạt 90% accurate với 100K Params, training 15 phút trên colab.

rnn,lstm,tranformer next...
