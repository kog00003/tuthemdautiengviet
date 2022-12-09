# vinlp-themdautiengviet

<h1>building model tự thêm dấu cho tiếng việt</h1>

on processing...

không dùng vocal/dictionary encode như thông thường nlp

<h3>data in:</h3>

không dùng cả câu chỉ dùng 3 chữ (chữ trước, chữ hiện tãi(cần thêm dấu), chữ tiếp theo)

<h3>encode chữ: </h3>

tách chữ thành: (phụ âm - nguyên âm - phụ âm cuối), đánh số cho từng giá trị.

?Tại sao: chữ có cùng nguyên/phụ âm có thể dấu cũng tương tự, không cần vocal file.

ex: toi la ai -> (15, 18, 15) (8, 1, 15) (31, 7, 15)

chuyển tất cả số sang binary (0,1,0...)

<h3>label:</h3>

Predict phụ âm (d/đ), nguyên âm (a,ă,â), dấu riêng rẽ: dùng score-softmax(CrossEntropy)
 
2 out cho d/đ

3 out cho a,ă,â..

6 out cho dấu


<h3>model:</h3>

simple chỉ linear+relu: đạt 90% accurate với 100K Params, training ~ 3M samples trong 15 phút trên colab.

rnn,lstm,tranformer next...
