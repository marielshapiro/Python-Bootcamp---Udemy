#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Object Oriented Programming Challenge
##For this challenge, create a bank account class that has two attributes: owner, balance
##and two methods: deposit, withdraw
##As an added requirement, withdrawals may not exceed the available balance.
##Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


# In[1]:


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f"Account Owner:  {self.owner}\nAccount Balance:  {self.balance}"
        
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposit of ${amount} Accepted')
        
    def withdraw(self, amount):
        
        if amount > self.balance:
            print('Withdrawl amount exceeds account balance')
        else:
            self.balance -= amount
            print(f'Withdrawl of ${amount} Accepted')


# In[2]:


acct1 = Account('John',100)


# In[3]:


print(acct1)


# In[4]:


acct1.owner


# In[5]:


acct1.balance


# In[6]:


acct1.deposit(80)


# In[7]:


acct1.balance


# In[8]:


acct1.withdraw(40)


# In[9]:


acct1.balance


# In[10]:


acct1.withdraw(500)

