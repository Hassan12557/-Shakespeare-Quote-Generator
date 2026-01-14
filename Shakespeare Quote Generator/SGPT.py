import tkinter as tk
from tkinter import messagebox
import tensorflow as tf
import numpy as np

 # Load the trained model
model = tf.keras.models.load_model('Shakespeare quote generator.h5')
 # Recompile the model (adjust the optimizer, loss, and metrics to match your training)
 model.compile(
     optimizer='adam',  # Replace with the optimizer used during training
     loss='mse',        # Replace with the loss function used during training
     metrics=[]         # Add any metrics used during training, if applicable
 )

 print("Model loaded and compiled successfully.")

# Preprocess input (adjust based on your model's preprocessing requirements)
def preprocess_input(keyword):
#     # Example preprocessing: Convert keyword into a numerical vector
#     # Modify this function to match how your model expects input data
     return np.array([[len(keyword)]])  # Example: Using keyword length
#
#
# # Generate quote using the trained model
 def generate_quote_from_model(keyword):
     input_data = preprocess_input(keyword)
     prediction = model.predict(input_data)
#
      generated_quote = prediction[0][0]  # Example of retrieving the result
     return generated_quote
#
#
# # Function for the "Generate Quote" button
 def generate_quote():
     keyword = entry.get().strip()
     if keyword:
try:
             # Generate a quote from the model
             quote = generate_quote_from_model(keyword)
             quote_label.config(text=quote)
         except Exception as e:
             messagebox.showerror("Error", f"An error occurred: {e}")
     else:
         messagebox.showwarning("Input Error", "Please enter a keyword!")
#
#
# # Function to copy the quote to clipboard
 def copy_to_clipboard():
     quote = quote_label.cget("text")
     if quote:
         root.clipboard_clear()
         root.clipboard_append(quote)
         messagebox.showinfo("Copied", "Quote copied to clipboard!")
     else:
         messagebox.showwarning("No Quote", "No quote to copy!")
 #Function to reset the input and output
 def generate_new():
     entry.delete(0, tk.END)
     quote_label.config(text="")
#
#
# # Create the GUI
 root = tk.Tk()
 root.title("Shakespearean Quote Generator")
 root.geometry("600x400")
 root.configure(bg='lightblue')
# # Title
 title_label = tk.Label(root, text="Shakespearean Quote Generator", font=("Garamond", 24, 'bold'), bg='lightblue')
 title_label.pack(pady=20)
#
# # Input field
 entry = tk.Entry(root, font=("Garamond", 16), width=30, justify='center')
 entry.pack(pady=10)
#
# # Generate Quote button
 generate_button = tk.Button(root, text="Generate Quote", command=generate_quote, font=("Garamond", 14), bg='lightgreen',
                             activebackground='green')
 generate_button.pack(pady=10)
# # Quote display
 quote_label = tk.Label(root, text="", font=("Garamond", 18, 'italic'), bg='lightblue', wraplength=500)
 quote_label.pack(pady=10)
#
# # Copy to Clipboard button
 copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Garamond", 14),
                         bg='lightyellow', activebackground='yellow')
 copy_button.pack(pady=10)
#
# # Generate New button
 new_button = tk.Button(root, text="Generate New", command=generate_new, font=("Garamond", 14), bg='lightcoral',
                        activebackground='red')
 new_button.pack(pady=10)
# # Footer
 footer_label = tk.Label(root, text="Inspired by the works of Shakespeare", font=("Garamond", 12), bg='lightblue')
 footer_label.pack(side=tk.BOTTOM, pady=10)
#
# # Run the GUI
root.mainloop()