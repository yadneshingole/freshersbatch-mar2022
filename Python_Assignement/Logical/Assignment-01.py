Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Len function is inbuilt function it is used to determine the length of diffrent collection such list,tuple,string and dictionary.
>>> a=[1,2,3,4]
>>> len(a)
4
>>> #It has return the length of list as 4
>>> #The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
>>> x=round(2.43)
>>> print(x)
2
>>> #Here we got nearest rounding number for 2.43 as 2
>>> y=round(2.73)
>>> print(y)
3
>>> #abs() is used to make any negative number to positive number multiplying it by -1.
>>> x=-90
>>> abs(x)
90
>>> y=20
>>> abs(y)
20
>>> #Note postive number does not affected.
>>> # We also have sqrt,sqaure,sum and many more
>>> import math
>>> math.sqrt(64)
8.0
>>> #For every object creation we can check id,type and sys.getrefcount
>>> a=10
>>> id(a)
2033838144
>>> type(a)
<class 'int'>
>>> import sys
>>> sys.getrefcount(10)
63
>>> #Everything in Python is based on object creation which include id,type,refcount and base address of an object._
>>> 