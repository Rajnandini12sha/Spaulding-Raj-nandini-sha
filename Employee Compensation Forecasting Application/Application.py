import tkinter as tk
from tkinter import filedialog
import pandas as pd
import sqlite3
import pandasql as psql
def open_csv_file():
    global data
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv")],
        title="Select a CSV file"
    )
    if file_path:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(file_path)
        print("CSV file loaded successfully!")
        # Display the first few rows of the CSV file in a new window
        top = tk.Toplevel(root)
        top.title("CSV Preview")
        text = tk.Text(top, wrap="none", width=120, height=20)
        text.insert("end", data.head().to_string(index=False))
        text.pack(expand=True, fill="both")

root = tk.Tk()
root.title("analysis app")
root.geometry("1000x1000")  # Set window size
root.configure(bg="grey")

# Create a button to open the file dialog
button = tk.Button(root, text="UPLOAD csv FILE", command=open_csv_file, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), padx=20, pady=10, relief="raised", bd=3, activebackground="#388E3C")
button.pack(pady=40)

status_var = tk.StringVar(root)
status_var.set("Status of the employee")  # default value

def on_status_change(*args):
    if 'data' not in globals():
        print("No CSV file loaded yet.")
        return
    df = data
    if status_var.get() == "active":
        filtered_df = df[df["Active?"] == "Y"]
        top = tk.Toplevel(root)
        top.title("Filtered Data")
        text = tk.Text(top, wrap="none", width=120, height=20)
        text.insert("end", filtered_df.to_string(index=False))
        text.pack(expand=True, fill="both")
        print("Active function executed")
    else:
        filtered_df = df[df["Active?"] == "N"]
        top = tk.Toplevel(root)
        top.title("Filtered Data")
        text = tk.Text(top, wrap="none", width=120, height=20)
        text.insert("end", filtered_df.to_string(index=False))
        text.pack(expand=True, fill="both")
        # Call your function for inactive
        print("Inactive function executed")



def group_employee():
    if 'data' not in globals():
        print("No CSV file loaded yet.")
        return
    df = data
    if "Years of Experience" not in df.columns:
        print("Column 'exp' not found in the data.")
        return
    grouped = df.groupby("Years of Experience").size().reset_index(name="count")
    top = tk.Toplevel(root)
    top.title("Grouped by exp")
    text = tk.Text(top, wrap="none", width=60, height=20)
    text.insert("end", grouped.to_string(index=False))
    text.pack(expand=True, fill="both")


def group_by_role():
    if 'data' not in globals():
        print("No CSV file loaded yet.")
        return
    df = data
    if "Role" not in df.columns:
        print("Column 'Role' not found in the data.")
        return
    grouped = df.groupby("Role").size().reset_index(name="count")
    top = tk.Toplevel(root)
    top.title("Grouped by Role")
    text = tk.Text(top, wrap="none", width=60, height=20)
    text.insert("end", grouped.to_string(index=False))
    text.pack(expand=True, fill="both")

    # Show bar chart
    try:
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(grouped["Role"], grouped["count"], color="#8BC34A")
        ax.set_xlabel("Role")
        ax.set_ylabel("Count")
        ax.set_title("Employee Count by Role")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        chart_win = tk.Toplevel(top)
        chart_win.title("Bar Chart - Grouped by Role")
        canvas = FigureCanvasTkAgg(fig, master=chart_win)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both")
    except ImportError:
        print("matplotlib is required to display the bar chart.")





def group_by_location():
    if 'data' not in globals():
        print("No CSV file loaded yet.")
        return
    df = data
    if "Location" not in df.columns:
        print("Column 'Location' not found in the data.")
        return
    grouped = df.groupby("Location").size().reset_index(name="count")
    top = tk.Toplevel(root)
    top.title("Grouped by Location")
    text = tk.Text(top, wrap="none", width=60, height=20)
    text.insert("end", grouped.to_string(index=False))
    text.pack(expand=True, fill="both")

    # Show bar chart
    try:
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(grouped["Location"], grouped["count"], color="#2196F3")
        ax.set_xlabel("Location")
        ax.set_ylabel("Count")
        ax.set_title("Employee Count by Location")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        chart_win = tk.Toplevel(top)
        chart_win.title("Bar Chart - Grouped by Location")
        canvas = FigureCanvasTkAgg(fig, master=chart_win)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both")
    except ImportError:
        print("matplotlib is required to display the bar chart.")


