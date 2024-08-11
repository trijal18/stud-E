import tkinter as tk
from tkinter import messagebox,font

import genrate_mcqs

questions=genrate_mcqs.genrate_mcqs(r"D:\study\4th sem\mc iot\Unit_3_Introduction_to_IoT.pdf")

# # Sample list of questions in JSON format
# questions = [
#     {
#         "question": "What is VNC used for in the context of a Raspberry Pi?",
#         "options": [
#             "To access the Raspberry Pi's graphical interface remotely",
#             "To control the Raspberry Pi's camera",
#             "To update the Raspberry Pi's operating system",
#             "To connect the Raspberry Pi to a network"
#         ],
#         "answer": "To access the Raspberry Pi's graphical interface remotely"
#     },
#     {
#         "question": "Which of the following is a commonly used programming language?",
#         "options": [
#             "Python",
#             "HTML",
#             "CSS",
#             "SQL"
#         ],
#         "answer": "Python"
#     },
#     {
#         "question": "What is the capital of France?",
#         "options": [
#             "Berlin",
#             "Madrid",
#             "Paris",
#             "Rome"
#         ],
#         "answer": "Paris"
#     }
# ]

current_question_index = 0

def load_next_question():
    global current_question_index
    
    if current_question_index < len(questions):
        question_data = questions[current_question_index]
        question_label.config(text=question_data["question"])
        
        # Clear previous radio buttons
        for button in option_buttons:
            button.destroy()

        # Create new radio buttons
        for idx, option in enumerate(question_data["options"]):
            rb = tk.Radiobutton(root, text=option, variable=var, value=option, 
                                bg="#f9f9f9", font=option_font, selectcolor="#add8e6", anchor="w")
            rb.pack(fill="both", padx=20, pady=5)
            option_buttons.append(rb)

    else:
        messagebox.showinfo("Quiz Finished", "You have completed the quiz!")
        root.quit()

def check_answer():
    global current_question_index
    selected_option = var.get()
    correct_answer = questions[current_question_index]["answer"]
    
    if selected_option == correct_answer:
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showinfo("Result", f"Wrong. The correct answer is: {correct_answer}")
    
    current_question_index += 1
    load_next_question()

# Initialize the main window
root = tk.Tk()
root.title("Quiz Application")
root.geometry("500x300")
root.config(bg="#f9f9f9")

# Custom fonts
question_font = font.Font(family="Helvetica", size=16, weight="bold")
option_font = font.Font(family="Helvetica", size=14)

# Question label
question_label = tk.Label(root, text="", bg="#f9f9f9", font=question_font, wraplength=450, justify="left")
question_label.pack(pady=20)

# Variable to store the selected option
var = tk.StringVar()

# List to keep track of option buttons (for clearing old ones)
option_buttons = []

# Load the first question
load_next_question()

# Submit button
submit_button = tk.Button(root, text="Submit", command=check_answer, bg="#4CAF50", fg="white", font=("Helvetica", 14), padx=10, pady=5)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
