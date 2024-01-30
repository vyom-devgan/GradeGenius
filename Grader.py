import re
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from traitlets import Bool
from typing import List

# Create the main Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Prompt the user to select a file using a file dialog
file_path = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])

# Check if the user selected a file
if file_path:
    if not file_path.endswith('.csv'):
        messagebox.showerror("Error", "Selected file is not a CSV file.")
    else:
        # Read the selected CSV file into a DataFrame named 'main'
        main: pd.DataFrame = pd.read_csv(file_path)

        # Perform operations on the 'main' DataFrame here

        print("File successfully loaded and processed.")
else:
    messagebox.showinfo("Info", "No file selected. Exiting program.")

def map_grade(x: float) -> str:
    """Maps numerical grades to letter grades."""
    if pd.isnull(x) or x == 0 or x == 'BLANK':
        return "BLANK"
    elif 95 <= x <= 100:
        return "A+"
    elif 87 <= x < 95:
        return "A"
    elif 80 <= x < 87:
        return "A-"
    elif 77 <= x < 80:
        return "B+"
    elif 73 <= x < 77:
        return "B"
    elif 70 <= x < 73:
        return "B-"
    elif 67 <= x < 70:
        return "C+"
    elif 63 <= x < 67:
        return "C"
    elif 60 <= x < 63:
        return "C-"
    elif 57 <= x < 60:
        return "D+"
    elif 53 <= x < 57:
        return "D"
    elif 50 <= x < 53:
        return "D-"
    elif x < 50:
        return "F"
    else:
        return "ERROR"

def grade(csv: pd.DataFrame) -> None:
    """Applies grade mapping to numerical columns."""
    for col in csv.columns:
        if col not in ["Last Name", "First Name", "Email Address"]:
            csv[col] = csv[col].apply(map_grade)

def checker(x: List[str]) -> bool:
    """Checks if column labels match the required format."""
    return True if ["Last Name", "First Name", "Email Address"] == x else False

# Direct Download - Check if labels are ["Last Name", "First Name", "Email Address"] in order
if checker(list(main.columns[:3])):
    main = main.iloc[2:]

# Spreadsheet download
else:
    main = main.drop(main.columns[3], axis=1)

    # Copy row 0 to use as column labels in the new main
    new_labels = main.iloc[0]

    # Remove rows 0,1,2,3
    main = main.iloc[4:]

    # Label columns
    main.columns = ["Last Name", "First Name", "Email Address"] + list(new_labels[3:])

    # Convert columns to numeric where possible
    main = main.apply(pd.to_numeric, errors='ignore')

# Reset index
main.reset_index(drop=True, inplace=True)

# Grade the main DataFrame if labels are correct
if checker(list(main.columns[:3])):
    grade(main)

# Save the graded DataFrame to CSV
main.to_csv('Graded.csv', index=False)