#!/usr/bin/env python
# coding: utf-8

# In[20]:


import csv
import os

os.chdir(r"C:\Users\Chanki Pandey\Desktop")
try:
    lst = []
    with open('hotels.csv', 'r') as file:
        my_reader = csv.reader(file, delimiter=',')
        for row in my_reader:
            lst.append(row)
    state = input("Enter the state : ").capitalize()
    corr = input("Enter the Cost or Rating : ").lower()
    operation = input("Enter the Operation : ").lower()

    newlst = []
    for i in lst:
        if state in i:
            newlst.append(i)

    if corr == 'cost':
        p = -2
        values = [int(i[p]) for i in newlst]
    elif corr == 'rating':
        p = -1
        values = [float(i[p]) for i in newlst]

    if operation == 'highest':
        optnvalue = max(values)
    elif operation == 'cheapest':
        optnvalue = min(values)
    elif operation == 'average':
        optnvalue = sum(values) / len(values)

    if operation == 'highest' or operation=='cheapest':
        hotel_code = ""
        for k in newlst:
            if str(optnvalue) == k[p]:
                hotel_code = hotel_code + k[1] + ", "
        print(f"\nHotel with {operation} {corr} in {state} is {hotel_code[:len(hotel_code) - 2]} with {corr} {optnvalue}.")
    elif operation == 'average':
        print(f"\nAverage {corr} of Hotel in {state} is {optnvalue:.2f}.")
except:
    print("Something went wrong! Please try again.")


# In[ ]:




