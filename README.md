# Food Delivery Management System

A comprehensive Python-based management system for a food delivery service. This application provides a structured way to manage restaurants, menu items, orders, delivery partners, shopping carts, ratings, and delivery fees.

## 🚀 Features

- **Restaurant Management**: Track restaurant details, cuisines, and operational status.
- **Menu System**: Add, remove, and update menu items with pricing and availability.
- **Order Tracking**: Manage the lifecycle of an order from placement to delivery.
- **Delivery Partners**: Assign and track delivery partners with real-time status updates.
- **Shopping Cart**: Dynamic cart management with item addition, removal, and promocode application.
- **Rating System**: Validate and submit ratings for both restaurants and delivery partners.
- **Fee Calculation**: Automated delivery fee calculation based on distance.

## 📂 Project Structure

```text
food/
├── app/
│   ├── main.py        # Core logic containing all management classes
│   └── Rating.py      # Independent module for handling ratings
└── README.md          # Project documentation
```

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.x

### Running the Application
To run the main application logic:
```bash
python app/main.py
```

To run the rating module specifically:
```bash
python app/Rating.py
```

## 💻 Code Overview

The system is built using Object-Oriented Programming (OOP) principles with several key classes:

- `Restaurant`: Handles restaurant metadata and menu operations.
- `MenuItem`: Represents individual food items.
- `Order`: Manages order status and ETA.
- `DeliveryPartner`: Manages partner availability and delivery status.
- `Cart`: Handles customer item selection and checkout.
- `Rating`: Validates and records feedback.
- `deliveryFee`: Calculates costs based on delivery distance.

## 📝 License
This project is for educational purposes.
