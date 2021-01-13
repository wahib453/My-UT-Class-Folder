#%%
import os
import csv
#%%
filePath: str = os.path.join('./','newEmployees.csv')

#%%
# print('some\tspace\nhere\tis\ta\nnew\tline')
# %%


# %%
class NewEmployee():

    def __init__(self,fName,lName,ssn):
        self.first_name = fName
        self.last_name = lName
        self.ssn: str = ssn
        self.valid_ssn = False
    
    def checkSSN(self):
        ssn_int = self.ssn.replace('-','')
        if len(ssn_int) == 9:
            self.valid_ssn = True
        else:
            self.valid_ssn = False

#%%
welcomeEmailList = []
invalidSSNEmailList = []

#%%
# with open(file=filePath,mode='r') as file_handle:
#     file_object = csv.reader(file_handle, delimiter = ',')
#     print(file_object)
#     for row in file_object:
#         print(row)
#         aNewEmployee = NewEmployee(fName=row[0],lName=row[1],ssn=row[2])
#         aNewEmployee.checkSSN()
#         if aNewEmployee.valid_ssn:
#             welcomeEmailList.append(aNewEmployee)
#         else:
#             invalidSSNEmailList.append(aNewEmployee)

# %%
welcomeEmailList
# %%
for employee in welcomeEmailList:
    welcomeMessage = f'Hi {employee.first_name}, {employee.last_name}'
    print(welcomeMessage)
# %%
for employee in invalidSSNEmailList:
    invalidSSNMessage = f'Hi {employee.first_name}, {employee.last_name} has an invalid ssn {employee.ssn}'
    print(invalidSSNMessage)
# %%
