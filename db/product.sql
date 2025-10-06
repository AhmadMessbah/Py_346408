create table if not exists products(
    id integer primary key autoincrement,
    product_name text,
    product_type text,
    expiration_date text,
    warehouse_code integer,
    unit_price text,
    stock_quantity integer
);
