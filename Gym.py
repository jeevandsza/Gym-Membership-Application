#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class GymManager :
   regimen = {}
   customers = dict()
   def __init__(self,s_id,s_name):
       self.s_id = s_id
       self.s_name = s_name
       
   @classmethod
   def addCustomer(cls,customer):
       GymManager.customers[customer.getPhoneNo()] = customer
       
ob = GymManager('s_1','John')

class Customer:
   
   def __init__(self,name='',age='',gender='',phoneNo='',email='',bmi='',duration=''):
       self.__name = name
       self.__phoneNo = phoneNo
       self.__age = age
       self.__gender = gender
       self.__email = email
       self.__bmi = bmi
       self.__duration = duration
       
   def setName(self,name):
       self.__name = name
   
   def getName(self):
       return self.__name
   
   def setAge(self,age):
       self.__age = age
       
   def getAge(self):
       return self.__age
   
   def setGender(self,gender):
       self.__gender = gender
       
   def getGender(self):
       return self.__gender
   
   def setPhoneNo(self,phoneNo):
       self.__phoneNo = phoneNo
       
   def getPhoneNo(self):
       return self.__phoneNo
   
   def setEmail(self,email):
       self.__email = email
       
   def getEmail(self):
       return self.__email
   
   def setBmi(self,bmi):
       self.__bmi = bmi
       
   def getBmi (self):
       return self.__bmi
   
   def setDuration(self,duration):
       self.__duration = duration
       
   def getDuration(self):
       return self.__duration
   
   def __str__(self):
       return self.getName()+" "+self.getPhoneNo()+" "+self.getDuration()+ " "+self.getAge()+" "+self.getEmail()+" "+self.getBmi()+" "+self.getGender()
   


print('  ***** Gym Manager Portal *****  ')
print("Hello , Please select a choice from the menu")

def menu():
   print("1. Create Member")
   print("2. View Member")
   print("3. Delete Member")
   print("4. Update Member")
   print("5. Create Regimen")
   print("6. View Regimen")
   print("7. Delete Regimen")
   print("8. Update Regimen")
   print("0. Exit")
   print("\nEnter your choice : ")
   
menu()    

