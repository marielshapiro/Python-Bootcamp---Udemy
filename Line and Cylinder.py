#!/usr/bin/env python
# coding: utf-8

# In[1]:


##accept coordinates as a pair of tuples and return the slope and distance of the line.


# In[2]:


class Line:
    

    def __init__(self,coor1,coor2):
        self.x1 = coor1[0]
        self.y1 = coor1[1]
        self.x2 = coor2[0]
        self.y2 = coor2[1]
    
    def distance(self):
        return ((self.x2-self.x1)**2 + (self.y2-self.y1)**2)**.5
    def slope(self):
        return (self.y2-self.y1)/(self.x2-self.x1)


# In[3]:


# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)


# In[4]:


li.distance()


# In[5]:


li.slope()


# In[6]:


##accept the height and radius of the cylinder and return the volume and surface area


# In[7]:


class Cylinder:
    
    pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.radius**2 * Cylinder.pi * self.height
    
    def surface_area(self):
        return (self.radius*2 * Cylinder.pi * self.height) + (2 * self.radius**2 * Cylinder.pi)


# In[8]:


c = Cylinder(2,3)


# In[9]:


c.volume()


# In[10]:


c.surface_area()

