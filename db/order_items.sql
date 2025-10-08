create table if not exists order_items (
    id integer primary key autoincrement ,
    product_id text,
    quantity integer,
    price real,
    discount real,
    description text
) ;
