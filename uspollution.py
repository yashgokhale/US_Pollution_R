import numpy as np
import os
import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import pandas as pd

#%matplotlib qt

os.chdir("C:/Users/yashg/OneDrive/Desktop/CMU/Fall 2019/Data Science/Project/Combined")

def click():
    e1=stateentry.get() #this will collect data from text box
    e2=cityentry.get()
    e3=parentry.get()
    output.delete(0.0,END)
    try:
        def graph(e1,e2,e3):
            fig=plt.figure()
            pollutant=pd.read_csv(f'{e3}.csv')
            polf=pollutant.groupby(['State_Name','City_Name'])    
            data=polf.get_group((e1,e2))        
            ans=data.groupby(['Year']).mean()        
            plt.plot(data['Year'],data[f'Avg_{e3}'],'k.',label='Scatter')
            plt.plot(np.unique(data['Year']),ans[f'Avg_{e3}'],'-',label='Averaged over Months')
            plt.xlabel('Year')
            plt.ylabel(f'Concentration of {e3}')
            plt.title(f'Trend of {e3} in {e2},{e1}')
            plt.legend()
            return fig
        fig=graph(e1,e2,e3)
    except:
        fig=plt.plot(0,0)
        plt.title('Unavailable')
    output.insert(END,fig)
 
#Setting up the GUI Window
window=Tk()
window.title("Parameter Graph")
window.configure(background="black")
Label(window,text="Enter the state:",bg="black",fg="white",font="none 12 bold").grid(row=1,column=0,sticky=W)

stateentry=Entry(window,width=20,bg="white")
stateentry.grid(row=2,column=0,sticky=W)
Label(window,text="Enter the city:",bg="black",fg="white",font="none 12 bold").grid(row=4,column=0,sticky=W)
cityentry=Entry(window,width=20,bg="white")
cityentry.grid(row=5,column=0,sticky=W) 
Label(window,text="Enter the parameter:",bg="black",fg="white",font="none 12 bold").grid(row=7,column=0,sticky=W)
parentry=Entry(window,width=20,bg="white")
parentry.grid(row=8,column=0,sticky=W) 

#add a submit button
Button(window,text="SUBMIT",width=6,command=click).grid(row=9,column=0,sticky=W)

output=Canvas(window,width=10,height=10,background="white")
output.grid(row=10,column=0,columnspan=2,sticky=W)

def close_window():
    window.destroy()
    exit
Label(window,text="click to exit",bg="black",fg="white",font="none 12 bold").grid(row=10,column=0,sticky=W)
Button(window,text="EXIT",width=14,command=close_window).grid(row=11,column=0,sticky=W)

    
window.mainloop()
