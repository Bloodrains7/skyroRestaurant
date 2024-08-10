# Skyro Restaurant API

Welcome to the Skyro Restaurant API project. This application provides endpoints for managing table reservations and generating PDF menus for a restaurant.

## Table of Contents

- [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [Table Reservations](#table-reservations)
  - [Menu](#menu)

## Installation

To get started with this project, follow these steps to install the necessary dependencies.

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/skyro-restaurant.git
   cd skyro-restaurant
   
2. **Create Database and Insert data**
   ```bash
   python -m init_data 
   
3. **Running the Application**
   ```bash
   uvicorn main:app --reload

## API Endpoints

### Table Reservations

#### Create Reservation

- **Endpoint:** `POST /reserve/`
- **Description:** Create a new table reservation.
- **Request Body:**

  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "date": "2024-08-15T19:00:00",
    "people": 4
  }
  
- **Response Body:**
  ```json
  {
  "message": "Reservation created successfully",
  "reservation_id": 123
  }
  
### Menu

#### Get Food Menu PDF

- **Endpoint:** `GET /menu/food/`
- **Description:** Generates a PDF of the food menu.
- **Response Body:**
    
    ```text
    Content-Type: application/pdf
    Content-Disposition: attachment; filename="food_menu.pdf"
    Body: PDF file containing the food menu
  
#### Get Drinks Menu PDF

- **Endpoint:** `GET /menu/drinks/`
- **Description:** Generates a PDF of the drinks menu.
- **Response Body:**
    
    ```text
    Content-Type: application/pdf
    Content-Disposition: attachment; filename="food_menu.pdf"
    Body: PDF file containing the food menu
