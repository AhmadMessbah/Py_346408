-- ============================================
-- DATABASE SCHEMA FOR SELLING SYSTEM
-- Complete database structure with table relationships
-- ============================================

-- ============================================
-- BASE ENTITIES (No dependencies)
-- ============================================

-- Banks table
create table if not exists banks(
    id integer primary key autoincrement,
    name text,
    account text,
    balance integer,
    description text
);

-- Customers table
create table if not exists customers(
    id integer primary key autoincrement,
    first_name text,
    last_name text,
    phone_number text,
    address text
);

-- Employees table
create table if not exists employees(
    id integer primary key autoincrement,
    first_name text,
    last_name text,
    salary integer,
    occupation text,
    phone_number text,
    username text unique,
    password text,
    role text
);

-- Products table
create table if not exists products(
    id integer primary key autoincrement,
    name text,
    brand text,
    model text,
    serial text,
    category text,
    unit text,
    expiration_date text
);

-- Sample table (for testing)
create table if not exists samples(
    id integer primary key autoincrement,
    name text,
    description text
);

-- ============================================
-- DEPENDENT ENTITIES (With foreign keys)
-- ============================================

-- Warehouses table (depends on: products)
create table if not exists warehouses (
    id integer primary key autoincrement,
    product_id integer,
    quantity integer,
    foreign key (product_id) references products(id) on delete restrict
);

-- Payments table (depends on: customers, employees)
create table if not exists payments(
    id integer primary key autoincrement,
    transaction_type text,
    payment_type text,
    date_time text,
    customer_id integer,
    total_amount integer,
    employee_id integer,
    description text,
    foreign key (customer_id) references customers(id) on delete restrict,
    foreign key (employee_id) references employees(id) on delete restrict
);

-- Warehouse Transactions table (depends on: products, customers, employees)
create table if not exists warehouse_transactions (
    id integer primary key autoincrement,
    product_id integer,
    quantity integer,
    transaction_type text,
    transaction_datetime text,
    customer_id integer,
    employee_id integer,
    foreign key (product_id) references products(id) on delete restrict,
    foreign key (customer_id) references customers(id) on delete restrict,
    foreign key (employee_id) references employees(id) on delete restrict
);

-- Financial Transactions table (depends on: customers, employees, payments)
create table if not exists financial_transactions(
    id integer primary key autoincrement,
    transaction_type text,
    customer_id integer,
    employee_id integer,
    amount integer,
    date_time text,
    payment_id integer,
    description text,
    foreign key (customer_id) references customers(id) on delete restrict,
    foreign key (employee_id) references employees(id) on delete restrict,
    foreign key (payment_id) references payments(id) on delete restrict
);

-- Orders table (depends on: customers, employees, payments, warehouse_transactions)
create table if not exists orders (
    id integer primary key autoincrement,
    order_type text,
    customer_id integer,
    employee_id integer,
    date_time text,
    payment_id integer,
    warehouse_transaction_id integer,
    tax integer,
    total_discount integer,
    total_amount integer,
    foreign key (customer_id) references customers(id) on delete restrict,
    foreign key (employee_id) references employees(id) on delete restrict,
    foreign key (payment_id) references payments(id) on delete set null,
    foreign key (warehouse_transaction_id) references warehouse_transactions(id) on delete set null
);

-- Order Items table (depends on: orders, products)
create table if not exists order_items (
    id integer primary key autoincrement,
    order_id integer,
    customer text,
    product_id integer,
    quantity integer,
    price integer,
    discount integer,
    description text,
    foreign key (order_id) references orders(id) on delete cascade,
    foreign key (product_id) references products(id) on delete restrict
);

-- Deliveries table (standalone)
create table if not exists deliveries(
    id integer primary key autoincrement,
    first_name text,
    last_name text,
    address text,
    description text
);

-- ============================================
-- SAMPLE DATA WITH CONSISTENT IDs
-- ============================================

