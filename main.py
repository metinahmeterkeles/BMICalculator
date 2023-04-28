from tkinter import *

window= Tk()
window.title('BMI Calculator')
window.minsize(300,300)
window.config(padx=30,pady=30)

def bmi_calculate ():
    weight = weight_entry.get()
    height = height_entry.get()

    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / (float(height)/100) ** 2
            print(bmi)
            if bmi < 16:
                result_label.config(text=f"Your BMİ {round(bmi,2)}. You are Severe Thinness")
            elif 16 < bmi < 17:
                result_label.config(text=f"Your BMİ {round(bmi,2)}. You are Moderate Thinness")

            elif 17 < bmi < 18.5:
                result_label.config(text=f"Your BMİ {round(bmi,2)}. You are Mild Thinness")

            elif 18.5 < bmi < 25:
                result_label.config(text=f"Your BMİ {round(bmi,2)}. You are Normal")

            elif 25 < bmi < 30:
                result_label.config(text=f"Your BMİ {round(bmi,2)}. You are Overweight")

            elif 30 < bmi < 35:
                result_label.config(text=f"Your BMİ {round(bmi,2)}. You are Obese Class I")

            elif 35 < bmi < 40:
                result_label.config(text=f"Your BMİ {round(bmi,2)}. You are Obese Class II")

            elif bmi > 40:
                result_label.config(text=f"Your BMİ {round(bmi,2)}. You are Obese Class III")

        except:
            result_label.config(text="Enter a valid number!")



weight_label = Label(text="Enter Your Weight (kg)")
weight_label.pack()

weight_entry = Entry()
weight_entry.pack()

height_label = Label(text="Enter Your Height (m)")
height_label.pack()

height_entry = Entry()
height_entry.pack()

my_button = Button(text="Calculate",command=bmi_calculate)
my_button.pack()

result_label = Label()
result_label.pack()

window.mainloop()