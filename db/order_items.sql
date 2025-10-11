create table if not exists order_items (
    id integer primary key autoincrement ,
    order_id integer,
    product_id text,
    quantity integer,
    price real,
    discount real,
    description text
) ;
