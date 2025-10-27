# 🏪 Store Management System

A comprehensive desktop application for managing retail store operations, built with Python and Tkinter using the MVC (Model-View-Controller) architecture pattern.

## 📋 Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Modules](#modules)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Core Functionality
- 👥 **Customer Management** - Complete CRUD operations for customer records
- 👨‍💼 **Employee Management** - Employee management with role-based access
- 📦 **Product Management** - Product catalog with categories, brands, and inventory
- 🛒 **Order Management** - Order processing and tracking
- 💳 **Payment Processing** - Payment handling and transaction recording
- 📍 **Delivery Management** - Delivery tracking and management
- 🏭 **Warehouse Management** - Inventory control and stock management
- 💰 **Financial Tracking** - Financial transactions and reporting
- 🏦 **Bank Account Management** - Multiple bank account management

### User Interface
- 🎨 Modern and intuitive GUI built with Tkinter
- 📊 Data tables with vertical scrollbars
- 🔍 Advanced search and filtering capabilities
- ✨ Consistent button layouts and user experience
- 🔄 Select and Refresh functionality across all views

### Data Management
- ✅ Input validation for all fields
- 💾 SQLite database for data persistence
- 🔒 Secure user authentication
- 📝 Comprehensive logging system

## 🏗️ Architecture

This project follows the **MVC (Model-View-Controller)** architectural pattern:

```
┌─────────────┐
│    View     │  User Interface Layer
└──────┬──────┘
       │
       ↓
┌─────────────┐
│ Controller  │  Business Logic Layer
└──────┬──────┘
       │
       ↓
┌─────────────┐
│  Repository │  Data Access Layer
└──────┬──────┘
       │
       ↓
┌─────────────┐
│  Database   │  SQLite Database
└─────────────┘
```

## 🛠️ Technology Stack

- **Language:** Python 3.x
- **GUI Framework:** Tkinter
- **Database:** SQLite
- **Architecture:** MVC Pattern
- **Testing:** Built-in unittest module

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/StoreAppPython.git
   cd StoreAppPython
   ```

2. **Install dependencies** (if any)
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database**
   ```bash
   # The database will be created automatically on first run
   # Or run the SQL script manually:
   sqlite3 db/selling_db < db/database_tables.sql
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

## 🚀 Usage

### Starting the Application

```bash
python app.py
```

The application will start with the login screen. Use your employee credentials to log in.

### Main Modules

Each module can be accessed independently by running:

```bash
python customer_main.py      # Customer Management
python employee_main.py      # Employee Management
python product_main.py       # Product Management
python order_main.py         # Order Management
python payment_main.py       # Payment Management
python warehouse_main.py     # Warehouse Management
python bank_main.py          # Bank Management
```

### Basic Operations

1. **Select** - Click on a row in the table to select and view details
2. **Refresh** - Refresh the table to show latest data
3. **Save** - Add a new record
4. **Edit** - Update the selected record
5. **Delete** - Remove the selected record

## 📁 Project Structure

```
StoreAppPython/
│
├── app.py                 # Main application entry point
├── login_view.py         # Login and authentication
│
├── model/                # Data models
│   ├── customer.py
│   ├── employee.py
│   ├── product.py
│   ├── order.py
│   ├── payment.py
│   └── ...
│
├── view/                 # User interface
│   ├── customer_view.py
│   ├── employee_view.py
│   ├── product_view.py
│   ├── component/        # Reusable UI components
│   │   ├── table.py
│   │   └── lable_with_entry.py
│   └── ...
│
├── controller/           # Business logic
│   ├── customer_controller.py
│   ├── employee_controller.py
│   └── ...
│
├── service/              # Service layer
│   ├── customer_service.py
│   └── ...
│
├── repository/           # Data access
│   ├── customer_repository.py
│   └── ...
│
├── tools/                # Utilities
│   ├── validators/
│   └── logging.py
│
├── test/                 # Unit tests
│   ├── customer_test.py
│   └── ...
│
└── db/                   # Database
    ├── database_tables.sql
    └── selling_db
```

## 📚 Modules

### Entities
- **Customer** - Customer information and contact details
- **Employee** - Employee management with roles and authentication
- **Product** - Product catalog with categories and inventory
- **Order** - Sales orders and transactions
- **OrderItem** - Order line items
- **Payment** - Payment records and methods
- **Delivery** - Delivery tracking
- **Warehouse** - Warehouse locations
- **WarehouseTransaction** - Stock movements
- **FinancialTransaction** - Financial records
- **Bank** - Bank account management
- **Sample** - Sample product management

### User Interface Components

#### Table Component
- Custom table widget with Treeview
- Vertical scrollbar support
- Row selection functionality
- Data refresh capability

#### LabelWithEntry Component
- Reusable input component
- Label and entry field combination
- Support for different data types
- Validation support

## 👥 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style
- Follow PEP 8 Python style guide
- Add comments for complex logic
- Write unit tests for new features
- Keep the MVC pattern consistent

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

Special thanks to all contributors who have made this project possible. See [CONTRIBUTION_REPORT.md](CONTRIBUTION_REPORT.md) for detailed contributor information.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the development team.

---

**Made with ❤️ by the Store Management Team**

