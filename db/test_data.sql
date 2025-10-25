-- ============================================
-- TEST DATA FOR SELLING SYSTEM
-- Comprehensive test data for all entities
-- ============================================

-- ============================================
-- BASE ENTITIES - Multiple records
-- ============================================

-- Banks (ID: 1-5)
insert or ignore into banks (id, name, account, balance, description) values 
(1, 'Melli Bank', 'checking', 5000000, 'Main checking account'),
(2, 'Saderat Bank', 'saving', 8000000, 'Savings account'),
(3, 'Parsian Bank', 'current', 3000000, 'Current account'),
(4, 'Mellat Bank', 'checking', 6000000, 'Business checking'),
(5, 'Tejarat Bank', 'saving', 4000000, 'Personal savings');

-- Customers (ID: 1-10)
insert or ignore into customers (id, first_name, last_name, phone_number, address) values 
(1, 'Ahmad', 'Rezaei', '09123456789', 'Tehran_Street1_123'),
(2, 'Reza', 'Mohammadi', '09123456790', 'Isfahan_Avenue2_456'),
(3, 'Mohammad', 'Ali Akbari', '09123456791', 'Shiraz_Road3_789'),
(4, 'Ali', 'Hosseini', '09123456792', 'Tabriz_Lane4_012'),
(5, 'Hassan', 'Kazemi', '09123456793', 'Mashhad_Boulevard5_345'),
(6, 'Farhad', 'Salehi', '09123456794', 'Qom_Street6_678'),
(7, 'Saeed', 'Rahimi', '09123456795', 'Ahvaz_Avenue7_901'),
(8, 'Majid', 'Naderi', '09123456796', 'Kerman_Road8_234'),
(9, 'Amir', 'Karimi', '09123456797', 'Rasht_Lane9_567'),
(10, 'Mohsen', 'Zarei', '09123456798', 'Yazd_Boulevard10_890');

-- Employees (ID: 1-6)
insert or ignore into employees (id, first_name, last_name, salary, occupation, phone_number, username, password, role) values 
(1, 'ali', 'Mohammadi', 5000000, 'cashier', '09123456800', 'aliuser', 'pass1234', 'cashier'),
(2, 'reza', 'Ahmadi', 6000000, 'manager', '09123456801', 'rezauser', 'pass1234', 'manager'),
(3, 'hassan', 'Karimi', 4500000, 'storekeeper', '09123456802', 'hassanuser', 'pass1234', 'storekeeper'),
(4, 'majid', 'Rezaei', 5500000, 'cashier', '09123456803', 'majiduser', 'pass1234', 'cashier'),
(5, 'sina', 'Hosseini', 4700000, 'sale', '09123456804', 'sinauser', 'pass1234', 'sale'),
(6, 'amir', 'Naderi', 5200000, 'storekeeper', '09123456805', 'amiruser', 'pass1234', 'storekeeper');

-- Products (ID: 1-20)
insert or ignore into products (id, name, brand, model, serial, category, unit, expiration_date) values 
(1, 'Laptop', 'Dell', 'XPS15', 'SN123456', 'Electronics', 'Piece', '2025/12/31'),
(2, 'Mouse', 'Logitech', 'MX3', 'SN789012', 'Electronics', 'Piece', NULL),
(3, 'Keyboard', 'Corsair', 'K95', 'SN345678', 'Electronics', 'Piece', NULL),
(4, 'Monitor', 'LG', '27GL850', 'SN901234', 'Electronics', 'Piece', NULL),
(5, 'Webcam', 'Logitech', 'C920', 'SN567890', 'Electronics', 'Piece', NULL),
(6, 'Speaker', 'Bose', 'SoundLink', 'SN234567', 'Electronics', 'Piece', NULL),
(7, 'Headphones', 'Sony', 'WH1000XM4', 'SN890123', 'Electronics', 'Piece', NULL),
(8, 'Tablet', 'Samsung', 'Galaxy Tab', 'SN456789', 'Electronics', 'Piece', '2026/01/15'),
(9, 'Phone', 'iPhone', '14 Pro', 'SN012345', 'Electronics', 'Piece', NULL),
(10, 'Watch', 'Apple', 'Watch Series 8', 'SN678901', 'Electronics', 'Piece', NULL),
(11, 'Printer', 'HP', 'LaserJet Pro', 'SN345012', 'Electronics', 'Piece', NULL),
(12, 'Scanner', 'Epson', 'V39', 'SN901345', 'Electronics', 'Piece', NULL),
(13, 'Router', 'TP-Link', 'Archer AX50', 'SN567234', 'Electronics', 'Piece', NULL),
(14, 'SSD', 'Samsung', '980 PRO', 'SN234678', 'Electronics', 'Piece', NULL),
(15, 'RAM', 'Corsair', 'Vengeance', 'SN890456', 'Electronics', 'Piece', NULL),
(16, 'Graphics Card', 'NVIDIA', 'RTX 4080', 'SN456123', 'Electronics', 'Piece', NULL),
(17, 'Motherboard', 'ASUS', 'ROG Strix', 'SN123789', 'Electronics', 'Piece', NULL),
(18, 'CPU', 'Intel', 'i9-13900K', 'SN789234', 'Electronics', 'Piece', NULL),
(19, 'Power Supply', 'Corsair', 'RM850x', 'SN345567', 'Electronics', 'Piece', NULL),
(20, 'Case', 'Fractal Design', 'Meshify C', 'SN012890', 'Electronics', 'Piece', NULL);

