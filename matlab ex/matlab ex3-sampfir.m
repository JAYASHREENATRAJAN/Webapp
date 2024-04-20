%FIR LPF USING FREQUENCY SAMPLING METHODE
clc;
clear;
close all;
n=33;
alpha=(n-1)/2;
hrk=[ones(1,9),0.5,zeros(1,14),0.5,ones(1,8)];
k1=0:(n-1)/2;
k2=(n+1)/2:n-1;
theetak=[(-alpha*(2*pi)/n)*k1,(alpha*(2*pi)/n)*(n-k2)];
hk=hrk.*(exp(1i*theetak));
hn=real(ifft(hk,n));
w=0:0.01:pi;
h=freqz(hn,1,w);
plot(w/pi,20*log10(abs(h)));
ylabel('magnitude in db');
xlabel('normalised frequency');
title('FIR lpf using frequency sampling method');
hold on;
