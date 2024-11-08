# PAT2_BMI

This Python-based BMI Calculator application provides users with an interactive graphical interface to calculate their Body Mass Index (BMI) and offers personalized health recommendations based on the result. The app also includes an animated image feature for added visual appeal.
Key Components
1. Required Libraries
The program uses the following libraries:
•	tkinter: A standard Python library used to build the graphical user interface (GUI). It provides widgets like labels, buttons, and entry fields.
•	messagebox: Used to display error messages when the user inputs invalid data.
•	Pillow (PIL): A Python Imaging Library that is used to open, manipulate, and display images. In this case, it handles the display of a panda image.

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

2. BMI Calculation Logic
The core functionality of the application lies in the calculate_bmi() function. This function calculates the BMI based on the user's input for weight and height.
•	The height input is converted from centimeters to meters, as BMI is calculated using meters.
•	The BMI is calculated using the formula: BMI=weightheight2BMI = \frac{weight}{height^2}BMI=height2weight
•	The resulting BMI is rounded to two decimal places for clarity.
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert height to meters
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
   
4. Categorizing BMI and Providing Recommendations
Once the BMI is calculated, the program categorizes the result into one of four ranges: Underweight, Normal weight, Overweight, or Obese. Depending on the category, the app dynamically updates the result text and provides specific health recommendations.
•	Underweight: Tips for gaining weight, like consuming calorie-dense foods.
•	Normal weight: General advice for maintaining a balanced diet and regular exercise.
•	Overweight: Suggestions for weight loss, including increasing physical activity and reducing sugar intake.
•	Obese: Strong recommendations for consulting a healthcare provider for a personalized weight loss plan.
Each category also triggers changes in the label’s text color and background for better visual distinction.
        if bmi < 18.5:
            result_label.config(text=f"BMI: {bmi} - Underweight", fg="#4a90e2", font=("Arial", 20, "bold"))
            recommendation_text = (
                "Recommendation:\n"
                "- Include calorie-dense foods such as nuts, seeds, and avocados.\n"
                "- Eat more frequently with balanced meals.\n"
                "- Consult a nutritionist for a personalized diet plan."
            )
            recommendation_label.config(bg="#add8e6", fg="black")
5. Error Handling
To ensure the application is user-friendly, a ValueError is caught if the user enters non-numeric values (such as text) in the weight or height fields. In such cases, a message box appears to inform the user to enter valid numeric data.
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")

6. Animated Image Border
A fun feature of the app is the animated border around the panda image. This animation changes the border color at regular intervals, cycling through a set of colors. The animation runs continuously, giving the interface a dynamic look.
def animate_border():
    global color_index
    colors = ["#ff5733", "#33ff57", "#3357ff", "#ff33a6", "#a633ff"]
    color_index = (color_index + 1) % len(colors)
    animated_frame.config(highlightbackground=colors[color_index])
    root.after(500, animate_border)  # Change every 500 milliseconds

7. Setting Up the GUI
The application window is initialized using tk.Tk(), and its properties are configured, such as size, title, and background color. The main interface is built using Label, Entry, and Button widgets, which allow the user to input data and see the results.
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("700x700")
root.config(bg="#282c34")
•	Labels display instructions and results.
•	Entry fields allow users to input their weight and height.
•	Button triggers the BMI calculation and updates the interface with the result and recommendations.
8. Displaying the Panda Image
The app also includes a panda image that is displayed in the bottom-left corner. The image is loaded using Pillow, resized, and placed within a frame that has the animated border effect.
animated_frame = tk.Frame(root, bg="#282c34", highlightthickness=4)
animated_frame.place(relx=0.01, rely=0.69)  # Positioned in the bottom-left corner

9. Main Event Loop
Finally, the program runs the main event loop, which continuously listens for user interactions and updates the GUI accordingly.
python
Copy code
root.mainloop()
 
Features Summary
•	BMI Calculation: Users can enter their weight and height, and the app calculates their BMI.
•	Health Recommendations: Based on the BMI result, the app provides tailored advice for each category.
•	Error Handling: The app catches invalid inputs and prompts users to correct their data.
•	Animated Image: A panda image with a changing border color makes the app more visually engaging.
This project showcases how to use Tkinter for GUI development, Pillow for image manipulation, and basic programming logic to create a functional and visually interactive BMI calculator.

