# tuthemdautiengviet

<h1>building model tự thêm dấu cho tiếng việt</h1>

on progressing...

demo

https://htmlpreview.github.io/?https://github.com/kog00003/tuthemdautiengviet/blob/main/js_version/index.html

<h3>data in:</h3>

không dùng cả câu chỉ dùng 3 chữ (chữ trước, chữ hiện tãi(cần thêm dấu), chữ tiếp theo)

<h3>encode chữ: </h3>

tách chữ thành: (phụ âm - nguyên âm - phụ âm cuối), đánh số (by position) cho từng giá trị.

?Tại sao: chữ có cùng nguyên/phụ âm có thể dấu cũng tương tự, không cần vocal file.

ex: toi la ai -> (15, 18, 15) (8, 1, 15) (31, 7, 15)

chuyển tất cả số sang binary (0,1,0...)

<h3>label:</h3>

Predict phụ âm (d/đ), nguyên âm (a,ă,â), dấu riêng rẽ: dùng score-softmax (CrossEntropy)
 
2 output cho d/đ

3 output cho a,ă,â..

6 output cho dấu


<h3>training/model:</h3>

condition: limit ~ 150K weights/params, with 6M samples, colab gpu

test 1:

(linear128, norm, relu) x 8 ~ 30 minutes : ~91% accurates

test 2:

RNN residual (drop output, stack all hidden data with x) - LinearNormRelu

89% accurates with only 75K params

93% with 150K



