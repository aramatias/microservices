# Order Management System (OMS) and Inventory Management System (IMS)

This project is a combined **Order Management System (OMS)** and **Inventory Management System (IMS)**. 
The system allows users to place orders, view available stock, and manage inventory. 
It includes the following functionalities:

- **OMS (Order Management System)**: Users can select items, place orders, and see the total price.
- **IMS (Inventory Management System)**: Admins or users with proper access can manage the inventory (add, update, delete items).

Both systems are built with HTML, CSS, and JavaScript for the frontend and Python (Flask) for the backend.

## Features

### Order Management System (OMS)
- **Item Selection**: Users can choose items from the inventory and place orders.
- **Stock Management**: Displays available stock for each item. If the stock is 0, the item will be marked as "Sold Out."
- **Total Price Calculation**: Automatically calculates the total price based on the selected item and quantity.
- **Order Notification**: Displays notifications for successful or failed order placement.

### Inventory Management System (IMS)
- **Inventory List**: View, update, or delete items from the inventory.
- **Add New Items**: Admins can add new items to the inventory with information like name, price, and quantity.
- **Update Items**: Update details such as item name, price, and quantity.
- **Delete Items**: Remove items from the inventory if needed.


----

## Installation

Follow these steps to set up the project locally:

### Clone the Repository

----

## File Directory Structure

ims/
│
├── ims.py               # Flask application file
├── templates/           # HTML templates for the system
│   ├── index.html       # Main order page (OMS)
├── static/              # Static files (CSS, JS, Images)
│   ├── styles.css       # Custom CSS styles
├── inventory.json       # Inventory data
└── requirements.txt     # Python dependencies

oms-ims/
│
├── oms.py               # Flask application file
├── templates/           # HTML templates for the system
│   ├── order_form.html  # Main order page (OMS)
│   ├── inventory.html   # Inventory management page (IMS)
├── static/              # Static files (CSS, JS, Images)
│   ├── styles.css       # Custom CSS styles
└── requirements.txt     # Python dependencies
└── README.md            # ReadMe File


----


## Install Dependencies
Make sure you have Python and pip installed, then create a virtual environment and install the required dependencies:

python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
pip install -r requirements.txt

----

## Set Up Flask
Ensure that you have Flask installed as part of the requirements. If not, you can install it manually:

pip install flask

----

## Running the Application
Run the Flask application locally by using the following command:

python app.py

This will start the server, and you can view the application at http://localhost:5000 & http://localhost:5001

----

Enjoy!

----

Developed by:
Arabela Mae O. Matias
Honey Mae Ocay
Arnold Christian Calamba

a Final Project Requirement for IT109 - CH1
