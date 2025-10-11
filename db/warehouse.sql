create table if not exists warehouse_transactions (
    id integer primary key autoincrement,
    product_id integer,
    quantity integer
);

