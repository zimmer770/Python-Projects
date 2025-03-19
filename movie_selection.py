import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Movie Selector")  # Window title
root.geometry("400x300")  # Window size (width x height)

# Add a label
label = tk.Label(root, text="Welcome to Movie Selector!", font=("Arial", 14))
label.pack(pady=20)  # Add some spacing

# Run the Tkinter event loop
root.mainloop()