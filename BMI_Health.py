
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert height to meters
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        # Set BMI result text and color
        if bmi < 18.5:
            result_label.config(text=f"BMI: {bmi} - Underweight", fg="#4a90e2", font=("Arial", 20, "bold"))
            recommendation_text = (
                "Recommendation:\n"
                "- Include calorie-dense foods\ such as nuts, seeds, and avocados.\n"
                "- Eat more frequently with balanced meals.\n"
                "- Consult a nutritionist for a personalized diet plan."
            )
            recommendation_label.config(bg="#add8e6", fg="black")
        elif 18.5 <= bmi < 24.9:
            result_label.config(text=f"BMI: {bmi} - Normal weight", fg="#27ae60", font=("Arial", 20, "bold"))
            recommendation_text = (
                "Recommendation:\n"
                "- Maintain a balanced diet with a variety of foods.\n"
                "- Continue regular physical activity, such as walking or jogging.\n"
                "- Ensure adequate hydration and sleep."
            )
            recommendation_label.config(bg="#d3f9d8", fg="black")
        elif 25 <= bmi < 29.9:
            result_label.config(text=f"BMI: {bmi} - Overweight", fg="#f1c40f", font=("Arial", 20, "bold"))
            recommendation_text = (
                "Recommendation:\n"
                "- Aim for 150 minutes of moderate exercise per week.\n"
                "- Choose whole foods and avoid sugary drinks.\n"
                "- Consider a diet high in fiber and low in refined carbs."
            )
            recommendation_label.config(bg="#fffacd", fg="black")
        else:
            result_label.config(text=f"BMI: {bmi} - Obese", fg="#e74c3c", font=("Arial", 20, "bold"))
            recommendation_text = (
                "Recommendation:\n"
                "- Consult with a healthcare provider for a comprehensive weight loss plan.\n"
                "- Incorporate both cardio and strength training exercises.\n"
                "- Focus on portion control and a diet low in processed foods."
            )
            recommendation_label.config(bg="#f8d7da", fg="black")

        # Display recommendation text
        recommendation_label.config(text=recommendation_text)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")

# Function to animate the border color around the panda image
def animate_border():
    global color_index
    colors = ["#ff5733", "#33ff57", "#3357ff", "#ff33a6", "#a633ff"]
    color_index = (color_index + 1) % len(colors)
    animated_frame.config(highlightbackground=colors[color_index])
    root.after(500, animate_border)  # Change every 500 milliseconds

# Initialize main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("700x700")
root.config(bg="#282c34")

# Load panda image
try:
    panda_image = Image.open("bmi.png")  # Adjust the path if needed
    panda_image = panda_image.resize((200, 200), Image.Resampling.LANCZOS)
    panda_image_tk = ImageTk.PhotoImage(panda_image)
except Exception as e:
    print(f"Error loading image: {e}")
    panda_image_tk = None

# Header Label
header_label = tk.Label(root, text="BMI Calculator", font=("Arial", 28, "bold"), bg="#282c34", fg="#61dafb")
header_label.pack(pady=20)

# Frame for input fields
input_frame = tk.Frame(root, bg="#282c34")
input_frame.pack(pady=10)

# Weight input
weight_label = tk.Label(input_frame, text="Weight (kg):", font=("Arial", 18), bg="#282c34", fg="white")
weight_label.grid(row=0, column=0, padx=15, pady=10, sticky="e")

weight_entry = tk.Entry(input_frame, font=("Arial", 18), width=12, borderwidth=2, relief="ridge", bg="#ffffff", fg="#333333")
weight_entry.grid(row=0, column=1, padx=15, pady=10)

# Height input
height_label = tk.Label(input_frame, text="Height (cm):", font=("Arial", 18), bg="#282c34", fg="white")
height_label.grid(row=1, column=0, padx=15, pady=10, sticky="e")

height_entry = tk.Entry(input_frame, font=("Arial", 18), width=12, borderwidth=2, relief="ridge", bg="#ffffff", fg="#333333")
height_entry.grid(row=1, column=1, padx=15, pady=10)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate BMI", font=("Arial", 18, "bold"), bg="#61dafb", fg="#282c34",
                             command=calculate_bmi)
calculate_button.config(width=15, height=1, relief="flat")
calculate_button.pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 20, "bold"), bg="#282c34", fg="white")
result_label.pack(pady=5)

# Recommendation Label (for displaying recommendations)
recommendation_label = tk.Label(root, text="", font=("Arial", 19), bg="#f0f0f0", fg="black", wraplength=800, justify="center")
recommendation_label.pack(pady=10)

# Animated frame for the panda image at the bottom-left corner
animated_frame = tk.Frame(root, bg="#282c34", highlightthickness=4)
animated_frame.place(relx=0.01, rely=0.69)  # Positioned in the bottom-left corner

# Place the panda image inside the animated frame
if panda_image_tk:
    panda_image_label = tk.Label(animated_frame, image=panda_image_tk, bg="#282c34")
    panda_image_label.pack()

# Start the color animation
color_index = 0
animate_border()

# Run the main loop
root.mainloop()


