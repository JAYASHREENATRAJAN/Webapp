%DIGITAL CHEBYSHEV LOWPASS FILTER USING IMPULSE INVARIENCE
clc;
ap=1;
as=15;
wp=0.2*pi;
ws=0.3*pi;
f=1;
[N,wc]=cheb1ord(wp,ws,ap,as,'s');
fprintf('the order of filter:%d\n',N);
fprintf('the cut off frequency:%d\n',wc);
[b,a]=cheby1(N,ap,wc,'low','s');
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