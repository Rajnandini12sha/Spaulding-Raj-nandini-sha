# Employee Data Analysis App

This is a simple desktop application built with Python and Tkinter for analyzing employee data from a CSV file. The app allows users to upload a CSV, filter and group employee data, apply a global salary hike, and download the updated data.

## Features

- **Upload CSV**: Load employee data from a CSV file(**Use the Spaulding.csv file which is uploaded for running the application**)
- **Preview Data**: View the first few rows of the uploaded CSV.
- **Filter by Status**: Filter employees by "Active" or "Inactive" status.
- **Group Data**: Group employees by experience, role, or location.
- **Apply Hike**: Apply a percentage hike to all employees' current compensation.
- **Download CSV**: Save the (possibly updated) data to a new CSV file.

## Requirements

- Python 3.8+
- pandas
- pandasql
- Tkinter (usually included with Python, may require `python3-tk` on some systems)

Example `requirements.txt`:
## How to Run

1. Install dependencies:
2. Run the app:
3. ## Modules and Functions

### Modules Used

- `tkinter`: For GUI components.
- `pandas`: For data manipulation.
- `sqlite3`: (Imported, but not used in this file.)
- `pandasql`: (Imported, but not used in this file.)

### Main Functions

#### `open_csv_file()`
- Opens a file dialog to select a CSV file.
- Loads the CSV into a global pandas DataFrame `data`.
- Displays a preview of the data in a new window.

#### `on_status_change(*args)`
- Triggered when the status dropdown changes.
- Filters the data by the "Active?" column ("Y" for active, "N" for inactive).
- Displays the filtered data in a new window.

#### `group_employee()`
- Groups employees by "Years of Experience".
- Displays the count for each experience group.

#### `group_by_role()`
- Groups employees by "Role".
- Displays the count for each role.

#### `group_by_location()`
- Groups employees by "Location".
- Displays the count for each location.

#### `apply_hike()`
- Reads a hike percentage from the entry box.
- Applies the hike to the "Current Comp (INR)" column for all employees.
- Shows a new window with the old and updated compensation.

#### `save_to_csv()`
- Opens a file dialog to save the current data to a CSV file.

### GUI Components

- **Upload Button**: Opens the CSV file dialog.
- **Status Dropdown**: Select "active" or "inactive" to filter employees.
- **Group Dropdown**: Choose to group by experience, role, or location.
- **Hike Entry & Button**: Enter a percentage and apply a salary hike.
- **Download Button**: Save the current data to a CSV.
- **Quit Button**: Exit the application.

## Notes

- The CSV file must have columns: "Active?", "Years of Experience", "Role", "Location", and "Current Comp (INR)".
- The app does not modify the original CSV until you save/export.
- Some modules (`sqlite3`, `pandasql`) are imported for possible future use but not currently used.

---
