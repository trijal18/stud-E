import tkinter as tk
from tkinter import messagebox, font, filedialog
import remove_files
import genrate_mcqs

# Initialize main application window
root = tk.Tk()
root.title("MCQ Quiz Application")
root.geometry("500x300")
root.config(bg="#f9f9f9")

# Global variables
current_question_index = 0
time_limit = 15  # Time limit per question in seconds
time_remaining = time_limit
timer_running = False
questions = []

# Custom fonts
question_font = font.Font(family="Helvetica", size=16, weight="bold")
option_font = font.Font(family="Helvetica", size=14)

def load_next_question():
    global current_question_index, time_remaining, timer_running
    
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
        
        # Reset the timer and start it
        time_remaining = time_limit
        timer_running = True
        update_timer()

    else:
        messagebox.showinfo("Quiz Finished", "You have completed the quiz!")
        root.quit()

def update_timer():
    global time_remaining, timer_running
    
    if time_remaining > 0:
        timer_label.config(text=f"Time remaining: {time_remaining} seconds")
        time_remaining -= 1
        root.after(1000, update_timer)
    else:
        if timer_running:
            timer_running = False
            messagebox.showinfo("Time's Up!", "You ran out of time!")
            check_answer(skip=True)

def check_answer(skip=False):
    global current_question_index, timer_running
    
    timer_running = False  # Stop the timer when an answer is checked
    if not skip:
        selected_option = var.get()
        correct_answer = questions[current_question_index]["answer"]
        
        if selected_option == correct_answer:
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Wrong. The correct answer is: {correct_answer}")
    
    current_question_index += 1
    load_next_question()

def start_quiz(file_path):
    global questions
    questions = genrate_mcqs.genrate_mcqs(file_path)
    quiz_page()

def open_file():
    file_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if file_path:
        start_quiz(file_path)

def drag_and_drop_page():
    drag_label = tk.Label(root, text="Drag and drop a file here or click to browse", 
                          bg="#f9f9f9", font=question_font, padx=20, pady=40)
    drag_label.pack(pady=20)

    browse_button = tk.Button(root, text="Browse", command=open_file, 
                              bg="#4CAF50", fg="white", font=("Helvetica", 14), padx=10, pady=5)
    browse_button.pack(pady=20)

def quiz_page():
    for widget in root.winfo_children():
        widget.destroy()
    
    global question_label, timer_label, var, option_buttons
    
    question_label = tk.Label(root, text="", bg="#f9f9f9", font=question_font, wraplength=450, justify="left")
    question_label.pack(pady=20)
    
    timer_label = tk.Label(root, text="", bg="#f9f9f9", font=("Helvetica", 12), fg="red")
    timer_label.pack(pady=10)
    
    var = tk.StringVar()
    option_buttons = []
    
    load_next_question()
    
    submit_button = tk.Button(root, text="Submit", command=check_answer, 
                              bg="#4CAF50", fg="white", font=("Helvetica", 14), padx=10, pady=5)
    submit_button.pack(pady=20)

drag_and_drop_page()

# Run the application
root.mainloop()
