create table if not exists order_items (
    id integer primary key autoincrement ,
    product text,
    unit_price float,
    quantity integer,
    total_price float
) ;
