#!/usr/bin/env python
# coding: utf-8

# In[3]:


def greet_user():
    """Display a simple greeting"""
    print('Hello')
greet_user()


# In[6]:


def greet_user(username):
    """Display a greeting message to the user"""
    print(f"hello, {username.title()} welcomeback")
greet_user('shareef')
greet_user('taLhA')


# In[10]:


def describe_pet(animal_type,pet_name):
    """Display information about a Pet"""
    print(f"I have a {animal_type}")
    print(f"\nmy {animal_type}'s name is {pet_name.title()}")


# In[11]:


describe_pet('dog,'bruno')


# In[13]:


def describe_pet(animal_type,pet_name):
    """Display information about a Pet"""
    print(f"I have a {animal_type}")
    print(f"\nmy {animal_type}'s name is {pet_name.title()}")


# In[14]:


describe_pet('dog','bruno')


# In[15]:


describe_pet('Kitty','cat')


# In[16]:


describe_pet(pet_name ='Kitty', animal_type ='cat')


# In[ ]:




