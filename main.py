import tkinter as tk # GUI library
from tkinter import PhotoImage # Display images
import sympy # Calculate equations
from math import sqrt, radians, degrees, sin, cos, tan, atan # Common math functions
import numpy as np # Display graph
import matplotlib.pyplot as plt # Display graph
from tkhtmlview import HTMLLabel

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pylator")
        self.root.geometry("1920x1080")  # window size

        # Create a left sidebar
        self.left_sidebar = tk.Frame(root, width=1000, bg="#1D1B1B")
        self.left_sidebar.pack(side=tk.LEFT, fill=tk.Y)

        # Create a frame for the top buttons
        self.top_frame = tk.Frame(root, bg="#1B1A15")
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        # Create a main content area
        self.main_content = tk.Frame(root, bg="#1B1A15")
        self.main_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # To store the result
        self.result_label = tk.Label()

        # Logo
        logo = PhotoImage(file='assets/logo.png')
        
        image_label = tk.Label(self.left_sidebar, image=logo, bg="#1D1B1B")
        image_label.image = logo
        image_label.pack(pady=10)


        # "Calculator Mode" button in the left sidebar
        self.calculator_button = tk.Button(self.left_sidebar, text="Calculator Mode", command=self.on_calculator_mode, bg="#1D1B1B", fg="#DBD5A1", font=('Inter', 14), relief=tk.FLAT, borderwidth=0, highlightthickness=0)
        self.calculator_button.pack(pady=(30,10), padx=80)
        self.current_mode = self.calculator_button
        self.on_calculator_mode()
        self.calculator_button.configure(bg='#D2CE61', fg='black', padx=10, pady=2)

        # Line below the button
        line1 = tk.Canvas(self.left_sidebar, height=2, bg="white", highlightthickness=0, width=self.calculator_button.winfo_reqwidth())
        line1.pack(pady=(2,5))

        # "Learner Mode" button in the left sidebar
        self.learner_button = tk.Button(self.left_sidebar, text="Learner Mode", command=self.on_learner_mode, bg="#1D1B1B", fg="#DBD5A1", font=('Inter', 14), relief=tk.FLAT, borderwidth=0, highlightthickness=0)
        self.learner_button.pack(pady=10)

        line2 = tk.Canvas(self.left_sidebar, height=2, bg="white", highlightthickness=0, width=self.calculator_button.winfo_reqwidth())
        line2.pack(pady=2)

        #Add Help Button
        self.help_button=tk.Button(self.left_sidebar, text="Help", command=self.on_help_mode, bg="#1D1B1B", fg="#DBD5A1", font=('Inter', 14), relief=tk.FLAT, borderwidth=0, highlightthickness=0)
        self.help_button.pack(pady=10)

        line3 = tk.Canvas(self.left_sidebar, height=2, bg="white", highlightthickness=0, width=self.calculator_button.winfo_reqwidth())
        line3.pack(pady=2)

        #Close calc button
        self.help_button=tk.Button(self.left_sidebar, text="Close", command=self.root.destroy, bg="#1D1B1B", fg="#DBD5A1", font=('Inter', 14), relief=tk.FLAT, borderwidth=0, highlightthickness=0)
        self.help_button.pack(pady=10)


    def calculator(self, value):
        current_entry = self.entry.get()

        if value == '=':
            try:
                result = eval(current_entry)
                self.entry.delete(0, tk.END) # clear output field
                self.entry.insert(tk.END, str(result)) # display output
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error") # display Error
        elif value == 'C': # clear output field
            self.entry.delete(0, tk.END)
        elif value == 'DEL': # remove last input
            current_entry = current_entry[:-1]
            self.entry.delete(0,tk.END)
            self.entry.insert(tk.END,current_entry)
        elif current_entry.startswith("Error"):
            self.entry.delete(0,tk.END)
            self.entry.insert(tk.END, value)
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_entry + str(value))

    def calculate_quadratic(self):
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        c = float(self.c_entry.get())

        # Calculate the quadratic formula
        discriminant = b**2 - 4*a*c

        if discriminant < 0:
            result = "No real roots (complex roots)"
        elif discriminant == 0:
            root = -b / (2*a)
            result = f"Single real root: {round(root, 2)}"
        else:
            root1 = (-b + (discriminant)**0.5) / (2*a)
            root2 = (-b - (discriminant)**0.5) / (2*a)
            result = f"Real roots: {round(root1, 2)}, {round(root2, 2)}"
        
        self.result_label.destroy() 
        self.result_label = tk.Label(self.main_content, text=result, bg="#D2CE61", fg='black', pady=10, padx=10, font=('Inter', 14))
        self.result_label.pack(side=tk.BOTTOM, pady=(10,200))

    def calculate_bmi(self):
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())

            # Calculate BMI
            bmi = weight / (height ** 2)

            if bmi < 18.5:
                result = "Underweight"
            elif 18.5 <= bmi < 24.9:
                result = "Normal Weight"
            elif 25 <= bmi < 29.9:
                result = "Overweight"
            else:
                result = "Obese"

            self.result_label.destroy() 
            self.result_label = tk.Label(self.main_content, text=f"Your BMI is: {round(bmi, 2)}\nYou are in the {result} range", bg="#D2CE61", fg='black', pady=10, padx=10, font=('Inter', 14))
            self.result_label.pack(side=tk.BOTTOM, pady=(10,300))
    
    def calculate_eq(self):
        a = float(self.entry_a.get())
        b = float(self.entry_b.get())
        c = float(self.entry_c.get())
        d = float(self.entry_d.get())
        e = float(self.entry_e.get())
        f = float(self.entry_f.get())
        x,y = sympy.symbols('x y')
        eq1 = sympy.Eq(a*x+b*y,c)
        eq2 = sympy.Eq(d*x+e*y,f)
        soln = sympy.solve((eq1,eq2),(x,y))

        self.result_label.destroy() 
        self.result_label = tk.Label(self.main_content, text=f"x: {round(soln[x],2)}, y: {round(soln[y],2)}", bg="#D2CE61", fg='black', pady=10, padx=10, font=('Inter', 14))
        self.result_label.grid(row=4,column=0, columnspan=4, pady=10)
    
    def calculate_electric(self):
        voltage = float(self.voltage_entry.get())
        current = float(self.current_entry.get())
        resistance = float(self.resistance_entry.get())

        if voltage == 0:
            voltage = current * resistance
            result = f"The voltage is {round(voltage, 2)}V"
        elif current == 0:
            current = voltage / resistance
            result = f"The current is {round(current, 2)}A"
        elif resistance == 0:
            resistance = voltage / current
            result = f"The resistance is {round(resistance, 2)}Ω"
        else:
            result = "Input the value to be calculated as 0"
        power = voltage * current
        result += f'\nThe Power is {power}W'

        self.result_label.destroy() 
        self.result_label = tk.Label(self.main_content, text=result, bg="#D2CE61", fg='black', pady=10, padx=10, font=('Inter', 14))
        self.result_label.pack(side=tk.BOTTOM, pady=(10,200))

        # Display V(I)=IR graph
        def graph(x_range):
            x = np.array(x_range)
            y = resistance*x
            plt.plot(x, y)
            plt.show()

        graph(range(0,int(current)))
    
    def calculate_triangle(self):
        side1 = float(self.side1.get())
        side2 = float(self.side2.get())
        hyp = float(self.side3.get())

        if side1 == 0:
            side1 = sqrt((hyp**2)-(side2**2))
            result = f"The first side is {round(side1, 2)}"
        elif side2 == 0:
            side2 = sqrt((hyp**2)-(side1**2))
            result = f"The second side is {round(side2, 2)}"
        elif hyp == 0:
            hyp = sqrt((side1**2)+(side2**2))
            result = f"The Hypotenuse is {round(hyp, 2)}"
        else:
            result = "Input the value to be calculated as 0"

        self.result_label.destroy() 
        self.result_label = tk.Label(self.main_content, text=result, bg="#D2CE61", fg='black', pady=10, padx=10, font=('Inter', 14))
        self.result_label.pack(side=tk.BOTTOM, pady=(10,200))

    def calculate_marathon(self):
        vertical = float(self.v_entry.get())
        horizontal = float(self.h_entry.get())
        angle = float(self.angle_entry.get())

        if vertical == 0:
            vertical = horizontal * tan(radians(angle))
            result = f"The vertical is {round(vertical, 2)}"
        elif horizontal == 0:
            horizontal = vertical / tan(radians(angle))
            result = f"The horizontal is {round(horizontal, 2)}"
        elif angle == 0:
            angle = degrees(atan(vertical/horizontal))
            result = f"The angle is {round(angle, 2)}°"
        else:
            result = "Input the value to be calculated as 0"

        self.result_label.destroy() 
        self.result_label = tk.Label(self.main_content, text=result, bg="#D2CE61", fg='black', pady=10, padx=10, font=('Inter', 14))
        self.result_label.pack(side=tk.BOTTOM, pady=(10,200))
        
    def on_calculator_mode(self):
        self.show_top_frame()

        self.calculator_button.configure(bg='#D2CE61', fg='black', padx=10, pady=2)
        self.current_mode.configure(bg='#1D1B1B',fg='#DBD5A1')
        self.current_mode = self.calculator_button

        for widget in self.top_frame.winfo_children():
            widget.destroy()
        for widget in self.main_content.winfo_children():
            widget.destroy()

        # "Basic" button at the top of the window
        self.basic_button = tk.Button(self.top_frame, text="Basic", command=lambda: self.on_button_click(self.basic_button), bg="#D2CE61", fg="black", font=('Inter', 14), relief=tk.FLAT, borderwidth=0, highlightthickness=0)
        self.basic_button.pack(side=tk.LEFT, padx=25, pady=25)
        self.current = self.basic_button
        self.on_button_click(self.basic_button)
        self.basic_button.configure(bg='#D2CE61',fg='black')

        # "Quadratic" button at the top of the window
        self.quadratic_button = tk.Button(self.top_frame, text="Quadratic", command=lambda: self.on_button_click(self.quadratic_button), bg="#1B1A15", fg="white", font=('Inter', 14), relief=tk.FLAT, borderwidth=0, highlightthickness=0)
        self.quadratic_button.pack(side=tk.LEFT, padx=10, pady=10)

        # "Body Mass Index (BMI)" button at the top of the window
        self.bmi_button = tk.Button(self.top_frame, text="Body Mass Index (BMI)", command=lambda: self.on_button_click(self.bmi_button), bg="#1B1A15", fg="white", font=('Inter', 14), bd=2, relief=tk.FLAT, borderwidth=0, highlightthickness=0)
        self.bmi_button.pack(side=tk.LEFT, padx=10, pady=10)

    def on_learner_mode(self):
        self.show_top_frame()

        self.learner_button.configure(bg='#D2CE61', fg='black', padx=10, pady=2)
        self.current_mode.configure(bg='#1D1B1B',fg='#DBD5A1')
        self.current_mode = self.learner_button

        for widget in self.top_frame.winfo_children():
            widget.destroy()
        for widget in self.main_content.winfo_children():
            widget.destroy()

        self.eq_button = tk.Button(self.top_frame, text="Eq Solver", command=lambda: self.on_button_click(self.eq_button), bg="#D2CE61", fg="black", font=('Inter', 14), relief=tk.FLAT, borderwidth=0, highlightthickness=0)
        self.eq_button.pack(side=tk.LEFT, padx=25, pady=25)
        self.current = self.eq_button
        self.on_button_click(self.eq_button)
        self.eq_button.configure(bg='#D2CE61',fg='black')

        self.electric_button = tk.Button(self.top_frame, text="Electric Solver", command=lambda: self.on_button_click(self.electric_button), bg="#1B1A15", fg="white", font=('Inter', 14), relief=tk.FLAT, borderwidth=0, highlightthickness=0)
        self.electric_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.triangle_button = tk.Button(self.top_frame, text="Triangle Solver", command=lambda: self.on_button_click(self.triangle_button), bg="#1B1A15", fg="white", font=('Inter', 14), relief=tk.FLAT, borderwidth=0, highlightthickness=0)
        self.triangle_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.marathon_button = tk.Button(self.top_frame, text="Marathon Solver", command=lambda: self.on_button_click(self.marathon_button), bg="#1B1A15", fg="white", font=('Inter', 14), relief=tk.FLAT, borderwidth=0, highlightthickness=0)
        self.marathon_button.pack(side=tk.LEFT, padx=10, pady=10)

    def on_button_click(self, button):
        button.configure(bg='#D2CE61',fg='black')
        self.current.configure(bg='#1B1A15',fg='white')
        self.current = button

        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        if button == self.basic_button:
            self.entry = tk.Entry(self.main_content, font=('Inter', 16), justify='right')
            self.entry.grid(row=0, column=0, columnspan=6, pady=10)

            # Buttons
            buttons = [
                '7', '8', '9', '/', 'C', '(',
                '4', '5', '6', '*', 'sin', ')',
                '1', '2', '3', '-', 'cos', 'DEL',
                '0', '.', '=', '+', 'tan', '%'
            ]

            # Create and place buttons in a grid
            row_val = 1
            col_val = 0

            for button in buttons:
                if col_val > 2:
                    fg = '#3EA089'
                else:
                    fg = '#DBD5A1'
                tk.Button(self.main_content, text=button, width=6, borderwidth=0,height=2, bg='#1B1A15',fg=fg,font=('Inter', 17),command=lambda b=button: self.calculator(b)).grid(row=row_val, column=col_val, padx=12, pady=3)
                col_val += 1
                if col_val > 5:
                    col_val = 0
                    row_val += 1

        elif button == self.quadratic_button:
            qe = PhotoImage(file='assets/qe.png')
            qe_label = tk.Label(self.main_content, image=qe,bg='#1B1A15')
            qe_label.image = qe
            qe_label.pack()
             
            a_label = tk.Label(self.main_content, text="Enter a:", fg="white", bg="#1B1A15", font=('Inter', 14))
            a_label.pack(side=tk.TOP, pady=(50, 5))

            self.a_entry = tk.Entry(self.main_content, font=('Inter', 16))
            self.a_entry.pack(side=tk.TOP, pady=(0, 5))
            self.a_entry.insert(0, "0")

            b_label = tk.Label(self.main_content, text="Enter b:", fg="white", bg="#1B1A15", font=('Inter', 14))
            b_label.pack(side=tk.TOP, pady=(5, 5))

            self.b_entry = tk.Entry(self.main_content, font=('Inter', 16))
            self.b_entry.pack(side=tk.TOP, pady=(0, 5))
            self.b_entry.insert(0, "0")

            c_label = tk.Label(self.main_content, text="Enter c:", fg="white", bg="#1B1A15", font=('Inter', 14))
            c_label.pack(side=tk.TOP, pady=(5, 5))
  
            self.c_entry = tk.Entry(self.main_content, font=('Inter', 16))
            self.c_entry.pack(side=tk.TOP, pady=(0, 5))
            self.c_entry.insert(0, "0")
 
            # Submit button
            submit_button = tk.Button(self.main_content, text="Submit", command=self.calculate_quadratic, font=('Inter', 14), bg='#D2CE61', fg='black', width=10, pady=7)
            submit_button.pack(side=tk.TOP)

        elif button == self.bmi_button:
            height_label = tk.Label(self.main_content, text="Enter Height (in m):", fg="white", bg="#1B1A15", font=('Inter', 14))
            height_label.pack(side=tk.TOP, pady=(100, 5))

            self.height_entry = tk.Entry(self.main_content, font=('Inter', 16))
            self.height_entry.pack(side=tk.TOP, pady=(0, 5))

            weight_label = tk.Label(self.main_content, text="Enter Weight (in kg):", fg="white", bg="#1B1A15", font=('Inter', 14))
            weight_label.pack(side=tk.TOP, pady=(5, 5))

            self.weight_entry = tk.Entry(self.main_content, font=('Inter', 16))
            self.weight_entry.pack(side=tk.TOP, pady=(0, 5))

            submit_button = tk.Button(self.main_content, text="Submit", command=self.calculate_bmi, font=('Inter', 14), bg='#D2CE61', fg='black', width=10, pady=7)
            submit_button.pack(side=tk.TOP, pady=10)
        
        elif button == self.eq_button:
            # Create labels and entry widgets for coefficients and variables
            tk.Label(self.main_content, text="Equation 1:", fg='white',bg='#1B1A15', font=('Inter',14)).grid(row=0, column=0, padx=5, pady=5)
            self.entry_a = tk.Entry(self.main_content, font=('Inter', 16), width=8)
            self.entry_a.grid(row=0, column=1, padx=5, pady=5)
            self.entry_a.insert(0, "2")

            self.entry_b = tk.Entry(self.main_content, font=('Inter', 16), width=8)
            self.entry_b.grid(row=0, column=2, padx=5, pady=5)
            self.entry_b.insert(0, "3")

            self.entry_c = tk.Entry(self.main_content, font=('Inter', 16), width=8)
            self.entry_c.grid(row=0, column=3, padx=5, pady=5)
            self.entry_c.insert(0, "10")

            tk.Label(self.main_content, text="Equation 2:", fg='white', bg='#1B1A15', font=('Inter', 14)).grid(row=1, column=0, padx=5, pady=5)
            self.entry_d = tk.Entry(self.main_content, font=('Inter', 16), width=8)
            self.entry_d.grid(row=1, column=1, padx=5, pady=5)
            self.entry_d.insert(0, "4")

            self.entry_e = tk.Entry(self.main_content, font=('Inter', 16), width=8)
            self.entry_e.grid(row=1, column=2, padx=5, pady=5)
            self.entry_e.insert(0, "-2")

            self.entry_f = tk.Entry(self.main_content, font=('Inter', 16), width=8)
            self.entry_f.grid(row=1, column=3, padx=5, pady=5)
            self.entry_f.insert(0, "0")

            solve_button = tk.Button(self.main_content, text="Solve Equations", command=self.calculate_eq, font=('Inter', 14), bg='#D2CE61', fg='black', width=15, pady=7)
            solve_button.grid(row=2, column=0, columnspan=4, pady=10)

        elif button == self.electric_button:
            circuit = PhotoImage(file='assets/circuit.png')
            circuit_label = tk.Label(self.main_content, image=circuit,bg='#1B1A15')
            circuit_label.image = circuit
            circuit_label.pack()

            voltage_label = tk.Label(self.main_content, text="Enter Voltage:", fg="white", bg="#1B1A15", font=('Inter', 14))
            voltage_label.pack(side=tk.TOP, pady=(30, 5))

            self.voltage_entry = tk.Entry(self.main_content, font=('Inter', 16))
            self.voltage_entry.pack(side=tk.TOP, pady=(0, 5))
            self.voltage_entry.insert(0, "0")

            current_label = tk.Label(self.main_content, text="Enter Current:", fg="white", bg="#1B1A15", font=('Inter', 14))
            current_label.pack(side=tk.TOP, pady=(5, 5))

            self.current_entry = tk.Entry(self.main_content, font=('Inter', 16))
            self.current_entry.pack(side=tk.TOP, pady=(0, 5))
            self.current_entry.insert(0, "0")

            resistance_label = tk.Label(self.main_content, text="Enter Resistance:", fg="white", bg="#1B1A15", font=('Inter', 14))
            resistance_label.pack(side=tk.TOP, pady=(5, 5))

            self.resistance_entry = tk.Entry(self.main_content, font=('Inter', 16))
            self.resistance_entry.pack(side=tk.TOP, pady=(0, 5))
            self.resistance_entry.insert(0, "0")

            submit_button = tk.Button(self.main_content, text="Submit", command=self.calculate_electric, font=('Inter', 14), bg='#D2CE61', fg='black', width=10, pady=7)
            submit_button.pack(side=tk.TOP)

        elif button == self.triangle_button:
            triangle = PhotoImage(file='assets/triangle.png')
            triangle_label = tk.Label(self.main_content, image=triangle,bg='#1B1A15')
            triangle_label.image = triangle
            triangle_label.pack()
            tk.Label(self.main_content, text="Keep the value you want to calculate as 0, and enter the rest", fg="white", bg="#1B1A15", font=('Inter', 14)).pack(side=tk.TOP, pady=(30, 0))

            side1_label = tk.Label(self.main_content, text="Enter first side:", fg="white", bg="#1B1A15", font=('Inter', 14))
            side1_label.pack(side=tk.TOP, pady=(30, 5))

            self.side1 = tk.Entry(self.main_content, font=('Inter', 16))
            self.side1.pack(side=tk.TOP, pady=(0, 5))
            self.side1.insert(0, "0")

            side2_label = tk.Label(self.main_content, text="Enter second side:", fg="white", bg="#1B1A15", font=('Inter', 14))
            side2_label.pack(side=tk.TOP, pady=(5, 5))

            self.side2 = tk.Entry(self.main_content, font=('Inter', 16))
            self.side2.pack(side=tk.TOP, pady=(0, 5))
            self.side2.insert(0, "0")

            side3_label = tk.Label(self.main_content, text="Enter Hypotenuse:", fg="white", bg="#1B1A15", font=('Inter', 14))
            side3_label.pack(side=tk.TOP, pady=(5, 5))

            self.side3 = tk.Entry(self.main_content, font=('Inter', 16))
            self.side3.pack(side=tk.TOP, pady=(0, 5))
            self.side3.insert(0, "0")

            submit_button = tk.Button(self.main_content, text="Submit", command=self.calculate_triangle, font=('Inter', 14), bg='#D2CE61', fg='black', width=10, pady=7)
            submit_button.pack(side=tk.TOP)

        elif button == self.marathon_button:
            marathon = PhotoImage(file='assets/marathon.png')
            marathon_label = tk.Label(self.main_content, image=marathon,bg='#1B1A15')
            marathon_label.image = marathon
            marathon_label.pack()
            tk.Label(self.main_content, text="Keep the value you want to calculate as 0, and enter the rest", fg="white", bg="#1B1A15", font=('Inter', 14)).pack(side=tk.TOP, pady=(30, 5))

            v_label = tk.Label(self.main_content, text="Enter Height:", fg="white", bg="#1B1A15", font=('Inter', 14))
            v_label.pack(side=tk.TOP, pady=(30, 5))

            self.v_entry = tk.Entry(self.main_content, font=('Inter', 16))
            self.v_entry.pack(side=tk.TOP, pady=(0, 5))
            self.v_entry.insert(0, "0")

            h_label = tk.Label(self.main_content, text="Enter Horizontal distance:", fg="white", bg="#1B1A15", font=('Inter', 14))
            h_label.pack(side=tk.TOP, pady=(5, 5))

            self.h_entry = tk.Entry(self.main_content, font=('Inter', 16))
            self.h_entry.pack(side=tk.TOP, pady=(0, 5))
            self.h_entry.insert(0, "0")

            angle_label = tk.Label(self.main_content, text="Enter Angle of depression:", fg="white", bg="#1B1A15", font=('Inter', 14))
            angle_label.pack(side=tk.TOP, pady=(5, 5))

            self.angle_entry = tk.Entry(self.main_content, font=('Inter', 16))
            self.angle_entry.pack(side=tk.TOP, pady=(0, 5))
            self.angle_entry.insert(0, "0")

            submit_button = tk.Button(self.main_content, text="Submit", command=self.calculate_marathon, font=('Inter', 14), bg='#D2CE61', fg='black', width=10, pady=7)
            submit_button.pack(side=tk.TOP)

            
    def on_help_mode(self):
        # Configure the help button appearance
        self.help_button.configure(bg='#D2CE61', fg='black', padx=10, pady=2)
        self.current_mode.configure(bg='#1D1B1B', fg='#DBD5A1')
        self.current_mode = self.help_button

        self.top_frame.pack_forget()

        # Destroy all widgets in top_frame and main_content
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        # Read and display the help.html content
        with open("assets/help.html", "r", encoding="utf-8") as file:
            html_content = file.read()

        # Create and pack the HTMLLabel for displaying the help content
        html_label = HTMLLabel(self.main_content, html=html_content)
        html_label.pack(fill="both", expand=True, padx=0, pady=0)  # Ensure no padding is applied
        html_label.configure(bg='#1b1a15')  # Set background color

    def hide_top_frame(self):
        self.top_frame.pack_forget()

    def show_top_frame(self):
        self.main_content.pack_forget()
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        self.main_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()