-- Samples (ID: 1-5)
insert or ignore into samples (id, name, description) values 
(1, 'Sample 1', 'Test sample for electronics'),
(2, 'Sample 2', 'Test sample for furniture'),
(3, 'Sample 3', 'Test sample for clothing'),
(4, 'Sample 4', 'Test sample for food'),
(5, 'Sample 5', 'Test sample for books');

-- ============================================
-- DEPENDENT ENTITIES - Multiple records with relationships
-- ============================================

-- Warehouses (ID: 1-10, depends on Products 1-20)
insert or ignore into warehouses (id, product_id, quantity) values 
(1, 1, 100),  -- Laptop stock
(2, 2, 200),  -- Mouse stock
(3, 3, 150),  -- Keyboard stock
(4, 4, 50),   -- Monitor stock
(5, 5, 80),   -- Webcam stock
(6, 6, 60),   -- Speaker stock
(7, 7, 90),   -- Headphones stock
(8, 8, 70),   -- Tablet stock
(9, 9, 120),  -- Phone stock
(10, 10, 110); -- Watch stock

-- Payments (ID: 1-15, depends on Customers 1-10, Employees 1-6)
insert or ignore into payments (id, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id, description) values 
(1, 'income', 'cash', '2024/01/01', 1, 500000, 1, 'Initial payment from customer 1'),
(2, 'income', 'card', '2024/01/02', 2, 750000, 2, 'Card payment from customer 2'),
(3, 'expense', 'check', '2024/01/03', 3, 300000, 3, 'Check payment'),
(4, 'income', 'cash', '2024/01/04', 4, 900000, 1, 'Cash payment from customer 4'),
(5, 'income', 'card', '2024/01/05', 5, 1200000, 2, 'Card payment from customer 5'),
(6, 'expense', 'transfer', '2024/01/06', 1, 200000, 4, 'Transfer payment'),
(7, 'income', 'cash', '2024/01/07', 6, 600000, 1, 'Cash payment from customer 6'),
(8, 'income', 'card', '2024/01/08', 7, 850000, 2, 'Card payment from customer 7'),
(9, 'income', 'cash', '2024/01/09', 8, 450000, 3, 'Cash payment from customer 8'),
(10, 'expense', 'check', '2024/01/10', 9, 400000, 5, 'Check payment from customer 9'),
(11, 'income', 'card', '2024/01/11', 10, 1100000, 2, 'Card payment from customer 10'),
(12, 'income', 'cash', '2024/01/12', 1, 550000, 4, 'Second payment from customer 1'),
(13, 'income', 'card', '2024/01/13', 2, 680000, 1, 'Card payment from customer 2'),
(14, 'expense', 'transfer', '2024/01/14', 3, 250000, 3, 'Transfer payment'),
(15, 'income', 'cash', '2024/01/15', 4, 720000, 2, 'Cash payment from customer 4');

