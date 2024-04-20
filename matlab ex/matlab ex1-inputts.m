% discrete time signals
clc;
clear all;
t=-3:1:3;
y=[zeros(1,3),ones(1,1),zeros(1,3)];
subplot(3,2,1);
stem(t,y);
xlabel('n');
ylabel('y(n)');
title('unit impulse signal');

t=-3:1:4;
y=[zeros(1,3),ones(1,5)];
subplot(3,2,2);
stem(t,y);
xlabel('n');
ylabel('y(n)');
title('unit step signal');

t=0:1:4;
y=t;
subplot(3,2,3);
stem(t,y);
xlabel('n');
ylabel('y(n)');
title('ramp signal');

t=0:.1:5;
a=2
y=exp(a*t);
subplot(3,2,4);
stem(t,y);
xlabel('n');
ylabel('y(n)');
title('Exponential signal');

t=0:.01:5;
y=sin(2*pi*t);
subplot(3,2,5);
stem(t,y);
xlabel('n');
ylabel('y(n)');
title('sinusoidal signal');

t=0:.01:5;
y=cos(2*pi*t);
subplot(3,2,6);
stem(t,y);
xlabel('n');
ylabel('y(n)');
title('cosin signal');

% continuous time signals
clc;
clear all;
t=-3:1:3;
y=[zeros(1,3),ones(1,1),zeros(1,3)];
subplot(3,2,1);
plot(t,y);
xlabel('t');
ylabel('y(t)');
title('unit impulse signal');

t=-3:1:4;
y=[zeros(1,3),ones(1,5)];
subplot(3,2,2);
plot(t,y);
xlabel('t');
ylabel('y(t)');
title('unit step signal');

t=0:1:4;
y=t;
subplot(3,2,3);
plot(t,y);
xlabel('t');
ylabel('y(t)');
title('ramp signal');

t=0:.1:5;
a=2
y=exp(a*t);
subplot(3,2,4);
plot(t,y);
xlabel('t');
ylabel('y(t)');
title('Exponential signal');

t=0:.01:5;
y=sin(2*pi*t);
subplot(3,2,5);
plot(t,y);
xlabel('t');
ylabel('y(t)');
title('sinusoidal signal');

t=0:.01:5;
y=cos(2*pi*t);
subplot(3,2,6);
plot(t,y);
xlabel('t');
ylabel('y(t)');
title('cosin signal');