status_var.trace_add("write", on_status_change)
dropdown = tk.OptionMenu(root, status_var, "active", "inactive")
dropdown.config(bg="#2196F3", fg="white", font=("Arial", 11), relief="groove", bd=2, activebackground="#1976D2")
dropdown["menu"].config(bg="white", fg="black", font=("Arial", 11))
dropdown.pack(pady=40)


group_options = ["Group by Experience", "Group by Role", "Group by Location"]
group_var = tk.StringVar(root)
group_var.set(group_options[0])

def on_group_change(*args):
    if group_var.get() == "Group by Experience":
        group_employee()
    elif group_var.get() == "Group by Role":
        group_by_role()
    elif group_var.get() == "Group by Location":
        group_by_location()

group_var.trace_add("write", on_group_change)
group_dropdown = tk.OptionMenu(root, group_var, *group_options)
group_dropdown.config(bg="#FF9800", fg="white", font=("Arial", 11), relief="groove", bd=2, activebackground="#F57C00")
group_dropdown["menu"].config(bg="white", fg="black", font=("Arial", 11))
group_dropdown.pack(pady=10)

# Add a button and entry for global hike percentage
hike_frame = tk.Frame(root)
hike_frame.pack(pady=10)
hike_label = tk.Label(hike_frame, text="Enter Hike Percentage:")
hike_label.pack(side="left")
hike_entry = tk.Entry(hike_frame, width=10)
hike_entry.pack(side="left")


def apply_hike():
    if 'data' not in globals():
        print("No CSV file loaded yet.")
        return
    try:
        hike_percent = float(hike_entry.get())
    except ValueError:
        print("Invalid hike percentage.")
        return
    global data
    if "Current Comp (INR)" not in data.columns:
        print("Column 'Salary' not found in the data.")
        return
    updated_data = data.copy()
    updated_data["Current Comp (INR)"] = (
        updated_data["Current Comp (INR)"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .astype(float)
    )
    updated_data["Current Comp (INR)"] = updated_data["Current Comp (INR)"].astype(float) * (1 + hike_percent / 100)
    print(f"Applied {hike_percent}% hike to all salaries.")
    # Display the updated data with the updated compensation column highlighted
    top = tk.Toplevel(root)
    top.title("Updated Data with Hike")
    text = tk.Text(top, wrap="none", width=120, height=20)
    display_df = updated_data.copy()
    display_df["OLD_COMP"] = data["Current Comp (INR)"].astype(str).str.replace(",", "", regex=False).astype(float)
    display_df["UPDATED_COMP"] = display_df["Current Comp (INR)"]
    cols = [col for col in display_df.columns if col not in ["OLD_COMP", "UPDATED_COMP"]] + ["OLD_COMP", "UPDATED_COMP"]
    text.insert("end", display_df[cols].to_string(index=False))
    text.pack(expand=True, fill="both")

hike_button = tk.Button(hike_frame, text="Apply Hike", command=apply_hike, bg="#9C27B0", fg="white", font=("Arial", 11, "bold"), padx=10, pady=5, relief="raised", bd=2, activebackground="#7B1FA2")
hike_button.pack(side="left", padx=5)

download_button = tk.Button(root, text="Download CSV", command=lambda: save_to_csv(), bg="#607D8B", fg="white", font=("Arial", 11, "bold"), padx=10, pady=5, relief="raised", bd=2, activebackground="#455A64")
download_button.pack(pady=10)
def save_to_csv():
    if 'data' not in globals():
        print("No CSV file loaded yet.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        data.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")


quit_button = tk.Button(root, text="Quit", command=root.quit, bg="#F44336", fg="white", font=("Arial", 11, "bold"), padx=10, pady=5, relief="raised", bd=2, activebackground="#B71C1C")
quit_button.pack(pady=10)
# Run the application
root.mainloop()
