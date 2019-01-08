Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> map(int,input().split())
38 24
<map object at 0x03671AD0>
>>> a,b = map(int,iniput().split())
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a,b = map(int,iniput().split())
NameError: name 'iniput' is not defined
>>> a,b = map(int,input().split())
38 24
>>> a
38
>>> b
24
>>> x = a*b
>>> x
912
>>> x=a*(b-1)
>>> x
874
>>> x=(a*(b-1))+1
>>> x
875
>>> 
============= RESTART: C:/Users/ruru/Desktop/BaekJoon/2614저작권.py =============
