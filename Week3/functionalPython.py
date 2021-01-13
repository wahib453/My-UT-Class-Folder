#%%
someString = "Happy 2021!!!!!"
nextMonth = "Feb."
#%%
def printSomeString(someString, nextMonth):
    print(someString)
    return [someString, nextMonth]
# %%
printSomeString(someString,nextMonth)
# %%
someVariable,someVariable2 = printSomeString(someString,nextMonth)
#%%
print(someVariable)
# %%
type(someVariable)
# %%
print(someVariable2)
# %%
