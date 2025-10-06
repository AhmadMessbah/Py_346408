create table if not exists payments(
    id integer primary key autoincrement,
    transaction_type text,
    payment_type text
    date_time text,
    customer_id integer,
    total_amount text,
    items_list text,
    employee_id integer
    description text
);