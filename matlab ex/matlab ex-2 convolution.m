% linear convolution
clc;
close all;
x=input('Enter the sequence x:');
h=input('Enter the sequence h:');
y=conv(x,h);
subplot(3,1,1);
stem(x);
title('input sequence');
subplot(3,1,2);
stem(h);
title('input sequence');
subplot(3,1,3);
stem(y);
title('output sequence for linear convolution');
y

