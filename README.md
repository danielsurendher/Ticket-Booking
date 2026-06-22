Railway Ticket Booking System

A Python-based Railway Ticket Booking System that uses MySQL Database for storing train, passenger, and ticket information. This project provides a simple command-line interface for managing trains, booking tickets, checking PNR status, and handling user authentication.
Features
 User Registration & Login System
 CAPTCHA Verification
 Add, Update, View, and Delete Trains
 Book Railway Tickets
 Passenger Information Management
 Mobile Number Validation
 Aadhaar Number Validation
 Multiple Payment Options (GPay, PhonePe, Paytm)
 PNR Status Checking
 Ticket Cancellation
 Automatic Seat Availability Management
 MySQL Database Integration
 Technologies Used
Python
MySQL
mysql-connector-python
Datetime Module
Random Module
 Database Tables
users – Stores login credentials
trains – Stores train details and seat availability
tickets – Stores passenger booking information
 How to Run
Install MySQL and create the required database.

Install MySQL Connector:

pip install mysql-connector-python
Update database credentials in railway.py.

Run the program:

python railway.py
 Functionalities
Train Management
Ticket Booking
Ticket Cancellation
PNR Status Check
User Authentication
Seat Availability Tracking
 Project Objective

The main objective of this project is to automate railway reservation operations through a user-friendly command-line application, reducing manual work and efficiently managing train and passenger records.

Developed using Python and MySQL for educational purposes. 
