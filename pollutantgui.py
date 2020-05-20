import numpy as np
import os
import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import pandas as pd


os.chdir("C:/Users/yashg/OneDrive/Desktop/CMU/Fall 2019/Data Science/Project/Combined")

root=tk.Tk()
root.wm_title("Pollutant Trend")

tk.Label(root, text="State Name").grid(row=0)
tk.Label(root, text="City Name").grid(row=1)
tk.Label(root, text="Parameter").grid(row=2)


e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

pol=input("Enter Pollutant")
state=input("Enter State")
city=input("Enter City")
pollutant=pd.read_csv(f'{pol}.csv')

polf=pollutant.groupby(['State_Name','City_Name'])

data=polf.get_group((state,city))

ans=data.groupby(['Year']).mean()

plt.plot(data['Year'],data[f'Avg_{pol}'],'k.')
plt.plot(np.unique(data['Year']),ans[f'Avg_{pol}'],'-')
plt.xlabel('Year')
plt.ylabel(f'Concentration of {pol}')
plt.title(f'Trend of {pol} in {city},{state}')

root.mainloop()