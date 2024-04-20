%DIGITAL BUTTERWORTH LOWPASS FILTER USING BILINEAR TRANSFORMATION
clc;
ap=3;
as=25;
wp=0.2*pi;
ws=0.45*pi;
f=1;
POP=2*f*tan(wp/2);
POS=2*f*tan(ws/2);
[N,wc]=buttord(POP,POS,ap,as,'s');
fprintf('the order of filter:%d\n',wc);
[b,a]=butter(N,wc,'low','s');
disp('the numerator term of analog filter transfer function Ha(s)');
b
disp('the denominator term of analog filter transfer function Ha(s)');
a
[bz,az]=bilinear(b,a,f);
freqz(bz,az);
title('digital butterworth low pass filter using bilinear transformation');
disp('the numerator term of digital filter transfer function H(z)');
bz
disp('the denominator term of digital filter transfer function H(z)');
az