-- Insert base data
insert or ignore into banks (id, name, account, balance, description) values 
(1, 'Melli Bank', 'checking', 5000000, 'Main checking account');

insert or ignore into customers (id, first_name, last_name, phone_number, address) values 
(1, 'Ahmad', 'Rezaei', '09123456789', 'Tehran_Iran_123');

insert or ignore into employees (id, first_name, last_name, salary, occupation, phone_number, username, password, role) values 
(1, 'ali', 'Mohammadi', 5000000, 'cashier', '09123456789', 'aliuser', 'pass1234', 'cashier');

insert or ignore into products (id, name, brand, model, serial, category, unit, expiration_date) values 
(1, 'Laptop', 'Dell', 'XPS15', 'SN123456', 'Electronics', 'Piece', '2025/12/31');

insert or ignore into samples (id, name, description) values 
(1, 'Sample 1', 'Test sample data');

-- Insert dependent data (using consistent IDs)
insert or ignore into warehouses (id, product_id, quantity) values 
(1, 1, 100);

insert or ignore into payments (id, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id, description) values 
(1, 'income', 'cash', '2024/01/01', 1, 500000, 1, 'Initial payment');

insert or ignore into warehouse_transactions (id, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id) values 
(1, 1, 10, 'output', '2024/01/01', 1, 1);

insert or ignore into orders (id, order_type, customer_id, employee_id, date_time, payment_id, warehouse_transaction_id, tax, total_discount, total_amount) values 
(1, 'frooshe', 1, 1, '2024/01/01', 1, 1, 100000, 5000, 95000);

insert or ignore into order_items (id, order_id, customer, product_id, quantity, price, discount, description) values 
(1, 1, 'Ahmad Rezaei', 1, 2, 100000, 5000, 'First order item');

insert or ignore into financial_transactions (id, transaction_type, customer_id, employee_id, amount, date_time, payment_id, description) values 
(1, 'sale', 1, 1, 500000, '2024/01/01', 1, 'Sale transaction');

insert or ignore into deliveries (id, first_name, last_name, address, description) values 
(1, 'Reza', 'Ahmadi', 'Tehran Street 1', 'Standard delivery');

-- ============================================
-- TABLE CREATION ORDER (Reflecting dependencies)
-- ============================================
-- 1. banks
-- 2. customers
-- 3. employees
-- 4. products
-- 5. samples
-- 6. warehouses (requires products)
-- 7. payments (requires customers, employees)
-- 8. warehouse_transactions (requires products, customers, employees)
-- 9. financial_transactions (requires customers, employees, payments)
-- 10. orders (requires customers, employees, payments, warehouse_transactions)
-- 11. order_items (requires orders, products)
-- 12. deliveries

-- ============================================
-- RELATIONSHIP SUMMARY
-- ============================================
-- customers (id: 1) -> payments (id: 1, customer_id: 1)
-- employees (id: 1) -> payments (id: 1, employee_id: 1)
-- products (id: 1) -> warehouses (id: 1, product_id: 1)
-- products (id: 1) -> warehouse_transactions (id: 1, product_id: 1)
-- products (id: 1) -> order_items (id: 1, product_id: 1)
-- customers (id: 1) -> warehouse_transactions (id: 1, customer_id: 1)
-- customers (id: 1) -> financial_transactions (id: 1, customer_id: 1)
-- customers (id: 1) -> orders (id: 1, customer_id: 1)
-- employees (id: 1) -> warehouse_transactions (id: 1, employee_id: 1)
-- employees (id: 1) -> financial_transactions (id: 1, employee_id: 1)
-- employees (id: 1) -> orders (id: 1, employee_id: 1)
-- payments (id: 1) -> financial_transactions (id: 1, payment_id: 1)
-- payments (id: 1) -> orders (id: 1, payment_id: 1)
-- warehouse_transactions (id: 1) -> orders (id: 1, warehouse_transaction_id: 1)
-- orders (id: 1) -> order_items (id: 1, order_id: 1)