while(True):
   option = int(input())
   if option == 1:
       name = str(input("Enter member's name : "))
       age = str(input("Enter member's age : "))
       gender = str(input("Enter member's gender : "))
       phoneNo = str(input("Enter member's phoneNo : "))
       email = str(input("Enter member's email : "))
       bmi = str(input("Enter member's bmi : "))
       if bmi<'18.5':
           r={'Mon':'Chest','Tue':'Biceps','Wed': 'Rest','Thu':'Back','Fri':'Tricep','Sat':'rest'}
       elif bmi <'25':
           r={'Mon' : 'Chest','Tue':'Biceps','Wed':'Cardio/Abs','Thu':'Back','Fri':'Triceps','sat':'Legs','Sun':'rest'}
       elif bmi <'30':
           r={'Mon':'Chest','Tue':'Biceps','Wed':'Abs/Cardio','Thu':'Back','Fri':'Triceps','Sat':'Legs','sun':'Cardio'}
       elif bmi>='30':
           r={'Mon':'Chest','Tue':'Biceps','Wed':'Cardio','Thu':'Back','Fri':'Triceps','Sat':'Cardio','Sun':'Cardio'}
           
       duration = str(input("Enter duration in months : "))
       customer = Customer(name,age,gender,phoneNo,email,bmi,duration)
       GymManager.regimen[phoneNo]=r
       GymManager.addCustomer(customer)
       
   elif option == 2:
       check_phn=input('Enter phone no. of member : ')
       print("Name\tage\tGender\tPhone\tEmail\tBmi\tDuration")
       for cusId in GymManager.customers.keys():
           if cusId==check_phn:
               customer=GymManager.customers[cusId]
               name = customer.getName()
               age = customer.getAge()
               gender = customer.getGender()
               phoneNo = customer.getPhoneNo()
               email = customer.getEmail()
               bmi = customer.getBmi()
               duration = customer.getDuration()
               print(name + "\t"+age+"\t"+gender+"\t"+phoneNo+"\t"+email+"\t"+bmi+"\t"+duration)
               
       print("\n")
       
   elif option == 3:
       check_phn=input('Enter phone number of the member you want to delete : ')
       try:
           for cusId in GymManager.customers.keys():
               if cusId==check_phn:
                   print('Member deleted')
                   
           GymManager.customers.pop(check_phn)
       except:
           print("Number doesn't exist\n")
           
   elif option == 4:
       check=input("Enter phone number : ")
       exr=input("Enter if you want to extend ot revoke:")
       if exr=='extend':
           for cusId in GymManager.customers.keys():
               customer = GymManager.customers[cusId]
               if cusId == check:
                   dur=customer.getDuration()
                   s=int(dur)+int(input("Enter how many months you mant to be extended for:"))
                   res=str(s)
                   customer.setDuration(res)
       elif exr=='revoke':
           for cusId in GymManager.customers.keys():
               customer = GymManager.customers[cusId]
               if cusId == check:
                   customer.setDuration('0')
                   print("Membership revoked")
                   
   elif option == 5:
       phn = input("Enter the phone number of member you want to create regiment of : ")
       for i in GymManager.regimen:
           if i==phn:
               for j in GymManager.regimen[i]:
                   GymManager.regimen[i][j]=input(j+":")
                   
   elif option == 6:
       check_phn = input('Enter phone no of member : ')
       for i in GymManager.regimen:
           if i==check_phn:
               for key,val in GymManager.regimen[i].items():
                   print(key,":",val)
       print("\n")
       
   elif option == 7:
       check_phn=input('Enter phone no of member : ')
       for i in GymManager.regimen:
           if i==check_phn:
               print("Workout regimen deleted!!")
       GymManager.regimen.pop(check_phn)
       print("\n")
       
   elif option == 8:
       check_phn = input("Enter phone number of member who's regimen you want to update : ")
       for i in GymManager.regimen:
           if i==check_phn:
               d=input("Enter the day which you want to update: ")
               for j in GymManager.regimen[i]:
                   if j==d:
                       GymManager.regimen[i][j]=input('Enter the workout: ')
                       print("Updated sucessfully!!")
                       
       print("\n")
   elif option == 0:
       break
       
   else:
       print("Please enter a valid number")
   menu()
   
def memenu():
   print("\n*********Member Portal*********\n")
   print("1.My Regimen")
   print("2.My Profile")
   print("3.Exit")
   print("\nEnter your choice: ")
   
memenu()
while(True):
   option = int(input())
   if option == 1:
       p=input("Enter your phone number: ")
       print("-- Your regimen based on your BMI --")
       for i in GymManager.regimen:
           if i==p:
               for key,val in GymManager.regimen[i].items():
                   print(key,":",val)
       print("\n")
       
   elif option == 2:
       p=input("Enter your phone number : ")
       try:
           for cusId in GymManager.customers.keys():
               if cusId == p:
                   customer = GymManager.customers[cusId]
                   name=customer.getName()
                   age = customer.getAge()
                   gender = customer.getGender()
                   phoneNo = customer.getPhoneNo()
                   email = customer.getEmail()
                   bmi = customer.getBmi()
                   duration = customer.getDuration()
                   print("*****your profile*****")
                   print("Name: ",name,"\nAge: ",age,"\nGender: ",gender,"\nPhone: ",phoneNo,"\nEmail: ",email,"\nBmi: ",bmi,"\nDuration: ",duration)
                   
       except:
           print("No user with this phone number exists")
           
   elif option == 3:
       break
       
   else:
       print("Please enter a valid number!!")
   memenu()


# In[ ]:




