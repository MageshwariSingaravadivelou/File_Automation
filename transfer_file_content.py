"""
Created on Wed Nov 18 14:20:22 2020
@author: MAGESHWARI
"""
import os
from tkinter import * 
from tkinter import messagebox as mb
from tkinter import filedialog
import re
import csv
import pandas as pd


def center_window(w=200, h=500):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


def browse1():
    global df1
    # global directory
    # global filename
    # global contents
    filepath =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
    select_file_field.insert(0,filepath) # insert the path in textbox
    df1 = pd.read_csv(filepath)
    # file = open(filepath,'r')  # open the selected file
    # contents = file.read()
    # print(contents)

def browse2():
    global df2
    global basefilepath
    basefilepath =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
    base_file_field.insert(0,basefilepath) # insert the path in textbox
    df2 = pd.read_csv(basefilepath)    
    # , usecols = ["Date","Link Clicks (e4) (event4)","Unique Visitors", "Visits"]

def browse3():
    global df3
    global filepath3
    filepath3 =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
    file3_field.insert(0,filepath3) # insert the path in textbox
    df3 = pd.read_csv(filepath3)    

def browse4():
    global df4
    global filepath4
    filepath4 =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
    file4_field.insert(0,filepath4) # insert the path in textbox
    df4 = pd.read_csv(filepath4)  

def browse5():
    global df5
    global filepath5
    filepath5 =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
    file5_field.insert(0,filepath5) # insert the path in textbox
    df5 = pd.read_csv(filepath5) 

def browse6():
    global df6
    global filepath6
    filepath6 =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
    file6_field.insert(0,filepath6) # insert the path in textbox
    df6 = pd.read_csv(filepath6)   

def browse7():
    global df7
    global filepath7
    filepath7 =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
    file7_field.insert(0,filepath7) # insert the path in textbox
    df7 = pd.read_csv(filepath7)  

def browse8():
    global df8
    global filepath8
    filepath8 =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
    file8_field.insert(0,filepath8) # insert the path in textbox
    df8 = pd.read_csv(filepath8)  

def browse9():
    global df9
    global filepath9
    filepath9 =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
    file9_field.insert(0,filepath9) # insert the path in textbox
    df9 = pd.read_csv(filepath9)     

def browse10():
    global df10
    global filepath10
    filepath10 =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
    file10_field.insert(0,filepath10) # insert the path in textbox
    df10 = pd.read_csv(filepath10)   

def browse11():
    global df11
    global filepath11
    filepath11 =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
    file11_field.insert(0,filepath11) # insert the path in textbox
    df11 = pd.read_csv(filepath11)   
    
def browse12():
    global df12
    global filepath12
    filepath12 =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
    file12_field.insert(0,filepath12) # insert the path in textbox
    df12 = pd.read_csv(filepath12)   

def submit():
    data1 = pd.concat([df2, df1])
    data1.drop_duplicates(subset ="Date", inplace = True) 
    data1.to_csv(basefilepath, index=False, columns=["Date","Link Clicks (e4) (event4)","Unique Visitors", "Visits"])
    data2 = pd.concat([df4, df3])
    data2.drop_duplicates(subset ="Date", inplace = True) 
    data2.to_csv(filepath4, index=False, columns=["Date","Link Clicks (e4) (event4)","Unique Visitors", "Visits"])
    data3 = pd.concat([df6, df5])
    data3.drop_duplicates(subset ="Date", inplace = True) 
    data3.to_csv(filepath6, index=False, columns=["Date","Link Clicks (e4) (event4)","Unique Visitors", "Visits"])
    data4 = pd.concat([df8, df7])
    data4.drop_duplicates(subset ="Date", inplace = True) 
    data4.to_csv(filepath8, index=False, columns=["Date","Link Clicks (e4) (event4)","Unique Visitors", "Visits"])
    data5 = pd.concat([df10, df10])
    data5.drop_duplicates(subset ="Date", inplace = True) 
    data5.to_csv(filepath10, index=False, columns=["Date","Link Clicks (e4) (event4)","Unique Visitors", "Visits"])
    data6 = pd.concat([df12, df11])
    data6.drop_duplicates(subset ="Date", inplace = True) 
    data6.to_csv(filepath12, index=False, columns=["Date","Link Clicks (e4) (event4)","Unique Visitors", "Visits"])
    
    print("File write successful")
    mb.showinfo('Result', 'File write successfully...')
        
def reset():
    select_file_field.delete(0, END)
    base_file_field.delete(0, END)
    file3_field.delete(0, END)
    file4_field.delete(0, END)
    file5_field.delete(0, END)
    file6_field.delete(0, END)
    file7_field.delete(0, END)
    file8_field.delete(0, END)
    file9_field.delete(0, END)
    file10_field.delete(0, END)
    file11_field.delete(0, END)
    file12_field.delete(0, END)

    # make_label()
    
# def make_label():
#     global total_block
#     total_block = Label(root,text=" ",font=("Times New Roman",12))
#     total_block.grid(row=2,column=1,sticky='w')
    
