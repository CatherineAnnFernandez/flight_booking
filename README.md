# **Flight Booking Project**
## **Overview**
The Flight Booking Project is a web application that allows users to search for, book, and manage flights. It includes functionalities for user management, flight information, and booking operations.

### **Features**
+ User Management: Register, login, and manage user profiles.
+ Flight Search: Search for available flights based on various criteria.
+ Booking System: Book and manage flight reservations.
+ Authentication: Secure user authentication and authorization.

### **Configuration**
Edit the config.py file to set up your database connection and other configurations as needed.

### **Usage**
Start the application by running:
python app.py
The application will be available at http://localhost:5000 by default.

### **API Endpoints**
+ User Management
  + POST /api/register: Register a new user
  + POST /api/login: Log in a user
  + GET /api/users/{id}: Get user details
+ Flight Search
  + GET /api/flights: Search for flights
  + GET /api/flights/{id}: Get flight details
+ Booking
  + POST /api/bookings: Create a new booking
  + GET /api/bookings/{id}: Get booking details
