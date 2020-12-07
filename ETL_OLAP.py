
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import os
os.getcwd()
os.chdir("../Noveenaa_Pious_ASN2")
car=pd.read_csv("Car_Sales_Data_Set.csv")
car.sort_values(by=['Country','Time_Year','Time_Quarter'],ascending=['True','True','True'],inplace=True)
car['Record_ID']= np.arange(1,101,1)
car.reset_index(drop=True,inplace=True)
car.to_csv("Car_Sales_Data_Set_Sorted.csv",index=False)
car=pd.read_csv("Car_Sales_Data_Set_Sorted.csv")
car
car1=car
def dimension_zero():
    print(car)
    
def country():
    c=car.groupby('Country')['Sales_Units'].mean()
    print(c)
    
def timeyr():
    t=car.groupby('Time_Year')['Sales_Units'].mean()
    print(t)
    
def time():
    car1['Time_Quarter-Time_Year']= car1["Time_Quarter"].map(str) + "-" + car1["Time_Year"].map(str)
    t1=car1.groupby(['Time_Quarter-Time_Year'])['Sales_Units'].mean()
    print(t1)

def car_manu():
    m=car.groupby(['Car_Manufacturer'])['Sales_Units'].mean()
    print(m)
    
def count_timeyr():
    c_t=car.groupby(['Country','Time_Year'])['Sales_Units'].mean()
    print(c_t)
    
def count_time():
    c_t1=car1.groupby(['Country','Time_Quarter-Time_Year'])['Sales_Units'].mean()
    print(c_t1)

def count_car():
    c_m=car.groupby(['Country','Car_Manufacturer'])['Sales_Units'].mean()
    print(c_m)

def timeyr_manu():
    t_m=car.groupby(['Time_Year','Car_Manufacturer'])['Sales_Units'].mean()
    print(t_m)
    
def time_manu():
    t1_m=car1.groupby(['Time_Quarter-Time_Year','Car_Manufacturer'])['Sales_Units'].mean()
    print(t1_m)

def contm():
    c_t_m=car.groupby(['Country','Time_Year','Car_Manufacturer'])['Sales_Units'].mean()
    print(c_t_m)
    
def contim():
    c_t1_m=car1.groupby(['Country','Time_Quarter-Time_Year','Car_Manufacturer'])['Sales_Units'].mean()
    print(c_t1_m)


choice = ''
while choice != 'e':
    
    print("\n 1. ()")
    print("2. Country()")
    print("3. Time_Year()")
    print("4. Time_Quarter-Time_Year()")
    print("5. Car_manufacturer()")
    print("6. Country,Time_Year()")
    print("7. Country,Time_Quarter-Time_Year()")
    print("8. Country,Car_Manufacturer()")
    print("9. Time_Year,Car_Manufacturer()")
    print("10.Time_Quarter-Time_Year,Car_Manufacturer()")
    print("11.Country,Time_Year,Car_Manufacturer()")
    print("12.Country,Time_Quarter-Time_Year,Car_Manufacturer()")
    print(" Enter e to exit.")
   
    choice = input("\n Which dimension you want to select? ")
    if choice == '1':
        dimension_zero()
    elif choice == '2':
        country()
    elif choice == '3':
        timeyr()
    elif choice == '4':
        time()
    elif choice == '5':
        car_manu()
    elif choice == '6':
        count_timeyr()
    elif choice == '7':
        count_time()
    elif choice == '8':
        count_car()
    elif choice == '9':
        timeyr_manu()
    elif choice == '10':
        time_manu()
    elif choice == '11':
        contm()
    elif choice == '12':
        contim()
    elif choice == 'e':
        print("\nEXIT.\n")
    else:
        print("\nInvalid data\n")
        

