create table if not exists order_items (
    id integer primary key autoincrement ,
    order_id integer,
    customer text ,
    product_id integer,
    quantity integer,
    price integer,
    discount integer,
    description text
) ;
