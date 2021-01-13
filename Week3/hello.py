#%%
print("Hello")
# %%
someString = "Hello"
#%%
print(someString)
# %%
# This is comment 
myOldDog: str = "Laika"
# %%
type(myOldDog)
# %%
myAge = 33

# %%
print(myAge + 1)
# %%
type(33)
# %%
type(33.0)
# %%
type(int(33.0))
# %%
str(33.0)

# %%
# six types in python
# int float bool str None object
#%%
myName = "Shawn Hartley"
myAge = 32
myBDay = '12/17/1987'

#%%
# String interpolation

myIntroduction = f"""
My name is {myName} and I am {myAge} years old.
I was born {myBDay}
"""
#%%
print(myIntroduction)
# print(someEdit)
# %%
# Lists
someListOfInt = [9,8,7,6,5,4,3,2,1,0]

# %%
# Indexing in python starts from 0
someListOfInt[0]
# %%
someListOfInt[3]
# %%
# Negative indexing
someListOfInt[-1]
# %%
someListOfInt[-2]
# %%
# Slice
someListOfInt[0:3]

# %%
someListOfInt[3]
# %%
# Slice
someListOfInt[-3:-1]

# %%
# Slice
someListOfInt[5:]
# %%
# Slice
someListOfInt[:5]
# %%
for anAlias in someListOfInt:
    print(anAlias)
# %%
for anAlias in someListOfInt:
    print(type(anAlias))
# %%
for x in someListOfInt:
    print(float(x))
#%%
type(None)
#%%
type(True)
# %%
aMixedList = ['a',1,11.0,True,None,[0,1,2]]
# %%
for element in aMixedList:
    print(type(element))
# %%
someDictionary = {
    "myName" : myName,
    "myAge" : myAge,
    "someInt" : 55,
    "someList" : aMixedList
}
#%%
print(someDictionary)
# %%
someDictionary['myName']
# %%
someDictionary['myAge']
# %%
someDictionary['myName'][2]
# %%
for key,value in someDictionary.items():
    print(f"The type for key: {key} is {type(value)}")
# %%
someString = "Hello"
#%%
someString[0]
# %%
if "H" in someString:
    print(True)
# %%
if 11 in someListOfInt:
    print(True)
# %%
someListOfInt
# %%
import os
#%%
someFilePath = os.path.join('./','hello.ipynb')
#%%
abs_path = os.path.join('A:','dataAustin','UT-MCC','Week3','hello.ipynb')
# %%
week2Path = os.path.join('..','Week2', 'vbaBasics.xlsm')
# %%
