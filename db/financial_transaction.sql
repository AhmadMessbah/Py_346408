create table if not exists financial_transactions(
    id integer primary key autoincrement,
    transaction_type text,
    customer_id integer,
    employee_id integer,
    amount integer,
    date_time text,
    payment_id integer,
    description text
);