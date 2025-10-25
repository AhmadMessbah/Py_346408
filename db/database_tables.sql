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
-- customers -> payments (1:N)
-- employees -> payments (1:N)
-- products -> warehouses (1:N)
-- products -> warehouse_transactions (1:N)
-- products -> order_items (1:N)
-- customers -> warehouse_transactions (1:N)
-- customers -> financial_transactions (1:N)
-- customers -> orders (1:N)
-- employees -> warehouse_transactions (1:N)
-- employees -> financial_transactions (1:N)
-- employees -> orders (1:N)
-- payments -> financial_transactions (1:N)
-- payments -> orders (1:N) [nullable]
-- warehouse_transactions -> orders (1:N) [nullable]
-- orders -> order_items (1:N) [cascade delete]

