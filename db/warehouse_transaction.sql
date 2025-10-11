create table if not exists warehouse_transactions (
    id integer primary key autoincrement,
    product_name text,
    warehouse_id integer,
    quantity real,
    transaction_date text,
    transaction_type text,
    sender text,
    receiver text
);