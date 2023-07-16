import tkinter as tk

def generate_pattern():
    N = int(entry_N.get())
    M = int(entry_M.get())
    pattern = ""

    for i in range(1, N, 2):
        pattern += (i * ".|.").center(M, "-") + "\n"
    pattern += "".center(M, "-") + "\n"
    for i in range(N-2, -1, -2):
        pattern += (i * ".|.").center(M, "-") + "\n"

    output_text.delete(1.0, tk.END)  # Clear previous output
    output_text.insert(tk.END, pattern)

# Create the main window
window = tk.Tk()
window.title("Pattern Generator")

# Create input labels and entry fields
label_N = tk.Label(window, text="Enter N:")
label_N.pack()
entry_N = tk.Entry(window)
entry_N.pack()

label_M = tk.Label(window, text="Enter M:")
label_M.pack()
entry_M = tk.Entry(window)
entry_M.pack()

# Create a button to generate the pattern
generate_button = tk.Button(window, text="Generate Pattern", command=generate_pattern)
generate_button.pack()

# Create an output text area
output_text = tk.Text(window)
output_text.pack()

# Start the GUI event loop
window.mainloop()
