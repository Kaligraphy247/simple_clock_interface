from tkinter import *
import time

# Defining Window GUI properties
root = Tk()
root.title('Clock GUI')
root.geometry("640x480")

# Functions
def update():
    '''Generic update function'''
    my_label.config(text="New Text")

def clock():
    ''' Shows the current date and time'''
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    am_pm = time.strftime("%p")
    month = time.strftime("%B")
    time_zone = time.strftime("%Z")
    locale = time.strftime("%c")
    year = time.strftime("%Y")
    day_of_year = time.strftime("%-j")
    day_of_month = time.strftime("%d")
    
    
    clock_label.config(text=f"{hour}:{minute}:{second} {am_pm}")
    clock_label.after(1000, clock)
    
    #tz_label.config(text=f"{day}, time zone is {time_zone}.")
    
    full_date_time.config(text=f"Today is {day}, Day {day_of_month}\n\n in the month of {month}, {year}.\n\nCurrent time is \n\n{hour}:{minute}:{second} {am_pm} - {time_zone}.")
    full_date_time.after(1000, clock)

# Main Program

intro = Label(root, text="Simple Clock Interface", font=("Cantarell Bold", 20))
intro.pack(pady=20)

clock_label = Label(root, text="", font=("Cantarell Bold", 48), fg="red", bg="white")
clock_label.pack(pady=20)

#my_label.after(5000, update) # 5000 here = 5 mili-seconds

#tz_label = Label(root, text="", font=("Cantarell Bold", 16))
#tz_label.pack(pady=10)

full_date_time = Label(root, text="sample", font=("Cantarell Bold", 20))
full_date_time.pack(pady=10)


clock()
 

 
root.mainloop()
