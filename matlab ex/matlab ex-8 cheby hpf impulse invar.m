%DIGITAL BUTTER WORTH HIGH PASS FILTER USING IMPULSE INVARIENCE
clc;
ap=3;
as=10;
fp=1000;
fs=3
50;
f=5000;
wp=(2*pi*fp)/f;
ws=(2*pi*fs)/f;
[N,wc]=buttord(wp,ws,ap,as,'s');
fprintf('the order of filter:%d\n',N);
fprintf('the cut off frequency:%d\n',wc);
[b,a]=butter(N,wc,'high','s');
disp('the numerator term of analog filter transfer function Ha(s)');
b
disp('the denominator term of analog filter transfer function Ha(s)');
a
[bz,az]=impinvar(b,a);
freqz(bz,az);
title('digital chebyshev low pass filter using impulse invarience');
disp('the numerator term of digital filter transfer function H(z)');
bz
disp('the denominator term of digital filter transfer function H(z)');
az