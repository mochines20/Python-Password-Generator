import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    # Function to generate passwords based on user input
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length")
        return

    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    result_var.set(password)
    generated_label.config(text="Password Generated!", fg="green")

def show_developer_name():
    developer_names = [
        "Anie Jane Austria",
        "Jeyze Dimaculangan",
        "Fiel Aerhoze Jardin",
        "Aeron Lising",
        "Lawrence Licauan",
        "John Carlo Manalo"
    ]
    developers_text = "\n".join(developer_names)
    messagebox.showinfo("Developers", f"Developers:\n{developers_text}")


# Create main window
window = tk.Tk()
window.title("Password Generator")

# Background Design
background_image = tk.PhotoImage(file="2.png")  
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create and place widgets
tk.Label(window, text="Password Length:", font=("Helvetica", 14)).place(relx=0.5, rely=0.4, anchor=tk.CENTER)
length_entry = tk.Entry(window, font=("Helvetica", 14))
length_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

generate_button = tk.Button(window, text="Generate Password", command=generate_password, font=("Helvetica", 12))
generate_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

result_var = tk.StringVar()
result_label = tk.Label(window, textvariable=result_var, font=("Helvetica", 12), wraplength=400)
result_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Label for indicating that a password has been generated
generated_label = tk.Label(window, text="", font=("Helvetica", 12), fg="green")
generated_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Button to show developer's name
developer_button = tk.Button(window, text="Show Developer", command=show_developer_name, font=("Helvetica", 12))
developer_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Run the main loop
window.mainloop()