-- Warehouse Transactions (ID: 1-12, depends on Products 1-10, Customers 1-10, Employees 1-6)
insert or ignore into warehouse_transactions (id, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id) values 
(1, 1, 10, 'output', '2024/01/01', 1, 1),   -- Customer 1 bought 10 laptops
(2, 2, 5, 'output', '2024/01/02', 2, 2),    -- Customer 2 bought 5 mice
(3, 3, 3, 'output', '2024/01/03', 3, 3),    -- Customer 3 bought 3 keyboards
(4, 4, 2, 'output', '2024/01/04', 4, 1),    -- Customer 4 bought 2 monitors
(5, 1, 20, 'input', '2024/01/05', NULL, 5), -- Employee restocks laptops
(6, 2, 50, 'input', '2024/01/06', NULL, 6), -- Employee restocks mice
(7, 5, 8, 'output', '2024/01/07', 5, 2),    -- Customer 5 bought 8 webcams
(8, 6, 4, 'output', '2024/01/08', 6, 3),    -- Customer 6 bought 4 speakers
(9, 7, 6, 'output', '2024/01/09', 7, 1),    -- Customer 7 bought 6 headphones
(10, 3, 30, 'input', '2024/01/10', NULL, 4), -- Employee restocks keyboards
(11, 8, 12, 'output', '2024/01/11', 8, 2),  -- Customer 8 bought 12 tablets
(12, 9, 15, 'output', '2024/01/12', 9, 5);  -- Customer 9 bought 15 phones

-- Orders (ID: 1-15, depends on Customers 1-10, Employees 1-6, Payments 1-15, Warehouse Transactions 1-12)
insert or ignore into orders (id, order_type, customer_id, employee_id, date_time, payment_id, warehouse_transaction_id, tax, total_discount, total_amount) values 
(1, 'frooshe', 1, 1, '2024/01/01', 1, 1, 100000, 5000, 95000),
(2, 'frooshe', 2, 2, '2024/01/02', 2, 2, 150000, 7500, 142500),
(3, 'kharid', 3, 3, '2024/01/03', 3, 3, 60000, 3000, 57000),
(4, 'frooshe', 4, 1, '2024/01/04', 4, 4, 180000, 9000, 171000),
(5, 'frooshe', 5, 2, '2024/01/05', 5, NULL, 240000, 12000, 228000),
(6, 'frooshe', 6, 3, '2024/01/06', 6, 6, 120000, 6000, 114000),
(7, 'kharid', 7, 4, '2024/01/07', 7, 7, 170000, 8500, 161500),
(8, 'frooshe', 8, 5, '2024/01/08', 8, 8, 90000, 4500, 85500),
(9, 'frooshe', 9, 6, '2024/01/09', 9, 9, 90000, 4500, 85500),
(10, 'kharid', 10, 1, '2024/01/10', 10, 10, 80000, 4000, 76000),
(11, 'frooshe', 1, 2, '2024/01/11', 11, 11, 220000, 11000, 209000),
(12, 'frooshe', 2, 3, '2024/01/12', 12, 12, 136000, 6800, 129200),
(13, 'frooshe', 3, 4, '2024/01/13', 13, NULL, 50000, 2500, 47500),
(14, 'kharid', 4, 5, '2024/01/14', 14, NULL, 44000, 2200, 41800),
(15, 'frooshe', 5, 1, '2024/01/15', 15, NULL, 144000, 7200, 136800);

-- Order Items (ID: 1-20, depends on Orders 1-15, Products 1-20)
insert or ignore into order_items (id, order_id, customer, product_id, quantity, price, discount, description) values 
(1, 1, 'Ahmad Rezaei', 1, 2, 100000, 5000, 'Laptop order'),
(2, 1, 'Ahmad Rezaei', 2, 3, 50000, 2500, 'Mouse order'),
(3, 2, 'Reza Mohammadi', 3, 1, 150000, 7500, 'Keyboard order'),
(4, 2, 'Reza Mohammadi', 4, 1, 600000, 30000, 'Monitor order'),
(5, 3, 'Mohammad Ali Akbari', 5, 2, 80000, 4000, 'Webcam order'),
(6, 4, 'Ali Hosseini', 6, 2, 900000, 45000, 'Speaker order'),
(7, 4, 'Ali Hosseini', 7, 1, 450000, 22500, 'Headphones order'),
(8, 5, 'Hassan Kazemi', 8, 1, 1200000, 60000, 'Tablet order'),
(9, 5, 'Hassan Kazemi', 9, 1, 2000000, 100000, 'Phone order'),
(10, 6, 'Farhad Salehi', 10, 1, 1500000, 75000, 'Watch order'),
(11, 7, 'Saeed Rahimi', 11, 1, 800000, 40000, 'Printer order'),
(12, 8, 'Majid Naderi', 12, 1, 300000, 15000, 'Scanner order'),
(13, 9, 'Amir Karimi', 13, 1, 900000, 45000, 'Router order'),
(14, 10, 'Mohsen Zarei', 14, 2, 350000, 17500, 'SSD order'),
(15, 11, 'Ahmad Rezaei', 15, 4, 150000, 7500, 'RAM order'),
(16, 11, 'Ahmad Rezaei', 16, 1, 5000000, 250000, 'Graphics Card order'),
(17, 12, 'Reza Mohammadi', 17, 1, 6000000, 300000, 'Motherboard order'),
(18, 13, 'Mohammad Ali Akbari', 18, 1, 8000000, 400000, 'CPU order'),
(19, 14, 'Ali Hosseini', 19, 1, 2000000, 100000, 'Power Supply order'),
(20, 15, 'Hassan Kazemi', 20, 2, 150000, 7500, 'Case order');

