%DIGITAL BUTTERWORTH LOWPASS FILTER USING IMPULSE INVARIENCE
clc;
ap=3;
as=25;
wp=0.2*pi;
ws=0.45*pi;
f=1;
[N,wc]=buttord(wp,ws,ap,as,'s');
fprintf('the order of filter:%d\n',N);
fprintf('the cut off frequency:%d\n',wc);
[b,a]=butter(N,wc,'low','s');
disp('the numerator term of analog filter transfer function Ha(s)');
b
disp('the denominator term of analog filter transfer function Ha(s)');
a
[bz,az]=impinvar(b,a);
freqz(bz,az);
title('digital butterworth low pass filter using impulse invarience');
disp('the numerator term of digital filter transfer function H(z)');
bz
disp('the denominator term of digital filter transfer function H(z)');
az