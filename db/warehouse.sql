create table if not exit warehouse_transactions (
    id integer primary key autoincrement,
    product_name text,
    warehouse_id integer,
    quantity real,
);