if __name__=="__main__":
    
    root = Tk()
    root.resizable(0,0) # to disable the maximize button
    root.title("Seeker Dashboard")
    root.configure(pady=60)

    select_file = Label(root, text="Input File 1: ",width=12)
    select_file.grid(column=0, row=0,sticky='w')
    
    select_file_field = Entry(root,width=50)
    select_file_field.grid(column=1, row=0)

    base_file = Label(root, text="Base File 1: ",width=12)
    base_file.grid(column=0, row=1,sticky='w')
    
    base_file_field = Entry(root,width=50)
    base_file_field.grid(column=1, row=1)

    file3 = Label(root, text="Input File 2: ",width=12)
    file3.grid(column=0, row=2,sticky='w')
    
    file3_field = Entry(root,width=50)
    file3_field.grid(column=1, row=2)

    file4 = Label(root, text="Base File 2: ",width=12)
    file4.grid(column=0, row=3,sticky='w')
    
    file4_field = Entry(root,width=50)
    file4_field.grid(column=1, row=3)

    file5 = Label(root, text="Input File 3: ",width=12)
    file5.grid(column=0, row=4,sticky='w')
    
    file5_field = Entry(root,width=50)
    file5_field.grid(column=1, row=4)

    file6 = Label(root, text="Base File 3: ",width=12)
    file6.grid(column=0, row=5,sticky='w')
    
    file6_field = Entry(root,width=50)
    file6_field.grid(column=1, row=5)

    file7 = Label(root, text="Input File 4: ",width=12)
    file7.grid(column=0, row=6,sticky='w')
    
    file7_field = Entry(root,width=50)
    file7_field.grid(column=1, row=6)

    file8 = Label(root, text="Base File 4: ",width=12)
    file8.grid(column=0, row=7,sticky='w')
    
    file8_field = Entry(root,width=50)
    file8_field.grid(column=1, row=7)

    file9 = Label(root, text="Input File 5: ",width=12)
    file9.grid(column=0, row=8,sticky='w')
    
    file9_field = Entry(root,width=50)
    file9_field.grid(column=1, row=8)

    file10 = Label(root, text="Base File 5: ",width=12)
    file10.grid(column=0, row=9,sticky='w')
    
    file10_field = Entry(root,width=50)
    file10_field.grid(column=1, row=9)

    file11 = Label(root, text="Input File 6: ",width=12)
    file11.grid(column=0, row=10,sticky='w')
    
    file11_field = Entry(root,width=50)
    file11_field.grid(column=1, row=10)

    file12 = Label(root, text="Base File 6: ",width=12)
    file12.grid(column=0, row=11,sticky='w')
    
    file12_field = Entry(root,width=50)
    file12_field.grid(column=1, row=11)
    
    browse1 = Button(root, text="....",width=5, command=browse1)
    browse1.grid(column=2, row=0,sticky='w', pady = 1, padx=1)

    browse2 = Button(root, text="....",width=5, command=browse2)
    browse2.grid(column=2, row=1,sticky='w', pady = 1, padx=1)

    browse3 = Button(root, text="....",width=5, command=browse3)
    browse3.grid(column=2, row=2,sticky='w', pady = 1, padx=1)

    browse4 = Button(root, text="....",width=5, command=browse4)
    browse4.grid(column=2, row=3,sticky='w', pady = 1, padx=1)

    browse5 = Button(root, text="....",width=5, command=browse5)
    browse5.grid(column=2, row=4,sticky='w', pady = 1, padx=1)

    browse6 = Button(root, text="....",width=5, command=browse6)
    browse6.grid(column=2, row=5,sticky='w', pady = 1, padx=1)

    browse7 = Button(root, text="....",width=5, command=browse7)
    browse7.grid(column=2, row=6,sticky='w', pady = 1, padx=1)

    browse8 = Button(root, text="....",width=5, command=browse8)
    browse8.grid(column=2, row=7,sticky='w', pady = 1, padx=1)

    browse9 = Button(root, text="....",width=5, command=browse9)
    browse9.grid(column=2, row=8,sticky='w', pady = 1, padx=1)

    browse10 = Button(root, text="....",width=5, command=browse10)
    browse10.grid(column=2, row=9,sticky='w', pady = 1, padx=1)

    browse11 = Button(root, text="....",width=5, command=browse11)
    browse11.grid(column=2, row=10,sticky='w', pady = 1, padx=1)

    browse12 = Button(root, text="....",width=5, command=browse12)
    browse12.grid(column=2, row=11,sticky='w', pady = 1, padx=1)

    submit = Button(root, text="Submit",width=16, command=submit)
    submit.grid(column=1, row=12,sticky='w',padx=5,pady=5)
    reset = Button(root, text="Reset",width=16, command=reset)
    reset.grid(column=1, row=12,sticky='e',padx=5,pady=5)    
    
    # total_block = Label(root,text=" ",font=("Times New Roman",12))
    # total_block.grid(row=2,column=1,sticky='w')
    
    #total_block_field = IntVar()
    #Label(root,textvariable=total_block_field)
    #total_block_field.grid(row=2,column=1,sticky='e')
    
    root.iconbitmap(r"C:/Users/mageshwari.singarava/Desktop/images.ico")
    center_window(500,500)  # to make the application window centered
    root.mainloop()
