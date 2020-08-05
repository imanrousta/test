# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:11:42 2019

@author: Iman
"""
import tkinter as tk 
from tkinter import * 
import secrets 

root=Tk()
root.title("Password Generator")

root.geometry("500x500")

n = 20
def password(): 
    myPassword = Label(root, text = secrets.token_hex(n)).pack() 

btn=Button(root, text="Generate Password!", command=password).pack()

root.mainloop() 