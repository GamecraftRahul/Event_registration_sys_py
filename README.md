# Event Registration System

A desktop-based Event Registration System developed using **Python**, **Tkinter**, **ttkbootstrap**, and **MySQL**. This application allows users to register participants for events, manage participant records, update information, and delete registrations through a modern graphical user interface.

---

## Features

- Register participants for events
- Store participant details in MySQL database
- View all registered participants
- Update participant information
- Delete participant records
- User-friendly GUI using ttkbootstrap
- Automatic data loading from database
- Form validation and error handling

---

## Technologies Used

- Python 3.x
- Tkinter
- ttkbootstrap
- MySQL
- mysql-connector-python

---

## Project Structure

```
Event Registration System/
│
├── event registration_sys.py
├── event registration systeam.sql
├── README.md
```

---

## Database Setup

### Step 1: Create Database

Run the SQL file provided in the project:

```sql
SOURCE event registration systeam.sql;
```

Or manually create the database:

```sql
CREATE DATABASE event_system;
USE event_system;
```

### Step 2: Create Participants Table

```sql
CREATE TABLE participants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    event_name VARCHAR(100) NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/event-registration-system.git
cd event-registration-system
```

### Install Required Packages

```bash
pip install mysql-connector-python
pip install ttkbootstrap
```

---

## Configure Database Connection

Open the Python file and update the database credentials:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'YOUR_PASSWORD',
    'database': 'event_system'
}
```

---

## Running the Application

```bash
python "event registration_sys.py"
```

---

## Application Modules

### Participant Registration
- Enter Name
- Enter Email
- Enter Phone Number
- Enter Event Name
- Click Register

### Update Participant
- Select a record from the table
- Modify the details
- Click Update

### Delete Participant
- Select a participant record
- Click Delete

### Clear Form
- Clears all input fields

### Data Management
- Loads all records from MySQL database
- Displays data in a Treeview table

---

## GUI Components

- Labels
- Entry Fields
- Buttons
- Treeview Table
- Message Boxes
- Bootstrap Themes

---

## Validation Features

- Prevents empty form submission
- Displays warning messages for invalid operations
- Database connection error handling
- Record selection validation before update or delete

---

## Screenshots

Add screenshots of:
- Main Dashboard
- Registration Form
- Participant Table
- Update Operation
- Delete Operation

---

## Future Enhancements

- Event-wise filtering
- Search participant functionality
- Export data to Excel
- PDF report generation
- User authentication system
- Email confirmation notifications
- Attendance management

---

## Learning Outcomes

This project demonstrates:

- Python GUI Development
- MySQL Database Connectivity
- CRUD Operations
- Event-Driven Programming
- Data Validation
- Desktop Application Development

---

## Author

**Rahul Kumar**

Python | MySQL | Tkinter Developer

---

## License

This project is developed for educational and learning purposes.
