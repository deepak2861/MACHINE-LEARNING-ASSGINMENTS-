#!/usr/bin/env python
# coding: utf-8

# In[1]:


import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#sort() function to used to sort the list
# min() is used to find  thje minimum of a list
# and the max() is used to find the  maximum values of list.
ages.sort()
print("Final Sorted ages: ", ages)
print("Min value of ages: ", min(ages))
print("Max value of ages: ", max(ages))
# insert(position, value) - inserts the value in list at specified position
ages.insert(0,min(ages))
# append(value) - appends the value at the end of list
ages.append(max(ages))
print("List after update: ", ages)
#The biggest advantage of using median() function is that the data-list does not need to be sorted
#before being sent as parameter to the median() function using statistice module
print("Median of ages: ", statistics.median(ages))
print("Average of ages: ", statistics.mean(ages))
print("Range of ages: ", max(ages)-min(ages))


# In[2]:


dog= dict()
#The update() method inserts the specified dictionary
dog.update({"name":"Chris", "color":"Green", "breed":"Husky", "legs":4, "age":3})
print("Added key-value pair to dog: ",dog)
#used  dict() function which creates a empty dictionary
student_dict = dict()
keyList = ["first_name", "last_name", "gender","age","marital status","skills","country","city","address"]
#added only keys to the dictionary with None value using update method
student_dict.update({key: None for key in keyList})
print("\nStudent_Dictionary after adding keys: ",student_dict)
#utilised len(dictionary) function to calculate the length
print("Length of Student_Dictionary: ", len(student_dict))
#updated student_dict with sample values
student_dict.update({"first_name": "Akhil", "last_name": "Reddy", "gender": "Male", "age": "24",
                     "marital status": "Single", "skills": ["Python","sql"], "country": "India","city": "Jmd",
                     "address": " Street"})

print("\nStudent_dict ", student_dict)
#accessing paritcular value of key in dict: dict["key"]
print("\nAccessing Skills value in dictionary: ",student_dict["skills"])
#type(value) - function gives the datatype of provided values
print("Data Type of Skills in Student Dict: ", type(student_dict["skills"]))
#The extend() adds all the elements of an iterable (list, tuple, string etc.) to the end of the list
student_dict["skills"].extend(["Apex", "JavaScript"])
print("Updated Skills list after adding new values: ", student_dict["skills"])
# dict.keys() and values() gives the list of keys and values as a list respectively
print("\n",student_dict.keys())
print(student_dict.values())


# In[3]:


#assigning the sisters
sisters = ("Harika", "sis")
print("Sisters: ", sisters,)
#assigning the brothers
brothers = ("Kulai","nvn","pochi","jana")
print("Brothers: ", brothers)
#concatenate the brothers and sisters
siblings = sisters+brothers
print("siblings: ",siblings)
#printing the no. of sibilings and find out the length
print("Number of Siblings:", len(siblings))
family_members = siblings+("Saradha","Mallikarjuna")
#get the final output of family_members
print("family_members: ", family_members)


# In[4]:


#Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("Length of it_companies:",len(it_companies))
# adds Twitter elements into the set
it_companies.add('Twitter')
print("it_companies: ", it_companies)
it_companies.update(['Tcs','Accenture','anilee','Wipro'])
print("it_companies after update: ",it_companies)
#remove() is used to  remove the element from the set
it_companies.remove("anilee")
print(it_companies)
#Difference between remove and discard
print("\nDifference between Remove() and Discard(): Discard() method is different from the remove() method, because the remove() method will throw an error if the specified item is not present in list, whereas the discard() method will not throw any error if item doesn't exist in list.")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#all set operation can be performed in set: union(), intersection()
print("\nUnion of A and B sets: ",A.union(B))
print("Intersection of A and B sets: ",A.intersection(B))
#issubset() returns true if it is subset of other else false
print("A is Subset of B? ",A.issubset(B))
#to check is A and B are disjoint sets ( no elements in common)
print("A and B are disjoint sets? ",A.isdisjoint(B))
print("(AUB) AND (BUA): ",(A.union(B)).intersection(B.union(A)))
#checking symmetric differece .. return the extra elements of set A that are not in B
print("Symmetric Difference of A with B: ",A.symmetric_difference(B))
#clear() clear/ delete all elements from set
A.clear()
B.clear()
print("After clear Set A values: ", A,"\tSet B values: ",B)
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("\nage list: ",age)
age_set = set(age)
print("set of ageslist: ", age_set)
print("Length of age list: ", len(age), "\nLength of age set",len(age_set))


# In[5]:


#Question 5
from math import pi
radius_of_circle = 30
_area_of_circle_ = pi * radius_of_circle **2
print("Area of a circle = ",_area_of_circle_," meters square")
_circum_of_circle_ = 2 * pi * radius_of_circle
print("Circumference of a circle = ",_circum_of_circle_, ' meters')

_radius_of_circle_ = float(input("Enter radius of circle: "))
_area_of_circle_ = pi * _radius_of_circle_ **2
print("Area of a circle = ",_area_of_circle_," meters square")


# In[10]:


print("I am a teacher and I love to inspire and teach people")
#split the string with using space
set_words = set(("I am a teacher and I love to inspire and teach people".split(" ")))
print("Number of Unique words: ",len(set_words), set_words)


# In[11]:


#Question 7
text = "\033[1m Name \t  Age \tCountry City\n Asabench 250 \tFinland Helsinki\033[0m"
print(text)


# In[12]:


#Question 8
radius = 10
area = 3.14 * radius ** 2
# using 'f' we can format the data. %.0f will give data without any decimals, %.2f displays until 2 decimals
print("The area of a circle with radius",radius,"is %.0f" %area, "meters square.")


# In[ ]:





# In[13]:


# Question 9
# 1lb = 0.453592kg
# Ask the user to enter the no of students he want
number_of_students = int(input("Enter number of students: "))
weight_of_students_lbs = list()  # to store weights in lbs
weight_of_students_kgs = list()  # to store weights in kgs

for each in range(number_of_students):
    weight_lb = int(input("Enter weight of {} student in lbs: ".format(each + 1)))
    weight_of_students_lbs.insert(each, weight_lb)
    # converting lbs to kg and adding to seperate list
    weight_kg = float("%.2f" % (weight_lb * 0.453592))
    weight_of_students_kgs.insert(each, weight_kg)

print("weight of students in lbs: ", weight_of_students_lbs)
print("weight of students in kgs: ", weight_of_students_kgs)


# In[ ]:




