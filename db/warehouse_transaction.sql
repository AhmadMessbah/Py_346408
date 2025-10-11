create table if not exists warehouse_transactions (
    id integer primary key autoincrement,
    product_id integer,
    quantity integer,
    transaction_type text,
    transaction_datetime text,
    customer_id integer,
    employee_id integer
);