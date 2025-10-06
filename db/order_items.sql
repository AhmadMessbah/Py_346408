create table if not exists order_items (
    id integer primary key autoincrement ,
    product text,
    quantity integer ,
    price integer
) ;
