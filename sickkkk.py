from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("600x500")
window.title("Sick Class")
frame = Frame(window)



# Sick Class


MSickID = Label(window, text ="SicknessCode")
MSickID.pack(side=LEFT)
MSickID.place(x=20, y=20)

sick_entry = Entry(window, bd =1)
sick_entry.pack(side = RIGHT)
sick_entry.place(x = 300, y = 20)

MDurationOfTreatment = Label(window, text = "DurationOfTreatment")
MDurationOfTreatment.pack(side =LEFT )
MDurationOfTreatment.place(x = 20, y= 80)

weeks_monthly = Label(window, text = "Weekly/Months")
weeks_monthly.pack(side = RIGHT)
weeks_monthly.place(x = 380, y = 80)

due_entry = Entry(window, bd =1, width = 8)
due_entry.pack(side =RIGHT)
due_entry.place(x = 300, y = 80)

MDoctorsID = Label(window, text="DoctorsPracticeNumber")
MDoctorsID.pack(side = LEFT)
MDoctorsID.place(x = 20, y = 150)

doc_entry = Entry(window, bd =1)
doc_entry.pack(side = RIGHT)
doc_entry.place(x = 300, y =150)

scan_fee = Label(window, text = "Scan/Consultation Fee")
scan_fee.pack(side = LEFT)
scan_fee.place(x = 20, y = 190)

scan_entry = Entry(window, bd =1)
scan_entry.pack(side = RIGHT)
scan_entry.place(x = 301, y = 190)


amount_paid = Label(window)
amount_paid.pack(side = LEFT)
amount_paid.place(x = 20, y = 260)

var = StringVar()

# The Calculations for the Sick Class
class Sick():
    def sickness(self):
        self.MSickID = MSickID
        self.MDurationOfTreatment = MDurationOfTreatment
        self.MDoctorsID = MDoctorsID
        self.medcancer = 400
        self.medinflu = 350.50

# Calculating Cancer
def sickness():
    if var.get() == "Cancer":
        if int(scan_entry.get()) > 600:
            messagebox.showinfo("Message", "Sorry we cannot treat you") # Error message will display
        elif int(scan_entry.get()) < 600:
           cancer_answer = int(scan_entry.get()) + 400
           amount_paid.config(text="AmountPaidForTreatment: " + str(cancer_answer))

    if var.get() == "Influenza": # Calculating Influenza
        if int(scan_entry.get()) >= 600:
            influ_answer = 350.50 + int(scan_entry.get())
            amount_paid.config(text="AmountPaidForTreatment: " + str(influ_answer))
        elif int(scan_entry.get()) < 600:
            influ_answer = 350.50 + int(scan_entry.get())
            discount = (influ_answer * (2/100)) + influ_answer # Calculating the discount recieve
            messagebox.showinfo("Message", "2% discount")
            amount_paid.config(text="Amount Paid For Treatment: "  + str(discount)) #discount will be included in the calculation




radbtn1 = Radiobutton(window, text = "Cancer" , variable = var, value ="Cancer") # Radiobutton for Cancer
radbtn1.pack(side = LEFT)
radbtn1.place(x = 20, y= 220)

radbtn2 = Radiobutton(window, text = "Influenza", variable = var, value = "Influenza")# Radiobutton for Influenza
radbtn2.pack(side = LEFT)
radbtn2.place(x = 20, y= 240)

cal_btn = Button(window, text = "Calculate", command = sickness) # Calculates the amount paid for treatment once pushed
cal_btn.pack(side = LEFT)
cal_btn.place(x = 20, y = 300)

# Function on the clear all button
def clear_all():
    sick_entry.delete(0,END)
    due_entry.delete(0,END)
    doc_entry.delete(0,END)
    scan_entry.delete(0,END)

clear_btn = Button(window, text = "Clear", command = clear_all) #Clears everything when the button is pushed
clear_btn.pack(side = RIGHT)
clear_btn.place(x = 300, y = 300)
exit_btn = Button(window, text="Exit", command=window.destroy).place(x=425, y=450)


window.mainloop()
