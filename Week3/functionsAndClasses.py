#%%
someList = [0,1,2,3,4,5,6,7,8,9]
#%%
def calculateMean(someList):
    """ This function calculate's mean values """
    numberOfElements = 0
    sumOfElements = 0
    for number in someList:
        sumOfElements = sumOfElements + number
        numberOfElements = numberOfElements + 1
    return sumOfElements/numberOfElements
#%%
print(calculateMean(someList=someList))
# %%
calculateMean
# %%
class Animal():

    def __init__(self, animalType):
        self.animalType = animalType
    
    def printAnimalType(self):
        print(self.animalType)
#%%
animalType = 'cat'
print(animalType)
#%%
randomVariableName = Animal('garbage')
#%%
cat.animalType
#%%
cat.printAnimalType()
#%%
cat.printAnimalType()
#%%
dog = Animal('dog')
# %%
dog.animalType = 'Dog'
# %%
type(dog.animalType)
# %%
dog.printAnimalType()
# %%
print(calculateMean)
# %%
class Mammal(Animal):

    def __init__(self, animalType):
        self.animalType = animalType
        self.warmBlooded = True
        self.hasFur = True
    
    def isHuman(self):
        if self.hasFur:
            return False
        else:
            return True
#%%
human = Mammal('homo sapien')
#%%
human.hasFur = False
# %%
human.printAnimalType()
# %%
human.isHuman()
# %%
human.warmBlooded
# %%
