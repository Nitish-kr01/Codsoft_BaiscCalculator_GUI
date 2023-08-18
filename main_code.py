#!/usr/bin/env python
# coding: utf-8

# ### Arithmetic Calculator using tkinter

# In[19]:


#Importing module

from tkinter import *


# In[20]:


#Defining button click function

def button_click(number):
    current=display.get()
    display.delete(0,END)
    display.insert(END,current+str(number))


# In[21]:


#Defining equal button function

def button_equal():
    try:
        expression=display.get()
        display.delete(0,END)
        expression=expression.replace("➗","/")
        expression=expression.replace("X","*")
        expression=expression.replace("➕","+")
        expression=expression.replace("➖","-")
        result=eval(expression)
        display.insert(END,result)
    except:
        display.delete(0,END)
        display.insert(END,"Error! 😔")


# In[22]:


#Defining clear button function

def button_clear():
    display.delete(0,END)


# In[23]:


#Defining delete button function

def button_delete():
    current=display.get()
    remaining=current[:-1]
    display.delete(0,END)
    display.insert(END,str(remaining))


# In[24]:


#creating Window

window=Tk()
window.title("Calculator")
window.resizable(False,False)
window.configure(bg="gray")


# In[25]:


#Creating display

display=Entry(window,font=("Arial",20))
display.grid(row=0,column=0,columnspan=4,padx=10,pady=10,sticky="we")


# In[26]:


#Placing number buttons

buttons=[("7",1,0),
         ("8",1,1),
         ("9",1,2),
         ("4",2,0),
         ("5",2,1),
         ("6",2,2),
         ("1",3,0),
         ("2",3,1),
         ("3",3,2),
         ("0",4,1),
         (".",4,2),
         ("00",4,0)]



# In[27]:


#Styling font

button_font=("Times New Roman", 12, "normal")


# In[28]:


#Creating number button

for button_text,row,column in buttons:
    button=Button(window,text=button_text,bg="yellow", activebackground="white",height=1,width=10,command=lambda text=button_text:button_click(text),font=button_font)
    button.grid(row=row,column=column,padx=5,pady=5,sticky="we")


# In[29]:


#Divide button

divide_button=Button(window,text="➗",command=lambda text="➗":button_click(text),height=1,width=10,bg="lightgrey",activebackground="white",font=button_font)
divide_button.grid(row=5,column=3,padx=5,pady=5,sticky="we")


# In[30]:


#Multiply button

multiply_button=Button(window,text="X",command=lambda text="X":button_click(text),height=1,width=10,bg="lightgrey",activebackground="white",font=button_font)
multiply_button.grid(row=5,column=2,padx=5,pady=5,sticky="we")


# In[31]:


#Add button

add_button=Button(window,text="➕",command=lambda text="➕":button_click(text),height=1,width=10,bg="lightgrey",activebackground="white",font=button_font)
add_button.grid(row=3,column=3,padx=5,pady=5,sticky="we")


# In[32]:


#Subtract button

subtract_button=Button(window,text="➖",command=lambda text="➖":button_click(text),height=1,width=10,bg="lightgrey",activebackground="white",font=button_font)
subtract_button.grid(row=4,column=3,padx=5,pady=5,sticky="we")


# In[33]:


#Clear button

clear_button=Button(window,text="C",command=button_clear,height=1,width=10,bg="lightblue",activebackground="white",font=button_font)
clear_button.grid(row=1,column=3,padx=5,pady=5,sticky="we")


# In[34]:


#Delete button

delete_button=Button(window,text="DEL",command=button_delete,height=1,width=10,bg="red",activebackground="white",font=button_font)
delete_button.grid(row=2,column=3,padx=5,pady=5,sticky="we")


# In[35]:


#Equal button

equal_button=Button(window,text="🟰",command=button_equal,height=1,width=10,bg="lightgrey",activebackground="white",font=button_font)
equal_button.grid(row=5,column=0,columnspan=2,padx=5,pady=5,sticky="we")


# In[36]:


window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