-- Financial Transactions (ID: 1-12, depends on Customers 1-10, Employees 1-6, Payments 1-15)
insert or ignore into financial_transactions (id, transaction_type, customer_id, employee_id, amount, date_time, payment_id, description) values 
(1, 'sale', 1, 1, 500000, '2024/01/01', 1, 'Laptop sale transaction'),
(2, 'sale', 2, 2, 750000, '2024/01/02', 2, 'Electronics sale transaction'),
(3, 'purchase', 3, 3, 300000, '2024/01/03', 3, 'Hardware purchase'),
(4, 'sale', 4, 1, 900000, '2024/01/04', 4, 'Accessories sale transaction'),
(5, 'sale', 5, 2, 1200000, '2024/01/05', 5, 'Premium product sale'),
(6, 'salary', NULL, 1, 5000000, '2024/01/06', NULL, 'Employee salary payment'),
(7, 'salary', NULL, 2, 6000000, '2024/01/07', NULL, 'Manager salary payment'),
(8, 'expense', 1, 1, 200000, '2024/01/08', 6, 'Office expense'),
(9, 'expense', 2, 2, 300000, '2024/01/09', 7, 'Equipment purchase'),
(10, 'sale', 10, 2, 1100000, '2024/01/10', 11, 'Large sale transaction'),
(11, 'purchase', 7, 3, 450000, '2024/01/11', 8, 'Inventory purchase'),
(12, 'sale', 8, 1, 450000, '2024/01/12', 9, 'Regular sale transaction');

-- Deliveries (ID: 1-8, standalone)
insert or ignore into deliveries (id, first_name, last_name, address, description) values 
(1, 'Reza', 'Ahmadi', 'Tehran_Street1_123', 'Standard delivery for order 1'),
(2, 'Hassan', 'Karimi', 'Isfahan_Avenue2_456', 'Express delivery for order 2'),
(3, 'Majid', 'Rezaei', 'Shiraz_Road3_789', 'Standard delivery for order 3'),
(4, 'Sina', 'Hosseini', 'Tabriz_Lane4_012', 'Express delivery for order 4'),
(5, 'Amir', 'Naderi', 'Mashhad_Boulevard5_345', 'Standard delivery for order 5'),
(6, 'Mohsen', 'Zarei', 'Qom_Street6_678', 'Priority delivery for order 6'),
(7, 'Farhad', 'Salehi', 'Ahvaz_Avenue7_901', 'Standard delivery for order 7'),
(8, 'Saeed', 'Rahimi', 'Kerman_Road8_234', 'Express delivery for order 8');

-- ============================================
-- DATA SUMMARY
-- ============================================
-- Banks: 5 records (ID 1-5)
-- Customers: 10 records (ID 1-10)
-- Employees: 6 records (ID 1-6)
-- Products: 20 records (ID 1-20)
-- Samples: 5 records (ID 1-5)
-- Warehouses: 10 records (ID 1-10, linked to Products 1-10)
-- Payments: 15 records (ID 1-15, linked to Customers 1-10, Employees 1-6)
-- Warehouse Transactions: 12 records (ID 1-12, linked to Products 1-10, Customers 1-10, Employees 1-6)
-- Orders: 15 records (ID 1-15, linked to Customers 1-10, Employees 1-6, Payments 1-15, Warehouse Transactions 1-12)
-- Order Items: 20 records (ID 1-20, linked to Orders 1-15, Products 1-20)
-- Financial Transactions: 12 records (ID 1-12, linked to Customers 1-10, Employees 1-6, Payments 1-15)
-- Deliveries: 8 records (ID 1-8)

-- Total: 103 records across 13 tables
