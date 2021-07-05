import control.matlab as c
import matplotlib.pyplot as plt
import sys
import numpy as np
from sympy import *
import math
koc=-0.4
ky=22
Tg=10.0
Ty=4.0
Tgm=1.0
f=True
tline=[]
for i in range(0, 10000,10):
   tline.append(i/1000)
w1=c.tf([koc,0],[1])
print("W1(p)=",w1)
w2=c.tf([1],[Tg,1])
print("W2(p)=",w2)
w3=c.tf([Tgm*0.01,1],[Tg*0.05,1])
print("W3(p)=",w3)
w4=c.tf([ky],[Ty,1])
print("W4(p)=",w4)
w5=c.series(w3, w4, w2)

w=c.feedback(w5,w1)
print('W(p)=',w)
#Переходная характеристика
t = np.linspace(100, stop=300)
size = (10, 10)
plt.figure(1, figsize=size)
y1, x1 = c.step(w, t)
lines = [y1]
lines[0] = plt.plot(t, y1, "b",)
plt.legend()
plt.title('Переходная характеристика')
plt.ylabel('Амплитуда')
plt.xlabel('Время(с)')
plt.grid(True)
plt.show()

#Проверка по корням характеристического уравнения
s=c.pole(w)
for i in s:
    print(i, "  ")
    if (i.real>=0):
        f=false
if f==true:
   print("Система устойчива")
else:
   print("Не устойчива")
c.pzmap (w)
plt.axis([-1, 0.1, -1, 1])
plt.show()

#Разомкнутая САУ
w7=c.series(w1,w2,w3,w4)
print("W7(p)=", w7)




#Критерий Найквиста и Лачх#
real1,imag1,freg1=c.nyquist(w7)
plt.vlines(-1, -3, 3,
          color = 'r',
          linewidth = 1,
          linestyle = '--')
circle1=plt.Circle((0,0),1,color='r', fill=False)
plt.axis([-1.5, 1.5, -1.5, 1.5])
plt.grid(True)
plt.gcf().gca().add_artist(circle1)
plt.show()

#ЛАЧХ И ЛФЧХ
mag,phase,omega = c.bode(w7,tline,dB=True)
plt.plot()
plt.show()

####Получение массива коэффи. и характери уравнения с jw####
v=symbols('v', real=True)
z=w.den
t=1
f=0
s=[0]
for i in z[0]:
     for l in i:
       k=len(i)-t
       f=f+l*(I*v)**k
       t=t+1
       s.append(l)
print(f)
print()
####Годограф Михайлова#####
zr=re(f)
zm=im(f)
print("Действительная часть", zr)
print("Мнимая часть", zm)
x=[zr.subs({v:q}) for q in np.arange(0, 100, 0.1)]
y=[zm.subs({v:q}) for q in np.arange(0, 100, 0.1)]
plt.vlines(0, -10, 10,
          color = 'r',
          linewidth = 1,
          linestyle = '-')
plt.hlines(0, -60, 10,
          color = 'r',
          linewidth = 1,
          linestyle = '-')
plt.axis([-60.0, 5.0, -10.0, 20.0])
plt.plot(x, y)
plt.grid(True)
plt.show()
###############################
# Создание и заполнение матрица по Гурвицу+расчет определителя###
# a=np.zeros((len(s)-2, len(s)-2))
#Формируем массив указанного массива заполненного нулями
#
# a[0][0]=47.09;
# a[0][1]=1;
# a[0][2]=0;
#
# a[1][0]=20;
# a[1][1]=23.3;
# a[1][2]=0;
#
# a[2][0]=0;
# a[2][1]=47.09;
# a[2][2]=1;
#
# l=(20*1)/23.3
# m=(20*1)/47.09
# print(a)
# print("a1= ",l)
# print("a2= ",m)
