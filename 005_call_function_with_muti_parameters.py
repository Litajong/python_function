#!/usr/bin/env python
# coding: utf-8

# In[2]:


# call function with multi-parameters

def make_schedule(period1, period2):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title())
    return schedule

student_schedule = make_schedule("mathematics", "history")
print("SCHEDULE: ", student_schedule)


# In[2]:


# Task: Define make_schedule() adding a 3rd period to
# Start with the above example code
# add a parameter period_3
# update function code to add period_3 to the schedule
# call student_schedule() with an additional argument such as 'science'
# print the schedule

# add a 3rd period parameter to make_schedule

def make_schedule(period1, period2, period3):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title() + ", [3rd] " + period3.title())
    return schedule

student_schedule = make_schedule("mathematics", "history", "science")
print("SCHEDULE: ", student_schedule)



# In[5]:


def format_info (name, age, school):
    return "Student: "+ name + "\nAge: " + str(age)+ "\nSchool: "+ school
print(format_info("Tobies Ledford", 15, "Oak"))


# In[ ]:




