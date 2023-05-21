import time
from plyer import notification
import tkinter as tk

def clear_default_text(event):
    if event.widget.get() in ["HH", "mm", "ss"]:
        event.widget.delete(0, tk.END)
        event.widget.config(validate="key", validatecommand=(validation, "%P"))

def validate_input(text):
    if len(text) == 0:
        return True
    return len(text) <= 2 and text.isdigit()

def countdown(t):
    if t >= 0:
        hour, minute, sec = t // 3600, (t // 60) % 60, t % 60
        entries[0].delete(0, tk.END)
        entries[1].delete(0, tk.END)
        entries[2].delete(0, tk.END)
        entries[0].insert(0, str(hour).zfill(2))
        entries[1].insert(0, str(minute).zfill(2))
        entries[2].insert(0, str(sec).zfill(2))
        window.after(1000, countdown, t - 1)  # Schedule the next update after 1 second
    else:
        notification.notify(title="Countdown Timer", message="Your timer is up.", timeout=5, app_icon="C:\\Users\\deniz\\VSCode Projects\\Countdown\\countdown.ico")

def get_input(entries):
    h = int(entries[0].get())
    m = int(entries[1].get())
    s = int(entries[2].get())
    t = h * 3600 + m * 60 + s
    countdown(t-1) 

# create window and give it a title and make it non-resizable
window = tk.Tk()
window.title("Countdown Timer")
window.resizable(width=False, height=False)

# Register the validation function
validation = window.register(validate_input)

# set window size and position
window_width = 200
window_height = 90
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2 - 50
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# create label
label = tk.Label(text="Input the countdown time", fg="white", bg="black", width=30, height=2)
label.grid(row=0, columnspan=3, sticky="nsew")

# create three entries
entries = []
strings = ["HH", "mm", "ss"]
for i in range(3):
    e = tk.Entry(fg="white", bg="black", width=10, justify='center')
    e.insert(0, strings[i])
    e.bind("<FocusIn>", clear_default_text)
    e.grid(row=1, column=i, sticky="nsew")
    entries.append(e)


# create button, set the command to get_input
button = tk.Button(text="Start", command=lambda: get_input(entries), width=5, height=2, fg="white", bg="black")
button.grid(row=2, columnspan=3, sticky="nsew")

window.mainloop()

