%DIGITAL CHEBYSHEV LOWPASS FILTER USING BILINEAR TRANSFORMATION
clc;
ap=1;
as=15;
wp=0.2*pi;
ws=0.3*pi;
f=1;
POP=2*f*tan(wp/2);
POS=2*f*tan(ws/2);
[N,wc]=cheb1ord(POP,POS,ap,as,'s');
fprintf('the order of filter:%d\n',N);
fprintf('the cut off frequency:%d\n',wc);
[b,a]=cheby1(N,ap,wc,'low','s');
disp('the numerator term of analog filter transfer function Ha(s)');
b
disp('the denominator term of analog filter transfer function Ha(s)');
a
[bz,az]=bilinear(b,a,f);
freqz(bz,az);
title('digital chebyshev low pass filter using bilinear transformatiobn');
disp('the numerator term of digital filter transfer function H(z)');
bz
disp('the denominator term of digital filter transfer function H(z)');
az