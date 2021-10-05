import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pyodbc
import numpy as np
import geopandas as gpd
import geoplot as gplt
x = 0
y = 0
window = tk.Tk()
frame = tk.Frame(master=window, bg="midnight blue")
frame.pack(fill=tk.BOTH, expand=True)
frame.pack()
#new = Toplevel(window)
window.geometry("750x500")
Label(frame, text="", bg="midnight blue",
      font=('Helvetica 17 bold')).pack(pady=15)
greeting = tk.Label(frame, text="Welcome to Covid assistant", font=(
    'Helvetica 20 bold'), fg="turquoise", bg="midnight blue")
greeting.pack()

Label(frame, text="", bg="midnight blue",
      font=('Helvetica 17 bold')).pack(pady=17)
label1 = tk.Label(frame, text="Username", width=20, font=(
    'Helvetica 17 bold'), fg="deeppink", bg="midnight blue")
label2 = tk.Label(frame, text="Password", width=20, font=(
    'Helvetica 17 bold'), fg="deeppink", bg="midnight blue")
entry2 = tk.Entry(frame, show="*", fg="deeppink", bg="white",
                  width=20, font=('Helvetica 17 bold'))
entry1 = tk.Entry(frame, fg="deeppink", bg="white",
                  width=20, font=('Helvetica 17 bold'))
label1.pack()
entry1.pack()
username = entry1.get()  # username get from user
label2.pack()
entry2.pack()
password = entry2.get()  # pass get from user


def showMsg():
    # if output!=0
    messagebox.showinfo(None, " Login successfuly ")


def Map_jeo():
    messagebox.showinfo(None, "Geoplot")
    # call function of map (x,y)
    # show plot , map


def open_win_map():
    #messagebox.showinfo(None, " Map ")
    new = Toplevel(frame)
    frame1 = tk.Frame(master=new, bg="midnight blue")
    frame1.pack(fill=tk.BOTH, expand=True)
    frame1.pack()
    new.geometry("750x500")
    new.title("Location x,y")
# enter to page of services
    labelx = tk.Label(frame1, text="Position of X", bg="white",
                      font=('Helvetica 17 bold')).pack(pady=15)
    entry3 = tk.Entry(frame1, fg="deeppink", bg="white",
                      width=20, font=('Helvetica 17 bold'))
    entry3.pack()

    labely = tk.Label(frame1, text="Position of Y", bg="white",
                      font=('Helvetica 17 bold')).pack(pady=15)
    entry4 = tk.Entry(frame1, fg="deeppink", bg="white",
                      width=20, font=('Helvetica 17 bold'))

    entry4.pack()

    x = entry3.get()
    y = entry4.get()
    submit = Button(frame1, height=5,
                    width=10, font=('Helvetica 17 bold'), fg="black", bg="white", text="Submit", command=Map_jeo).pack()

# input:
# Gender-> Male:1, Transgender:2, Female: 3
# Contact-> No:1, Don't-Know:2, Yes:3
# Age-> 0-9:1, 10-19:2, 20-24:3, 25-59:4, 60+:5
# Fever-> yes:1, no:0
# Tiredness-> yes:1, no:0
# Dry-cough-> yes:1, no:0
# Difficulty-in-breathing-> yes:1, no:0
# Sore-Throat-> yes:1, no:0
# Pains-> yes:1, no:0
# Nasal-Congestion-> yes:1, no:0
# Runny_Nose-> yes:1, no:0
# Diarrhea-> yes:1, no:0
# output:
# probability of being infected in scale of 0 to 100


