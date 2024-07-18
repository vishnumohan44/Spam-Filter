import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle
import predict

def check():
    try:
        Message = msg_entry.get()
        if Message == '':
            raise ValueError
        ans = predict.spam_predict(Message)
        if ans[0]==0: pred = "Geniune"
        else: pred = "Spam"
        result = f"Message: {Message}\nPrediction: {pred}\n"

        # Display result
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, result)
        result_text.config(state=tk.DISABLED)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid message.")

# Create the main window
window = tk.Tk()
window.title("Spam Checker")
# window.geometry('300x250')

# Apply a themed style
style = ThemedStyle(window)
style.set_theme("arc")

# Custom styling for buttons
style.configure("TButton",
                font=("Helvetica", 12),
                padding=20,
                relief=tk.RAISED)

# Create the widgets
frame = ttk.Frame(window, padding=20)
frame.grid(row=0, column=0, sticky="nsew")

msg_label = ttk.Label(frame, text="Message:")
msg_label.grid(row=0, column=0, sticky=tk.W)

msg_entry = ttk.Entry(frame, width = 29)
msg_entry.grid(row=0, column=1)

# age_label = ttk.Label(frame, text="Age:")
# age_label.grid(row=1, column=0, sticky=tk.W)

# age_entry = ttk.Entry(frame)
# age_entry.grid(row=1, column=1)

# gender_label = ttk.Label(frame, text="Gender:")
# gender_label.grid(row=2, column=0, sticky=tk.W)

# gender_var = tk.StringVar(window)
# gender_var.set("Male")  # Default value

# gender_option = ttk.Combobox(frame, textvariable=gender_var, values=("Male", "Female", "Other"))
# gender_option.grid(row=2, column=1)

# country_label = ttk.Label(frame, text="Country:")
# country_label.grid(row=3, column=0, sticky=tk.W)

# country_var = tk.StringVar(window)
# country_var.set("United States")  # Default value

# country_option = ttk.Combobox(frame, textvariable=country_var, values=("United States", "Canada", "United Kingdom", "Australia"))
# country_option.grid(row=3, column=1)

check_button = ttk.Button(frame, text="Check Message", command=check)
check_button.grid(row=4, columnspan=2, pady=10)

result_text = tk.Text(frame, height=4, width=30)
result_text.config(state=tk.DISABLED)
result_text.grid(row=5, columnspan=2, pady=10)

# Start the main loop
window.mainloop()
