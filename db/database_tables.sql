-- ============================================
-- DATABASE SCHEMA FOR SELLING SYSTEM
-- Based on Entity definitions with proper nullable fields
-- ============================================

-- ============================================
-- BASE ENTITIES (No dependencies)
-- ============================================

-- Banks table
create table if not exists banks(
    id integer primary key autoincrement,
    name text not null,
    account text not null,
    balance integer not null,
    description text
);

-- Customers table
create table if not exists customers(
    id integer primary key autoincrement,
    first_name text not null,
    last_name text not null,
    phone_number text not null,
    address text not null
);

-- Employees table
create table if not exists employees(
    id integer primary key autoincrement,
    first_name text not null,
    last_name text not null,
    salary integer not null,
    occupation text not null,
    phone_number text not null,
    username text unique not null,
    password text not null,
    role text not null
);

-- Products table
create table if not exists products(
    id integer primary key autoincrement,
    name text not null,
    brand text not null,
    model text not null,
    serial text not null,
    category text not null,
    unit text not null,
    expiration_date text
);

-- Sample table (for testing)
create table if not exists samples(
    id integer primary key autoincrement,
    name text not null,
    description text
);

-- ============================================
-- DEPENDENT ENTITIES (With foreign keys)
-- ============================================

-- Warehouses table (depends on: products)
create table if not exists warehouses (
    id integer primary key autoincrement,
    product_id integer not null,
    quantity integer not null,
    foreign key (product_id) references products(id)
);

-- Payments table (depends on: customers, employees)
create table if not exists payments(
    id integer primary key autoincrement,
    transaction_type text not null,
    payment_type text not null,
    date_time text not null,
    customer_id integer not null,
    total_amount integer not null,
    employee_id integer not null,
    description text,
    foreign key (customer_id) references customers(id),
    foreign key (employee_id) references employees(id)
);

-- Warehouse Transactions table (depends on: products, customers, employees)
create table if not exists warehouse_transactions (
    id integer primary key autoincrement,
    product_id integer not null,
    quantity integer not null,
    transaction_type text not null,
    transaction_datetime text not null,
    customer_id integer not null,
    employee_id integer not null,
    foreign key (product_id) references products(id),
    foreign key (customer_id) references customers(id),
    foreign key (employee_id) references employees(id)
);

-- Financial Transactions table (depends on: customers, employees, payments)
create table if not exists financial_transactions(
    id integer primary key autoincrement,
    transaction_type text not null,
    customer_id integer not null,
    employee_id integer not null,
    amount integer not null,
    date_time text not null,
    payment_id integer not null,
    description text not null default '',
    foreign key (customer_id) references customers(id),
    foreign key (employee_id) references employees(id),
    foreign key (payment_id) references payments(id)
);

-- Orders table (depends on: customers, employees, payments, warehouse_transactions)
-- tax, total_discount, total_amount are nullable based on entity definition
create table if not exists orders (
    id integer primary key autoincrement,
    order_type text not null,
    customer_id integer not null,
    employee_id integer not null,
    date_time text not null,
    payment_id integer not null,
    warehouse_transaction_id integer not null,
    tax integer,
    total_discount integer,
    total_amount integer,
    foreign key (customer_id) references customers(id),
    foreign key (employee_id) references employees(id),
    foreign key (payment_id) references payments(id),
    foreign key (warehouse_transaction_id) references warehouse_transactions(id)
);

-- Order Items table (depends on: orders, products)
-- discount and description are nullable based on entity definition
create table if not exists order_items (
    id integer primary key autoincrement,
    order_id integer not null,
    customer text not null,
    product_id integer not null,
    quantity integer not null,
    price integer not null,
    discount integer,
    description text,
    foreign key (order_id) references orders(id),
    foreign key (product_id) references products(id)
);

-- Deliveries table (standalone)
create table if not exists deliveries(
    id integer primary key autoincrement,
    first_name text not null,
    last_name text not null,
    address text not null,
    description text
);

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