def diagnose(features):
    arr = np.array([features]).astype('float')
    arr[0, 0] = arr[0, 0]/6
    arr[0, 1] = arr[0, 1]/6
    arr[0, 2] = arr[0, 2]/20
    coef = np.array([[-0.02752593,  0.03977402,  0.02206546, -0.00929782,  0.01594905,
                      -0.00560558, -0.02683619,  0.00352665, -0.00270834, -0.02176323,
                      0.01276784, -0.00998991]])
    intercept = 1.10297915
    if np.sum(arr[0, 3:11]) == 0 and arr[0, 1] == 1/6:
        ret_value = 5.491
    elif np.sum(arr[0, 3:11]) == 0 and arr[0, 1] == 2/6:
        ret_value = 30.323
    else:
        ret_value = float(
            1 / (1+np.exp(-1*(intercept+np.sum(np.multiply(coef, arr))))))*100
    return np.round(ret_value, 3)


def open_win_predict():
    #messagebox.showinfo(None, " predict ")
    new = Toplevel(frame)
    frame2 = tk.Frame(master=new, bg="purple")
    frame2.pack(fill=tk.BOTH, expand=True)
    frame2.pack()
    # new.geometry("900x3000")
    new.title("Symptoms")
    label_gender = tk.Label(frame2, text="answer each question by entering the respective number", width=50, font=(
        'Helvetica 13'), fg="deeppink", bg="midnight blue").pack()
    label_gender = tk.Label(frame2, text="Gender-> Male:1, Transgender:2, Female: 3", width=50, font=(
        'Helvetica 13'), fg="deeppink", bg="midnight blue").pack()
    entry_gender = tk.Entry(frame2, fg="deeppink", bg="white",
                            width=50, font=('Helvetica 9'))
    entry_gender.pack()
    label_contact = tk.Label(frame2, text="Contact-> No:1, Don't-Know:2, Yes:3", width=50, font=(
        'Helvetica 13'), fg="deeppink", bg="midnight blue").pack()
    entry_contact = tk.Entry(frame2, fg="deeppink", bg="white",
                             width=50, font=('Helvetica 9'))
    entry_contact.pack()
    label_age = tk.Label(frame2, text="Age-> 0-9:1, 10-19:2, 20-24:3, 25-59:4, 60+:5", width=50, font=(
        'Helvetica 13'), fg="deeppink", bg="midnight blue").pack()
    entry_age = tk.Entry(frame2, fg="deeppink", bg="white",
                         width=50, font=('Helvetica 9'))
    entry_age.pack()
    label_fever = tk.Label(frame2, text="Fever-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="deeppink", bg="midnight blue").pack()
    entry_fever = tk.Entry(frame2, fg="deeppink", bg="white",
                           width=50, font=('Helvetica 9'))
    entry_fever.pack()
    label_tiredness = tk.Label(frame2, text="Tiredness-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="deeppink", bg="midnight blue").pack()
    entry_tiredness = tk.Entry(frame2, fg="deeppink", bg="white",
                               width=50, font=('Helvetica 9'))
    entry_tiredness.pack()
    label_drycough = tk.Label(frame2, text="Dry_cough-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="deeppink", bg="midnight blue").pack()
    entry_drycough = tk.Entry(frame2, fg="deeppink", bg="white",
                              width=50, font=('Helvetica 9 '))
    entry_drycough.pack()

    label_difficulty_in_breathing = tk.Label(frame2, text="Difficulty-in-breathing-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="deeppink", bg="midnight blue").pack()
    entry_difficulty_breath = tk.Entry(frame2, fg="deeppink", bg="white",
                                       width=50, font=('Helvetica 9'))
    entry_difficulty_breath.pack()
    label_Sore_Throat = tk.Label(frame2, text="Sore-throat-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="deeppink", bg="midnight blue").pack()
    entry_sore_throat = tk.Entry(frame2, fg="deeppink", bg="white",
                                 width=50, font=('Helvetica 9'))
    entry_sore_throat.pack()
    label_pains = tk.Label(frame2, text="Pains-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="deeppink", bg="midnight blue").pack()
    entry_pains = tk.Entry(frame2, fg="deeppink", bg="white",
                           width=50, font=('Helvetica 9'))
    entry_pains.pack()
    label_nasal_congestion = tk.Label(frame2, text="Nasal-congestion-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="deeppink", bg="midnight blue").pack()
    entry_nasal_congestion = tk.Entry(frame2, fg="deeppink", bg="white",
                                      width=50, font=('Helvetica 9'))
    entry_nasal_congestion.pack()
    label_runny_nose = tk.Label(frame2, text="Runny-nose-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="deeppink", bg="midnight blue").pack()
    entry_runny_nose = tk.Entry(frame2, fg="deeppink", bg="white",
                                width=50, font=('Helvetica 9'))
    entry_runny_nose.pack()
    label_Diarrhea = tk.Label(frame2, text="Diarrhea-> yes:1, no:0", width=50, font=(
        'Helvetica 13'), fg="deeppink", bg="midnight blue").pack()
    entry_diarrhea = tk.Entry(frame2, fg="deeppink", bg="white",
                              width=50, font=('Helvetica 9'))
    entry_diarrhea.pack()

    def predict_symp():
        in_val = [entry_gender.get(), entry_contact.get(), entry_age.get(), entry_fever.get(),
                  entry_tiredness.get(), entry_drycough.get(), entry_difficulty_breath.get(),
                  entry_sore_throat.get(), entry_pains.get(), entry_nasal_congestion.get(),
                  entry_runny_nose.get(), entry_diarrhea.get()]
        messagebox.showinfo(
            None, "probability of infection: " + str(diagnose(in_val)))
        new.destroy()
        # call function with symptoms values

    submit_symp = Button(frame2, width=50, pady=10, font=('Helvetica 13 bold'),
                         fg="black", bg="deeppink", text="Submit", command=predict_symp).pack()


def open_win():
    # call databasefunc(username,password)
    # if output!=0
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-T8NB059;'
                          'Database=SE_project;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    username = entry1.get()
    password = entry2.get()
    cursor.execute('execute u_p_check ' + str(username) +
                   ', ' + str(password) + ';')
    for row in cursor:
        if row[0] == 1:
            new = Toplevel(frame)
            frame1 = tk.Frame(master=new, bg="midnight blue")
            frame1.pack(fill=tk.BOTH, expand=True)
            frame1.pack()
            new.geometry("750x500")
            new.title("Services")
            # enter to page of services
            Label(frame1, text="", bg="midnight blue",
                  font=('Helvetica 17 bold')).pack(pady=15)
            Label(frame1, text="Choose your service from check list",
                  fg="turquoise", bg="midnight blue", font=('Helvetica 20 bold')).pack(pady=30)
            Label(frame1, text="", bg="midnight blue",
                  font=('Helvetica 17 bold')).pack(pady=17)
            Button(frame1, height=2,
                   width=25, font=('Helvetica 17 bold'), fg="salmon", bg="skyblue2", text="Map", command=open_win_map).pack()
            Label(frame1, text="", bg="midnight blue",
                  font=('Helvetica 10 bold')).pack(pady=1)
            Button(frame1, height=2,
                   width=25, font=('Helvetica 17 bold'), fg="salmon", bg="skyblue2", text="Prediction based on Symptoms", command=open_win_predict).pack()

        else:
            messagebox.showinfo(None, "wrong username or password :(")
    conn.close()
    # Create a Label in New window

    # else
    # messagebox.showerror("error", "try again") #abort


# Create a label
Label(frame, text="", bg="midnight blue",
      font=('Helvetica 17 bold')).pack(pady=30)
# Create a button to open a New Window
tk.Button(frame, text="Login", command=open_win, width=20, font=(
    'Helvetica 17 bold'), fg="midnight blue", bg="turquoise").pack()
window.mainloop()
window.destroy()


greeting.pack()
# enter to page of services

Button(frame, text="Map", command=open_win_map).pack()

Button(frame, text="Prediction based on Symptoms",
       command=open_win_predict).pack()


# if C1.get() == 1:
# call function of Map
# display plot
# else if C2.get() == 1:
# call predict function
# display probability of infection
# else
#messagebox.showinfo(None, " Choose a service ")

window.mainloop()
