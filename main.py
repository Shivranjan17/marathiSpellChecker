import tkinter as tk
from tkinter import scrolledtext
import subprocess

def check_spelling():
    input_text = input_entry.get().strip()

    try:
        process = subprocess.Popen(['aspell', '-a', '--lang=mr'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, _ = process.communicate(input_text)

        # Extract suggestions from Aspell output
        suggestions = []
        for line in stdout.split('\n'):
            if line.startswith('&'):
                parts = line.split(':', 1)
                suggestions.append(parts[1].strip())

        # Display suggestions in the result_text widget
        result_text.delete('1.0', tk.END)
        if suggestions:
            for word in suggestions:
                result_text.insert(tk.END, f"{word}\n")
        else:
            result_text.insert(tk.END, "No suggestions found")

    except Exception as e:
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Marathi Spell Checker")

# Create and place GUI components
input_label = tk.Label(root, text="Enter Marathi text:", font=("Helvetica", 12))
input_label.pack(pady=5)

input_entry = tk.Entry(root, width=50, font=("Helvetica", 12))
input_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Spelling", command=check_spelling, font=("Helvetica", 12))
check_button.pack(pady=5)

result_text = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD, font=("Helvetica", 12))
result_text.pack(pady=5)

# Run the GUI
root.mainloop()
